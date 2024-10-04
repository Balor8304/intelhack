from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage

# Load environment variables from .env
load_dotenv()

# Create a ChatGoogleGenerativeAI model
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

chat_history = []
model_name = "Business advertisement AI"

# Initial System Message
system_message = SystemMessage(content="""You are a social media marketing AI specializing in crafting compelling advertising content for diverse platforms. Your goal is to help users effectively promote their business ideas by generating tailored advertisements that resonate with the unique characteristics and audience expectations of each platform.

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
Prioritize clarity, engagement, and audience understanding in all generated content.""")

chat_history.append(system_message)

def generate_image_prompt(user_description):
    prompt_input = f"""
    Generate a detailed qualifying prompt for image generation based on the following product description: '{user_description}'. 
    The prompt should include the following elements:
    
    1. Visual Style: Specify a style (e.g., realistic, abstract, minimalist, vibrant).
    2. Color Palette: Suggest dominant colors that should be present in the image.
    3. Key Attributes: Highlight specific features or aspects of the product that should be visually represented.
    4. Mood and Tone: Describe the overall mood or emotion the image should convey (e.g., energetic, serene, luxurious).
    
    Ensure the prompt is focused on visual elements and characteristics without including any text.
    """
    
    # Append user prompt to chat history
    chat_history.append(HumanMessage(content=prompt_input))

    # Generate the image prompt response
    img_prompt_response = model.invoke(chat_history)
    chat_history.append(AIMessage(content=img_prompt_response.content))

    return img_prompt_response.content

def moss(query):
    if query.lower() == "exit":
        return 
    chat_history.append(HumanMessage(content=query))
    
    # AI response using history
    result = model.invoke(chat_history)
    response = result.content
    chat_history.append(AIMessage(content=response))
    
    return response
    # Generate image prompt based on the query

print("------Message History------")
for message in chat_history:
    print(message.content)