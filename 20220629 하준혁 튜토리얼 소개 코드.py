# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 20:28:06 2022

@author: 하준혁(keita268@gmail.com)
"""

# kaggle practice competition인 titanic을 해보겠습니당.
# https://www.kaggle.com/competitions/titanic/overview
# 이건 시작이지만, 앞으로 좋은 주제 잡아서 잘해봐용

# 목차
# 1. 데이터 인풋
# 2. 데이터 조회
# 3. 간단한 알고리즘("Women and children first")
# 4. 데이터 아웃풋 / 제출


#%% 1. 데이터 인풋.
#
# .csv 파일은 유서 깊은 2차원 데이터 저장 방식입니다. 
# tab, /, ;등으로 칸을 나누게 됩니다.
# 우리는 보통 엑셀로 이를 열어서 보지만, 사실 이건 notepad로도 읽을 수 있답니다.
# 여기서 다운로드한 엑셀은 ,로 나누는 방식이었네요. 중요하진 않습니다.

# 파이썬으로 이걸 읽는 방식은 여러가지가 있지만, 가장 제네럴한건 pandas죠.
# pandas는 제가 만든 HandyEEG와 같은 모듈입니다. 훨씬 잘 만들었다는 차이점만 있죠.
# 보통 모듈이라면 import pandas로 임포트 하지만, 
# 이는 너무 많이 쓰여서 pd로 줄여부르는게 대세기 때문에, as pd를 붙여줍니다.
import pandas as pd

# 이제 읽어볼까요.
# 파일을 읽으려면 위치를 알려줘야 합니다.
# 파일의 위치, 주소는 "문자 타입"의 데이터입니다. 당연하죠?
file_1 = 'D:/HJH/20220629 titanic keggle/Dataset/gender_submission.csv'
# 이렇게 하면 파일의 주소를 저장시킬 수 있는 것입니다.

# 이건 csv니까, csv를 읽는 함수(기능)을 사용합니다.
gender_submission_df = pd.read_csv(file_1)
# gender_submission_df 라는 변수는, 
# file_1의 주소를 가진 csv를 
# pandas의 read_csv라는 기능을 통해 읽어낸 데이터 프레임입니다.
# spyder를 사용한다면,
# 오른쪽 위의 창에 있는 Variable explorer에서 확인할 수 있습니다.

# 이렇게 나머지 2개의 파일도 읽어낼건데요, 
# 사실 저는 주소를 한 줄로 길게 적는게 위험하다고 생각합니다.
# 바꾸기도 쉽지않고, 다른 컴퓨터는 저랑 폴더구조가 다르니까요.
# 그래서 각 파일의 주소를 (직전 폴더까지의 주소) + (파일이름) 으로 만들어서
# 읽어낼 수 있도록 하고 싶습니다.

# 저의 경우, 폴더의 주소는 아래와 같겠죠.
directory = 'D:/HJH/20220629 titanic keggle/Dataset/'

# 이제 파일 이름을 각각 지정해주면,
filename_2 = 'train.csv'
filename_3 = 'test.csv'

# 그럼 파일이름을 더하기로 나타낼 수 있습니다.
file_2 = directory + filename_2
file_3 = directory + filename_3

# 각각 읽어낼 수도 있죠
train_df = pd.read_csv(file_2)
test_df = pd.read_csv(file_3)

# 이걸로 읽는 것은 끝났네요.

#%% 2. 데이터 조회
# 
# 데이터를 넣었으니 필요한 데이터를 꺼낼 수 있어야겠죠. 
# 해당 데이터의 형태, 즉 사이즈는 2개의 숫자로 만들 수 있습니다.
# Variable explorer를 확인해보면,
# train_df의 Size는 891개의 행, 12개의 열로 이루어져 있네요.
# 이건 파이썬 그 자체로 알아냈다기 보다는, spyder의 기능을 통해 알아낸 거죠?
# 직접 알아내는 방법은, 그 자료한테 직접 물어보면 됩니다.
print(train_df.size)
# 엇. 이러면 10692가 나오네요. 이건 891 * 12니까 맞기는 하지만,
# 우리가 원한건 그 모양입니다. 그건 이렇게 불러내죠
print(train_df.shape)
# 이제 (891, 12)가 나오네요. 전체 모양을 한번 볼까요?
print(train_df)


# 좋아요. 이제 우리는 891명의 
# Id, 생사여부, 몇등석에 앉았는지, 성별, 나이,
# 타이타닉에 탄 (형제, 자매, 배우자)의 수, (부모님, 자녀)의 수,
# 티켓 번호, 티켓 값, 호실 번호, 승선지(배를 탄 곳) 을 알 수 있습니다.

# 먼저 아무나 한명 알아보자고요. 제 행운의 숫자는... 11.
# 11번 사람의 데이터를 다 보겠습니다.
# 역시 해당 자료에게 직접 물어보면 됩니다. 
print(train_df.loc[11])
# 사용하는 함수는 .loc 함수인데, (location 이라는 뜻? 일 듯?)
# 거기에 [11]을 뒤에 붙이면 11에 사는 데이터를 불러줍니다.
# 891개의 데이터가 있으니까. 0~890까지 주소가 있겠죠.

# 어쨌든 11에 사는 데이터는 58세의 Miss Elizabeth입니다.
# 살았고요, 가족은 아무도 안탔고요, 1등석이고요. 다 알았네요.

# 이번엔 그 데이터안에서 하나만 알아보고자 합니다.
# 먼저 아까 Miss. Elizabeth의 데이터를 하나의 변수에 넣어둘까요?
miss_elizabeth = train_df.loc[11]

# 이제 Miss. Elizabeth의 나이를 알아보겠습니다.
# 역시 그 자료에게 직접 물어보면 됩니다.
print(miss_elizabeth['Age'])
# 춘추가 58.0세네요.

# 그럼 이제 조회하는 방법은 다 알았습니다.

#%% 3. 간단한 알고리즘
#
# 데이터를 사용할 수 있다면 이제 가정을 증명할 시간입니다.
# 가정은 어쩌면 페미니즘적이지는 못하겠지만...
# 재난시 구조의 대상 선정의 제 1원칙으로 유명한
# "아이와 여자를 먼저 구하라"라는 말이 타이타닉 침몰 당시 지켜지기로 유명했잖아요?
# 이 말이 얼마나 사실 이었는지 알아봅시다.

# 일단, 남자가 몇명이었는지, 여자가 몇명이었는지 부터 세어 보자구요.
# 근데 어떻게 셀까요?
# .loc[0]부터 시작해서, 이사람이 남자였다면, 남자카운트를 1 더하고.
# 여자였다면, 여자카운트를 1 더하고. 이런식으로 해보겠습니다.

male_count = 0
female_count = 0

for i in range(len(train_df)) :
# 이건 for문입니다. 반복문이라고 합니다.
# 저는 목적이 이루어질때까지 계속되기 때문에 for라는 이름이 붙은 것 같아요.
# in은 i가 될 대상들입니다. 
# range는 0부터 내부숫자 까지 모든 숫자의 list를 만들어주는 함수구요.
# len은 내부변수의 길이를 숫자로 표시합니다.
# 그니까, 이건 0부터 890(train_df의 길이만큼)까지 숫자를 i에 순서대로 집어넣어서
# 아래에 있는 내용을 진행하겠다는 겁니다.
# 우리는 train_df의 모든 주소에 직접 하나씩 방문해서 남잔지 여잔지 확인할겁니다.
    sex = train_df.loc[i]['Sex']    
    
# 그럼 변수 sex가 남자라면 male_colunt를 1 더하고,
    if sex == 'male' :
        male_count = male_count + 1
# 아니면 female_count를 1 더하면 되겠죠.
    else :
        female_count = female_count + 1

# 잘됐나 확인해볼까요?
print(male_count, female_count)
# 남자는 577명, 여자는 314명. 더해서 891명 맞네요.


# 이번엔 남자산사람/남자죽은사람/여자산사람/여자죽은사람으로 해보죠.
male_live = 0
male_dead = 0
female_live = 0
female_dead = 0

for i in range(len(train_df)) :
    sex = train_df.loc[i]['Sex']
    survive = train_df.loc[i]['Survived']
    if sex == 'male' and survive == 1 :
        male_live += 1 # 이게 원래 변수에다가 1씩 더하는 간단한 공식입니다.
    elif sex == 'male' and survive == 0 :
        male_dead += 1
    elif sex == 'female' and survive == 1 :
        female_live += 1
    elif sex == 'female' and survive == 0 :
        female_dead += 1
        
print(male_live, male_dead, female_live, female_dead)
# 각각 109, 468, 233, 81.

# 그럼 남자 생존율, 여자 생존율을 내보면...
male_rate = male_live / male_count
female_rate = female_live / female_count

print(male_rate, female_rate)
# 18.9%, 74.2%. 확실한 차이가 있군요.


# 나이까지 해볼까요. 어린이의 기준을... 17살로 잡아보죠.
# 이때는 어린나이부터 성인으로 쳐줬으니까요.
male_kid_live = 0
male_kid_dead = 0
male_adult_live = 0
male_adult_dead = 0
female_kid_live = 0
female_kid_dead = 0
female_adult_live = 0
female_adult_dead = 0
# 이러한 자료구조는 원래 더 깔끔하게 하는 방법과 스킬들이 있지만...
# 이번에는 아주 직관적으로 가기로하죠.

for i in range(len(train_df)) :
    sex = train_df.loc[i]['Sex']
    survive = train_df.loc[i]['Survived']
    age = train_df.loc[i]['Age']
    
    if sex == 'male' and survive == 1 and age <= 17.0 :
        male_kid_live += 1
    elif sex == 'male' and survive == 0 and age <= 17.0 :
        male_kid_dead += 1
    elif sex == 'male' and survive == 1 and age >= 17.0 :
        male_adult_live += 1
    elif sex == 'male' and survive == 0 and age >= 17.0 :
        male_adult_dead += 1
    elif sex == 'female' and survive == 1 and age <= 17.0 :
        female_kid_live += 1
    elif sex == 'female' and survive == 0 and age <= 17.0 :
        female_kid_dead += 1
    elif sex == 'female' and survive == 1 and age >= 17.0 :
        female_adult_live += 1
    elif sex == 'female' and survive == 0 and age >= 17.0 :
        female_adult_dead += 1
        
# 먼저, 총 인원은 891, 남자는 577, 여자는 314였죠.
# 남자 애들은 몇명일까요? 남자 애들은 살거나 죽거나 했겠지요. 두개를 더하면 됩니다.
male_kid = male_kid_live + male_kid_dead
print(male_kid)
# 58명. 그중 얼마나 살았을까요?
print(male_kid_live)
# 23명... 39.7%의 생존율이네요. 전체 남자의 생존율은 18.9%, 유의한 차이가 있네요.

# 여자애들은요?
female_kid = female_kid_live + female_kid_dead
print(female_kid, female_kid_live)
# 55중 38, 69.1%, 이는 전체 여자인 74.2%보다 적네요.
# 이유가 뭘까요... 일단 샘플이 적죠. 
# 그래서 엄마 아빠가 없이 탔다거나, 가난했다거나 한 경우가 많아서
# 좀 많이 죽지 않았을까 싶네요. 이건 확인 안했습니다.

# 이런식으로 가정하는 거죠... 하지만 자세한 분석은 이렇게 하는게 아니기도 하고,
# 그럴 시간도 없으니까 그냥 그렇구나 하고 넘기겠습니다.

# 그래서, 대충 가정하자면, 여자는 다 살았고, 남자는 다 죽었다고 가정하겠습니다.

#%% 4. 데이터 아웃풋 / 제출
# 다음에 마저 쓰는걸로...

