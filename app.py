import pandas as pd
import streamlit as st

import os

# タイトルを表示
st.title('Training journal app')

# ユーザー入力を受け取る
date = st.date_input('日付')
train_name = st.selectbox('トレーニング内容', ['ベンチプレス', 'スクワット', 'デッドリフト'])
set_num = st.number_input('セット数', min_value=1)
set_reps = st.slider('レップス', min_value=0, max_value=50, step=1, value=10)

# 空のデータフレームを作成
if 'training_log.csv' not in os.listdir():
    df = pd.DataFrame(columns=['日付', 'トレーニング内容', 'セット数', 'レップス'])
    df.to_csv('training_log.csv', index=False)

# ボタンが押されたらデータフレームに追加
if st.button('保存'):
    # データフレームを読み込む
    df = pd.read_csv('training_log.csv')
    # 新しいデータを追加
    new_data = pd.DataFrame({
        '日付': [date],
        'トレーニング内容': [train_name],
        'セット数': [set_num],
        'レップス': [set_reps]
    })
    df = pd.concat([df, new_data], ignore_index=True)
    # データフレームを保存
    df.to_csv('training_log.csv', index=False)

    # データフレームを表示
    st.write(df)
