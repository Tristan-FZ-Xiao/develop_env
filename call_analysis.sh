#!/bin/bash

# Need tool list:
# 1. cscope
# 2. tceetree
# 3. dot

echo "call_analysis {path} {target_call} {filter} {output}"

call_analysis() { cscope -Rcbkq -P $1; tceetree -f -r $2 -o /proc/self/fd/1 | egrep -v "$3" | dot -Tpdf -o $4; }

path="$1"
target="$2"
filter="$3"
output="$4"

call_analysis "$path" "$target" "filter" "$output"
