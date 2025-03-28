
import streamlit as st

st.title("체형 분석기")

height = st.number_input("키 (cm)", min_value=0.0, format="%.1f")
weight = st.number_input("몸무게 (kg)", min_value=0.0, format="%.1f")

if st.button("분석하기"):
    if height <= 0 or weight <= 0:
        st.warning("키와 몸무게를 올바르게 입력해주세요.")
    else:
        height_m = height / 100
        bmi = weight / (height_m ** 2)
        st.write(f"BMI: {bmi:.1f}")
        
        if bmi < 18.5:
            st.write("**[체형] 저체중입니다.**")
            st.write("**[운동 추천]** 전신 근력 운동, 요가")
            st.write("**[식습관]** 고칼로리 식단, 단백질 섭취")
        elif bmi < 23:
            st.write("**[체형] 정상 체중입니다.**")
            st.write("**[운동 추천]** 유산소 + 근력 운동")
            st.write("**[식습관]** 균형 잡힌 식단")
        elif bmi < 25:
            st.write("**[체형] 과체중입니다.**")
            st.write("**[운동 추천]** 유산소 위주")
            st.write("**[식습관]** 저지방, 채소 중심")
        else:
            st.write("**[체형] 비만입니다.**")
            st.write("**[운동 추천]** 걷기, 자전거, 근력")
            st.write("**[식습관]** 저당, 고섬유질 식단")
