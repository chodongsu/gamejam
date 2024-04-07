# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
image background corridor = "images/ep2/background/2층복도.png"
image background house = "images/ep2/background/자취방.png"
image background meteor = "images/ep2/background/멸망.webp"

image bomi happy = "images/ep2/bomi/보미_웃음.png"
image bomi default = "images/ep2/bomi/보미_평소.png"
image bomi sad = "images/ep2/bomi/보미_시무룩.png"
image bomi back = "images/ep2/bomi/보미_뒷모습.png"
image bomi hi = "images/ep2/bomi/보미_인사1.png"
image bomi bye = "images/ep2/bomi/보미_인사2.png"

image phone zero = "images/ep2/phone/잠금화면.png"
image phone one = "images/ep2/phone/카톡_1.png"
image phone two = "images/ep2/phone/카톡_2.png"
image phone three = "images/ep2/phone/카톡_3.png"
image phone four = "images/ep2/phone/카톡_4.png"

label ep2_start:
    play music "audio/ep2/bgm/ep2.mp3" fadein 2.0
    scene background corridor :
        zoom 0.5
    narration "(복도로 나간 000)"
    #보미 뒷모습
    show bomi back
    narration "눈앞에 보이는 윤보미"

    e "어... 쟤는..?"
    #보미가 놀라는 모습
    show bomi hi
    bomi "어? ㅇㅇㅇ! 너 ㅇㅇㅇ 맞지?"

    e "어??"
    #보미 웃는표정
    show bomi   
    bomi "우와! 너도 {color=#FF5D5D}이거{/color} 하러 온거야??"

    e "(윤봄이, 초등학교 동창이다. 어릴 때에는 꽤 친했던 것 같기도 한데...)"

    e "(중학교시절 부터였나?)"

    e "(내가 친구들과 잘 어울리지 못하다 보니 자연스레 멀어졌다...)"

    e "(사실 나는 예전에 봄이를....)"

    e "(아니다...)"

    bomi "나 사실 예전부터 엄청 해보고 싶었는데 이번에 용기내서 도전하는 거거든!"
    #보미디폴트표정
    show bomi  
    bomi "너는 어떻게 온거야? 너도 {color=#FF5D5D}이거{/color} 하는거 맞지?"
    menu:
        bomi "너는 어떻게 온거야? 너도 {color=#FF5D5D}이거{/color} 하는거 맞지?{fast}"
        "..어? ..응!":
            jump second_y
        "..아니. 난 다시 나갈거야..":
            jump second_n

label second_y:
# 1번 선택시
    #보미웃는표정
    show bomi smile
    bomi "정말?? 안그래도 혼자 신청한거라 좀 걱정했는데! 너도 같이 한다니 너무 좋아!!"

    bomi "우리 진짜 오랜만에 만난 것 같은데 이렇게 만나다니!"
    
    bomi "혹시 우리 운명인 건 아닐까?"

    e "우..운..운명이라니.."
    #보미디폴트
    show bomi
    bomi "왜~ 너 기억안나?"
    bomi "우리 어릴때 커서 결혼하기로 했잖아!"

    e "(당황하며) ...그게 무슨 소리야! 당연히"
    menu:
        e "(당황하며) ...그게 무슨 소리야! 당연히{fast}"
        "기억…나…":
            show bomi happy
            bomi "너 어 릴 때 엄청 귀여웠는데! 그런데 크고나서는 자주 볼 일이 없어서 속상했어.."
            bomi "그런데 이렇게 다시 만나니까 너무 좋다!!!!"
            #(호감도 +10)
        "…그런 거 기억 안 나…":
            show bomi sad
            bomi "아… 그렇구나..."
            show bomi
            bomi "그래~ 예전 일이 뭐가 중요해! 지금 우리가 같이 만난게 중요한거지!"
            #(호감도 +3)
    e "으응..."
    #보미 일반표정
    show bomi 
    bomi "나 번호 그대론데. 너 번호 바뀌었어?"

    e "아...아니..."
    #보미웃는표정
    show bomi bye
    bomi "그럼 다음주에 보자!"
    
    bomi "연락할게!"
    hide bomi with dissolve 
    e "내 번호 가지고 있었구나..."
    
    e "그런데 무슨 연락을 한다는 거지?"
    
    e "일단 집에 가자..."

    #장면 페이드아웃 이후 집 화면
    scene black with dissolve
    scene background house with dissolve :
        zoom 2.7

    e "(무슨 일이 있었던 거지..?)"

    e "(그러니까 내가 여자애랑 부딪히고.. 정신을 잃고...)"
    
    e "(무슨 이상한 곳에 가서.. 봄이를 만나고..?)"

    e "({color=#FF5D5D}라피{/color}..? 무슨 이상한거에 등록한 것 같은데..?)"
    #벨소리울리는소리
    play sound "audio/ep2/eff/문자알림음.mp3"
    narration "띠링!"
    show phone four at center :
        zoom 0.7
    bomi "오늘 만나서 너무 반가웠어!"
    # 봄 : 오늘 만나서 너무 반가웠어!
    show phone one at center :
        zoom 0.7
    bomi "오늘 만나서 너무 반가웠어!"
    show phone two at center :
        zoom 0.7
    bomi "우리 다음주부터 {color=#FF5D5D}라피신{/color} 열심히 해보자!"
    # 봄 : 우리 다음주부터 라피신 열심히 해보자!
    e "(아… 라피신 그런 이름이었지..)"

    e "답장 보내야 겠지..?"
    show phone three at center :
        zoom 0.7
    e "그래!"
    show phone four at center :
        zoom 0.7
    bomi "약속한 거다? 너 다음 주에 안 나오면 반칙이다~!"
    stop music fadeout 5.0
    #노래끝
    #화면 페이드아웃
    scene black with dissolve
    jump ep3_start

# 2번 선택 시
label second_n:
    stop music
    scene background meteor
    narration "잘못된 선택으로 인해 지구가 멸망했다.."
    return