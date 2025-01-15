# Drwosiness
 졸음감지

- python, OpenCV 기반 졸음 감지 프로그램
- HOG + Linear SVM을 이용하여 얼굴을 Detection 하고  Eensamble of Reguration Tree 모델을 이용하여 눈동자를 Detection 한다. 
- 탐지된 눈동자의 가로, 세로의 거리를 Euclidean 거리로 구하고  가로 세로 종횡 비율이 일정 값 이하가 되면 "눈 감김"으로 판단하는 기본적인 ML 모델과 알고리즘으로 개발되었다.  
- 참조 사이트:  https://blog.naver.com/tory0405/223133963646
  
![image](https://github.com/user-attachments/assets/bb261bab-b024-418e-854c-e35250df0676)
![image](https://github.com/user-attachments/assets/b5dbc142-6c67-43ee-9dd4-b510f105a58c)

