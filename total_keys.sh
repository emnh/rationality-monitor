#!/bin/bash
# TODO: process these commands to see which were good
exit
cat log_of_apm.txt | cut -f1 -d, | uniq -d | wc -l
cat log_of_apm.txt | cut -f1 -d, | uniq -D | wc -l
cat log_of_apm.txt | cut -f1 -d, | uniq -u | wc -l
cat log_of_apm.txt | egrep '2023-12-05|2023-12-06' | cut -f1 -d, | uniq -u | wc -l
cat log_of_apm.txt | egrep -a '2023-12-05|2023-12-06' | cut -f1 -d, | uniq -u | wc -l
cat log_of_apm.txt | egrep -a '2023-12-06' | cut -f1 -d, | uniq -u | wc -l
cat log_of_apm.txt | cut -f1 -d,
cat log_of_apm.txt | cut -f1 -d, | uniq -c
cat log_of_apm.txt | cut -f1 -d, | uniq -c | grep -vc '^1'
cat log_of_apm.txt | cut -f1 -d, | uniq -c | grep -c '^1'
cat log_of_apm.txt | cut -f1 -d, | uniq -c | grep -c '^\s*1'
cat log_of_apm.txt | cut -f1 -d, | uniq -c | grep -vc '^\s*1'
cat log_of_apm.txt | cut -f1 -d, | uniq -c | grep -v '^\s*1' | cut -f1
cat log_of_apm.txt | cut -f1 -d, | uniq -c | grep -v '^\s*1' | cut -f1 -d" "
cat log_of_apm.txt | cut -f1 -d, | uniq -c | grep -v '^\s*1' 
cat log_of_apm.txt | cut -f1 -d, | uniq -c | grep -v '^\s*1' 
cat log_of_apm.txt | cut -f1 -d, | uniq -c | grep -vc '^\s*1' 
cat log_of_apm.txt | cut -f1 -d, | uniq -c | grep -c '^\s*1' 
cat log_of_apm.txt | cut -f1 -d, | uniq -d | fgrep -c
cat log_of_apm.txt | cut -f1 -d, | uniq -d | wc -l
cat log_of_apm.txt | cut -f1 -d, | uniq -D | wc -l
cat log_of_apm.txt | cut -f1 -d, | uniq -u | wc -l
cat log_of_apm.txt | egrep '2023-12-05|2023-12-06' | cut -f1 -d, | uniq -u | wc -l
cat log_of_apm.txt | egrep -a '2023-12-05|2023-12-06' | cut -f1 -d, | uniq -u | wc -l
cat log_of_apm.txt | egrep -a '2023-12-06' | cut -f1 -d, | uniq -u | wc -l
