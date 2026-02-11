# write your bash commands here

for textfile in fortunes/pets*.txt
do
    echo -n "$textfile: "
    grep -i "cat" $textfile | wc -l
done    