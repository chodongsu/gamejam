# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
image outside = "images/ep1/backgrounds/background.PNG"
image oasis = "images/ep1/backgrounds/오아시스_왼쪽.PNG"
image oasis mental = "images/ep1/backgrounds/오아시스_정신차리기.png"

image gaeul falldown= "images/ep1/characters/가을_넘어짐.PNG"
image gaeul upside = "/images/ep1/characters/가을_밑에서봄.PNG"
image gaeul trouble = "images/ep1/characters/가을_곤란.PNG"
image gaeul smile = "images/ep1/characters/가을_웃음.PNG"

# 게임에서 사용할 캐릭터를 정의합니다.
define player_name = "이경"
define narration = Character(_(''), cloor="#e888c2")
define e = Character("player_name",dynamic = True, color="#ffffff")
define gaeul = Character(_('서가을'), color="#7d2926f8")
define bomi = Character(_('윤보미'), color="#ffe289")
define gyeoul = Character(_('한겨울'), color="#9c94a0ff")
define cat = Character(_('고양이'), color="#c69a3b")
define bambi = Character(_('루돌프'), color="#9c623eaa")
define citiman = Character(_('지나가는시민1'), color="#3a409b")

define align_center = Character(None,
    what_size=30, #폰트 사이즈
    what_xalign=0.5, #창 내에 텍스트를 중앙에 배치
    window_xalign=0.5, #창을 가로로 중앙에 배치
    window_yalign=0.3, #창을 세로로 중앙에 배치
    what_text_align=0.5, #창 내에 텍스트를 중앙에 배치 (만일을 대비해서)
    window_background=None,#창 제거, 글자만 보이기
    what_outlines=[(3, "#000000", 2, 2), (3, "#ffffff", 0, 0)],
    #경계선 보이기
    what_slow_cps=6 #텍스트 보이는 속도 조절 
    )
    
screen set_name(title, init_name):
    frame:
        xpadding 50
        ypadding 50
        xalign 0.5 yalign 0.5
        vbox:
            # spacing 20
            text title :
                xalign 0.5
                textalign 0.5
            input default init_name xalign 0.5

label ep1_start:

# 클러스터 전까지 ----------------------------------------------------------------------------

    play music "/audio/ep1/bgm/에피1_bgm.mp3"

    $ name = renpy.call_screen("set_name", title="{b}{size=+10}캐릭터 이름 입력{/size}{/b}\n\
    이름은 최대 4글자까지만 가능합니다\n\
    입력하지 않을 시 '이경'으로 설정됩니다\n", init_name = "")
    $ e = Character(name, color="#ffffff")

    scene outside

    align_center "...오늘도 지루한 하루였다.\n\n
    집이든 학교든 누구에게도 환영받지 못하는 삶...\n\n
    지금 당장 내가 사라지더라도 누구 하나 알아차려줄 사람이 있을까?\n\n
    그래도 오늘은 다르다.\n\n
    내 흑백 세상 속에서 유일하게 색을 가지고 있는 하나의 존재.\n\n
    '낯선 동네에서 익숙한 계절의 향기가 난다' 의 마지막 화가 나오는 날이기 때문\n\n 
    얼른 집에 가 봐야....\n" 

    scene black
    stop music 
    play sound "audio/ep1/eff/어깨부딪히는소리.mp3" 

    narration "쿵!" with vpunch
    gaeul "앗..!"
    e "으악!!"
    e "..."
    e "아 잠깐 정신이..."

# 오아시스 ----------------------------------------------------------------------------
    scene oasis with dissolve
    pause 1.0
    scene black with dissolve
    pause 1.0
    scene oasis mental with dissolve :
        zoom 0.5
    pause 1.0
    scene black with dissolve
    pause 1.0
    scene oasis with dissolve
    show gaeul upside with dissolve

    gaeul "저기...괜찮아요...?"

    e "(희미한 목소리가 들린다. 이 목소리는...여잔가...?)"
    show gaeul trouble
    gaeul "어떡해.. 정신이 좀 드세요?"

    e "(아까 나는 집에가서 애니를..보려고..)"

    e "(잠시만 여긴 어디지?)"

    e "..여긴...어디.."
#이미지 : 가을이 평소 표정
    show gaeul smile
    gaeul "아! 아까 잠깐 정신을 잃으셔서 제가 데려왔어요!"

    e "..."
#이미지 : 난감한표정짓는 가을이
    gaeul "그냥 학생들이 공부하는 곳인데 여기는 휴게공간이니깐 충분히 쉬다가 가시면 돼요!"

    e "...(끄덕끄덕)"
    show gaeul trouble
    gaeul "저..진짜 죄송한데 제가 지금 급하게 할 일이 있어서 먼저 가볼게요!!! 죄송해요!!"

    narration "(급하게 나가는 가을)"
#이미지 : 가을이 페이드아웃
    hide gaeul trouble
    e "..여긴 어디지..?"
#배경 : 오아시스 배경
#사운드 : 웅성웅성 사운드
    e "(주위를 둘러보니 그냥 소파들이랑 의자들이랑..진짜 쉬는 공간인가 보네...)"

    e "(얼른 나가봐야겠다...)"
    hide background with fade
    jump ep2_start

