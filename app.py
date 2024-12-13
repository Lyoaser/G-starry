from flask import Flask, request, jsonify
from sparkai.llm.llm import ChatSparkLLM, ChunkPrintHandler
from sparkai.core.messages import ChatMessage

app = Flask(__name__)

# 配置参数
SPARKAI_URL = 'wss://spark-api.xf-yun.com/v1.1/chat'
SPARKAI_APP_ID = '5a515d4c'
SPARKAI_API_SECRET = 'MmYwMzk5Yjg2YTNhNzI1MDY1NDE2ZDVi'
SPARKAI_API_KEY = 'c0fcc14f93a2be176374856a78c17cdd'
SPARKAI_DOMAIN = 'lite'

# 初始化星火认知大模型
spark = ChatSparkLLM(
    spark_api_url=SPARKAI_URL,
    spark_app_id=SPARKAI_APP_ID,
    spark_api_key=SPARKAI_API_KEY,
    spark_api_secret=SPARKAI_API_SECRET,
    spark_llm_domain=SPARKAI_DOMAIN,
    streaming=False,
)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    messages = [ChatMessage(role="user", content=user_message)]
    handler = ChunkPrintHandler()
    response = spark.generate([messages], callbacks=[handler])
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
