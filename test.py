import requests
import time


session = requests.Session()

body = {
    "fb_dtsg": "NAcMqMgefqV4JFy8LZGi3_oD4njM8MlgV8SjJMmOj_6PsRtrao16PZA:17843708194158284:1709017255",
    "fb_api_req_friendly_name": "PolarisPostCommentInputRevampedMutation",
    "variables": '{"connections":["client:root:__PolarisPostComments__xdt_api__v1__media__media_id__comments__connection_connection(data:{},media_id:\\"3311880987322075007\\",sort_order:\\"popular\\")"],"request_data":{"comment_text":"Verify me pls"},"media_id":"3311880987322075007"}',
    "server_timestamps": "true",
    "doc_id": "6524763637625554",
}

response = session.get(
    "https://www.instagram.com/",
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "cookie": 'ig_did=DA297C9F-7520-422A-B603-8D882E711E8F; ig_nrcb=1; datr=vWBPZYdAcIc7cGcDIOXf5t63; fbm_124024574287414=base_domain=.instagram.com; ps_n=0; ps_l=0; mid=Zcsb5wALAAFlAQbQ2wuum7jgqnDc; dpr=1.100000023841858; ig_direct_region_hint="ODN\\05457160838095\\0541740076959:01f7777f6842cf37d644ab2ea9d7cc9a7c0a7f70cc3eb2b416b85060b2e5ae8a1c0e49ed"; shbid="7146\\05457160838095\\0541740294939:01f7f8ab8b1e56980b030ac3ddc5a9a87486a24f6ef9e75cca9c314c79780ccf26c145a2"; shbts="1708758939\\05457160838095\\0541740294939:01f7d509f198e3e2aac7031493094679a8891f6ff11464fa75a7fd9bc3a15b93b60cbcb9"; ds_user_id=59926273089; csrftoken=lKSRna5YfBw8tOrUBXVha9wKwcBbyqCc; sessionid=59926273089%3AbEWe0xXDnRa8ro%3A20%3AAYc3ZlpAw8Rip1zHO2egPM0_2u_yQZ0Q6oyAyMF1Ow; fbsr_124024574287414=aB_3KcUU9dQ7HQpV7aHtaHH99uuzCyu6ldHRh4URZkQ.eyJ1c2VyX2lkIjoiMTAwMDczMTY5OTAwMTk4IiwiY29kZSI6IkFRRHJScE8xcXhmbDQxSGtlTnB5YUVnTXV4dlpSaTZmS1p0NkR6TTFQbThTeEpfZXhBd2pCU1Qyd0ZKeE9yS0xYUjJjSzZJUnhDZHF2dGEzaDd1NXhxQThUUnBtRDIxQlBMRVRDV2NhUkpqZXdKX3pQVW5CNDdHUDdZZEVpTnIxUzl2bEJxOUF3MHJlaVlCTnlmbURtYldpSjB6TU1HVHEtM090STUtcm50MTI3MHliU3VZY1daeWVzejE5YUxXSHRfTlpYbTI5SGlvRDhweGQwRldhN1J1ZUlON3VmMWZnZUdVd0ZOMmtiSjh3R1lBOVVlVkRoMExpN092eGZGeTNBQkx4OEhRUVNqSjRXUFAwNHduT2J0WFdTS1VYMVp4ejRYckU4VTRTbVFTeE5TUGZTSDhqNTlELVNNeVJWc3J3WHVndDJTaUFzb1JVb0tMZC1uU3U1YUFMIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCTzM0ODFsSWRuQzJnUXRUSGhZUUd4SFpBbURGR0p3UjVHSENzQXo5SjJEajRPZEJCRG9qR1ZxSUY2aGJuMnVIdWdrOGdaQ094VlpDUVJvZEJVNUZEbkpxNHZKRkFnN0RkblQwbU1pQUtsWWVaQXFlVjBIQlJaQ2tLZ2RnTVhUMDhYUWsyWGtZNnNubkx3NTNVdEs5Q1JTU251Q1NPYVkyT2U5c2hrNkR5OTNrZG5aQkI4QnJwd0sxeW1GQUxPZGp2NnhGa3E4U0lzWkQiLCJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImlzc3VlZF9hdCI6MTcwOTAyNjA4OX0; fbsr_124024574287414=0E0osRf6Cfphz7NSPeJ7DY2fVUwkjNqdYOuN-pbGzQg.eyJ1c2VyX2lkIjoiMTAwMDczMTY5OTAwMTk4IiwiY29kZSI6IkFRQUNfdEc1blZHMWQySEJuQ2RZZDBkcWc3b1JzY3o0d3pCaUFFdEt2WUNRV3Y3M21hekhCV0hFRmxxUGhJWUpMRzRuTVVkUEt5NlV4Y0RJSzlaZU96eEVHUG1oUURyblFrcjJBZEFLWVo2ZjU0OTRkazNLc1NTMHJnclhLdDlxcG5FdDVHZHBZb182MmNTUEI0Ukx2TW5NZ1lhMHUtM0ZnRThtaXJsRV83SjhLRVBRZ25uREpiZ0k5WnRvNExVMXhsSjhCM0l6MkNQU0hFZFRtMUdtanhqZ0IxNFlxN2pKa0VDMTlBN1VuclRsQmRYNFAzTlhIYWhsaFg0S2JJcjlJTUpuR2VzNHNlQURDZmpqMlFpdW5uaFRRQThINjRGWDhrNVJZNF9TcUlwWHhsb0dsQUFRaDFEdnJFUzduZWhnX2puRXhkRVEzMTlJdlp1c3RtenBGUF9SIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCT3ljWkE4c0pJZnZmZndGRFVwYVI5OHhyQVlDbzNmTEpFaXp0bVpBYzVxbURjNVNtNFZPZW1tWTZMNXJVbVFRSm1zS2VxSjZKQWU2d3lqdnhITE5rQmVqc1JORFFGNEg1YVpCWEQ2ZkZqaDNRM05xVDRLZElkcExzSlZvaWh0UU1NM1JIMm45cGJzMlpDZWU0QzJnMXNqUFpCcXdkc1JQMzBoUXVaQlNwa3JvSkJYakd3dFpCU3U0YWhKck1FY0sxd1pEWkQiLCJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImlzc3VlZF9hdCI6MTcwOTAyNzAyNn0; rur="RVA\\05459926273089\\0541740563028:01f7beda3b55b69b569922eaa24c13ba9c6d926565c212c8dae0a3a6f339fe7e120a8801"',
        "Referer": "https://www.instagram.com/p/C32KjX7s8d_/",
        "Referrer-Policy": "strict-origin-when-cross-origin",
    },
)

with open("index.html", "w", encoding="utf-8") as file:
    file.write(response.text)
exit()

url = "https://www.instagram.com/api/graphql"
headers = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9,la;q=0.8,ru;q=0.7,es;q=0.6",
    "content-type": "application/x-www-form-urlencoded",
    "dpr": "1",
    "sec-ch-prefers-color-scheme": "dark",
    "sec-ch-ua": '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    "sec-ch-ua-full-version-list": '"Not A(Brand";v="99.0.0.0", "Google Chrome";v="121.0.6167.189", "Chromium";v="121.0.6167.189"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": '""',
    "sec-ch-ua-platform": '"Windows"',
    "sec-ch-ua-platform-version": '"15.0.0"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "viewport-width": "1920",
    "x-asbd-id": "129477",
    "x-csrftoken": "lKSRna5YfBw8tOrUBXVha9wKwcBbyqCc",
    "x-fb-friendly-name": "PolarisPostCommentInputRevampedMutation",
    "x-fb-lsd": "0slW8DgkR6sYZcm82-kwPv",
    "x-ig-app-id": "936619743392459",
    "cookie": 'ig_did=DA297C9F-7520-422A-B603-8D882E711E8F; ig_nrcb=1; datr=vWBPZYdAcIc7cGcDIOXf5t63; fbm_124024574287414=base_domain=.instagram.com; ps_n=0; ps_l=0; mid=Zcsb5wALAAFlAQbQ2wuum7jgqnDc; dpr=1.100000023841858; ig_direct_region_hint="ODN\\05457160838095\\0541740076959:01f7777f6842cf37d644ab2ea9d7cc9a7c0a7f70cc3eb2b416b85060b2e5ae8a1c0e49ed"; shbid="7146\\05457160838095\\0541740294939:01f7f8ab8b1e56980b030ac3ddc5a9a87486a24f6ef9e75cca9c314c79780ccf26c145a2"; shbts="1708758939\\05457160838095\\0541740294939:01f7d509f198e3e2aac7031493094679a8891f6ff11464fa75a7fd9bc3a15b93b60cbcb9"; ds_user_id=59926273089; csrftoken=lKSRna5YfBw8tOrUBXVha9wKwcBbyqCc; sessionid=59926273089%3AbEWe0xXDnRa8ro%3A20%3AAYc3ZlpAw8Rip1zHO2egPM0_2u_yQZ0Q6oyAyMF1Ow; fbsr_124024574287414=aB_3KcUU9dQ7HQpV7aHtaHH99uuzCyu6ldHRh4URZkQ.eyJ1c2VyX2lkIjoiMTAwMDczMTY5OTAwMTk4IiwiY29kZSI6IkFRRHJScE8xcXhmbDQxSGtlTnB5YUVnTXV4dlpSaTZmS1p0NkR6TTFQbThTeEpfZXhBd2pCU1Qyd0ZKeE9yS0xYUjJjSzZJUnhDZHF2dGEzaDd1NXhxQThUUnBtRDIxQlBMRVRDV2NhUkpqZXdKX3pQVW5CNDdHUDdZZEVpTnIxUzl2bEJxOUF3MHJlaVlCTnlmbURtYldpSjB6TU1HVHEtM090STUtcm50MTI3MHliU3VZY1daeWVzejE5YUxXSHRfTlpYbTI5SGlvRDhweGQwRldhN1J1ZUlON3VmMWZnZUdVd0ZOMmtiSjh3R1lBOVVlVkRoMExpN092eGZGeTNBQkx4OEhRUVNqSjRXUFAwNHduT2J0WFdTS1VYMVp4ejRYckU4VTRTbVFTeE5TUGZTSDhqNTlELVNNeVJWc3J3WHVndDJTaUFzb1JVb0tMZC1uU3U1YUFMIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCTzM0ODFsSWRuQzJnUXRUSGhZUUd4SFpBbURGR0p3UjVHSENzQXo5SjJEajRPZEJCRG9qR1ZxSUY2aGJuMnVIdWdrOGdaQ094VlpDUVJvZEJVNUZEbkpxNHZKRkFnN0RkblQwbU1pQUtsWWVaQXFlVjBIQlJaQ2tLZ2RnTVhUMDhYUWsyWGtZNnNubkx3NTNVdEs5Q1JTU251Q1NPYVkyT2U5c2hrNkR5OTNrZG5aQkI4QnJwd0sxeW1GQUxPZGp2NnhGa3E4U0lzWkQiLCJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImlzc3VlZF9hdCI6MTcwOTAyNjA4OX0; fbsr_124024574287414=0E0osRf6Cfphz7NSPeJ7DY2fVUwkjNqdYOuN-pbGzQg.eyJ1c2VyX2lkIjoiMTAwMDczMTY5OTAwMTk4IiwiY29kZSI6IkFRQUNfdEc1blZHMWQySEJuQ2RZZDBkcWc3b1JzY3o0d3pCaUFFdEt2WUNRV3Y3M21hekhCV0hFRmxxUGhJWUpMRzRuTVVkUEt5NlV4Y0RJSzlaZU96eEVHUG1oUURyblFrcjJBZEFLWVo2ZjU0OTRkazNLc1NTMHJnclhLdDlxcG5FdDVHZHBZb182MmNTUEI0Ukx2TW5NZ1lhMHUtM0ZnRThtaXJsRV83SjhLRVBRZ25uREpiZ0k5WnRvNExVMXhsSjhCM0l6MkNQU0hFZFRtMUdtanhqZ0IxNFlxN2pKa0VDMTlBN1VuclRsQmRYNFAzTlhIYWhsaFg0S2JJcjlJTUpuR2VzNHNlQURDZmpqMlFpdW5uaFRRQThINjRGWDhrNVJZNF9TcUlwWHhsb0dsQUFRaDFEdnJFUzduZWhnX2puRXhkRVEzMTlJdlp1c3RtenBGUF9SIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCT3ljWkE4c0pJZnZmZndGRFVwYVI5OHhyQVlDbzNmTEpFaXp0bVpBYzVxbURjNVNtNFZPZW1tWTZMNXJVbVFRSm1zS2VxSjZKQWU2d3lqdnhITE5rQmVqc1JORFFGNEg1YVpCWEQ2ZkZqaDNRM05xVDRLZElkcExzSlZvaWh0UU1NM1JIMm45cGJzMlpDZWU0QzJnMXNqUFpCcXdkc1JQMzBoUXVaQlNwa3JvSkJYakd3dFpCU3U0YWhKck1FY0sxd1pEWkQiLCJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImlzc3VlZF9hdCI6MTcwOTAyNzAyNn0; rur="RVA\\05459926273089\\0541740563028:01f7beda3b55b69b569922eaa24c13ba9c6d926565c212c8dae0a3a6f339fe7e120a8801"',
    "Referer": "https://www.instagram.com/p/C32KjX7s8d_/",
    "Referrer-Policy": "strict-origin-when-cross-origin",
}


response = session.post(url, headers=headers, data=body)
print(response.text)
