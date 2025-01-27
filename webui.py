import streamlit as st
from webui_pages.utils import *
from streamlit_option_menu import option_menu
from webui_pages import *
import os
from configs import VERSION
from server.utils import api_address

import os
import streamlit as st
from dotenv import load_dotenv
from streamlit_cognito_auth import CognitoAuthenticator

api = ApiRequest(base_url=api_address())

load_dotenv()
# pool_id = os.getenv("POOL_ID")
# app_client_id = os.getenv("APP_CLIENT_ID")
# app_client_secret = os.getenv("APP_CLIENT_SECRET")

if __name__ == "__main__":
    st.set_page_config(
        "Langchain-Chatchat WebUI",
        os.path.join("img", "chatchat_icon_blue_square_v2.png"),
        initial_sidebar_state="expanded",
        menu_items={
            'Get Help': 'https://github.com/chatchat-space/Langchain-Chatchat',
            'Report a bug': "https://github.com/chatchat-space/Langchain-Chatchat/issues",
            'About': f"""欢迎使用 Langchain-Chatchat WebUI {VERSION}！"""
        }
    )

#     authenticator = CognitoAuthenticator(
#     pool_id=pool_id,
#     app_client_id=app_client_id,
#     app_client_secret=app_client_secret,
# )
    
    # is_logged_in = authenticator.login()
    # if not is_logged_in:
    #     st.stop()

    # def logout():
    #     authenticator.logout()

    if not chat_box.chat_inited:
        st.toast(
            f"欢迎使用 [`Langchain-Chatchat`](https://github.com/chatchat-space/Langchain-Chatchat) ! \n\n"
            f"当前使用模型`{LLM_MODEL}`, 您可以开始提问了."
        )

    pages = {
        "对话": {
            "icon": "chat",
            "func": dialogue_page,
        },
        "知识库管理": {
            "icon": "hdd-stack",
            "func": knowledge_base_page,
        },
    }

    with st.sidebar:
        #add logo 
        st.image(
            os.path.join(
                "img",
                "toast_shark.jpg",
            ),
            # width = 150,
            use_column_width=True
        )
        #add "powered by" logo

        st.image(
            os.path.join(
                "img",
                "powered_by.png",
            ),
            width = 150,
            use_column_width=False
        )


        st.image(
            os.path.join(
                "img",
                "logo-long-chatchat-trans-v2.png",
            ),
            width = 150,
            use_column_width=False
        )
        st.caption(
            f"""<p align="right">当前版本：{VERSION}</p>""",
            unsafe_allow_html=True,
        )
        options = list(pages)
        icons = [x["icon"] for x in pages.values()]

        default_index = 0
        selected_page = option_menu(
            "",
            options=options,
            icons=icons,
            # menu_icon="chat-quote",
            default_index=default_index,
        )

        # st.text(f"Welcome,\n{authenticator.get_username()}")
        # st.button("Logout", "logout_btn", on_click=logout)

    if selected_page in pages:
        pages[selected_page]["func"](api)


