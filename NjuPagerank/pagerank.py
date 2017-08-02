# -*-coding:utf-8 -*-
from numpy import *
from numpy.linalg import *
import DetectionAll
import InputData


GetExeTime = DetectionAll.Ctimer()


def hang_pot(array): #找到悬挂点
	a_array = array.max(axis=1)
	n = array.shape[1]
	hang_array = ones((1, n))-a_array
	hang_array = hang_array.transpose()
	return hang_array


def normalize(H): #对原始的0，1矩阵进行归一化
	a = H.sum(axis=1, dtype=float)
	b = (a == 0)
	a[b] += 1
	n = a.shape[0]
	# print a
	for i in range(n):
		for j in range(n):
			H[i, j] = H[i, j]*1.0/a[i]
	return H

@GetExeTime.exeTime
def iteration(pi0, H, alpha, epsilon): #进行迭代计算权值
	hang_array = hang_pot(H)
	n = H.shape[1]
	H = normalize(H)
	k = 0
	pi = pi0
	residual = 1
	while residual >= epsilon:
		prevpi = pi
		k += 1
		pi = alpha*dot(pi, H)+dot((alpha*dot(pi, hang_array)+1-alpha)*1.0/n, ones((1, n)))
		residual = norm(pi-prevpi, 1)
	return pi


def pagerankmain(file, OffsetRow, OffsetCol):
    ReadMatrix = InputData.InputMatrix()
    array = ReadMatrix.ReadCsv(file, OffsetRow, OffsetCol)
    n = array.shape[1]
    pi0 = ones((1, n))
    alpha = 0.85
    epsilon = 1e-5
    pi = iteration(pi0, array, alpha, epsilon)
    return pi

