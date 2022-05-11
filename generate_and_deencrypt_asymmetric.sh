openssl genrsa -out bob.key 4096 &> /dev/null
openssl rsa -in bob.key -pubout > bob.pub

echo "YOUR TOP SECRET" > secret.txt
openssl rsautl -encrypt -inkey bob.pub -pubin -in secret.txt -out secret.enc

cat secret.enc | base64 > secret.enc.b64
rm secret.enc

cat secret.enc.b64 | base64 -d > secret.enc
rm secret.txt

openssl rsautl -decrypt -inkey bob.key -in secret.enc > secret.txt
rm secret.enc
