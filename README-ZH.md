# 介绍:
输出全球拍摄的提示词
这个节点用于通过自定义模版生成FLUX或者/SD35的摄影提示词，或者通过输出关键词给GPT或其他的大语言模型细化提示词

# 使用方法:
-进入 comfyui

-点击 comfyui manager

-通过GIT URL 安装 [https://github.com/jinwei1660/Comfyui_AJPrompt.git](https://github.com/jinwei1660/Comfyui_AJPrompt.git) or 或者进入目录 ./comfyui/custom_nodes run 
```shell
git clone https://github.com/jinwei1660/Comfyui_AJPrompt.git
```


1.通过自定义模版输出提示词，模版部分可以自行修改，关键词用{}引用，当选择忽略时，不输出内容。

![image](https://github.com/user-attachments/assets/20108cd4-beb7-4c61-81e8-92ffa5204067)

2.通过输出关键词，让GPT或者其他的大语言模型进行提示词细化

![image](https://github.com/user-attachments/assets/c64186bc-8ba0-4d91-971e-b286f4985228)


#FLUX/SD35 效果预览
![ComfyUI_0037](https://github.com/user-attachments/assets/e6f462f1-7ee3-4ef3-98c3-c7ff74c4d419)
![ComfyUI_0042](https://github.com/user-attachments/assets/438f6958-0c3e-4879-af1a-b7fbf5db523d)
![ComfyUI_0047](https://github.com/user-attachments/assets/f7a2b16b-0437-44f8-9aa9-c7a4deed3273)
![ComfyUI_0252](https://github.com/user-attachments/assets/51a9962a-7a73-46fe-b628-b6ca3f8c7365)
