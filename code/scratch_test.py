from google import genai
from pydantic import BaseModel
from typing import Dict, Optional, List
import os

class ImageNote(BaseModel):
    image_id: str
    note: str

class VLMAnalysis(BaseModel):
    evidence_standard_met: bool = True
    evidence_standard_met_reason: str = ""
    risk_flags: str = "none"
    issue_type: str = "unknown"
    object_part: str = "unknown"
    claim_status: str = "not_enough_information"
    claim_status_justification: str = ""
    supporting_image_ids: str = "none"
    valid_image: bool = True
    severity: str = "unknown"
    per_image_notes: Optional[List[ImageNote]] = None

from dotenv import load_dotenv
load_dotenv()

# Using API key from environment variable
key = os.getenv("GOOGLE_API_KEY", "")
client = genai.Client(api_key=key)

try:
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=["Answer the following test. Set evidence_standard_met = True, issue_type = 'scratch', object_part = 'screen', claim_status = 'supported', severity = 'low'. Add notes for img_1 and img_2."],
        config={
            "temperature": 0.1,
            "response_mime_type": "application/json",
            "response_schema": VLMAnalysis,
        }
    )
    print("SUCCESS!")
    print("Response text:", response.text)
except Exception as e:
    import traceback
    traceback.print_exc()
