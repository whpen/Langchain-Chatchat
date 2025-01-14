# prompt模板使用Jinja2语法，简单点就是用双大括号代替f-string的单大括号
# 本配置文件支持热加载，修改prompt模板后无需重启服务。


# LLM对话支持的变量：
#   - input: 用户输入内容

# 知识库和搜索引擎对话支持的变量：
#   - context: 从检索结果拼接的知识文本
#   - question: 用户提出的问题


PROMPT_TEMPLATES = {
    # LLM对话模板
    "llm_chat": "{{ input }}",

    # 基于本地知识问答的提示词模
    "knowledge_base_chat": """<指令>根据已知信息，简洁和专业的来回答问题。如果无法从中得到答案，请说 “根据已知信息无法回答该问题”，不允许在答案中添加编造成分，如果问题是中文，答案请使用中文；If the question in English, Please respond in English. </指令>
   
<已知信息>{{ context }}</已知信息>

<问题>{{ question }}</问题>""",
}

# PROMPT_TEMPLATES = {
#     # LLM对话模板
#     "llm_chat": "{{ input }}",

#     # 基于本地知识问答的提示词模
#     "knowledge_base_chat": """
#     仔细阅读下面的已知信息，然后简洁和专业的来回答下面的问题，仅需回答一次，无需多轮回答。如果无法从已知信息中得到答案，请说 “根据已知信息无法回答该问题”，不允许在答案中添加编造成分！
   
#     已知信息：{{ context }}；

#     问题：{{ question }}；
#     """,
# }