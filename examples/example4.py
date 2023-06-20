def example4(openai):
    response, token_dict = get_completion_and_token_count(openai, messages)
    print(response)


# combined
messages = [
    {
        "role": "system",
        "content": """You are an assistant who \
responds in the style of Dr Seuss. \
All your responses must be one sentence long.""",
    },
    {"role": "user", "content": """write me a story about a happy carrot"""},
]


def get_completion_and_token_count(
    openai, messages, model="gpt-3.5-turbo", temperature=0, max_tokens=500
):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )

    content = response.choices[0].message["content"]

    token_dict = {
        "prompt_tokens": response["usage"]["prompt_tokens"],
        "completion_tokens": response["usage"]["completion_tokens"],
        "total_tokens": response["usage"]["total_tokens"],
    }

    return content, token_dict
