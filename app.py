
import os
from typing import List

from save_db_utils import add_notion_db_page, write_notion_db_page
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_sdk.errors import SlackApiError
from summarize_utils import get_pdf_text, get_sections, load_pdf, make_xml_file, write_markdown

# # tokens
# SLACK_BOT_TOKEN_PART1 = 'xapp-1-A05G52XKT9T-5551918442851-54e6799de989b66d368'
# SLACK_BOT_TOKEN_PART2 = 'f1632d2cf80c5512f078806b3c69bf80b34265d36494b'
# SLACK_APP_TOKEN_PART1 = 'xoxb-3090891879607-5549135666453-vo7'
# SLACK_APP_TOKEN_PART2 = 'VW8SR3iPDg8rHfYNvBu0Y'

# 初期化
app = App(token=os.environ.get(SLACK_BOT_TOKEN))


# メンション
@app.event("app_mention")
def handle_app_mention_events(body, logger, say):
    logger.info(body)
    bot_user_id = body['authorizations'][0]['user_id']
    text = body['event']['text']
    user = body['event']['user']


# アプリ起動時
if __name__ == "__main__":
    SocketModeHandler(app, os.environ[SLACK_APP_TOKEN]).start()