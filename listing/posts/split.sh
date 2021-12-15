split -d -a 2 -l 25 myposts.json myposts_ 

for file in myposts_0*
do
    mv "$file" "${file/_0/}.json"
done

for file in myposts_*
do
    mv "$file" "${file/_/}.json"
done
