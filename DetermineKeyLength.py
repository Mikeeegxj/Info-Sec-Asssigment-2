def calculateSimilarity(base_string, comparison_string):
    """
    Calculates the similarity count between two strings, comparing them character by character.
    """
    similarity_score = 0
    base_string = base_string.lower()
    comparison_string = comparison_string.lower()
    for index in range(min(len(base_string), len(comparison_string))):
        if base_string[index] == comparison_string[index]:
            similarity_score += 1
    return similarity_score

def determineKeyLength(ciphertext):
    """
    Determines the key length for a Vigenère cipher by comparing shifted versions of the ciphertext
    against the original ciphertext, calculating similarity counts for various key lengths.
    """
    # Define the range for potential key lengths commonly used in Vigenère ciphers
    minimum_key_length = 4
    maximum_key_length = 13
    
    while minimum_key_length <= maximum_key_length:
        shift_pattern = "*" * minimum_key_length
        shifted_ciphertext = shift_pattern + ciphertext
        score = calculateSimilarity(ciphertext, shifted_ciphertext)
        print(f"Similarity score for key length {minimum_key_length}: {score}")
        minimum_key_length += 1


ciphertext = "pchhlptizjhfatcrifnkhctoqvgxbusvwggszbjchmwvghnvetdsqnrkxtslmdbsuczhttiysunjtcldlhcwjkqkitktmsumgtjthlipmwvghfnxgxfdxwtacmoiyxgjvlmjxgftiytnckwoudnnvfdwexekgdoemxfbvihmwzgwsrxpiszcfxapivyfbcdouegmhnwwbrxgzgkudettcpgqwxkwhmunryovmgtufcgxwmryoxwvbdegkuxxiysquvngrzslqitihbihvdeqhunbcxhkynhhzbjvkwhrzouwvizcqmfbhtivmgwhftdljtkvphyplxeuoykgiysvypltkvdnvatislmqgapcqyuxacsucptrfbwcpndlggiwuavoxwvbdeqguvatisdlgfpemeoaxgjoqxuxacsumyadtcqnkgjfivfamgrrhuubcxzhwqfbfrlnauxugdlgfpkqkyftcuqoycktucyytmxdsdwehguwqavhiysdoemxfbuonxhtrdmcktkmscetacmrjggqzrwbgutjhnhqpcvldgretftdwftxjovyengzhlyufpiyhnunryovnjxcvkbitdhkcfegqryoqaggnjswbgkteczyzbhkbxggkdlgrhnbcvpuimxgjwwyuljtvdmehbdghwvapkcizgkhvfycexhwcunttszbjcplttiucvbtjadlmxijcqfkgtsfregkhvlkcdbikvhmcftwzdquthdcuyehcmsqnkhcrzrhnbcvoxwvbdegdhfhuwsuhqydiarzrkdksfnkhckcecfwtigfixxgruhihlttiucvrxjgxyuydiqguubhcwpcvxsnoqacgscsxhiigfdrmgwpjqkyoxufffipwjthlhilttiuycgsrbrhafdlgfxclwfkhpgkiywvmeatdslmkghvqxlgtcurryugdkogxtxhjhkyuxrlflnkxhdouegpjdhwvhutrdmyxlzzoxklrlgvnjbhzbvyemxfb"
determineKeyLength(ciphertext)
