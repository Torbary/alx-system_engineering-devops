#!/usr/bin/bash
#Get the Url from the command line arguemnts

url="$1"

# send a request to the URL using curl and store the output in a  variable
response=$(curl -sI "$url")

#Get the content lemgth of the response using grep
content_length=$(echo "$response" | grep -i "Content-Length:" | awk '{print $2}')

echo "$content_length"
