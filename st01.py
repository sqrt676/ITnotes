import streamlit as st

st.title("IT department notes for AKTU")

st.header("Developed by sqrt676 for his friends LOL")


course = st.selectbox(
    'Select your course',
    ('DA','BCA','RTS','CN',
'ITCS','SE'))


#cc={a:"1"}
#subject=st.selectbox('Select your term in which you registered',('t1','t2','t3'))


if course=='DA':
    finallink="https://drive.google.com/drive/folders/13xPN3UHssFbm37MJaqTzkCRT-JuVWKzH?usp=sharing"
if course=="BCA":
    finallink="https://drive.google.com/drive/folders/14w84YznuU6URcKf-dNPRlPPQObV3f8pZ?usp=sharing"
if course=="CN":
    finallink="https://drive.google.com/drive/folders/10qtAmabG2KUtTnJoUmnSmEf7IOaiJiQN?usp=sharing"
if course=="SE":
    finallink="https://drive.google.com/drive/folders/11_-sZfGTEERNqzdSqsUCj7tVHcK7vXUX?usp=sharing"
if course=="RTS":
    finallink="https://drive.google.com/drive/folders/15Qz4ZHX7hm8mMH5zFTgFVUzBjAuws0lF?usp=sharing"
if course=="ITCS"
    finallink="https://drive.google.com/drive/folders/13JspqgPYNk2YCH8jjNxA_gS4Jx5UB2ls?usp=sharing"

url = finallink
st.write("Click on the [link](%s)" % url)
