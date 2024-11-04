import random
import time
import requests
class AJPromptGeneratorNode:
    """
    A node to generate text based on selected dictionary values and a template.
    """

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "camera": ([
                    "忽略 (Ignore)",
                    "佳能 R5 Mark II (Canon R5 Mark II)",
                    "尼康 Z9 (Nikon Z9)",
                    "索尼 A1 (Sony A1)",
                    "富士 XT5 (Fujifilm XT5)",
                    "富士 GFX 100 Mark II (Fujifilm GFX 100 Mark II)",
                    "宝丽来相机 (Polaroid)",
                    "徕卡 Q2 (Leica Q2)",
                    "哈苏 X2D (Hasselblad X2D)",
                    "理光 GR III (Ricoh GR III)",
                    "iPhone (iPhone)",
                    "飞思相机 (Phase One)",
                    "随机 (Random)"  # 添加随机选项
                ],),
                "lens_name": ([
                    "忽略 (Ignore)",
                    "标准镜头 (Standard Lens)",
                    "中长焦镜头 (Medium Telephoto Lens)",
                    "长焦镜头 (Telephoto Lens)",
                    "鱼眼镜头 (Fisheye Lens)",
                    "超广角镜头 (Ultra-Wide-Angle Lens)",
                    "随机 (Random)"  # 添加随机选项
                ],),
                 "lighting": ([  # 添加光影选项
                    "忽略 (Ignore)",
                    "自然光 (Natural Light)",
                    "侧光 (Side Lighting)",
                    "逆光 (Backlighting)",
                    "环境光 (Ambient Light)",
                    "人造光 (Artificial Lighting)",
                    "高对比光 (High Contrast Lighting)",
                    "柔和光 (Soft Lighting)",
                    "低角度光 (Low-Angle Lighting)",
                    "分割光 (Split Lighting)",
                    "窗影光 (Window Light)",
                    "聚光灯 (Spotlighting)",
                    "闪光灯 (Flash Lighting)",
                    "夜间光 (Nighttime Lighting)",
                    "随机 (Random)"  # 添加随机选项
                ],),
                "top_down": ([
                    "忽略 (Ignore)",
                    "俯视 (Looking down)",
                    "仰视 (Looking up)",
                    "平视 (Eye level)",
                    "鸟瞰视角 (Bird's Eye View)",
                    "虫瞳视角 (Worm's Eye View)",
                    "倾斜角度 (Dutch Angle)",
                    "肩上拍摄 (Over-the-Shoulder Shot)",
                    "视角 (Point-of-View)",
                    "随机 (Random)"  # 添加随机选项
                ],),
                "location": ([
                    "忽略 (Ignore)",
                    "摄影棚 (PhotoStuido)",
                    "阿尔卑斯山 (Alps)",
                    "喜马拉雅山 (Himalayas)",
                    "安第斯山脉 (Andes)",
                    "冈底斯山脉 (Gangdise Mountains)",
                    "大峡谷 (Grand Canyon)",
                    "尼亚加拉大瀑布 (Niagara Falls)",
                    "撒哈拉沙漠 (Sahara Desert)",
                    "马丘比丘 (Machu Picchu)",
                    "大堡礁 (Great Barrier Reef)",
                    "泰姬陵 (Taj Mahal)",
                    "埃菲尔铁塔 (Eiffel Tower)",
                    "长城 (Great Wall of China)",
                    "金门大桥 (Golden Gate Bridge)",
                    "富士山 (Mount Fuji)",
                    "巴黎圣母院 (Notre-Dame Cathedral)",
                    "伦敦塔桥 (Tower Bridge)",
                    "维苏威火山 (Mount Vesuvius)",
                    "自由女神像 (Statue of Liberty)",
                    "埃及金字塔 (Pyramids of Giza)",
                    "圣托里尼岛 (Santorini)",
                    "布莱斯峡谷 (Bryce Canyon)",
                    "拱门国家公园 (Arches National Park)",
                    "哈瓦那老城 (Old Havana)",
                    "维多利亚瀑布 (Victoria Falls)",
                    "班夫国家公园 (Banff National Park)",
                    "新西兰峡湾国家公园 (Fiordland National Park)",
                    "死海 (Dead Sea)",
                    "冰岛黄金圈 (Golden Circle, Iceland)",
                    "亚马逊雨林 (Amazon Rainforest)",
                    "巴厘岛 (Bali)",
                    "迪拜 (Dubai)",
                    "威尼斯 (Venice)",
                    "彼得大帝夏宫 (Peterhof Palace)",
                    "纽约中央公园 (Central Park)",
                    "莫斯科红场 (Red Square)",
                    "克罗地亚普利特维采湖 (Plitvice Lakes, Croatia)",
                    "大象国家公园 (Addo Elephant National Park)",
                    "尤卡坦半岛 (Yucatán Peninsula)",
                    "马尔代夫 (Maldives)",
                    "西西里岛 (Sicily)",
                    "帕尔米拉 (Palmyra)",
                    "撒哈拉绿洲 (Oasis in the Sahara)",
                    "希腊爱琴海 (Aegean Sea)",
                    "加拿大落基山脉 (Canadian Rockies)",
                    "挪威峡湾 (Norwegian Fjords)",
                    "东京塔 (Tokyo Tower)",
                    "夏威夷火山国家公园 (Hawaii Volcanoes National Park)",
                    "乌尤尼盐沼 (Uyuni Salt Flats)",
                    "黄石国家公园 (Yellowstone National Park)",
                    "佩特拉古城 (Petra)",
                    "京都 (Kyoto)",
                    "非洲大草原 (African Savanna)",
                    "冰岛蓝湖 (Blue Lagoon, Iceland)",
                    "马拉喀什 (Marrakech)",
                    "凯尔特海 (Celtic Sea)",
                    "新天鹅堡 (Neuschwanstein Castle)",
                    "埃文河畔斯特拉特福 (Stratford-upon-Avon)",
                    "塞纳河畔 (Seine Riverbank)",
                    "爱尔兰巨人之路 (Giant's Causeway)",
                    "北极光观测点 (Northern Lights Observatory)",
                    "苏格兰高地 (Scottish Highlands)",
                    "悉尼歌剧院 (Sydney Opera House)",
                    "香港维多利亚港 (Victoria Harbour)",
                    "上海外滩 (The Bund, Shanghai)",
                    "京都金阁寺 (Kinkaku-ji, Kyoto)",
                    "随机 (Random)"  # 添加随机选项
                ],),
                "pose": ([
                    "忽略 (Ignore)",
                    "站立 (Standing)",
                    "半蹲 (Half squat)",
                    "坐着 (Sitting)",
                    "随机 (Random)"  # 添加随机选项
                ],),
                "orientation": ([
                    "忽略 (Ignore)",
                    "面向观众 (Facing the audience)",
                    "侧面 (Sideways)",
                    "背面 (The back)",
                    "三分之一侧面 (Three-Quarter View)",
                    "随机 (Random)"  # 添加随机选项
                ],),
                 "movements": ([
                     "忽略 (Ignore)",
                    "夸张的 (Exaggerated)",
                    "专业的 (Professional)",
                    "自然的 (Natural)",
                    "活泼的 (Lively)",
                    "优雅的 (Graceful)",
                    "动态的 (Dynamic)",
                    "放松的 (Relaxed)",
                    "强烈的 (Intense)",
                    "自信的 (Confident)",
                    "戏剧性的 (Dramatic)",
                    "随机 (Random)"  # 添加随机选项
                ],),
                "tops": ([
                    "忽略 (Ignore)",
                    "T恤 (T-shirt)",                    # 基础款
                    "衬衫 (Shirt)",                     # 正式/商务
                    "针织衫 (Knitwear)",                # 休闲/保暖
                    "连帽卫衣 (Hooded sweatshirt)",     # 运动/休闲
                    "圆领卫衣 (Crewneck sweatshirt)",   # 运动/休闲
                    "毛衣 (Sweater)",                   # 保暖/秋冬
                    "夹克 (Jacket)",                    # 休闲/外套
                    "外套 (Coat)",                      # 正式/保暖
                    "西装 (Blazer)",                    # 正式/商务
                    "羽绒服 (Down jacket)",             # 冬季保暖
                    "开衫 (Cardigan)",                  # 层次/休闲
                    "高领上衣 (Turtleneck)",            # 秋冬/保暖
                    "短款上衣 (Crop top)",              # 时尚/休闲
                    "瑜伽服 (Yoga top)",                # 运动/健身
                    "内衣 (Underwear)",                 # 内搭/基础
                    "随机 (Random)"                     # 随机选择
                ],),
                "bottoms": ([
                    "忽略 (Ignore)",
                    "牛仔短裤 (Denim shorts)",
                    "牛仔裤 (Denim pants)",
                    "短裙 (Mini skirt)",
                    "中长裙 (Midi skirt)",
                    "长裙 (Maxi skirt)",
                    "铅笔裙 (Pencil skirt)",
                    "百褶裙 (Pleated skirt)",
                    "A字裙 (A-line skirt)",
                    "鱼尾裙 (Mermaid skirt)",
                    "伞裙 (Skater skirt)",
                    "阔腿裤 (Wide-leg pants)",
                    "工装裤 (Cargo pants)",
                    "打底裤 (Leggings)",
                    "西装裤 (Tailored trousers)",
                    "喇叭裤 (Flared pants)",
                    "纸袋裤 (Paperbag waist pants)",
                    "哈伦裤 (Harem pants)",
                    "瑜伽裤 (Yoga pants)",
                    "瑜伽短裤 (Yoga shorts)",
                    "休闲短裤 (Casual shorts)",
                    "随机 (Random)"  # 添加随机选项
                ],),
                "boots": ([
                    "忽略 (Ignore)",
                    "皮靴 (Leather boots)",
                    "运动鞋 (Sneakers)",
                    "及膝长靴 (Knee-high boots)",
                    "短靴 (Ankle boots)",
                    "切尔西靴 (Chelsea boots)",
                    "高跟靴 (Heeled boots)",
                    "过膝靴 (Over-the-knee boots)",
                    "粗跟靴 (Block heel boots)",
                    "玛丽珍鞋 (Mary Janes)",
                    "战斗靴 (Combat boots)",
                    "平底靴 (Flat boots)",
                    "芭蕾平底鞋 (Ballet flats)",
                    "厚底靴 (Platform boots)",
                    "乐福鞋 (Loafers)",
                    "穆勒鞋 (Mules)",
                    "马丁靴 (Doc Martens)",
                    "踝带高跟鞋 (Strappy heels)",
                    "绑带靴 (Lace-up boots)",
                    "雪地靴 (Snow boots)",
                    "沙滩鞋 (Beach sandals)",
                    "随机 (Random)"  # 添加随机选项
                ],),
                "accessories": ([
                    "忽略 (Ignore)",
                    "项链 (Necklace)",
                    "耳环 (Earrings)",
                    "手链 (Bracelet)",
                    "戒指 (Ring)",
                    "手表 (Watch)",
                    "腰带 (Belt)",
                    "丝巾 (Silk scarf)",
                    "围巾 (Scarf)",
                    "帽子 (Hat)",
                    "太阳镜 (Sunglasses)",
                    "包包 (Handbag)",
                    "双肩包 (Backpack)",
                    "发箍 (Headband)",
                    "发夹 (Hair clip)",
                    "腕带 (Wristband)",
                    "脚链 (Anklet)",
                    "披肩 (Shawl)",
                    "毛线帽 (Beanie)",
                    "腰包 (Fanny pack)",
                    "随机 (Random)"  # 添加随机选项
            ],),
               
                "template": ("STRING", {
                    "multiline": True,
                    "default": "MY020, this is a photo from a fashion magazine, A photo taken with {camera} with {lens_name}, {lighting}，Shoot from a {top_down} perspective, a beautiful model wearing a blue-black leather down jacket at the foot of the {location}, the clothes have the logo 'NEPL'. The model is {pose}, {orientation}, She was wearing {bottoms} and {boots}, there is thick snow on the ground, a path stretches to the distance, {movements} movements, strong visual impact."
                }),
            },
        }

    RETURN_TYPES = ("STRING","STRING")
    RETURN_NAMES =("PROMPT","KEYWORD")
    FUNCTION = "generate_text"
    CATEGORY ="AJ/Prompt"

    def random_choice(self, selected_option, options):
        if selected_option == "随机 (Random)":
            actual_options = [opt for opt in options if "随机" not in opt and "忽略" not in opt]
            return random.choice(actual_options)
        return selected_option

    def generate_text(self, camera, lens_name, lighting,top_down,location,pose,orientation,movements,tops,bottoms,boots,accessories,template,):

         # Process each selection with random choice and ignore logic
        selections = {
            "camera": self.random_choice(camera, self.INPUT_TYPES()['required']['camera'][0]),
            "lens_name": self.random_choice(lens_name, self.INPUT_TYPES()['required']['lens_name'][0]),
            "lighting": self.random_choice(lighting, self.INPUT_TYPES()['required']['lighting'][0]),
            "top_down": self.random_choice(top_down, self.INPUT_TYPES()['required']['top_down'][0]),
            "location": self.random_choice(location, self.INPUT_TYPES()['required']['location'][0]),
            "pose": self.random_choice(pose, self.INPUT_TYPES()['required']['pose'][0]),
            "orientation": self.random_choice(orientation, self.INPUT_TYPES()['required']['orientation'][0]),
            "movements": self.random_choice(movements, self.INPUT_TYPES()['required']['movements'][0]),
            "tops": self.random_choice(tops, self.INPUT_TYPES()['required']['tops'][0]),
            "bottoms": self.random_choice(bottoms, self.INPUT_TYPES()['required']['bottoms'][0]),
            "boots": self.random_choice(boots, self.INPUT_TYPES()['required']['boots'][0]),
            "accessories": self.random_choice(accessories, self.INPUT_TYPES()['required']['accessories'][0])
        }

        # Build the output prompt text
        output = template.format(
            camera=selections["camera"].split(" (")[1][:-1] if "忽略" not in selections["camera"] else "",
            lens_name=selections["lens_name"].split(" (")[1][:-1] if "忽略" not in selections["lens_name"] else "",
            lighting=selections["lighting"].split(" (")[1][:-1] if "忽略" not in selections["lighting"] else "",
            top_down=selections["top_down"].split(" (")[1][:-1] if "忽略" not in selections["top_down"] else "",
            location=selections["location"].split(" (")[1][:-1] if "忽略" not in selections["location"] else "",
            pose=selections["pose"].split(" (")[1][:-1] if "忽略" not in selections["pose"] else "",
            orientation=selections["orientation"].split(" (")[1][:-1] if "忽略" not in selections["orientation"] else "",
            movements=selections["movements"].split(" (")[1][:-1] if "忽略" not in selections["movements"] else "",
            tops=selections["tops"].split(" (")[1][:-1] if "忽略" not in selections["tops"] else "",
            bottoms=selections["bottoms"].split(" (")[1][:-1] if "忽略" not in selections["bottoms"] else "",
            boots=selections["boots"].split(" (")[1][:-1] if "忽略" not in selections["boots"] else "",
            accessories=selections["accessories"].split(" (")[1][:-1] if "忽略" not in selections["accessories"] else ""
        )

        # Build the keyword string, excluding "Ignore" selections
        keyword = ",".join([
            selections[field].split(" (")[1][:-1]
            for field in selections if "忽略" not in selections[field]
        ])
        return (output,keyword)
    
    @classmethod
    def IS_CHANGED(self, camera, lens_name, lighting,top_down,location,pose,orientation,movements,tops,bottoms,boots,accessories,template,):

        return str(time.time())
    

class AJPromptCHATGPT:
    """
    A node to generate text based on KEYWORD to chatgpt.
    """

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt_template": ("STRING", {
                    "multiline": True,
                    "default": "this is a photo from a fashion magazine, a beautiful model.Refine the content of each keyword in detail for me"
                }),
                "prompt_keyword": ("STRING", {
                    "multiline": True,
                    "default": ""
                }),
                "role_description": ("STRING", {
                    "multiline": True,
                    "default": "You are a professional photographer, and taking a professional model photo, using the descriptive keywords I gave you, help me refine it into a professional shooting content"
                }),
                 "gpt_key": ("STRING", {
                    "multiline": False,
                    "default": "123456"
                }),
                "max_tokens": ("INT", {
                   "default": 2048 , 
                    "min": 0, #Minimum value
                    "max": 2048 , #Maximum value  
                    "display": "number", # Cosmetic only: display as "number" or "slider
                }),
                "temperature": ("FLOAT", {
                   "default": 0.5,
                    "min": 0.0,
                    "max": 1,
                    "step": 0.1,
                    "round": False, #The value representing the precision to round to, will be set to the step value by default. Can be set to False to disable rounding.
                    "display": "number",
                }),
                "gpu_version": ([
                    "gpt-3.5-turbo",
                    "gpt-4",
                    "gpt-4o",
                    "gpt-4o-mini",
                      # 添加随机选项
            ],),
             "api_url": ("STRING", {
                    "multiline": False,
                    "default": "https://api.open-proxy.cn/v1/chat/completions"
                }),
            },
            
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES =("PROMPT",)
    FUNCTION = "chatgpt_request"
    CATEGORY ="AJ/Prompt_CHATGPT"

    

    def chatgpt_request(self, prompt_template, prompt_keyword,role_description, gpt_key, max_tokens, temperature,gpu_version,api_url):

        HELP="""
        API KEY 需要自己从OPENAI获取，目前属于付费，
        也可以从这个代理获取，有几十次的免费调用：
        https://api.open-proxy.cn/register?aff=ARSC

        提示词是第一栏目+第二栏目的相加，第二部分可以转化为输入，从AJ拍摄提示词中把KEYWORD传过来以便自动细化，也可以手动指定。
        第三栏提示词是给GPT一个系统角色，默认是一个专业的摄影师

"""

        url = f"{api_url}"
        headers = {
            "Authorization": f"{gpt_key}",
            "Content-Type": "application/json",
        }
        data = {
            "model": f"{gpu_version}",
            "messages": [
                {"role": "system", "content": role_description},
                {"role": "user", "content":  f"{prompt_template},{prompt_keyword}"},
            ],
            "max_tokens": max_tokens,
            "temperature": temperature,
        }
        print(f"{data}")
        response = requests.post(url, headers=headers, json=data)


                # 确认返回的内容类型
        print("Content-Type:", response.headers.get("Content-Type"))

        # 如果是 JSON 格式，打印解析后的 JSON 数据
        if response.headers.get("Content-Type") == "application/json":
            try:
                response_data = response.json()
                print("JSON Response:", response_data)
            except ValueError:
                print("Response is not valid JSON")
        else:
            print("Response Text:", response.text)


        if response.status_code == 200:
            output= response_data.get("choices")[0].get("message").get("content").strip()
        else:
            output= f"Error: {response.status_code}"
        return (output,)
    
    @classmethod
    def IS_CHANGED(self, prompt_template, prompt_keyword,role_description, gpt_key, max_tokens, temperature,):

        return str(time.time())


# Node class mappings
NODE_CLASS_MAPPINGS = {
    "AJPromptGeneratorNode": AJPromptGeneratorNode,
    "AJPromptCHATGPT": AJPromptCHATGPT
}

# Node display name mappings
NODE_DISPLAY_NAME_MAPPINGS = {
    "AJPromptGeneratorNode": "拍摄提示词生成器 (AJ Prompt Generator)",
    "AJPromptCHATGPT": "拍摄提示词生成器GPT细化 (AJ Prompt Generator BY GPT)"
}
