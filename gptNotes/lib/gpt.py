import g4f


def gpt_response(prompt: str) -> str:
    return g4f.ChatCompletion.create(model='gpt-3.5-turbo', messages=[{'role': 'user', 'content': prompt}])


def gpt_improve(text: str) -> str:
    return gpt_response(f'исправь ошибки в этом тексте: {text}')


def gpt_append(text: str) -> str:
    return gpt_response(f'продолжи этот текст: {text}')


def gpt_retell(text: str) -> str:
    return gpt_response(f'кратко перескажи этот текст: {text}')
