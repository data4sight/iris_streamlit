import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import io  # io 모듈 임포트 추가

# 1. 데이터 로드 및 전처리
@st.cache_data  # 데이터 로딩 함수를 캐싱하여 성능 향상
def load_data():
    # 예시 데이터: Iris 데이터셋 (pandas DataFrame으로 로드)
    data = sns.load_dataset('iris')
    df = pd.DataFrame(data)
    return df

df = load_data()

# 2. Streamlit 앱 UI 구성
st.title('*****Iris 데이터 분석 Streamlit 앱')  # 앱 제목

st.header('데이터 미리보기')
st.dataframe(df.head())  # 데이터프레임 상위 5행 출력

st.header('데이터 정보')
#df.info()  # 데이터프레임 정보 출력
buffer = io.StringIO()
df.info(buf=buffer)
s = buffer.getvalue()
st.text(s)


# 3. 데이터 시각화
st.header('산점도 (Sepal Length vs Sepal Width)')
fig, ax = plt.subplots()
sns.scatterplot(x='sepal_length', y='sepal_width', hue='species', data=df, ax=ax)
st.pyplot(fig)  # Matplotlib 그림 출력

st.header('히스토그램 (Petal Length)')
fig, ax = plt.subplots()
sns.histplot(df['petal_length'], kde=True, ax=ax)
st.pyplot(fig)



# 4. 사용자 상호 작용 요소
st.header('종(Species) 선택')
species_options = df['species'].unique()  # 종 목록 가져오기
selected_species = st.multiselect('분석할 종을 선택하세요:', species_options, default=species_options[0])  # 다중 선택 위젯

# 선택된 종에 따라 데이터 필터링
filtered_df = df[df['species'].isin(selected_species)]

st.write(f'선택된 종: {selected_species}')
st.dataframe(filtered_df)

# 5. 통계 분석
st.header('선택된 종의 통계량')
st.write(filtered_df.describe())
