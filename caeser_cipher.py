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

