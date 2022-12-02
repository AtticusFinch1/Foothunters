# import asyncio
# import websockets


# async def handler(websocket):
#     while True:
#         message = await websocket.recv()
#         print(message)


# async def main():
#     url = "wss://dev.foothunters.com/app/vvplayers?protocol=7&client=js&version=7.0.6&flash=false"
#     data = {"auth":"vvplayers:dfb221d9fa563e691ac165625849625676d383704fa25bfab9eb91321e12dd1f"}
#     async with websockets.connect(url) as ws:
#         await handler(ws)
#         await asyncio.Future()  # run forever



# if __name__ == "__main__":
#     asyncio.run(main())

# import asyncio
# from pywsitest import WSTest, WSResponse, WSMessage

# ws_test = (
#     WSTest("wss://dev.foothunters.com/app/vvplayers?protocol=7&client=js&version=7.0.6&flash=false")
#     .with_parameter("channel", "private-App.Models.Room.143")
#     .with_response(
#         WSResponse()
#         .with_attribute("event")
#         .with_trigger(
#             WSMessage()
#             .with_attribute("event", "MessageRead")
#         )
#     )
#     .with_response(
#         WSResponse()
#         .with_attribute("message", "test")
#     )
# )

# asyncio.get_event_loop().run_until_complete(ws_test.run())
import json
import requests
from requests.auth import HTTPBasicAuth

almUserName = "Oliver"
almPassword = "password"
headers = {
    'Accept': "application/json",
    'Content-Type': "application/json",   
    'Cookie':'_ga=GA1.1.355600800.1665981596; _hjSessionUser_3162940=eyJpZCI6IjIyODU1ZWEwLTcyNGYtNTVmMC04NDQ2LTIzMWU5OTcwMjJmMyIsImNyZWF0ZWQiOjE2NjU5ODE1OTY0ODgsImV4aXN0aW5nIjp0cnVlfQ==; zfm_cnt_ck_id=gvr0erjlluj1669262282635; _hjSessionUser_3256203=eyJpZCI6IjcxZGRhMTFjLTlkODctNTU5MS1hZDc5LWY5MGRmZmU4NzViNCIsImNyZWF0ZWQiOjE2NjkyNjIyODIzMDYsImV4aXN0aW5nIjp0cnVlfQ==; _ga_WWMVMGZRR9=GS1.1.1669982249.61.1.1669982326.0.0.0; _ga_X5T3N3G6LH=GS1.1.1669982250.68.1.1669982326.0.0.0; XSRF-TOKEN=eyJpdiI6IjZpeFVGWVlMUDliWkFxV3BvU3RaZlE9PSIsInZhbHVlIjoiNnQzUDJxV01DSHZ3NHNnMnAyZ0pGTlZocUhDOWp4TCt4Ylh1WlhxU2UyTVBFa1BQQzMrZEJFTm51UElIQTcrUElzNkZPTmYxMW5EVk9HNUduSk9DQXlja0xtc0hHa0FSMkxMSWYyU0JnbGc5WHAvL2tuUnJxbjF0cWdGYi9vRG4iLCJtYWMiOiIxMWMxZTE4NTE0NWFlZGZiMjhhNDQxZDVkNTk1MWFlYzJlYjBlYWFiYzlhNGM0MmJlMDEyOTc0MWJlMGMzNDY0IiwidGFnIjoiIn0%3D; foothunters_session=eyJpdiI6ImRtcjdCWW9ybUFna3RRN2YraTlJRHc9PSIsInZhbHVlIjoiQTBXMVN5bEF5V1RicEhNOG54UDhlWGRndUtuTWMxZWsvQ0cybmkyL2Zya3Z4YnFyMEo4bE0xNDU1NmIzTzRzejQzN0ZDdWtQdmFTTTRGMW52MVRFeHl4T3V3dllBb2FyTnNsRU5Dem05YjR2b0hkbkdxeG1ycjM5c3R0cWVNaHciLCJtYWMiOiI3MTdkNmU2MDAzZDdlNDI0NzgwMGZiZTFmYjU3MjA5NGIxZGQ0ZWZkMjMzOGQ5ODliYmE5YjM4ZmI0M2FjNWZiIiwidGFnIjoiIn0%3D' 
    }
payload = {
    'username':'Oliver'
}
response = requests.post('https://dev.foothunters.com/api/players/get', data=payload)
player = response.json()["player"]
print(player["followers_count"])
