#!/bin/bash
#bash file to show ip address
ifconfig en0 | grep inet | awk '{print $2}'

