import openai
import gradio

openai.api_key = "sk-None-MaDmKKVRK5rBi7HbCuTpT3BlbkFJy19LqWs5XaedvSLNbBGw"

class Car_is_vision:

    def __init__(self, color, age):
        self._color = "blue"

def get_completion(prompt, model="gpt-4o-mini"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

# def collect_messages(_):
#     prompt = inp.value_input
#     inp.value = ''
#     context.append({'role':'user', 'content':f"{prompt}"})
#     response = get_completion_from_messages(context) 
#     context.append({'role':'assistant', 'content':f"{response}"})
#     panels.append(
#         pn.Row('User:', pn.pane.Markdown(prompt, width=600)))
#     panels.append(
#         pn.Row('Assistant:', pn.pane.Markdown(response, width=600, style={'background-color': '#F6F6F6'})))
 
#     return pn.Column(*panels)


gradio = gradio.Interface(fn=get_completion_from_messages, inputs="text", outputs="text", title="my title")

gradio.launch()