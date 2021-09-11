import discord

end_msg = "\n\n개발자 : ! 자곱#9937 | [개발자 서버](https://discord.gg/VgBm4PYVjq) | [초대링크](https://discord.com/oauth2/authorize?client_id=817999653500747806&permissions=1342450743&scope=bot)"

help_embed = discord.Embed(title="명령어", description="자동자가진단 봇에 대한 도움말 입니다. ㅈ명령어 로 확인 가능합니다.\n평일날에만 자가진단이 작동하며, 공휴일 제외 기능을 추가할 예정입니다.",color=0x62c1cc)
help_embed.add_field(name="ㅈ정보등록", value="ㅈ정보등록 [이름] [생년월일] [지역] [학교이름] [학교타입] [비밀번호]```ㅈ정보등록 홍길동 721027 서울시 길동고 고등학교 1234``````ㅈ정보등록 홍길동 050201 충청남도 길동중 중학교 2580```※정보등록은 `개인DM`에서만 작동합니다.", inline=False)
help_embed.add_field(name="ㅈ정보삭제", value="※디스코드 아이디를 기준으로 삭제합니다.\n※만약 디스코드 계정이 바뀌었을 경우 ! 자곱#9937 님께 문의 부탁드립니다.", inline=False)
help_embed.add_field(name="ㅈ정보확인", value="※디스코드 아이디를 기준으로 확인합니다.\n※만약 디스코드 계정이 바뀌었을 경우 ! 자곱#9937 님께 문의 부탁드립니다.", inline=False)
help_embed.add_field(name="ㅈ진단참여", value="수동으로 자가진단을 실시합니다.", inline=False)
help_embed.add_field(name="ㅈ자가진단실시", value="중지되었던 자동자가진단을 다시 실시합니다.\nㅈ진단참여 명령어를 통한 수동자가진단은 정상적으로작동합니다.", inline=False)
help_embed.add_field(name="ㅈ자가진단중지", value="이제부터 자동자가진단이 작동되지않습니다.\nㅈ진단참여 명령어를 통한 수동자가진단은 정상적으로작동합니다.", inline=False)
help_embed.add_field(name="ㅈ급식", value="ㅈ급식\nㅈ급식 <날짜> <태그>의 형식으로 타인의 급식도 볼 수 있습니다.", inline=False)
help_embed.add_field(name="기타명령어",value="`ㅈ학년반정보입력 [학년] [반]`\n`ㅈ급식`, `ㅈ내일급식`, `ㅈ어제급식`\n`ㅈ시간표`\n`ㅈ학사일정`", inline=False)
help_embed.add_field(name="기타",value="자동자가진단은 7시 00분에서 7시 16분 사이에 랜덤하게 작동하며,\n자동자가진단 DM 메시지를 통하여 그 다음날의 작동 시간을 알 수 있습니다.", inline=False)
help_embed.add_field(name="정보",value=end_msg)
