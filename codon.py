
#코돈표 작성
amino = {
    "UUU" : 'phenylalanine',
    "UUC" : 'phenylalanine',
    "UUA" : 'leucine',
    "UUG" : "leucine",
    "CUU" : 'leucine',
    "CUC" : 'leucine',
    "CUA" : 'leucine',
    "CUG" : 'leucine',
    "AUU" : 'isoleucine', 
    "AUC" : 'isoleucine',
    "AUA" : 'isoleucine',
    "AUG" : 'methionine', 
    "GUU" : 'valine',
    "GUC" : 'valine',
    "GUA" : 'valine',
    "GUG" : 'valine',
    "UCA" : 'serine',
    "UCU" : 'serine',
    "UCC" : 'serine',
    "AGU" : 'serine',
    "AGC" : 'serine',
    "CCU" : 'proline',
    "CCC" : 'proline',
    "CCA" : 'proline',
    "CCG" : 'proline',
    "ACU" : 'threonine',
    "ACC" : 'threonine',
    "ACA" : 'threonine',
    "ACG" : 'threonine',
    "GCU" : 'alanine',
    "GCC" : 'alanine',
    "GCA" : 'alanine',
    "GCG" : 'alanine',
    "UAU" : 'tylosin',
    "UAC" : 'tylosin',
    "CAU" : 'histidine',
    "CAC" : 'histidine',
    "CAA" : 'glutamine',
    "CAG" : 'glutamine',
    'AAU' : 'asparagine',
    'AAC' : 'asparagine',
    'AAA' : 'lysine',
    'AAG' : 'lysine',
    'GAU' : 'aspartic_acid',
    'GAC' : 'aspartic_acid',
    'GAA' : 'glutamate',
    'GAG' : 'glutamate',
    'UGU' : 'cysteine',
    'UGC' : 'cysteine',
    'UGG' : 'tryptophan',
    'AGU' : 'serine',
    'AGC' : 'serine',
    'CGU' : 'arginine',
    'CGC' : 'arginine',
    'CGA' : 'arginine',
    'CGG' : 'arginine',
    'AGG' : 'arginine',
    'AGC' : 'arginine',
    'GGU' : 'glycine',
    'GGC' : 'glycine',
    'GGA' : 'glycine',
    'GGG' : 'glycine',
    'UAA' : 'stop_codon',
    'UAG' : 'stop_codon',
    'UGA' : 'stop_codon',
}

# mRNA 염기서열 입력
#작동 확인됨
mRNA = list(input().upper())

rightRNA = True

# A, G, U, C 외 다른 알파벳 있으면 오류메세지 출력 --> rigntmRNA == false
#작동 확인됨
for i in range(len(mRNA)) :
    if mRNA[i] == 'A' or mRNA[i] == 'G' or mRNA[i] == 'C' or mRNA[i] == 'U' :
        pass
    else :
        rightRNA = False
        print('mRNA 염기서열이 아닙니다.')
        break


#rightRNA가 True일 경우 개시코돈 파인딩 로직 작동
#연속적으로 A,U,G 존재할 때 반복문 중지 
#개시코돈이 없을 경우 오류 메세지 출력
count_ = 0
if rightRNA == True :

    #개시코돈 찾기
    for i in range(len(mRNA)) :
        if mRNA[len(mRNA)-2] == "A" :
            print('개시코돈이 존재하지 않습니다.')
            rightRNA = False
            break
        elif mRNA[i] == 'A' :
            if mRNA[i + 1] == 'U' :
                if mRNA[i + 2] =='G' :
                    break
                else :
                    count_ += 1
            else :
                count_ += 1
        else :
            if i == len(mRNA) :
                print('개시코돈이 존재하지 않습니다.')
                rightRNA = False
                break
            count_ += 1

#rightRNA가 True일 경우 아래 로직 작동
if rightRNA == True :
    
    #개시코돈이 시작하는 부분부터 새로운 리스트에 append해줌
    mRNA1 = []
    for i in range(count_, len(mRNA)) :
        mRNA1.append(mRNA[i])

    #염기서열을 3개씩 묶어 코돈으로 만들어주기 위해서 리스트 길이를 3의 배수로 맞춰줌. --> pop()을 사용하여 맨 뒤의 나머지 염기 제거
    if (len(mRNA1) + 1 - count_)%3 != 0 :
        for i in range((len(mRNA1) - count_)%3) :
            mRNA1.pop()
    
    #염기서열을 3개씩 묶어 코도능로 만들어줌
    newRNA = []
    for i in range(0,len(mRNA1)-1,3) :
        codon = mRNA1[i] + mRNA1[i+1] + mRNA1[i+2]
        newRNA.append(codon)
    
    #코돈을 해석한 아미노산들을 출력, 종결코돈이 나오면 멈춘다.
    for i in range(len(newRNA)) :
        if newRNA[i] == 'UAA' or newRNA[i] == 'UGA' or newRNA[i] == 'UAG' :
            break
        else :
            print(amino[newRNA[i]], '-', end = "")
else :
    pass

# coding from crzstarcoder
