#!/usr/bin/env python
# coding: utf-8

# In[122]:


# 라이브러리 가져오기
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
get_ipython().run_line_magic('config', "InlineBackend.figure_format = 'retina'")
# print('슝=3')

# 데이터셋 pandas로 불러오기
"""
오류
import os
csv_path = os.getenv("HOME") +"/aiffel/pokemon_eda/data/Pokemon.csv"
original_data = pd.read_csv(csv_path)
print('슝=3')
"""
csv_path = "./data/Pokemon.csv" 
original_data = pd.read_csv(csv_path)
# print(original_data)
# print('슝=3')

#복사본 만들기
pokemon = original_data.copy()
# print(pokemon.shape) 
# 데이터셋의 크기 출력, 결과값 : (800, 13) 포켓몬 800마리와13개의 특성
# pokemon.head() # 상위 5개의 행을 출력

# 전설의 포켓몬 데이터셋
legendary = pokemon[pokemon["Legendary"] == True].reset_index(drop=True)
# print(legendary.shape) # 결과값 (65, 13) 65개가 전설
# legendary.head()

# 일반 포켓몬의 데이터셋
ordinary = pokemon[pokemon["Legendary"] == False].reset_index(drop=True)
# print(ordinary.shape) # 결과값 (735, 13) 전설 65개 일반 735개 총 800개
# ordinary.head()

# 데이터셋을 불러왔으니, 데이터셋을 분석해야함

# 1.1 빈 데이터(결측치) 확인
pokemon.isnull().sum() # 열 단위로 결측값 개수를 합산하여 결측값 분포를 확인
# 결측치가 Type 2에만 386개가 있음.

# 1.2 전체 컬럼 이해하기
# print(len(pokemon.columns))
# pokemon.columns

# 2.1  "# : ID number"
# len(set(pokemon["#"])) # 721 전체 데이터는 800개니까 중복데이터가 있다는 것을 뜻함
# pokemon[pokemon["#"] == 6]
# 2.2 Name
len(set(pokemon["Name"])) # 800개의 고유한 값을 가짐

# 3 1 Type 1 & Type 2 포켓몬의 속성
# pokemon.loc[[6, 10]] 
# len(list(set(pokemon["Type 1"]))), len(list(set(pokemon["Type 2"]))) 
# Type 1은 18개의 속성, Type 2는 19개의 속성을 가진다. 어떤 속성이 한가지 더 많을까?
set(pokemon["Type 2"]) - set(pokemon["Type 1"]) # 차칩합으로 확인 가능!
# NaN 데이터 외의 나머지 속성은 모두 같은 세트의 데이터가 들어가 있음
types = list(set(pokemon["Type 1"]))
# print(len(types)) # 18개의 속성을 가짐
# print(types) 
"""
['Grass', 'Poison', 'Normal', 'Bug', 'Fairy', 'Ghost', 
'Steel', 'Ground', 'Electric', 'Psychic', 'Rock', 'Ice', 
'Dragon', 'Dark', 'Fire', 'Flying', 'Water', 'Fighting']
"""
# NaN 값을 구하고 싶을 때 isna() 함수를 씀
# pokemon["Type 2"].isna().sum()  # 하나의 속성 386개, 두 개의 속성 414개

# 3.2 Type 1 데이터 분포 plot
"""
# 첫 번째 그래프: 일반 포켓몬(Type 1 분포)

plt.figure(figsize=(10, 7))  # 전체 그래프의 크기를 (10, 7)로 설정

plt.subplot(211) # 첫 번째 서브플롯(2행 1열 중 첫 번째)
sns.countplot(data=ordinary, x="Type 1", order=types).set_xlabel('') # Type 1의 개수를 세어서 막대그래프 출력
plt.title("[Ordinary Pokemons]") # 그래프 제목 설정

# 두 번째 그래프: 전설의 포켓몬(Type 1 분포)

plt.subplot(212) # 두 번째 서브플롯(2행 1열 중 두 번째)
sns.countplot(data=legendary, x="Type 1", order=types).set_xlabel('') # Type 1의 개수를 세어서 막대그래프 출력
plt.title("[Legendary Pokemons]") # 그래프 제목 설정
plt.show() 
# 일반 포켓몬은 물, 노멀, 벌레 속성이 많고, 전설 포켓몬은 드레곤과 사이킥 속성이 많음 

# Type1별로 Legendary의 비율을 보여주는 피벗 테이블

pd.pivot_table(pokemon, index="Type 1", values="Legendary").sort_values(by=["Legendary"], ascending=False)
# 플라잉 속성이 50%로 가장 높음
"""

# 3.3 Type 2 데이터 분포 plot
"""
plt.figure(figsize=(12, 10))  # 화면 해상도에 따라 그래프 크기를 조정

# 첫 번째 그래프: 일반 포켓몬(Type 2 분포)
plt.subplot(211)  # 첫 번째 서브플롯 (2행 1열 중 첫 번째)
sns.countplot(data=ordinary, x="Type 2", order=sorted(set(pokemon["Type 2"].dropna()))).set_xlabel('')  
plt.title("[Ordinary Pokemons]")  # 그래프 제목 설정

# 두 번째 그래프: 전설의 포켓몬(Type 2 분포)
plt.subplot(212)  # 두 번째 서브플롯 (2행 1열 중 두 번째)
sns.countplot(data=legendary, x="Type 2", order=sorted(set(pokemon["Type 2"].dropna()))).set_xlabel('')  
plt.title("[Legendary Pokemons]")  # 그래프 제목 설정

plt.show()  # 그래프 출력

# Type2별로 Legendary의 비율을 보여주는 피벗 테이블
pd.pivot_table(pokemon, index="Type 2", values="Legendary").sort_values(by=["Legendary"], ascending=False)
# 불 속성이 25%로 가장 높음
"""

# 4. 모든 스탯의 총합

# 4.1 Total:모든 스탯의 총합
stats = ["HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed"] # 포켓몬의 스탯 열을 리스트로 저장
"""
# total 값과 sum of all stats 값이 같은지 검증
print("#0 pokemon: ", pokemon.loc[0, "Name"]) # 인덱스 0번 포켓몬의 이름 출력
print("total: ", int(pokemon.loc[0, "Total"])) # 첫 번째 포켓몬의 총 능력치(Total) 출력
print("stats: ", list(pokemon.loc[0, stats])) # 첫 번째 포켓몬의 개별 능력치 출력
print("sum of all stats: ", sum(list(pokemon.loc[0, stats]))) # 첫 번째 포켓몬의 개별 능력치 합산값 출력

# Total 값과 개별 스탯의 합이 같은 포켓몬 수 확인 
sum(pokemon["Total"].values == pokemon[stats].sum(axis=1).values) # 800개로 다 같음
"""

# 4.2 Total값에 따른 분포 plot
"""
fig, ax = plt.subplots() # 그래프 fig와 ax 생성
fig.set_size_inches(12, 6) # 그래프 크기를 (12, 6)으로 설정

# Scatter Plot 생성
sns.scatterplot(data=pokemon, x="Type 1", y="Total", hue="Legendary")
# - x축: 포켓몬의 Type 1
# - y축: 포켓몬의 Total
# - hue="Legendary": 전설 포켓몬과 일반 포켓몬을 색상으로 구분
plt.show() # 총 스탯 값이 매우 높음
"""
# 5. 세부 스탯
# 5.1 세부스탯: HP, Attack, Defense, Sp. Atk, Sp. Def, Speed
"""
figure, ((ax1, ax2), (ax3, ax4), (ax5, ax6)) = plt.subplots(nrows=3, ncols=2)
figure.set_size_inches(12, 18)  # 화면 해상도에 따라 그래프 크기를 조정해 주세요.

# "HP" 스탯의 scatter plot
sns.scatterplot(data=pokemon, y="Total", x="HP", hue="Legendary", ax=ax1)

# "Attack" 스탯의 scatter plot
sns.scatterplot(data=pokemon, y="Total", x="Attack", hue="Legendary", ax=ax2)

# "Defense" 스탯의 scatter plot
sns.scatterplot(data=pokemon, y="Total", x="Defense", hue="Legendary", ax=ax3)

# "Sp. Atk" 스탯의 scatter plot
sns.scatterplot(data=pokemon, y="Total", x="Sp. Atk", hue="Legendary", ax=ax4)

# "Sp. Def" 스탯의 scatter plot
sns.scatterplot(data=pokemon, y="Total", x="Sp. Def", hue="Legendary", ax=ax5)

# "Speed" 스탯의 scatter plot
sns.scatterplot(data=pokemon, y="Total", x="Speed", hue="Legendary", ax=ax6)

plt.show() 
# HP, Defense, Sp. Def 는 전설보다 일반 포켓몬이 더 높은 스탯을 가지는 경우도 있음
# Attack, Sp. Atk, Speed 는 전설이 최대치를 차지하고 있음
"""

# 6. 세대
"""
plt.figure(figsize=(12, 10))  
# 첫 번째 그래프: 일반 포켓몬의 세대(Generation) 분포
plt.subplot(211)
sns.countplot(data=ordinary, x="Generation").set_xlabel('')
plt.title("[Ordinary Pokemons]")
plt.subplot(212)
# 두 번째 그래프: 전설의 포켓몬의 세대(Generation) 분포
sns.countplot(data=legendary, x="Generation").set_xlabel('')
plt.title("[Legendary Pokemons]")
plt.show()
# 전설의 포켓몬은 1, 2 세대에는 많지 않음.
"""

# 1.11. 전설의 포켓몬과 일반 포켓몬, 그 차이는? 
# 목표는 전설과 일반을 분류하는 것, 특징들을 세분화해서 확인
"""
# 1.11.1 전설의 포켓몬 Total 값

fig, ax = plt.subplots()
fig.set_size_inches(8, 4)

sns.scatterplot(data=legendary, y="Type 1", x="Total")
plt.show()
# Total 값들이 같은 값을 가지는 경우가 많다.

# 전설이 가지는 Total 값 확인
print(sorted(list(set(legendary["Total"])))) # [580, 600, 660, 670, 680, 700, 720, 770, 780] 9개의 값

# 그래프로 확인
fig, ax = plt.subplots()
fig.set_size_inches(8, 4)

sns.countplot(data=legendary, x="Total")
plt.show() # 총 65마리의 전설 포켓몬이 9개의 Total 값만 가진다.

round(65 / 9, 2) # 7.22 : 7.22 포켓몬 끼리는 같은 스탯값을 가진다.

# 1.11.2 일반 포켓몬 Total 값

# ordinary 포켓몬의 'Total' 값 집합
print(sorted(set(ordinary["Total"])))

# 이 집합의 크기(길이)
print(len(set(ordinary["Total"]))) # 195개
round(735 / 195, 2) # 3.77 포켓몬만 같은 Total 스탯을 가짐
# 전설의 Total 값은 다양하지 않고, 전설의 Total 값 중에는 일반이 가지지 못하는 값이 존재
# Total 값은 전설인지 아닌지를 예측하는 중요한 컬럼

# 이름에서의 차이
n1, n2, n3, n4, n5 = legendary[3:6], legendary[14:24], legendary[25:29], legendary[46:50], legendary[52:57]
names = pd.concat([n1, n2, n3, n4, n5]).reset_index(drop=True)
names # 비슷한 이름이 많음, 세트로 이름이 지어져 있는 경우가 많음

formes = names[13:23]
formes # formes 가 들어가있는 이름도 많음, formes 이름은 전설일 확률이 높음
"""

# 전설 name_count 컬럼 생성
legendary["name_count"] = legendary["Name"].apply(lambda i: len(i))    
# legendary.head()

# 일반 name_count 컬럼 생성
ordinary["name_count"] = ordinary["Name"].apply(lambda i: len(i))
# ordinary.head()

"""
# name_count 그래프
plt.figure(figsize=(12, 10))   # 화면 해상도에 따라 그래프 크기를 조정해 주세요.

plt.subplot(211)
sns.countplot(data=legendary, x="name_count").set_xlabel('')
plt.title("Legendary")
plt.subplot(212)
sns.countplot(data=ordinary, x="name_count").set_xlabel('')
plt.title("Ordinary")
plt.show()
# 전설은 16자리 이상의 이름이 다수
# 일반은 10자리 이상의 이름이 소수

# 전설의 이름이 10자리 이상일 확률 : 41.54 %
print(round(len(legendary[legendary["name_count"] > 9]) / len(legendary) * 100, 2), "%")

# 일반의 이름이 10자리 이상일 확률 : 15.65 %
print(round(len(ordinary[ordinary["name_count"] > 9]) / len(ordinary) * 100, 2), "%")

# 만약 "Latios"가 전설의 포켓몬이라면, "%%% Latios" 또한 전설의 포켓몬이다!
# 적어도 전설의 포켓몬에서 높은 빈도를 보이는 이름들의 모임이 존재한다!
# 전설의 포켓몬은 긴 이름을 가졌을 확률이 높다!
"""
# 데이터 전처리 : 이름의 길이(10글자 이상)
pokemon["name_count"] = pokemon["Name"].apply(lambda i: len(i))
# pokemon.head()

pokemon["long_name"] = pokemon["name_count"] >= 10
# pokemon.head()

# 데이터 전처리 : 토큰 추출
"""
한 단어면 ex. Venusaur
두 단어이고, 앞 단어는 두 개의 대문자를 가지며 대문자를 기준으로 두 부분으로 나뉘는 경우 ex. VenusaurMega Venusaur
이름은 두 단어이고, 맨 뒤에 X, Y로 성별을 표시하는 경우 ex. CharizardMega Charizard X
알파벳이 아닌 문자를 포함하는 경우 ex. Zygarde50% Forme
"""
# 띄워쓰기를 빈칸으로 처리
pokemon["Name_nospace"] = pokemon["Name"].apply(lambda i: i.replace(" ", ""))
# pokemon.tail()

# 이름이 알파벳로 이루어 졌는지 아닌지 판별
pokemon["name_isalpha"] = pokemon["Name_nospace"].apply(lambda i: i.isalpha())
# pokemon.head()

# 알파벳이 아니니 다른 문자가 이름에 포함된 것 : 9마리
# print(pokemon[pokemon["name_isalpha"] == False].shape)
pokemon[pokemon["name_isalpha"] == False]

# 9마리의 이름을 대체
pokemon = pokemon.replace(to_replace="Nidoran♀", value="Nidoran X")
pokemon = pokemon.replace(to_replace="Nidoran♂", value="Nidoran Y")
pokemon = pokemon.replace(to_replace="Farfetch'd", value="Farfetchd")
pokemon = pokemon.replace(to_replace="Mr. Mime", value="Mr Mime")
pokemon = pokemon.replace(to_replace="Porygon2", value="Porygon Two")
pokemon = pokemon.replace(to_replace="Ho-oh", value="Ho Oh")
pokemon = pokemon.replace(to_replace="Mime Jr.", value="Mime Jr")
pokemon = pokemon.replace(to_replace="Porygon-Z", value="Porygon Z")
pokemon = pokemon.replace(to_replace="Zygarde50% Forme", value="Zygarde Forme")

pokemon.loc[[34, 37, 90, 131, 252, 270, 487, 525, 794]]

# 바꿔준 'Name' 컬럼으로 'Name_nospace'를 만들고, 다시 isalpha()로 체크
# 바꿔준 'Name' 컬럼을 사용하여 'Name_nospace' 다시 생성
pokemon["Name_nospace"] = pokemon["Name"].apply(lambda i: i.replace(" ", ""))
# 다시 isalpha()로 알파벳 여부 체크
pokemon["name_isalpha"] = pokemon["Name_nospace"].apply(lambda i: i.isalpha())
pokemon[pokemon["name_isalpha"] == False]
# name_isalpha 컬럼이 False인 컬럼이 없음 
# 모든 이름이 알파벳으로만 이루어졌음을 뜻함

# 토큰화 함수 만들기
import re

name = "CharizardMega Charizard X"

def tokenize(name):
    tokens = []  # 토큰을 저장할 리스트
    name_split = name.split(" ")  # 공백 기준으로 분리
    for part_name in name_split:
        a = re.findall('[A-Z][a-z]*', part_name)  # 대문자로 시작하는 단어 추출
        tokens.extend(a)
    return np.array(tokens)

# name = "CharizardMega Charizard X"
# tokenize(name)

# 전설 이름에 적용
all_tokens = list(legendary["Name"].apply(tokenize).values)

token_set = []
for token in all_tokens:
    token_set.extend(token)

# print(len(set(token_set)))
# print(token_set)

# Counter를 이용하여 어떤 토큰이 가장 많이 쓰이는지 찾기
from collections import Counter

most_common = Counter(token_set).most_common(10) 
# most_common

# 전설 이름에 등장하는 토큰이 포켓몬 이름에 있는지 여부를 나타내는 컬럼 만들기
for token, _ in most_common:
    # pokemon[token] = ... 형식으로 사용하면 뒤에서 warning이 발생합니다
    pokemon[f"{token}"] = pokemon["Name"].str.contains(token)
# pokemon.head(10)

#데이터 전처리 : Type1 & 2 범주형 데이터 전처리
# print(types) # 타입 확인

for t in types:
    pokemon[t] = (pokemon["Type 1"] == t) | (pokemon["Type 2"] == t)
    
# pokemon[[["Type 1", "Type 2"] + types][0]].head()


# 원본데이터 불러오기
# print(original_data.shape)
original_data.head()

original_data.columns


features = ['Total', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', 'Generation']
target = 'Legendary'

# original_data'에서 'features' 컬럼에 해당하는 데이터를 변수 'X'에 저장
X = original_data[features]
# print(X.shape)
# X.head()

# 'target' 컬럼의 데이터를 변수 'y'에 저장
y = original_data[target]
# print(y.shape)
# y.head()

# 훈련 데이터 640개와 학습 데이터 160개로 분리
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=15)

# print(X_train.shape, y_train.shape)
# print(X_test.shape, y_test.shape)

# 의사 결정 트리 모델 학습
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier(random_state=25) # random_state는 모델의 랜덤성을 제어

model.fit(X_train, y_train)
y_pred = model.predict(X_test)

from sklearn.metrics import confusion_matrix
confusion_matrix(y_test, y_pred)
"""
array([[144,   3],
       [  5,   8]])
144 가 의미하는 것 : 일반 포켓몬을 일반 포켓몬이라고 알맞게 판단한 경우 (TN)
3 이 의미하는 것 : 일반 포켓몬을 전설의 포켓몬이라고 잘못 판단한 경우 (FP)
5 가 의미하는 것 : 전설의 포켓몬을 일반 포켓몬이라고 잘못 판단한 경우 (FN)
8 이 의미하는 것 : 전설의 포켓몬을 전설의 포켓몬이라고 알맞게 판단한 경우 (TP)

160개의 학습 데이터 중 3+5=8개 가 틀렸으니 나쁘지 않은 결과
152 / 160 * 100 = 정확도 95%
정확도만 믿으면 안되는 함정이 있는데 바로 이 데이터셋이 불균형한 데이터이기 때문임
전체 데이터 800마리 중 65마리만 전설. 따라서 모두 일반 포켓몬이라고 찍어도
92%의 정확도를 달성할 수 있음. 따라서 다른 척도로 성능을 평가해야 함
"""
# 모델 평가 classification_report 활용
from sklearn.metrics import classification_report
# print(classification_report(y_test, y_pred))
"""
 precision    recall  f1-score   support

       False       0.97      0.98      0.97       147
        True       0.73      0.62      0.67        13

    accuracy                           0.95       160
   macro avg       0.85      0.80      0.82       160
weighted avg       0.95      0.95      0.95       160

리콜 값이 낮다는 것은 전설을 일반으로 판단하는 경우가 많다는 사실
"""

# 피쳐 엔지니어링 데이터로 학습하면 얼마나 차이가 날까?

# print(len(pokemon.columns))
# print(pokemon.columns)

# 컬럼을 제외(머신러닝 모델에 문자열을 입력할 수 없음)
features = ['Total', 'HP', 'Attack', 'Defense','Sp. Atk', 'Sp. Def', 'Speed', 'Generation', 
            'name_count','long_name', 'Forme', 'Mega', 'Mewtwo','Deoxys', 'Kyurem', 'Latias', 'Latios',
            'Kyogre', 'Groudon', 'Hoopa','Poison', 'Ground', 'Flying', 'Normal', 'Water', 'Fire',
            'Electric','Rock', 'Dark', 'Fairy', 'Steel', 'Ghost', 'Psychic', 'Ice', 'Bug', 'Grass', 'Dragon', 'Fighting']

# len(features) : 38

# 정답 데이터 준비
target = "Legendary"
# target

# 사용할 feature에 해당하는 데이터를 'X' 변수에 저장
X = pokemon[features]
# print(X.shape)
# X.head()

# 정답 데이터 'y'.
y = pokemon[target]
# print(y.shape)
# y.head()

# X_train y_test 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=15)

# print(X_train.shape, y_train.shape)
# print(X_test.shape, y_test.shape)

# 의사 결정 트리를 활용하여 학습
model = DecisionTreeClassifier(random_state=25)
# model

# 모델 학습
model.fit(X_train, y_train)

# 예측 수행
y_pred = model.predict(X_test)

# 예측 결과 출력 (일부 샘플)
# print(y_pred[:10]) # [ True False  True False False False False False False False]

# confusion matrix 확인
confusion_matrix(y_test, y_pred)
"""
array([[141,   6],
       [  1,  12]])
"""
# classification 확인
classification_report(y_test, y_pred) # 리콜값이 0.62에서 0.92까지 올라감
# 데이터 처리만으로 좋은 결과를 만들어 낼 수 있음


# In[ ]:





# In[ ]:




