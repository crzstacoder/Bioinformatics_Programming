
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

mRNA = list(input().upper())

#입력한 염기서열 모두 대문자로 + A, G, U, C 외 다른 알파벳 있으면 오류메세지 출력 --> rigntmRNA == false
rightRNA = True


#작동 확인됨
for i in range(len(mRNA)) :
    if mRNA[i] == 'A' or mRNA[i] == 'G' or mRNA[i] == 'C' or mRNA[i] == 'U' :
        pass
    else :
        rightRNA = False
        print('mRNA 염기서열이 아닙니다.')
        break



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

if rightRNA == True :
    mRNA1 = []
    for i in range(count_, len(mRNA)) :
        mRNA1.append(mRNA[i])


    if (len(mRNA1) + 1 - count_)%3 != 0 :
        for i in range((len(mRNA1) - count_)%3) :
            mRNA1.pop()

    newRNA = []
    for i in range(0,len(mRNA1)-1,3) :
        codon = mRNA1[i] + mRNA1[i+1] + mRNA1[i+2]
        newRNA.append(codon)
            
    for i in range(len(newRNA)) :
        if newRNA[i] == 'UAA' or newRNA[i] == 'UGA' or newRNA[i] == 'UAG' :
            break
        else :
            print(amino[newRNA[i]], '-', end = "")
else :
    pass