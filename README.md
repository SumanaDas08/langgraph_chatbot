# LangGraph Chatbot

A streaming chatbot built with LangGraph and NVIDIA NIM API.

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```
   python -m venv myenv
   myenv\Scripts\activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Create a `.env` file and add your NVIDIA API key:
   ```
   NVIDIA_API_KEY=your_nvidia_api_key_here
   ```
5. Run the app:
   ```
   python -m streamlit run streaming_steam.py
   ```

## Get NVIDIA API Key
- Go to [build.nvidia.com](https://build.nvidia.com)
- Sign in and click **Get API Key**
