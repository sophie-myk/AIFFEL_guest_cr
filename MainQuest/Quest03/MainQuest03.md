## 1. 개요
폐렴은 전 세계적으로 발생률과 사망률이 높은 호흡기 잘환으로   
빠르고 정확하게 진단해야하기 위해서는 환자의 흉부 X-ray 이미지를 판독하는   
전문가의 숙련도가 매우 중요하다. 최근 의료 분야에서 인공지능 기술,  
특히 딥러닝을 활용한 영상 진단 보조가 활발히 연구되고 있다.  

## 2. 목적
CNN 기반을 Base Model로 구현해서 X-ray 이미지를 분류할 수 있는 CNN 모델을 구축한다.
의료분야는 데이터가 부족하기 때문에 Data Augmentation 을 적용해서 데이터 수를 늘리는 작업이 필요하다.  
Normal Data 와 Augmented Data를 Base Model에 동일하게 적용해서 성능을 비교해본다.

## 3. 목차
1. 개요
2. 목적
3. 목차
4. 실습코드
5. 실습결과
6. Summary
7. 회고

## 4. 실습코드

### A. [CNN Base Model](https://github.com/Mchoon84/AIFFEL_guest_cr/blob/main/MainQuest/Quest03/MainQuest03-1_CNN_BaseModel.ipynb)
#### (1) Set-up
#### (2) 데이터 가져오기
#### (3) 데이터 시각화
#### (4) CNN 모델링
#### (5) 데이터 imbalance 처리
#### (6) 모델 훈련
#### (7) 결과 확인

### B. [Augmented CNN](https://github.com/Mchoon84/AIFFEL_guest_cr/blob/main/MainQuest/Quest03/MainQuest03-2_Augmented_CNN.ipynb)
### C. [ResNet18](https://github.com/Mchoon84/AIFFEL_guest_cr/blob/main/MainQuest/Quest03/MainQuest03-3_ResNet18.ipynb)

## 5. 실습결과
CNN Base Model  
![image](https://github.com/user-attachments/assets/c0a8479a-bc7c-4448-90c9-bf34833a85d7)  
Loss: 1.6094
상대적으로 높은 편.  
모델이 예측을 하는 데 있어 아직 불확실성이 많거나, 충분히 학습되지 못한 상태.  

Accuracy (정확도): 0.689  
약 68.9%로, 분류 문제에서 ‘무작위 추측’보다는 낫지만, 여전히 만족스럽지 않은 수준.  

Precision (정밀도): 0.668  
“양성(폐렴)이라고 예측한 사례 중 실제로 양성인 비율”이 약 66.8%  
즉, 양성으로 예측했을 때 실제 양성이 아닐 확률도 약 33%.  

Recall (재현율): 0.997  
매우 높은 재현율로, 실제 양성(폐렴)을 놓치는 경우가 거의 없음.  
그러나 이처럼 극단적으로 높은 재현율이 나오면서, 동시에 정확도(Accuracy)와 정밀도(Precision)가 낮은 것은  
양성을 과다 예측(False Positive가 많음)하는 경향 때문일 수 있음.  

Recall은 극도로 높으나 Precision과 Accuracy가 낮게 나타나기 때문에  
이 모델은 양성을 놓치지 않기 위해 과도하게 양성으로 예측한다고 볼 수 있다.  
의료분야에서 Recall의 수치가 높은 것은 의미가 있지만,  
음성을 양성으로 판단하는 경우도 많다는 것을 반증한다.  
따라서 Precision과 Accuracy를 높여야 실제로 쓸 수 있을 것이다.  


Augmented CNN  
![image](https://github.com/user-attachments/assets/630650cb-94d9-4a17-b55d-2b32cee3c801)  

Loss: 0.408 (정도)  
비교적 낮은 손실값으로, 모델의 예측이 안정적임.  

Accuracy (정확도): 약 0.878 (87.8%)  
의사들이 정확도가 약 90% 정도라고 하니 괜찮은 수치.  

Precision (정밀도): 약 0.865  
양성(폐렴)이라고 예측한 사례 중 실제로 양성인 비율”이 86.5%  
이전 모델에 비교해 많이 좋아짐.  

Recall (재현율): 약 0.954  
거의 대부분의 폐렴 환자를 놓치지 않고 양성으로 예측  

정확도가 기존 0.689(베이스 모델)에서 0.878로 크게 향상되었고    
Precision이 0.668 → 0.865로 증가해 양성 예측 시 오진이 크게 줄어들었다.  
Recall은 0.997 → 0.954로 조금 낮아졌지만, 여전히 95% 이상으로 매우 우수하다.  
결과적으로, Precision과 Recall 둘 다 높은 수준에서 균형을 이룬 모델이고  
손실(Loss)도 크게 줄어들어 학습이 더욱 안정적으로 이뤄졌음을 알 수 있다.  

데이터 증강을 통해 학습 데이터 다양성을 확보함으로써, 과적합이 줄고 일반화 성능이 향상된 것 같다.  
이전 베이스 모델은 정밀도(Precision)와 정확도(Accuracy)가 낮았던 반면,  
증강을 적용하니 Accuracy와 Precision, Recall 모두 고르게 높은 결과가 나왔다.  

ResNet18  
![image](https://github.com/user-attachments/assets/50b3a891-c0db-49bb-9d49-05d27ba7b7db)  

Loss: 약 0.752  
증강 CNN 모델(0.408)보다는 높고, 베이스 모델(1.609)보다는 낮은 편  
아직 예측 과정에서 다소 오차가 존재함  

Accuracy (정확도): 약 0.777  
전체적인 분류 정확도가 77.7% 정도이며, 증강 CNN 모델(87.8%)에 비해서는 낮음  

Precision (정밀도): 약 0.925  
양성(폐렴)이라고 예측한 사례 중 실제로 양성인 비율이 매우 높음
세 모델 중에서 Precision이 가장 높은 결과일 수 있습니다  
(양성으로 예측 시 적중률이 매우 높다는 뜻)  

Recall (재현율): 0.700  
실제 양성(폐렴)을 얼마나 놓치지 않고 잡아내는가를 나타내는데, 70%로 상대적으로 낮음
즉, 실제 양성이지만 음성으로 잘못 예측될 확률이 높아서  
Recall이 높아야하는 의학 분야에는 적합하지 않는 것으로 보임  

![image](https://github.com/user-attachments/assets/5df25736-36fd-4cf8-beb3-f690479e4949)  

## 6. Summary  
Augmented CNN 이 전반적인 정확도(Accuracy)가 가장 높고,  
Precision과 Recall 모두 0.85~0.95대로 고르게 우수하며,  
Base Model 대비 Recall은 조금 낮아졌지만(0.997→0.954),  
Precision이 크게 개선되어 균형 잡힌 모델이었다.  
세 모델 중 가장 안정적이고 높은 종합 성능을 보여주었다.  

## 7. 회고
"시간이 남았다면 질 좋은 데이터 더 확보하는데 시간을 쏟아라"  
는 말이 증명이 된 것 같다.  
데이터의 절대적인 양이 부족할 수 밖에 없는 의료 분야에서는  
Data Augmentation 은 필수적으로 해야겠다고 생각했다.  

실제로 모델을 구현해보고, 데이터 증강, 모델 변경도 해보면서  
많은 것을 배울 수 있었다.  
지난 프로젝트에서 Accuracy 를 높이는게 쉽지 않다고 생각했는데,  
조금씩 배워가면서 어렵지만 해낼수 있겠다는 자신감이 생긴다. 
