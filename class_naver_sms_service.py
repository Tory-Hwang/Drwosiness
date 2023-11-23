import hmac, hashlib, base64
import time, requests, json
import datetime

class naver_sms_sender:
    def __init__(self):
        self.access_key = "s3eXXncMlCE4yFSQBvRm"
        self.secret_key = "VXmRLti915ILkmAHuO68AR13r1ZQhVTGhS5jqwag"
        self.service_key = "ncp:sms:kr:258976261309:drowsiness"

        # 전화번호
        self.from_number ="01042270078"

        # <https://api.ncloud-docs.com/docs/ko/ai-application-service-sens-smsv2>
        self.url = "https://sens.apigw.ntruss.com"
        self.uri = f"/sms/v2/services/{self.service_key}/messages"

        self.timestamp = int(time.time() * 1000)
        self.timestamp = str(self.timestamp)
        current_time = datetime.datetime.now()
        self.contents = current_time.strftime("운전 중 졸음이 감지 되었습니다\t[%Y년 %m월 %d일 %H시 %M분 %S초]")
        
    def make_signature(self, secret_key, access_key, timestamp, uri):
        secret_key = bytes(secret_key, 'UTF-8')
        method = "POST"
        message = method + " "  + uri + "\n" + timestamp + "\n" + access_key
        message = bytes(message, 'UTF-8')
        signingKey = base64.b64encode(hmac.new(secret_key, message, digestmod=hashlib.sha256).digest())
        return signingKey

    def send_sms(self, to_number):

        header = {
        "Content-Type": "application/json; charset=utf-8",
        "x-ncp-apigw-timestamp": self.timestamp,
        "x-ncp-iam-access-key": self.access_key,
        "x-ncp-apigw-signature-v2": self.make_signature(self.secret_key, self.access_key, self.timestamp, self.uri)
        }

        # from : SMS 인증한 사용자만 가능
        data = {
            "type":"SMS",
            "from":self.from_number,
            "content":self.contents,
            "subject":"DROWSINESS다",
            "messages":[
                {
                    "to":to_number,
                }
                ]
            }

        res = requests.post(self.url+self.uri,headers=header,data=json.dumps(data))
        datas = json.loads(res.text)
        if res.status_code == 202:
            reid = datas['requestId']
            print("전송 성공{0}".format(reid))
        else:
            print("전송 실패")

#sms_sender=naver_sms_sender()
#sms_sender.send_sms("01042270078")