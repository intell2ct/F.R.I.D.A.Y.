import matplotlib.pyplot as plt
import csv
import numpy as np
from matplotlib.gridspec import GridSpec

# 전세 데이터 처리
capitalAreaCharterCnt = 0  # 수도권 전세 데이터 카운터 초기화
provinceCharterCnt = 0  # 지방 전세 데이터 카운터 초기화
capitalAreaCharterSample = []  # 수도권 전세 샘플을 저장할 리스트
provinceCharterSample = []  # 지방 전세 샘플을 저장할 리스트
xbarCharterList = []  # x축 라벨을 저장할 리스트

# 'charter.csv' 파일을 읽고 데이터 처리
with open('charter.csv', 'r') as file:
    data = csv.reader(file)  # csv 파일을 읽기 위한 reader 생성
    header = next(data)  # 첫 번째 행은 헤더
    wholeCountryCharter = next(data)  # 두 번째 행은 전국 전세 데이터
    capitalAreaCharter = next(data)  # 세 번째 행은 수도권 전세 데이터
    provinceCharter = next(data)  # 네 번째 행은 지방 전세 데이터

    # 수도권 전세 데이터에서 4번째 데이터마다 샘플링
    for index in range(len(capitalAreaCharter)):
        capitalAreaCharterCnt += 1
        if capitalAreaCharterCnt % 4 == 2:  # 인덱스가 2일 때마다 샘플링
            capitalAreaCharterSample.append(capitalAreaCharter[capitalAreaCharterCnt])
    
    # 지방 전세 데이터에서 4번째 데이터마다 샘플링
    for index in range(len(provinceCharter)):
        provinceCharterCnt += 1
        if provinceCharterCnt % 4 == 2:  # 인덱스가 2일 때마다 샘플링
            provinceCharterSample.append(provinceCharter[provinceCharterCnt])
            xbarCharterList.append(header[provinceCharterCnt][2:7])  # x축 라벨 추가

# 월세 데이터 처리
capitalAreaMonthlyCnt = 0  # 수도권 월세 데이터 카운터 초기화
provinceMonthlyCnt = 0  # 지방 월세 데이터 카운터 초기화
capitalAreaMonthlySample = []  # 수도권 월세 샘플을 저장할 리스트
provinceMonthlySample = []  # 지방 월세 샘플을 저장할 리스트
xbarMonthlyList = []  # x축 라벨을 저장할 리스트

# 'monthly.csv' 파일을 읽고 데이터 처리
with open('monthly.csv', 'r') as file:
    data = csv.reader(file)  # csv 파일을 읽기 위한 reader 생성
    header = next(data)  # 첫 번째 행은 헤더
    wholeCountryMonthly = next(data)  # 두 번째 행은 전국 월세 데이터
    capitalAreaMonthly = next(data)  # 세 번째 행은 수도권 월세 데이터
    provinceMonthly = next(data)  # 네 번째 행은 지방 월세 데이터

    # 수도권 월세 데이터에서 4번째 데이터마다 샘플링
    for index in range(len(capitalAreaMonthly)):
        capitalAreaMonthlyCnt += 1
        if capitalAreaMonthlyCnt % 4 == 2:  # 인덱스가 2일 때마다 샘플링
            capitalAreaMonthlySample.append(capitalAreaMonthly[capitalAreaMonthlyCnt])
    
    # 지방 월세 데이터에서 4번째 데이터마다 샘플링
    for index in range(len(provinceMonthly)):
        provinceMonthlyCnt += 1
        if provinceMonthlyCnt % 4 == 2:  # 인덱스가 2일 때마다 샘플링
            provinceMonthlySample.append(provinceMonthly[provinceMonthlyCnt])
            xbarMonthlyList.append(header[provinceMonthlyCnt][2:7])  # x축 라벨 추가

# 데이터 시각화
plt.rc('xtick', labelsize=7)  # x축 틱 라벨의 글꼴 크기 설정
plt.rc('ytick', labelsize=7)  # y축 틱 라벨의 글꼴 크기 설정
plt.rc('axes', labelsize=7)  # 축 라벨의 글꼴 크기 설정
plt.rcParams['font.family'] = 'Malgun Gothic'  # 폰트 설정 (맑은 고딕)

fig = plt.figure(figsize=(10, 10))  # 10x10 크기의 figure 생성
gs = GridSpec(5, 1, height_ratios=[1, 1, 0.1, 1, 1], hspace=0.3)  # GridSpec 설정

# 수도권 전세 그래프
ax1 = fig.add_subplot(gs[0])
ax1.plot(list(map(int, capitalAreaCharterSample)), color='blue', label='수도권 전세')  # 데이터 플로팅
ax1.set_title('수도권/지방 전세 비교 그래프')  # 그래프 제목 설정
ax1.set_ylabel('(천원)', loc='top')  # y축 라벨 설정
ax1.set_xticks(np.arange(0, 36))  # x축 틱 설정
ax1.set_xticklabels([''] * 36)  # x축 라벨 비움
ax1.grid()  # 그리드 추가
ax1.legend()  # 범례 추가
ax1.set_ylim(4750, 5100)  # y축 범위 설정

# 지방 전세 그래프
ax2 = fig.add_subplot(gs[1])
ax2.plot(list(map(int, provinceCharterSample)), color='purple', label='지방 전세')
ax2.set_xlabel('(날짜)', loc='right')  # x축 라벨 추가
ax2.set_xticks(np.arange(0, 36))
ax2.set_xticklabels(xbarCharterList, rotation=45)  # x축 라벨 설정
ax2.grid()
ax2.legend()
ax2.set_ylim(2450, 2800)

# 수도권 월세 그래프
ax3 = fig.add_subplot(gs[3])
ax3.plot(list(map(int, capitalAreaMonthlySample)), color='red', label='수도권 월세')  # 데이터 플로팅
ax3.set_title('수도권/지방 월세 비교 그래프')  # 그래프 제목 설정
ax3.set_ylabel('(천원)', loc='top')  # y축 라벨 설정
ax3.set_xticks(np.arange(0, 36))  # x축 틱 설정
ax3.set_xticklabels([''] * 36)  # x축 라벨 비움
ax3.grid()  # 그리드 추가
ax3.legend()  # 범례 추가
ax3.set_ylim(690, 730)  # y축 범위 설정

#지방 월세 그래프
ax4 = fig.add_subplot(gs[4])
ax4.plot(list(map(int, provinceMonthlySample)), color='green', label='지방 월세')
ax4.set_xlabel('(날짜)', loc='right')
ax4.set_xticks(np.arange(0, 36))
ax4.set_xticklabels(xbarMonthlyList, rotation=45)
ax4.grid()
ax4.legend()
ax4.set_ylim(490, 530)

plt.show()
plt.close(fig)
