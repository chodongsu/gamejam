# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"
image ep3_cluster = "images/ep3/backgrounds/cluster.png"
image ep3_home = "images/ep3/backgrounds/home.png"
image ep3_gyeoul computer = "images/ep3/characters/gyeoul_computer1.png"
image ep3_gyeoul angry = "images/ep3/characters/angly1.png"
image ep3_bambi = "images/ep3/characters/bambi.png"
image ep3_gyeoul smile = "images/ep3/characters/gyeoul_smile1.png"
image ep3_quiz = "images/ep3/etc/quiz_1.png"

label ep3_start:
    $ scenter = Character(None,
    what_size=50, #폰트 사이즈
    what_xalign=0.5, #창 내에 텍스트를 중앙에 배치
    window_xalign=0.5, #창을 가로로 중앙에 배치
    window_yalign=0.5, #창을 세로로 중앙에 배치
    what_text_align=0.5, #창 내에 텍스트를 중앙에 배치 (만일을 대비해서)
    window_background=None,#창 제거, 글자만 보이기
    what_outlines=[(3, "#000000", 2, 2), (3, "#ffffff", 0, 0)],#경계선 보이기
    what_slow_cps=3 #텍스트 보이는 속도 조절
    )

    play sound "audio/ep3/sound/typing.mp3"
    scenter "Episode.3"

    play music "audio/ep3/bgm/ep3.mp3"
    scene home :
        zoom 2.7
#자취방배경
##### 희망찬 브금
    e "(오늘부터 라피신 시작이다.)"

    e "(비록 시작은 이상했지만 나름 나쁘지 않은 것 같기도...)" 

    e "(이왕 시작한 거 열심히 해보자 [e]!)"
#화면페이드아웃
    scene ep3_cluster with fade :
        zoom 2.9
#클러스터 배경 사슴 설명
###### 기본 브금
    show ep3_bambi
    bambi "{color=#ff0000}42경산{/color}은 동료학습을 기반으로 ..."

    bambi "{color=#ff0000}프랑스 에꼴 교육 모델{/color}을 기반으로... 정부지원사업..."
    hide ep3_bambi
    show ep3_gyeoul computer
#겨울이 컴퓨터하고있는사진'
    e "[e] 옆자리엔 겨울이가 컴퓨터를 하고있다."

    e "(우와... 예쁘다... 누구지? 이런 애도 여기 오는 구나...)"
#밤비온
    hide ep3_gyeoul
    show ep3_bambi
    bambi " ...그럼 지금부터 {color=#ff0000}라피신{/color}을 시작하시면 됩니다!"
    hide ep3_bambi
    e "...?"

    e "설명이 이게 끝인가? 강사는? 도와주는 사람이 아무도 없어...?"

    e "일단 문제라도 열어보자..."

# <문제 pdf 창>
# do you check your left neighbor?
# …right…

    e "너의... 이웃...에게... 질문...해라...?"

    e "..."

    e "질문... 내가 할 수... 있을까...?"
######(웅성이는 소리 - 준콱 사운드 부탁)
    play sound "audio/ep3/sound/woong.mp3"
    narration "주변은 점점 시끄러워졌다."
#! 여기서 겨울 복장 : 검정 후드, 묶은 머리, 검은 뿔테 안경, 화장기 없는 모습, 검색 키워드에 nerd, Geek넣어서 하면 도움 될 듯.
    show ep3_gyeoul computer
    citiman "…. 고마워! 이제 어떻게 하는지 알겠다!"
#겨울웃는사진
    show ep3_gyeoul smile
    gyeoul "(웃음) 또 모르는 거 있으면 물어봐 ㅎㅎ"

    e "(와... 웃는 모습 진짜 예쁘다...)"

    e "(...보기랑 다르게 엄청 착한가 보다...)"
#겨울이컴퓨터하는사진으로
    show ep3_gyeoul computer
    e "..."

    e "...동료 학습...이라고 했으니깐..."
    play sound "audio/ep3/sound/foot.mp3"
    e "..."
    e "나도...물어...볼까?"

#발소리
    e "저...저기..."
#겨울이화나는표정
    show ep3_gyeoul angry with hpunch
    stop music
    play music "audio/ep3/bgm/gyeoul first.mp3"
    gyeoul "..."

    narration "[e]을 위아래로 훑어보는 겨울."

    e "(뭐지... 나.. 지금... 이상한가...?)"
###### 날카로운 브금
    gyeoul "뭐야?"

    e "그... 그게... 그..."

    gyeoul "뭐야? 너 말 못해?"
    scene black with dissolve
    e "그 ...미...미안... 미안해..."
    hide gyeoul
    e "(도망치듯 자리를 벗어나고 나니 등 뒤가 축축한 것이 느껴진다.)"

    e "(숨쉬기가 답답하고 이 느낌은 마치...)"
    
    e "(고등학교 시절 일진에게 찍혔을 때의 느낌...)"

    e "..."

    e "(나... 잘못 걸린걸까...?)"

    e "아니야. 여기서 포기하면 아무것도 안되는 거야. 다시 혼자서라도 해보자."
    scene ep3_cluster with fade :
        zoom 2.9
#(딸깍거린는 효과음) / click
    play sound "audio/ep3/sound/click.mp3"
    e "..."

    e "..."
    play sound "audio/ep3/sound/click.mp3"
    e "..."
    play sound "audio/ep3/sound/click.mp3"
    e "..."

    e "어… 이걸 이렇게 하면 되는...건가...?"

    show ep3_quiz at center :
        zoom 0.63
        ypos 750
    $ choice_position = "bottom"

    menu:
        "1번":
            e "…역시 이런건 나랑 안맞아…"
            scene black with dissolve
        "2번":
            e "…생각보다 재미있을 지도…?"
            scene black with dissolve
        "3번":
            e "…역시 이런건 나랑 안맞아…"
            scene black with dissolve
        "4번":
            e "…역시 이런건 나랑 안맞아…"
            scene black with dissolve

    play music "audio/ep3/bgm/ep3.mp3"
#자취방도착
    scene ep3_home :
        zoom 2.7
    narration "기숙사에 도착한 [e]"

# 문제 틀리면 (힘든 하루였다.)
# 문제 맞추면 (보람찬 하루였다.)
#페이드아웃
    e "얼떨결에 시작했는데 {color=#ff0000}라피신{/color}..."
    scene black with dissolve
    e "생각보다 나쁘지 않을지도..."
    e "...(스르륵)"

    e "다사다난 했던 하루를 마무리하며 잠이 들어버린 [e]"

    stop music fadeout 2.0
    jump ep4_start
# # 에피 3 끝 