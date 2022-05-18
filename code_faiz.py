# SpmlCpzCq2z1CvujlGCdoh1CpzC1olCtlhupunCvmCspmlECdlCzov2skCsp3lCmvyCzvtl1opunC4vy1o6G 
#characterList = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0',' ','!','?',',','.']
characterList = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?,.'
stringToDecode = 'SpmlCpzCq2z1CvujlGCdoh1CpzC1olCtlhupunCvmCspmlECdlCzov2skCsp3lCmvyCzvtl1opunC4vy1o6G'


for keyShift in range(len(characterList)):
    message = ''

    for e in stringToDecode: 
        
        number = characterList.find(e) #finding the what the index is of a character in the stringToDecode is in the characterList
        number =(number + keyShift) % len(characterList) #shifting according to index
        message += characterList[number] #passing key(index) to characterlist and addding it to the plaintext message

    print(keyShift, message)