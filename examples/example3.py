def example3(openai):
    response = get_completion_from_messages(openai, messages, temperature=1)
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


def get_completion_from_messages(
    openai, messages, model="gpt-3.5-turbo", temperature=0, max_tokens=500
):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,  # this is the degree of randomness of the model's output
        max_tokens=max_tokens,  # the maximum number of tokens the model can ouptut
    )
    return response.choices[0].message["content"]
