print("____ENCRYPTION____")
word=input("\nenter the message: ")
code=int(input("give the key: "))
encrypted_message=""
for char in word:
    ordinal_ch=ord(char)
    ordinal_ch+=code
    if ordinal_ch > ord('z'):
        ordinal_ch= ord('a') + (ordinal_ch - ord('z'))-1
    newchar=chr(ordinal_ch)
    encrypted_message += newchar
print("message:" ,encrypted_message)

decrypted_message=""
for char in encrypted_message:
    ordinal_ch=ord(char)
    ordinal_ch-=code
    if( ordinal_ch<ord('a')):
        ordinal_ch= ord('z')-(ord('a')-ordinal_ch-1)
    newchar=chr(ordinal_ch)
    decrypted_message+=newchar
print("____DECRYPTION____")
print("orginal message  ;",decrypted_message)
    
