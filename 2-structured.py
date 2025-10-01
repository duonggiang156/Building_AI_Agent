#%%
import os
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    )

# --------------------------------------------------------------
# Step 1: Define the response format in a Pydantic model
# --------------------------------------------------------------

#%%
class CalendarEvent(BaseModel):
    name: str
    date: str
    participants: list[str]

# --------------------------------------------------------------
# Step 2: Call the model
# --------------------------------------------------------------
#%%

completion = client.beta.chat.completions.parse(
    model="gemini-2.5-flash",
    messages=[
        {"role":"system", "content":"Extract the event information."},
        {
            "role":"user",
            "content":"Tôi và Dương tham dự lễ tốt nghiệp vào chủ nhật."
        }
    ],
    response_format=CalendarEvent,
)

# --------------------------------------------------------------
# Step 3: Parse the response
# --------------------------------------------------------------
event = completion.choices[0].message.parsed
# event.name
# event.date
# event.participants
print(event)