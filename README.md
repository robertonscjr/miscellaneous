# misc3114

openssl aes-256-cbc -in attack-plan.txt -out message.enc

openssl aes-256-cbc -d -in message.enc -out plain-text.txt

Recursively delete all files of a specific extension in the current directory: `find . -name "*.bak" -type f -delete`

Replacing all occurrences of one string in all files in the current directory: `find . -type f -exec sed -i 's/foo/bar/g' {} +`

Get second column: `awk '{print $2}' FILE`

HTTP request: `curl -X <METHOD> -H "Content-Type: application/json" -d '{"key1":"value"}' <URL>`

Using xargs with parameters:
```
cat foo.txt | xargs -I % sh -c 'echo %; mkdir %'
one 
two
three

ls 
one two three
```
