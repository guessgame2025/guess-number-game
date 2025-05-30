import streamlit as st
import random

st.set_page_config(page_title="石头剪刀布", layout="centered")

choices = ["石头", "剪刀", "布"]

# 初始化游戏状态
if "user_score" not in st.session_state:
    st.session_state.user_score = 0
    st.session_state.computer_score = 0
    st.session_state.result = ""
    st.session_state.computer_choice = ""

# 游戏逻辑
def play(user_choice):
    computer = random.choice(choices)
    st.session_state.computer_choice = computer

    if user_choice == computer:
        st.session_state.result = "🤝 平局！"
    elif (user_choice == "石头" and computer == "剪刀") or \
         (user_choice == "剪刀" and computer == "布") or \
         (user_choice == "布" and computer == "石头"):
        st.session_state.user_score += 1
        st.session_state.result = "✅ 你赢了！"
    else:
        st.session_state.computer_score += 1
        st.session_state.result = "❌ 你输了！"

# 页面展示
st.title("✊ 石头 ✌️ 剪刀 ✋ 布")

st.subheader("请选择你的出拳：")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("✊ 石头"):
        play("石头")
with col2:
    if st.button("✌️ 剪刀"):
        play("剪刀")
with col3:
    if st.button("✋ 布"):
        play("布")

if st.session_state.result:
    st.markdown(f"🧠 电脑出的是：**{st.session_state.computer_choice}**")
    st.markdown(f"🏆 结果：**{st.session_state.result}**")

st.markdown("---")
st.markdown(f"👩 你：{st.session_state.user_score}  🆚  电脑：{st.session_state.computer_score}")

if st.button("🔄 重新开始"):
    st.session_state.user_score = 0
    st.session_state.computer_score = 0
    st.session_state.result = ""
    st.session_state.computer_choice = ""