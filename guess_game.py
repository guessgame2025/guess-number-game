import streamlit as st
import random

# 初始化
if "num" not in st.session_state:
    st.session_state.num = random.randint(1, 100)
    st.session_state.count = 0
    st.session_state.result = ""

# 页面标题 + 样式
st.set_page_config(page_title="猜数字小游戏", layout="centered")
st.markdown("""
    <style>
    .title {
        font-size:36px; 
        font-weight:bold; 
        color:#4CAF50;
        text-align:center;
        margin-bottom:20px;
    }
    .guess-button {
        background-color:#4CAF50;
        color:white;
        font-size:20px;
        padding:10px 20px;
        border:none;
        border-radius:8px;
        cursor:pointer;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🎯 猜数字小游戏</div>', unsafe_allow_html=True)

# 输入数字
guess = st.number_input("请输入你猜的数字（1~100）", min_value=1, max_value=100, step=1)

# 提交按钮
if st.button("提交"):
    st.session_state.count += 1
    if guess > st.session_state.num:
        st.session_state.result = "你猜的太大了 🎈"
    elif guess < st.session_state.num:
        st.session_state.result = "你猜的太小了 🎯"
    else:
        st.session_state.result = f"🎉 恭喜你，猜对了！你总共猜了 {st.session_state.count} 次。"
        # 重新开始
        st.session_state.num = random.randint(1, 100)
        st.session_state.count = 0

# 显示结果
if st.session_state.result:
    st.success(st.session_state.result)