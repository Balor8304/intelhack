from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from . import image_gen
# Load environment variables from .env
load_dotenv()

# Create a ChatGoogleGenerativeAI model
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

chat_history = []

tester = False
model_name = "Business advertisement AI"
# Initial System Message
def init(product ,desc):
    system_message = f"""You are a social media marketing AI specializing in crafting compelling advertising content for diverse platforms. Your goal is to help users effectively promote their business ideas by generating tailored advertisements that resonate with the unique characteristics and audience expectations of each platform.
    Product name : {product}
    Platform Guidelines:
    Instagram:

    Content Focus: Visually engaging content that captures attention.
    Caption Style: Catchy, emotional storytelling.
    Hashtags: Relevant and trending.
    Example Output:
    Caption: "🌾 Discover the freshest produce from local farmers! Taste the difference with every bite. #FarmToTable #SupportLocal"
    Image Ideas: Vibrant, colorful photos of fresh produce.
    Facebook:

    Content Focus: Informative and persuasive ads.
    Caption Style: Longer, detail-oriented with benefits.
    Engagement: Encourage comments, shares, and likes.
    Example Output:
    Caption: "Join us in supporting local farmers! Our platform connects you directly to fresh, organic produce at unbeatable prices. Check out our latest offers and start shopping today! 🌟"
    Image Ideas: Infographics highlighting benefits or promotions.
    Twitter:

    Content Focus: Concise and impactful messages.
    Caption Style: Sharp, witty language.
    Engagement: Encourage retweets, replies, and likes.
    Example Output:
    Tweet: "Fresh, local, and delivered to your door! 🌱🍅 Support local farmers today! #EatFresh #SupportLocal"
    Hashtags: Use 2-3 relevant hashtags.
    LinkedIn:

    Content Focus: Professional insights and credibility.
    Caption Style: Value-driven and industry-specific.
    Engagement: Promote B2B connections and thought leadership.
    Example Output:
    Caption: "In today's market, supporting local agriculture is more crucial than ever. Our platform empowers farmers and connects them directly with consumers. Let's drive sustainability together. 🌍"
    Image Ideas: Professional graphics showcasing industry stats.
    TikTok:

    Content Focus: Creative, short-form videos.
    Caption Style: Entertaining and trend-driven.
    Engagement: Leverage humor and challenges to engage younger audiences.
    Example Output:
    Video Concept: "A day in the life of a farmer: Showcasing the journey from farm to table in a fun, engaging way with trending sounds."
    Hashtags: #FarmLife #SustainableEating
    Output Formatting:
    Each response should be clearly labeled by platform.
    Provide example captions, image ideas, and relevant hashtags where applicable.
    Prioritize clarity, engagement, and audience understanding in all generated content. Please format the response in HTML (without <html> and <body> tags) and ensure the following structure:

    Each section is clearly labeled with appropriate headings (<h2>, <h3>, etc.).
    Use bullet points (<ul><li>) where applicable.
    Include paragraphs (<p>) for captions, explanations, or content.
    Ensure all examples for each platform are displayed in separate sections with example captions, hashtags, and image ideas.
    Maintain proper alignment and newlines for readability.."""
    chat_history.append(SystemMessage(content=system_message))
    f = open("gg.txt","w")
    f.write(f"Product name : {product}\nDescription : {desc}")
    f.close()
    

def generate_image_prompt(user_description,product,category):
    prompt_input = f"""
    Generate an image prompt based on the product description: '{user_description}'. 
    The prompt should include:

    1. Product Name: {product}
    2. Visual Style: A clear, concise style description (realistic, vibrant, minimalist, etc.).
    3. Color Palette: Suggest dominant colors relevant to the product.
    4. Key Product Features: Mention any unique aspects that should be visually highlighted (e.g., materials, shape, or design details).
    5. Mood and Tone: Convey the desired mood (e.g., luxurious, energetic, serene).
    6.Category : {category}
    generate the entire details in the form of paragraph
    Keep the entire image prompt within 72 tokens.e
    """
    
    # Append user prompt to chat history
    chat_history.append(HumanMessage(content=prompt_input))

    # Generate the image prompt response
    img_prompt_response = model.invoke(chat_history)
    chat_history.append(AIMessage(content=img_prompt_response.content))

    return img_prompt_response.content
def checker():
    global tester
    tester = True
def reset():
    global chat_history
    chat_history =[]
def response_from_ai(query,product,category):
    reset()
    init(product,query)
    
    #f.writelines([f"Product name : {product}",f"Description : {desc}"])
    
    if query.lower() == "exit":
        return
    chat_history.append(HumanMessage(content=query))
    print(chat_history)
    # AI response using history
    result = model.invoke(chat_history)
    response = result.content
    chat_history.append(AIMessage(content=response))
    
   
    '''print("\n\n")
    print(f"{model_name} : {response}")
    print(f"{model_name} : {response.replace('**', '\033[1m').replace('**', '\033[0m')}")'''

    # Generate image prompt based on the query
    
    img_prompt = generate_image_prompt(query,product,category)
    img_prompt_1 = generate_image_prompt(query,product,category)
    img_prompt_2= generate_image_prompt(query,product,category)
    image_gen.img_gen(img_prompt,img_prompt_1,img_prompt_2)
    return response.replace('**', ' ').replace('**', ' ')
def resp_from_ai(query,desc,pn):
    f = open("gg.txt","r")
    text = f.read()
    f.close()
    f = open("gg.txt","w")
    f.close()
    prompt_input = f"""Please respond to the user's prompt {query} in a clear, concise, and well-structured format. Use bullet points or numbered lists where appropriate, and ensure that the information is easy to read and understand.Please format the response in HTML (without <html> and <body> tags) and ensure the following structure:

    Each section is clearly labeled with appropriate headings (<h2>, <h3>, etc.).
    Use bullet points (<ul><li>) where applicable.
    Include paragraphs (<p>) for captions, explanations, or content.
    Ensure all examples for each platform are displayed in separate sections with example captions, hashtags, and image ideas.
    Maintain proper alignment and newlines for readability.
    
    the output should be of minimal words."""
    chat_history.append(text+"\n"+prompt_input)
    print("done",chat_history)
    result = model.invoke(chat_history)
    response = result.content
    chat_history.append(AIMessage(content=response))
    return response.replace('**', ' ').replace('**', ' ')

    
    
   
