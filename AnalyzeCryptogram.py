from collections import Counter


def analyzeCryptograms(text, key_length):
    """
    Analyzes encrypted text by generating and examining subtexts based on a given key length.
    This function outputs the most common characters for each segment of the text created by the key.
    """
    cryptograms_analysis = [None] * key_length

    print("\n----Analyzing most common characters in each subtext segment----")
    for segment_index in range(key_length):
        # Extract characters that align with this segment position for the entire text
        segment_characters = text[segment_index::key_length]
        # Count character frequencies in this segment
        frequency_count = Counter(segment_characters)
        # Store and print the top three most common characters in this segment
        cryptograms_analysis[segment_index] = frequency_count.most_common(3)
        print(f"Cryptogram {segment_index+1}: {cryptograms_analysis[segment_index]}")
    
    # Decrypting based on frequency analysis assumption that 'e' is the most common character
    print("\n----Decrypting based on common character assumption 'e'----")
    for segment_index, analysis in enumerate(cryptograms_analysis):
        decrypted_chars = [None] * 3
        for idx, (character, _) in enumerate(analysis):
            # Assuming the most common character aligns with 'e'
            decrypted_chars[idx] = chr((ord(character) - ord('e') + 26) % 26 + ord('a'))
        print(f"Cryptogram {segment_index+1}: {decrypted_chars}")

encrypted_text = "pchhlptizjhfatcrifnkhctoqvgxbusvwggszbjchmwvghnvetdsqnrkxtslmdbsuczhttiysunjtcldlhcwjkqkitktmsumgtjthlipmwvghfnxgxfdxwtacmoiyxgjvlmjxgftiytnckwoudnnvfdwexekgdoemxfbvihmwzgwsrxpiszcfxapivyfbcdouegmhnwwbrxgzgkudettcpgqwxkwhmunryovmgtufcgxwmryoxwvbdegkuxxiysquvngrzslqitihbihvdeqhunbcxhkynhhzbjvkwhrzouwvizcqmfbhtivmgwhftdljtkvphyplxeuoykgiysvypltkvdnvatislmqgapcqyuxacsucptrfbwcpndlggiwuavoxwvbdeqguvatisdlgfpemeoaxgjoqxuxacsumyadtcqnkgjfivfamgrrhuubcxzhwqfbfrlnauxugdlgfpkqkyftcuqoycktucyytmxdsdwehguwqavhiysdoemxfbuonxhtrdmcktkmscetacmrjggqzrwbgutjhnhqpcvldgretftdwftxjovyengzhlyufpiyhnunryovnjxcvkbitdhkcfegqryoqaggnjswbgkteczyzbhkbxggkdlgrhnbcvpuimxgjwwyuljtvdmehbdghwvapkcizgkhvfycexhwcunttszbjcplttiucvbtjadlmxijcqfkgtsfregkhvlkcdbikvhmcftwzdquthdcuyehcmsqnkhcrzrhnbcvoxwvbdegdhfhuwsuhqydiarzrkdksfnkhckcecfwtigfixxgruhihlttiucvrxjgxyuydiqguubhcwpcvxsnoqacgscsxhiigfdrmgwpjqkyoxufffipwjthlhilttiuycgsrbrhafdlgfxclwfkhpgkiywvmeatdslmkghvqxlgtcurryugdkogxtxhjhkyuxrlflnkxhdouegmpjdhwvhutrdmyxlzzoxklrlgvnjbhzbvyemxfb"
key_length = 7 #Based on previous result
analyzeCryptograms(encrypted_text, key_length)
