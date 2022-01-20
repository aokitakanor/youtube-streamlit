import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time
st.title("Streamlit 超入門")

st.write("Dataframe")

df  =pd.DataFrame({
    "1列目":[1,2,3,4],
    "2列目":[10,20,30,40]
})

"・DateFrameの表示方法"
st.write(df)
"・高さ幅指定"
st.dataframe(df.style.highlight_max(axis = 0),width = 100,height = 100)
"・スタティックな表"
st.table(df.style.highlight_max(axis = 0))

"・マークダウン記法"
"""
# 章
## 節 
### 項

```
python
import streamlit as st
import numpy as np
import pandas as pd
```
"""

#チャート，グラフ
#折れ線グラフ
df = pd.DataFrame(
    np.random.rand(20,3),
    columns=['a','b','c']
)
df
st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)

#マップ(新宿付近の地図情報)
df = pd.DataFrame(
    np.random.rand(100,2)/[50,50]+[35.69,139.70],
    columns=['lat','lon']
)
st.map(df)

st.write("Display Image")




"・インタラクティブなウィジェット"
if st.checkbox("Show Image"):
    img = Image.open("SOUND.PNG")
    st.image(img, caption ="SOUND",use_column_width = True)
"・セレクトボックス"
option = st.selectbox(
    "あなたが好きな数字を教えてください．",
    list(range(1,11))
)
"あなたの好きな数字は",option,"です．"

st.write("Interacutive widgets")


"・レイアウトを整える"
#サイドバー(.sidebarを挿入)
"・サイドバー"
left_column, right_column = st.columns(2)
st.sidebar.write("サイドバー")
text = st.sidebar.text_input("あなたの趣味を教えてください")
condition = st.sidebar.slider("あなたの今の調子は？",0,100,50)

"あなたの趣味は：",text
"コンディション：",condition
"・2カラム"
left_column, right_column = st.columns(2)
button = left_column.button("右カラムの文字を表示")
if button:
    right_column.write("ここは右カラムです．")

"・エクスパンダー"
expander = st.expander("問い合わせ")
expander.write("問い合わせ内容を開く")

"・プログレスバーの表示"
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i+1)
    time.sleep(0.1)
"Done!"