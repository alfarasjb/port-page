import streamlit as st 
from streamlit_lottie import st_lottie
import requests
from PIL import Image

## CONSTANTS ## 
lottie = "https://lottie.host/377d5b04-9280-4c5f-9ade-d1ce09f7d432/gZTkVdRlID.json"



content = {
	'icon' : 'images/graph-eu.png',
	'info' : {
		'git' : {
			'title' : 'GitHub',
			'link' : 'https://github.com/alfarasjb',
			'icon' : 'https://cdn-icons-png.flaticon.com/64/25/25231.png'
		},
		'linkedin' : {
			'title' : 'LinkedIn',
			'link' : 'https://www.linkedin.com/in/jay-alfaras',
			'icon' : 'https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg'
		},
		'products' : {
			'title' : 'Products',
			'link' : 'https://www.mql5.com/en/users/alfarasjb/seller'
		},
		'articles' : {
			'title' : 'Articles',
			'link' : 'https://medium.com/@alfarasjb'
		},
	},
}

img_proj_1 = Image.open(content['icon'])
img_proj_2 = Image.open('images/TradeTool-Large.png')


# more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet
st.set_page_config(page_title = 'Jay Alfaras', page_icon = img_proj_1, layout = 'centered')

st.title('Jay Benedict Alfaras')
st.subheader("Algorithmic Trading - MQL4 | MQL5 | Python | Pinescript")

# Use local css
def local_css(file_name):
	with open(file_name) as f:
		st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html = True)

def info_row(info):
    title = info['title']
    link = info['link']
    st.write(f'{title}: {link}')

local_css('style/style.css')
# ---- WHAT I DO 
with st.container():
	st.write('---')
	left_column, right_column = st.columns(2)
	with left_column:
		#st.header('Core Focus')
		st.write("""
			I am an Algorithmic Trading Developer from the Philippines. My work focuses on deploying trading research and ideas into live market
			conditions, mainly through the MetaTrader platform. 
			""")
		#st.write('##')
		st.write("""
			I hold a Bachelor's Degree in Electronics Engineering, which allowed me to develop an intuition for problem solving. This led
			me to develop a strong passion for studying Financial Markets and generating systematic solutions for live market trading
			implementation across various asset classes. 
		""")

		git_icon = content['info']['git']['icon']
		git_link = content['info']['git']['link']

		linkedin_icon = content['info']['linkedin']['icon']
		linkedin_link = content['info']['linkedin']['link']

		git_repo = f"[![repo]({git_icon})]({git_link})"
		
		linkedin = f"[![linkedin]({linkedin_icon})]({linkedin_link})"
		col_1, col_2, _, _, _ = st.columns(5)
		with col_1:
			st.markdown(linkedin, unsafe_allow_html=True)
		with col_2:
			st.markdown(git_repo, unsafe_allow_html=True)

	with right_column:
		st_lottie(lottie, height = 300 ,key ='trading')


# ---- CONTACT
with st.container():
	st.write('---')
	#st.header('Get In Touch!')
	#st.write("Got a trading idea? Get In Touch!")
	st.write('##')
	st.subheader("Got a trading idea? Get in touch!")
	contact_form = """
	<form action="https://formsubmit.co/alfarasjb@gmail.com" method="POST">
	<input type = "hidden" name = "_captcha" value = "false">
     <input type="text" name="name" placeholder = "Your Name" required>
     <input type="email" name="email" placeholder = "Your Email" required>
     <textarea name = "message" placeholder = "Your Message Here" required></textarea>
     <button type="submit">Send</button>
</form> 
	"""

	left_column, right_column = st.columns(2)
	with left_column:
		st.markdown(contact_form, unsafe_allow_html = True)
	with right_column:
		st.empty()
