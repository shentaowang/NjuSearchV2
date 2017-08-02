#coding:utf-8
import jieba
from difflib import unified_diff
from difflib import SequenceMatcher
import sys

class FileDiff(object):
    def TwoFileCompare(self, file1, file2):
        fp1 = open(file1, "r")
        fp2 = open(file2, "r")
        content1 = ""
        content2 = ""
        list1 = []
        list2 = []
        for i in fp1.readlines():
            content1 = content1 + i
        for i in fp2.readlines():
            content2 = content2 + i
        seg_list1 = jieba.cut(content1, cut_all=False)
        seg_list2 = jieba.cut(content2, cut_all=False)
        for word in seg_list1:
            list1.append(word)
        for word in seg_list2:
            list2.append(word)
        for line in unified_diff(list1, list2, fromfile="before.py", tofile ="after.py"):
            sys.stdout.write(line)

    def TwoFileSimilarity(self, file1, file2):
        fp1 = open(file1, "r")
        fp2 = open(file2, "r")
        content1 = ""
        content2 = ""
        list1 = []
        list2 = []
        for i in fp1.readlines():
            content1 = content1 + i
        for i in fp2.readlines():
            content2 = content2 + i
        junk = [" ", "\n", "\t" ]
        s = SequenceMatcher(lambda x:x in junk,content1,content2)
        return s.ratio()

