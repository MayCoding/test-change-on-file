import sys
import json
import datetime
import base64
import requests


def base64_encoding(contentBody):
    """
    BASE64 인코딩
    """
    contentBody_bytes = contentBody.encode('UTF-8')
    contentBody_base64 = base64.b64encode(contentBody_bytes)
    content = contentBody_base64.decode('UTF-8')

    return content

def update_github_content(repo,filename,content,sha):
    """
    레포, 파일이름, 콘텐츠 내용을 받아 깃헙의 콘텐츠를 업데이트합니다.
    """
    today = datetime.datetime.now().strftime('%Y.%m.%d %H:%m:%s')
    OWNER = 'MayCoding'
    HEADERS = {"Accept": "application/vnd.github+json", 
                    "Authorization":"Bearer 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",
                    "X-GitHub-Api-Version":"2022-11-28"}
    if content:
        content = base64_encoding(content)
    URL = f"https://api.github.com/repos/{OWNER}/{repo}/contents/{filename}"
    body = {
            "message":f"Automate {today}",
            "committer":
                {
                "name":"MayCoding",
                "email":"maycoding0719@gmail.com"
                },
            "content":content
            }
    if sha:
        body["sha"]=sha
    res = requests.put(URL, headers=HEADERS, data=json.dumps(body))
    print(res.text)

def process_changes(changes):
    # 변경 내용을 처리하는 로직 작성
    print(changes)
    # 변경 내용을 사용하여 작업 수행

    repo = 'test-change-on-file'
    update_github_content(repo,'result_test.txt',changes,None)
    

if __name__ == "__main__":
    changes = sys.argv[1]
    process_changes(changes)
