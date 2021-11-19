# Using xargs with parameters
cat foo.txt | xargs -I % sh -c 'echo %; mkdir %'
