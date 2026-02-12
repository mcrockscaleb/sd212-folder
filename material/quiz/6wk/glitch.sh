# FILL THIS IN WITH YOUR SOLUTION TO PROBLEM 3
grep 'PAID' transactions.csv | grep '0.00' | cut -d: -f2 | sort -u
