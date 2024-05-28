import matplotlib.pyplot as plt
import csv

def load_data(filename):  # filename: 읽을 CSV 파일의 이름을 나타내는 문자열
    with open(filename, 'r') as file:
        data = csv.reader(file)
        header = next(data)  # 첫 번째 줄은 헤더
        _ = next(data)  # 전체 국가 데이터를 건너뜀
        capital_data = next(data)  # 수도권 데이터
        province_data = next(data)  # 지방 데이터
        
        samples_capital = []
        samples_province = []
        x_labels = []
        cnt = 0
        for index in range(len(capital_data)):
            cnt += 1
            # 4번째 열마다 데이터 수집 (2번째, 6번째, 10번째, ...)
            if cnt % 4 == 2:
                samples_capital.append(int(capital_data[cnt]))
                samples_province.append(int(province_data[cnt]))
                x_labels.append(header[cnt][2:7])  # 날짜 라벨 설정
        return samples_capital, samples_province, x_labels

# 월세와 전세 데이터를 각각 로드
capital_monthly, province_monthly, x_monthly = load_data('monthly.csv')
capital_charter, province_charter, x_charter = load_data('charter.csv')

# 데이터 시각화 부분
# 그래프 설정
plt.rc('xtick', labelsize=7)  # x축 눈금 폰트 크기
plt.rc('ytick', labelsize=7)  # x축 눈금 폰트 크기
plt.rc('axes', labelsize=7)   # x,y축 label 폰트 크기

# Runtime Configuration Parameters의 dict데이터에 폰트를 변경하기위한 설정
# 해당 설정을 통해 한글출력가능
plt.rcParams['font.family'] = 'Malgun Gothic'

# pyplot의 그래프는 figure와 Ax로 구성
# (Ax)그래프가 들어가는 figure(액자)를 미리 선언
fig, (ax1, ax3) = plt.subplots(2, 1, figsize=(10, 6), sharex=True)

# 수도권 월세를 왼쪽 Y축에 표시
ax1.plot(range(len(x_monthly)), capital_monthly, color='red', label='수도권 월세')
ax1.set_ylabel('수도권 월세 (천원)', color='red')
ax1.tick_params(axis='y', labelcolor='red')
ax1.grid()
ax1.legend(loc='upper left')
ax1.set_title('수도권/지방 월세 비교 그래프')  # 월세 그래프 제목 설정

# 지방 월세를 오른쪽 Y축에 표시
ax2 = ax1.twinx()
ax2.plot(range(len(x_monthly)), province_monthly, color='green', label='지방 월세')
ax2.set_ylabel('지방 월세 (천원)', color='green')
ax2.tick_params(axis='y', labelcolor='green')
ax2.legend(loc='upper right')

# 수도권 전세를 왼쪽 Y축에 표시
ax3.plot(range(len(x_charter)), capital_charter, color='blue', label='수도권 전세')
ax3.set_ylabel('수도권 전세 (천원)', color='blue')
ax3.tick_params(axis='y', labelcolor='blue')
ax3.grid()
ax3.legend(loc='upper left')
ax3.set_title('수도권/지방 전세 비교 그래프')  # 전세 그래프 제목 설정

# 지방 전세를 오른쪽 Y축에 표시
ax4 = ax3.twinx()
ax4.plot(range(len(x_charter)), province_charter, color='purple', label='지방 전세')
ax4.set_ylabel('지방 전세 (천원)', color='purple')
ax4.tick_params(axis='y', labelcolor='purple')
ax4.legend(loc='upper right')

# 공통 X축 설정
plt.xticks(range(len(x_monthly)), x_monthly, rotation=45)
plt.xlabel('(날짜)')

plt.tight_layout()  # 레이아웃 조정
plt.show()  # 그래프 출력
plt.close(fig) # 출력 종료
