#!/bin/bash
wget https://artifacts.elastic.co/downloads/kibana/kibana-5.5.1-x86_64.rpm
sha1sum kibana-5.5.1-x86_64.rpm 
sudo rpm --install kibana-5.5.1-x86_64.rpm
