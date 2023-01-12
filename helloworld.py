import streamlit as st
#import pandas as pd
#import numpy as np
def my_function():
  st.write("# Hello")

st.title('Hello World!')
st.write("""Hello World! 
	_This is some really cool stuff._  
	We can now write multiline markdown and **get them displayed on html** as easy as 1 2 3.  
	Don't forget to add two whitespaces before hitting the return key for newline.
	You new line will automatically displayed on a new line. However if you don't add the white
	spaces, despite the new line character the text will be displayed on same line.""")
st.button(label="Hello",on_click = onClickRun);
st.image('surprise.gif')
st.write("""# About adding Headings
To add headers in your webpage, simply use the '#' character. Using multiple 
'#' will create smaller subheadings like this one 
### Small Sub Heading
#### More smaller sub-sub heading
##### Even more smaller sub-sub-sub heading
###### You got the point! :-D
#Adding Interactive Elements!
StreamLit allows to easily add checkboxes, sliders, progress bars etc.""")
chkRed = st.checkbox("Show in Red")
if chkRed:
	st.markdown(":red[Red highlight on.]")
else:
	st.write("Red highlight is off!")	
