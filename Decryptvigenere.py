def decryptVigenereCipher(cipher_text, decryption_key):
    """
    Decrypts a cipher text encrypted with the Vigenère cipher using a specified decryption key.
    """
    decrypted_text = ""

    # Normalize the decryption key to ensure consistency
    decryption_key = decryption_key.lower()

    # Iterate through each character in the cipher text
    for index, cipher_char in enumerate(cipher_text):
        key_char = decryption_key[index % len(decryption_key)]

        if cipher_char.isalpha():
            # Decrypt the character and add it to the decrypted text
            offset = (ord(cipher_char) - ord(key_char)) % 26
            decrypted_char = chr(offset + ord('a'))
            decrypted_text += decrypted_char
        else:
            # Append non-alphabetic characters unchanged
            decrypted_text += cipher_char

    print(decrypted_text)

# Input cipher text and the decryption key determined from analysis
cipher_text = "pchhlptizjhfatcrifnkhctoqvgxbusvwggszbjchmwvghnvetdsqnrkxtslmdbsuczhttiysunjtcldlhcwjkqkitktmsumgtjthlipmwvghfnxgxfdxwtacmoiyxgjvlmjxgftiytnckwoudnnvfdwexekgdoemxfbvihmwzgwsrxpiszcfxapivyfbcdouegmhnwwbrxgzgkudettcpgqwxkwhmunryovmgtufcgxwmryoxwvbdegkuxxiysquvngrzslqitihbihvdeqhunbcxhkynhhzbjvkwhrzouwvizcqmfbhtivmgwhftdljtkvphyplxeuoykgiysvypltkvdnvatislmqgapcqyuxacsucptrfbwcpndlggiwuavoxwvbdeqguvatisdlgfpemeoaxgjoqxuxacsumyadtcqnkgjfivfamgrrhuubcxzhwqfbfrlnauxugdlgfpkqkyftcuqoycktucyytmxdsdwehguwqavhiysdoemxfbuonxhtrdmcktkmscetacmrjggqzrwbgutjhnhqpcvldgretftdwftxjovyengzhlyufpiyhnunryovnjxcvkbitdhkcfegqryoqaggnjswbgkteczyzbhkbxggkdlgrhnbcvpuimxgjwwyuljtvdmehbdghwvapkcizgkhvfycexhwcunttszbjcplttiucvbtjadlmxijcqfkgtsfregkhvlkcdbikvhmcftwzdquthdcuyehcmsqnkhcrzrhnbcvoxwvbdegdhfhuwsuhqydiarzrkdksfnkhckcecfwtigfixxgruhihlttiucvrxjgxyuydiqguubhcwpcvxsnoqacgscsxhiigfdrmgwpjqkyoxufffipwjthlhilttiuycgsrbrhafdlgfxclwfkhpgkiywvmeatdslmkghvqxlgtcurryugdkogxtxhjhkyuxrlflnkxhdouegmpjdhwvhutrdmyxlzzoxklrlgvnjbhzbvyemxfb"
keyword = "product"
decryptVigenereCipher(cipher_text, keyword)
