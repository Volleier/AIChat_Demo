import openai

# 设置你的 OpenAI API 密钥

# 定义一个函数来与 OpenAI GPT-3 模型交互


def get_gpt3_response(prompt):
    try:
        # 使用新的 Completion API 方式
        response = openai.completions.create(
            model="gpt-3.5-turbo",  # 你可以选择 gpt-4 或其他模型
            prompt=prompt,           # 传入的用户提示
            max_tokens=150,          # 最大 token 数量
            temperature=0.7,         # 控制文本的随机性
        )

        # 返回生成的内容
        return response.choices[0].text.strip()

    except Exception as e:
        return f"Error: {str(e)}"


# 示例：调用 GPT-3 来回答问题
if __name__ == "__main__":
    prompt = "Explain the process of photosynthesis."
    response = get_gpt3_response(prompt)
    print("GPT-3 Response: ", response)
