#!/bin/bash
echo Username: 
read username

split -d -a 4 -l 25 ${username}_posts.json "listing/posts/${username}_ n"

for file in "listing/posts/${username}_ n000"*
do
    mv "$file" "${file/ n000/}.json"
done

for file in "listing/posts/${username}_ n00*"*
do
    mv "$file" "${file/ n00/}.json"
done

for file in "listing/posts/${username}_ n0"*
do
    mv "$file" "${file/ n0/}.json"
done

split -d -a 5 -l 25 ${username}_comments.json "listing/comments/${username}_ n"

for file in "listing/comments/${username}_ n0000"*
do
    mv "$file" "${file/ n0000/}.json"
done

for file in "listing/comments/${username}_ n000"*
do
    mv "$file" "${file/ n000/}.json"
done

for file in "listing/comments/${username}_ n00"*
do
    mv "$file" "${file/ n00/}.json"
done

for file in "listing/comments/${username}_ n0"*
do
    mv "$file" "${file/ n0/}.json"
done
