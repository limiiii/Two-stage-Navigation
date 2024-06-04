#!/home/yang/anaconda3/envs/pytorch3.8/bin/python
# -*- coding: utf-8 -*-

import openai

class Chatgptserver:
    def __init__(self):
        # 设置OpenAI API密钥
        openai.api_base = "https://api.gpts.vin/v1"
        openai.api_key = 'sk-ylD92cAf8EVxzgB44c7fC5A9847949B3891aE8F3Ff4bF732'
        
        #self.user_input = "现在需要你按照如下的规则提取示例语句中的物品名称，仿照下面的四个回答的例子返回由物品名称组成的列表，注意你只需要返回列表即可,并且每个物品只允许存在一个单词、不需要附带任何的说明！示例一：Pass the pool and go indoors using the double glass doors. Pass the large table with chairs and turn left and wait by the wine bottles that have grapes by them. 回答：['pool', 'door', 'chair', 'bottle'];示例二：Walk straight through the room and exit out the door on the left. Keep going past the large table and turn left. Walk down the hallway and stop when you reach the 2 entry ways. One in front of you and one to your right. The bar area is to your left.回答：['room', 'door', 'table', 'hallway', 'bar'];示例三：Enter house through double doors, continue straight across dining room, turn left into bar and stop on the circle on the ground.回答：['door', 'dinning room', 'bar'];示例四：Standing in front of the family picture, turn left and walk straight through the bathroom past the tub and mirrors. Go through the doorway and stop when the door to the bathroom is on your right and the door to the closet is to your left.回答：['family picture', 'bathroom', 'tub', 'mirrors', 'door', 'bathroom', 'closet'];下面请你提取如下语句的关键物品，返回一个列表："
        self.user_input = "现在需要你按照如下的规则提取示例语句中的物品名称，仿照下面的四个回答的例子返回由物品名称组成的列表，注意你只需要返回列表即可,并且在列表中的每个物品可以重复出，但只允许用一个单词表述，不需要附带任何的说明！示例一：Pass the pool and go indoors using the double glass doors. Pass the large table with chairs and turn left and wait by the wine bottles that have grapes by them. 回答：['pool', 'door', 'chair', 'bottle'];示例二：Walk straight through the room and exit out the door on the left. Keep going past the large table and turn left. Walk down the hallway and stop when you reach the 2 entry ways. One in front of you and one to your right. The bar area is to your left.回答：['room', 'door', 'table', 'hallway', 'bar'];示例三：Enter house through double doors, continue straight across dining room, turn left into bar and stop on the circle on the ground.回答：['door', 'dinning room', 'bar'];示例四：Standing in front of the family picture, turn left and walk straight through the bathroom past the tub and mirrors. Go through the doorway and stop when the door to the bathroom is on your right and the door to the closet is to your left.回答：['family picture', 'bathroom', 'tub', 'mirrors', 'door', 'bathroom', 'closet'];下面请你提取如下语句的关键物品，返回一个列表："
        print("chatgptserver started!")
    def chat_with_gpt(self, message):
        msgs = self.user_input + message
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": msgs}
            ]
        )
    # 提取ChatGPT的回复消息
        reply = response.choices[0].message.content
        print(type(reply))
        reply = eval(reply)
        return reply
