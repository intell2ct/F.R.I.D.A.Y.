import matplotlib.pyplot as plt
import csv
import numpy as np

# 해당 list의 특정 index값만 추출하기위한 Cnt 
capitalAreaCharterCnt = 0
provinceCharterCnt = 0
# 특정 index의 값들만을 추출하여 저장한 list
capitalAreaCharterSample = []
provinceCharterSample = []

# x축에 표시할 항목의 이름을 저장한 리스트(일자)
xbarCharterList = []

# 파일 가공처리 부분
with open( 'charter.csv', 'r') as file :
    data = csv.reader(file)
    # 헤더 - 연도별 항목들을 출력
    header = next(data)
    # 전체항목 - 전 지역의 전세값을 더하여 나타내는 데이터
    wholeCountryCharter = next(data)
    # 수도권의 전세값들을 나타내는 데이터
    capitalAreaCharter = next(data)
    # 지방의 전세값들을 나타내는 데이터
    provinceCharter = next(data)

    # 반복문을 통하여 수도권데이터에서 원하는 값만을 추출
    for index in range(len(capitalAreaCharter)) :
        # 횟수를 증가시키고 증가한 횟수에 따른 조건을 통해 원하는 데이터를 추출하여 저장
        capitalAreaCharterCnt += 1
        if capitalAreaCharterCnt % 4 == 2 :
            capitalAreaCharterSample.append(capitalAreaCharter[capitalAreaCharterCnt])
    # 반복문을 통하여 지방데이터에서 원하는 값만을 추출
    for index in range(len(provinceCharter)) :
        # 횟수를 증가시키고 증가한 횟수에 따른 조건을 통해 원하는 데이터를 추출하여 저장
        provinceCharterCnt += 1
        if provinceCharterCnt % 4 == 2 :
            provinceCharterSample.append(provinceCharter[provinceCharterCnt])
            # x축에 일자를 나타내기위해 header에서 해당 일자를 추출하여 가공 및 저장
            xbarCharterList.append(header[provinceCharterCnt][2:7])

# 데이터 시각화 부분
plt.rc('xtick', labelsize=7)  # x축 눈금 폰트 크기
plt.rc('ytick', labelsize=7)  # x축 눈금 폰트 크기
plt.rc('axes', labelsize=7)   # x,y축 label 폰트 크기

# Runtime Configuration Parameters의 dict데이터에 폰트를 변경하기위한 설정
# 해당 설정을 통해 한글출력가능
plt.rcParams['font.family'] = 'Malgun Gothic'

# pyplot의 그래프는 figure와 Ax로 구성
# (Ax)그래프가 들어가는 figure(액자)를 미리 선언
fig = plt.figure()

# subplot()을 통하여 액자안에 여러개의 그래프 추가 가능
# 수도권의 전세 그래프를 시각화
ax1 = fig.add_subplot(2,1,1)
ax1.plot(list(map(int, capitalAreaCharterSample)), color='blue', label='수도권 전세')
plt.title('수도권/지방 전세 비교 그래프')
plt.ylabel('(천원) ', loc='top') # y라벨 추가 
plt.xticks(np.arange(0,36), xbarCharterList)# x축 항목값 설정
plt.grid() # 격자무늬 추가
plt.legend() # 범례 추가

# 지방의 전세 그래프를 시각화
ax2 = fig.add_subplot(2,1,2)
ax2.plot(list(map(int, provinceCharterSample)), color='purple', label='지방 전세')
plt.xlabel('(날짜)', loc='right') # x라벨 추가
plt.xticks(np.arange(0,36), xbarCharterList)# x축 항목값 설정
plt.grid() # 격자무늬 추가
plt.legend() # 범례 추가

fig.subplots_adjust(hspace = 0.1) # 두 그래프 사이의 상하 간격 설정

# 두 그래프 사이의 간격차를 나타내기 위한 불필요한  요소 제거
ax1.spines.bottom.set_visible(False)
ax2.spines.top.set_visible(False)
ax1.xaxis.tick_top()
ax1.tick_params(labeltop=False)
ax2.xaxis.tick_bottom()

# 각 그래프별 나타낼 y축 범위 설정
ax1.set_ylim(4750, 5100) # 위 그래프 y축 범위 설정
ax2.set_ylim(2450, 2800) # 아래 그래프 y축 범위 설정

# 그래프 출력
plt.show()

## =====================================================

# 해당 list의 특정 index값만 추출하기위한 Cnt 
capitalAreaMonthlyCnt = 0
provinceMonthlyCnt = 0

# 특정 index의 값들만을 추출하여 저장한 list
capitalAreaMonthlySample = []
provinceMonthlySample = []

# x축에 표시할 항목의 이름을 저장한 리스트(일자)
xbarMonthlyList = []

# 파일 가공처리 부분
with open( 'monthly.csv', 'r') as file :
    data = csv.reader(file)
    # 헤더 - 연도별 항목들을 출력
    header = next(data)
    # 전체항목 - 전 지역의 월세값을 더하여 나타내는 데이터
    wholeCountryMonthly = next(data)
    # 수도권의 월세값들을 나타내는 데이터
    capitalAreaMonthly = next(data)
    # 지방의 월세값들을 나타내는 데이터
    provinceMonthly = next(data)

    # 반복문을 통하여 수도권데이터에서 원하는 값만을 추출
    for index in range(len(capitalAreaMonthly)) :
        # 횟수를 증가시키고 증가한 횟수에 따른 조건을 통해 원하는 데이터를 추출하여 저장
        capitalAreaMonthlyCnt += 1
        if capitalAreaMonthlyCnt % 4 == 2 :
            capitalAreaMonthlySample.append(capitalAreaMonthly[capitalAreaMonthlyCnt])
    # 반복문을 통하여 지방데이터에서 원하는 값만을 추출
    for index in range(len(provinceMonthly)) :
        # 횟수를 증가시키고 증가한 횟수에 따른 조건을 통해 원하는 데이터를 추출하여 저장
        provinceMonthlyCnt += 1
        if provinceMonthlyCnt % 4 == 2 :
            provinceMonthlySample.append(provinceMonthly[provinceMonthlyCnt])
            # x축에 일자를 나타내기위해 header에서 해당 일자를 추출하여 가공 및 저장
            xbarMonthlyList.append(header[provinceMonthlyCnt][2:7])

# 데이터 시각화 부분
plt.rc('xtick', labelsize=7)  # x축 눈금 폰트 크기
plt.rc('ytick', labelsize=7)  # x축 눈금 폰트 크기
plt.rc('axes', labelsize=7)   # x,y축 label 폰트 크기

# Runtime Configuration Parameters의 dict데이터에 폰트를 변경하기위한 설정
# 해당 설정을 통해 한글출력가능
plt.rcParams['font.family'] = 'Malgun Gothic'

# pyplot의 그래프는 figure와 Ax로 구성
# (Ax)그래프가 들어가는 figure(액자)를 미리 선언
fig = plt.figure()

# subplot()을 통하여 액자안에 여러개의 그래프 추가 가능
# 수도권의 월세 그래프를 시각화
ax3 = fig.add_subplot(2,1,1)
ax3.plot(list(map(int, capitalAreaMonthlySample)), color='red', label='수도권 월세')
plt.title('수도권/지방 월세 비교 그래프')
plt.ylabel('(천원) ', loc='top') # y라벨 추가
plt.xticks(np.arange(0,36), xbarMonthlyList) # x축 항목값 설정
plt.grid() # 격자무늬 추가
plt.legend() # 범례 추가

# 지방의 월세 그래프를 시각화
ax4 = fig.add_subplot(2,1,2)
ax4.plot(list(map(int, provinceMonthlySample)), color='green', label='지방 월세')
plt.xlabel('(날짜)', loc='right') # x라벨 추가
plt.xticks(np.arange(0,36), xbarMonthlyList) # x축 항목값 설정
plt.grid() # 격자무늬 추가
plt.legend() # 범례 추가

fig.subplots_adjust(hspace = 0.1) # 두 그래프 사이의 상하 간격 설정

# 두 그래프 사이의 간격차를 나타내기 위한 불필요한  요소 제거
ax3.spines.bottom.set_visible(False)
ax4.spines.top.set_visible(False)
ax3.xaxis.tick_top()
ax3.tick_params(labeltop=False)
ax4.xaxis.tick_bottom()

ax3.set_ylim(690, 730) # 위 그래프  y축 범위 설정
ax4.set_ylim(490, 530) # 아래 그래프  y축 범위 설정

# 그래프 출력
plt.show()
