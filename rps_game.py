import streamlit as st
import random

st.set_page_config(page_title="石头剪刀布", layout="centered")

choices = {
    "石头": "✊",
    "剪刀": "✌️",
    "布": "✋"
}

# 初始化状态
if "user_score" not in st.session_state:
    st.session_state.user_score = 0
    st.session_state.computer_score = 0
    st.session_state.result = ""
    st.session_state.computer_choice = ""
    st.session_state.history = []

# 游戏逻辑
def play(user_choice):
    computer = random.choice(list(choices.keys()))
    st.session_state.computer_choice = computer

    if user_choice == computer:
        result = "🤝 平局"
    elif (user_choice == "石头" and computer == "剪刀") or \
         (user_choice == "剪刀" and computer == "布") or \
         (user_choice == "布" and computer == "石头"):
        result = "✅ 你赢了"
        st.session_state.user_score += 1
    else:
        result = "❌ 你输了"
        st.session_state.computer_score += 1

    # 保存历史记录
    st.session_state.history.append({
        "你": f"{choices[user_choice]} {user_choice}",
        "电脑": f"{choices[computer]} {computer}",
        "结果": result
    })

    st.session_state.result = result

# 标题
st.title("🪨 ✂️ 🧻 石头剪刀布")
st.caption("和电脑来一场对战吧！")

# 出拳选择
st.subheader("请出拳：")
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

# 显示结果
if st.session_state.result:
    st.markdown("### 🎯 对战结果")
    st.info(f"你出了：{choices[st.session_state.history[-1]['你'].split()[1]]}，电脑出了：{choices[st.session_state.computer_choice]}")
    st.success(f"结果：{st.session_state.result}")

# 分数板
st.markdown("### 🧮 比分")
st.write(f"👩 你：{st.session_state.user_score} &nbsp;&nbsp;&nbsp; 🤖 电脑：{st.session_state.computer_score}", unsafe_allow_html=True)

# 显示历史记录
if st.session_state.history:
    st.markdown("### 🕹️ 历史对战")
    for i, record in enumerate(reversed(st.session_state.history[-5:]), 1):
        st.write(f"{i}. 你：{record['你']} | 电脑：{record['电脑']} | {record['结果']}")

# 重置按钮
if st.button("🔄 重新开始游戏"):
    st.session_state.user_score = 0
    st.session_state.computer_score = 0
    st.session_state.result = ""
    st.session_state.computer_choice = ""
    st.session_state.history = []
