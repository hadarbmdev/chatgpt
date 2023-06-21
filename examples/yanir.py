def yanir(openai):
    response, token_dict = get_completion_from_messages(openai, messages)
    print(token_dict)
    print(response)
    return response


def get_completion_from_messages(
    openai, messages, model="gpt-3.5-turbo", temperature=0, max_tokens=200
):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    token_dict = {
        "prompt_tokens": response["usage"]["prompt_tokens"],
        "completion_tokens": response["usage"]["completion_tokens"],
        "total_tokens": response["usage"]["total_tokens"],
    }

    return content, token_dict


delimiter = "####"
system_message = f"""
You will be provided with a query which will contain onle '?'. \
Please respond with a funny prank that can be done at software company office,  \
to a guy named Yanir who is 40 years old.
The prank should be easy to perform, respectful, not shaming, but giving a hillarious and funny moments to the team. \
The total response should be limited to one short sentence.

"""
user_message = f"""\
?"""
messages = [
    {"role": "system", "content": system_message},
    {"role": "user", "content": f"{user_message}"},
]
