#!/home/yang/anaconda3/envs/pytorch3.8/bin/python
# -*- coding: utf-8 -*-

import openai

class Chatgptserver2:
    def __init__(self):
        # 设置OpenAI API密钥
        openai.api_base = "https://api.gpts.vin/v1"
        openai.api_key = 'sk-ylD92cAf8EVxzgB44c7fC5A9847949B3891aE8F3Ff4bF732'
        #self.user_input = "仿照下面的四个回答的例子按照句子中物品出现的顺序返回由数字组成的列表，其中的数字0表示当前目标物品没有方位信息、1表示在前方、2表示在后方、3表示在左边、4表示在右边，注意句子中一个物品对应一个动作，并且你只需要返回仅含有数字的python列表即可， 不需要附带任何的说明！示例一：Pass the pool and go indoors using the double glass doors. Pass the large table with chairs and turn left and wait by the wine bottles that have grapes by them. 回答：['0', '0', '0', '3']，解释：在经过pool、door和table时没有指示方位，而最后通过左转找到bottle，因此依次返回0、0、0、3;示例二：Enter house through double doors, continue straight across dining room, turn left into bar and stop on the circle on the ground.回答：['0', '1', '3']，解释：通过门进入房间，并一直直行经过;餐厅，最后左转进入吧台，因此依次返回表示无方位信息、直行和左转的0、1、3；;示例三：Find a nearby sofa, and walk straight to the chair in front of you, then turn around and walk straight past the television and stop next to your bed.回答：['0', '1', '2', '0']，解释：找到一个邻近的沙发，并直行到前方的椅子旁，然后向后转经过电视机，并最后在床边停下，注意向后转及其后续任意一个动作都视为是向后转; 示例四：Go all the way to the refrigerator, then turn around to the sofa, straight forward to the bed, and stop at the edge of the chair.回答：['0', '2', '1', '0']下面请你提取如下语句的信息，一个标志物对应一个动作，返回一个由数字字符组成的列表：" 
        self.user_input = "仿照下面的四个回答的例子按照句子中物品出现的顺序返回由数字组成的列表，其中的数字0表示当前目标物品没有方位信息、1表示在前方、2表示在后方、3表示在左边、4表示在右边，注意：句子中一个物品对应一个动作,遇到turn back或turn around时要输出2，且不要遇到to就输出方向1，此外你只需要返回仅含有数字的python列表即可， 不需要附带任何的说明！示例一：First, find a ball in your left and turn left to bed. Turn back pass the hallway and straight forward to the refrigerator.回答：['3', '3', '2', '1']，解释：找到左手边，因此依次返回3、3、2、1;示例二：Start from a nearby door, turn right to the hallway and turn back past the bed. Then finally get to the chair in front of you. 回答：['0', '4', '2', '1']，解释：从附近的门开始，并右转通过大厅，再向后经过床，最后直行到椅子旁，因此依次返回0、4、2、1；;示例三：Find a nearby sofa, and walk straight to the chair in front of you, then turn around and walk straight past the television and stop next to your bed.回答：['0', '1', '2', '0']，解释：找到一个邻近的沙发，并直行到前方的椅子旁，然后向后转经过电视机，并最后在床边停下，注意向后转及其后续任意一个动作都视为是向后转; 示例四：Go all the way to the refrigerator, then turn around to the sofa, straight forward to the bed, and stop at the edge of the chair in your right.回答：['1', '2', '1', '4']下面请你提取如下语句的信息，一个标志物对应一个动作，返回一个由数字字符组成的列表："
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
        reply = eval(reply)
        return reply
