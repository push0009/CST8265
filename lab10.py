
def dc_message():
    print("Decrypt Encrypted Message")
    enc_msg = input("Enter Encrypted Message: ")
    for key in range(0, 25):
        translated = ''
        for i in range(len(enc_msg)):
            if ord(enc_msg[i]) == 32:
                translated += chr(ord(enc_msg[i]))
            elif ((ord(enc_msg[i]) - key) < 97) and ((ord(enc_msg[i]) - key) > 90):
                temp = (ord(enc_msg[i]) - key) + 26
                translated += chr(temp)
            elif (ord(enc_msg[i]) - key) < 65:
                temp = (ord(enc_msg[i]) - key) + 26
                translated += chr(temp)
            else:
                translated += chr(ord(enc_msg[i]) - key)
        print('key %s: %s' % (key, translated))

def encryption():
    print("Encr")
    print("lower or UPPER case")
    msg = input("Enter text: ")
    key = int(input("Enter key(0-25): "))
    encrypted_text = ""
    for i in range (len(msg)):
        if ord(msg[i]) == 32:
            encrypted_text += chr(ord(msg[i]))
        elif ord(msg[i]) + key > 122:
            temp_data = (ord(msg[i]) + key) - 122
            encrypted_text += chr(96 + temp_data)
        elif (ord(msg[i]) + key > 90) and (ord(msg[i]) <= 96):
            temp_data = (ord(msg[i]) + key) - 90
            encrypted_text += chr(64 + temp_data)
        else:
            encrypted_text += chr(ord(msg[i]) + key)
    print("Encrypted: " + encrypted_text)

def decryption():
    print("Decr")
    print("lower or UPPER case")
    encrp_msg = input("Enter encrypted text: ")
    key = int(input("Enter key(0-25): "))
    dec_text = ""
    for i in range(len(encrp_msg)):
        if ord(encrp_msg[i]) == 32:
            dec_text += chr(ord(encrp_msg[i]))
        elif ((ord(encrp_msg[i]) - key) < 97) and ((ord(encrp_msg[i]) - key) > 90):
            temp_data = (ord(encrp_msg[i]) - key) + 26
            dec_text += chr(temp_data)
        elif (ord(encrp_msg[i]) - key) < 65:
            temp_data = (ord(encrp_msg[i]) - key) + 26
            dec_text += chr(temp_data)
        else:
            dec_text += chr(ord(encrp_msg[i]) - key)
    print("Decrypted text: " + dec_text)

def main():
    chc = int(input("1. Encryption\n2. Decryption\n3. Decrypt Message\nChoose(1,2,3): "))
    if chc == 1:
        encryption()
    elif chc == 2:
        decryption()
    elif chc == 3:
        dc_message()
    else:
        print("Wrong!!!!")

if __name__ == "__main__":
    main()


# QVIREFVGL - 13 - DIVERSITY
# ZJ -  17 - IS
# DJG - 15 - OUR
# LMKXGZMA - 19 - STRENGTH