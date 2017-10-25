#!/bin/bash

# Need tool list:
# 1. cscope
# 2. tceetree
# 3. dot

call_analysis() { cscope -Rcbkq -P $1; tceetree -f -r $2 -o /proc/self/fd/1 | dot -Tpdf -o $3; }

path="$1"
target="$2"
output="$3"

call_analysis "$path" "$target" "$output"
