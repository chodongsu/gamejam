# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
image outside = "images/ep1/backgrounds/background.PNG"
image oasis = "images/ep1/backgrounds/오아시스_왼쪽.PNG"
image oasis mental = "images/ep1/backgrounds/오아시스_정신차리기.png"

image gaeul falldown= "images/ep1/characters/가을_넘어짐.PNG"
image gaeul upside = "/images/ep1/characters/가을_밑에서봄.PNG"
image gaeul trouble = "images/ep1/characters/가을_곤란.PNG"
image gaeul smile = "images/ep1/characters/가을_웃음.PNG"
image gaeul sorry = "images/ep1/characters/가을_미안_눈물없음.png"
image gaeul sorry2 = "images/ep1/characters/가을_미안손얼굴눈물없음.png"
image gaeul surprise = "images/ep1/characters/가을_놀램.png"


# 게임에서 사용할 캐릭터를 정의합니다.
define player_name = "이경"
define narration = Character(_(''), color="#e888c2", who_outlines=[(0.3, "#000000", 0, 0.3)])
define e = Character("player_name", dynamic = True, color="#ffffff", who_outlines=[(0.3, "#000000", 0, 0.3)])
define gaeul = Character(_('서가을'), color="#7d2926f8", who_outlines=[(0.3, "#000000", 0, 0.3)])
define bomi = Character(_('윤보미'), color="#ffe289", who_outlines=[(0.3, "#000000", 0, 0.3)])
define gyeoul = Character(_('한겨울'), color="#9c94a0ff", who_outlines=[(0.3, "#000000", 0, 0.3)])
define cat = Character(_('고양이'), color="#c69a3b", who_outlines=[(0.3, "#000000", 0, 0.3)])
define bambi = Character(_('루돌프'), color="#9c623eaa", who_outlines=[(0.3, "#000000", 0, 0.3)])
define citiman = Character(_('지나가는시민1'), color="#3a409b", who_outlines=[(0.3, "#000000", 0, 0.3)])

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

# 호감도 수치
define persistent.love = [0, 0, 0]

init:    
    screen stat_overlay:       
    # 호감도 창        
        frame:            
            # 호감도 창 테두리와 컨텐츠와의 간격            
            padding (20, 20)            
            # 호감도 배경 (반투명 - 뒤 2자리 코드가 투명도)            
            background "#4f5a6680"            
            # x, y축 정렬            
            align (1.0, 0.0)            
            # 호감도 창 크기            
            xmaximum 350         
            ymaximum 300            
            # 텍스트와 호감도 바가 수직으로 배치됨            
            vbox:                                
                text "서가을{space=15}[persistent.love[0]]" size 16                
                bar:                    
                    value persistent.love[0]                    
                    # 호감도 바 범위                    
                    range 100                                        
                    # 아래 지정한 fixed_bar 스타일을 따름                    
                    style "fixed_bar"                                    
                    # 다음 캐릭터의 바와 이전 캐릭터 텍스트 사이의 간격                
                    # padding을 쓸 경우, 바, 텍스트 간격 모두 동일하게 적용됨                
                text " " size 3                 
                text "윤보미{space=15}[persistent.love[1]]" size 16           

                bar:
                    value persistent.love[1]                    
                    range 100                    
                    xalign 0.0                    
                    style "fixed_bar"                 
                text " " size 3                 
                text "한겨울{space=15}[persistent.love[2]]" size 16                 
                bar:                    
                    value persistent.love[2]                    
                    range 100                    
                    xalign 0.5                    
                    style "fixed_bar" 

init -5 python:    
    # 호감도 바 스타일    
    style.fixed_bar = Style(style.default)        
    # bar width    
    style.fixed_bar.xmaximum = 200        
    # bar height    
    style.fixed_bar.ymaximum = 15        
    # bar의 gutter 부분 간격; 5로 지정할 시 5만큼 색이 칠해져있음    
    style.fixed_bar.left_gutter = 0     
    style.fixed_bar.right_gutter = 0

    style.fixed_bar.left_bar = Frame("images/bar_full.png", 0, 0)    
    style.fixed_bar.right_bar = Frame("images/bar_empty.png", 0, 0) 


label start:

# 클러스터 전까지 ----------------------------------------------------------------------------

    show screen stat_overlay

    play music "/audio/ep1/bgm/에피1_bgm.mp3"

    $ name = renpy.call_screen("set_name", title="{size=+10}{color=#ff74ce}캐릭터 이름 입력{/color}{/size}\n\
    이름은 최대 4글자까지만 가능합니다\n\
    입력하지 않을 시 '이경'으로 설정됩니다\n", init_name = "")
    # $ e = Character(name, color="#ffffff") //이거 주석처리함
    # $player_name = renpy.input("당신의 이름을 입력해주세요\n\n이름은 3글자까지 가능합니다")
    align_center "당신의 이름은 [player_name]입니다."

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
    show gaeul sorry with dissolve

    gaeul "저기...괜찮아요...?"

    e "(희미한 목소리가 들린다. 이 목소리는...여잔가...?)"
    show gaeul surprise
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
    show gaeul sorry2
    gaeul "저..진짜 죄송한데 제가 지금 급하게 할 일이 있어서 먼저 가볼게요!!! 죄송해요!!"

    narration "(급하게 나가는 가을)"
#이미지 : 가을이 페이드아웃
    hide gaeul sorry2
    e "..여긴 어디지..?"
#배경 : 오아시스 배경
#사운드 : 웅성웅성 사운드
    e "(주위를 둘러보니 그냥 소파들이랑 의자들이랑..진짜 쉬는 공간인가 보네...)"

    e "(얼른 나가봐야겠다...)"
    hide background with fade
    jump ep2_start

