split -d -a 3 -l 25 mycomments.json mycomments_ 

for file in mycomments_00*
do
    mv "$file" "${file/_00/}.json"
done

for file in mycomments_0*
do
    mv "$file" "${file/_0/}.json"
done

for file in mycomments_*
do
    mv "$file" "${file/_/}.json"
done
