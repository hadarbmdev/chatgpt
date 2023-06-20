def example1(openai):
    response = get_completion(openai, "What is the capital of France?")
    print(response)


def get_completion(openai, prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]
