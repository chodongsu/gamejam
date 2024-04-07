image cluster = "images/ep6/background/사람 있는 클러스터.png"
image home = "images/ep6/background/자취방사진 2.png"
image sikdang = "images/ep6/background/식당.PNG"
image ep6_quiz = "images/ep6/etc/quiz_2.png"

image bambi = "images/ep6/etc/밤비.png"
image notice = "images/ep6/etc/시스템_공지1.png"
image computer1 = "images/ep6/etc/컴퓨터_조배정.png"

image gyeoul jjz = "images/ep6/gyeoul/후드 째려보는 겨울 2.png"
image gyeoul angry = "images/ep6/gyeoul/angly.png"
image gyeoul silmang = "images/ep6/gyeoul/약간 실망한 겨울.PNG"
image ep6_gyeoul = "images/ep6/gyeoul/gyeoul_little.png"
image ep6_gyeoul smile = "images/ep6/gyeoul/gyeoul_smile.png"
image ep6_gyeoul angry = "images/ep6/gyeoul/gyeoul_angry.png"
image ep6_gyeoul smile2 = "images/ep6/gyeoul/gyeoul_smile2.png"

image gaeul sad = "images/ep6/gaeul/가을_슬픔.PNG"
image gaeul angry = "images/ep6/gaeul/가을_화남.PNG"
image gaeul = "images/ep6/gaeul/가을_무표정.PNG"
image gaeul = "images/ep6/gaeul/가을_디폴트.PNG"

image bomi smile = "images/ep6/bomi/보미_행복.PNG"
image bomi = "images/ep6/bomi/보미_디폴트.PNG"
image bomi hello = "images/ep6/bomi/보미_인사2.PNG"
image bomi sad = "images/ep6/bomi/보미_우울.PNG"

image phone k1 = "images/ep6/phone/ep6카톡_1.png"
image phone k2 = "images/ep6/phone/ep6카톡_2.png"
image phone k3 = "images/ep6/phone/ep6카톡_3.png"
image phone k4 = "images/ep6/phone/ep6카톡_4.png"
image phone k5 = "images/ep6/phone/ep6카톡_5.png"
image phone k6 = "images/ep6/phone/ep6카톡_6.png"
image phone k7 = "images/ep6/phone/ep6카톡_7.png"
image phone k8 = "images/ep6/phone/ep6카톡_8.png"
image phone lock = "images/ep6/phone/잠금화면_2.png"
image phone lock1 = "images/ep6/phone/잠금화면_3.png"



# define narration = Character(_(''), cloor="#e888c2")
# define gaeul = Character(_('서가을'), color="#7d2926f8")
# define bomi = Character(_('윤보미'), color="#36824b")
# define gyeoul = Character(_('한겨울'), color="#9c94a0ff")
# define cat = Character(_('고양이'), color="#c69a3b")
# define bambi = Character(_('루돌프'), color="#9c623eaa")
# define citiman = Character(_('지나가는시민1'), color="#3a409b")
# define player_name = "플레이어이름"
# define e = Character("player_name",dynamic = True,color="#ff0000")
#!!!나이트타임입력
transform nighttime:
    matrixcolor BrightnessMatrix (-0.5)

transform nighttime2:
    matrixcolor BrightnessMatrix (0)
#ep6 start

label ep6_start:
# 배경
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
    play sound "audio/ep6/eff/typing.mp3"
    scenter "Episode.6"
    play music "audio/ep6/bgm/ep6.mp3"
    scene home
    # 에피6

    #**에피 6**

    #클러스터
    #시스템 창 or 슬랙 알림으로 오늘이 러쉬발표날이라는거 알려줌
    scene cluster :
        zoom 2.9
    play sound "audio/ep6/eff/slack.mp3"
    show notice at center :
        zoom 0.7
        ypos 700  # 캐릭터의 세로 위치
    narration "RUSH 발표날"
    hide notice with dissolve
#밤비등장
    show bambi
    bambi "여러분~ 벌써 라피신 절반이 지나갔네요! 이제 남은 절반동안도 열심히 달려볼까요?"

    bambi "오늘은 드디어 {color=#ff0000}RUSH{/color}가 시작되는 날입니다!"

    bambi "잠시 후 팀원과 팀장이 발표되니 모두 확인해 주세요!"

    e "(아.. 오늘이 러쉬였구나.. 한번 확인 해 볼까..?)"
    hide bambi with dissolve
    show computer1 at center :
        zoom 0.63
        ypos 900
    e "(어디보자… 조원이...)"

    e "( 윤보미, 서가을, 한겨울..?)"
   
    e "(이게 말이 되나??)"

    e "(그리고 내 사진 옆에 있는 별은 뭐지...?)"
#밤비등장
    bambi "아! 사진 옆에 별이 붙어있는 사람이 팀장입니다!"
    
    bambi "그럼 다들 화이팅~ *^^*"
#밤비아웃
    e "(잠깐 별이 팀장...??!!?!?)"

    e "(지금이라도 취소해야...!)"
#밤비등장
    bambi "그럴 일은 없겠지만! 만약 팀원 중 한명이라도 취소한다면 팀원 전체가 0점처리되니,"
    
    bambi "모두 책임감 있게 진행해 주세요~!"
#밤비아웃
    e "(이게 무슨..! 평생 단 한 번도 조장같은거 해본 적이 없는데..!)"

    e "(하 망했다...)"
    scene black with dissolve
    #화면 블랙으로 페이드아웃
    #카톡화면등장(문자알림음 등장)
    #노뚝이 슬랙으로 단톡방 만듦

# 여기는 슬랙 대화창으로 보여지는게 좀 많음
    play sound "audio/ep6/eff/letter.mp3"
# <모바일 화면 창>
    scene home :
        zoom 2.62
    show phone k1 at center :
        zoom 0.65
        ypos 970
    bomi "하이하이~! 다들 반가워~~"
    show phone k2 at center :
        zoom 0.65
        ypos 970
    bomi "우리 러쉬 열심히 해보자! >_<"
    show phone k3 at center :
        zoom 0.65
        ypos 970
    gaeul "다들 잘 부탁해~"
    show phone k4 at center :
        zoom 0.65
        ypos 970
    bomi "팀장님도 잘 부탁해~!!"   
    e "(아... 단톡... 방 처음인데... 뭐라고 해야...)"
    show phone k5 at center :
        zoom 0.65
        ypos 970
    bomi "그럼 12시에 모여서 다같이 밥먹으면서 이야기 해 볼까?"
    show phone k6 at center :
        zoom 0.65
        ypos 970
    gaeul "좋아 그렇게 하자"
    show phone k7 at center :
        zoom 0.65
        ypos 970
    gyeoul "ㅇㅋ"

    e "(다같이 점심...? 재미있겠다...)"
    show phone k8 at center :
        zoom 0.65
        ypos 970
    e "그...그러자.."
    hide phone
    e "(이렇게 핸드폰 알람이 많이 울린 적이 있었나...?)"
    
    play sound "audio/ep6/eff/shower.mp3"
    e "슬슬 씻어야지."
    
    
#문자알림음
    show  phone lock1
    narration "띠링"

# 보미 갠톡 온거임
    gyeoul "우리 같은조더라"

    gyeoul "팀장. 잘 해보자"
# 근데 준비한다고 못봄.

# 배경 그림에 주인공 준비하는데 핸드폰 위로 메시지 창 띠링 띠링 뜨고 마는거임.
    narration "연락을 못 본 [player_name]..."
    scene black with dissolve
    narration "그렇게 시간이 흐른 후"
#(대충 셔츠에 청바지 입고 어색해하는 주인공 그림)
    e "아..! 이러다 늦겠다... 빨리 가야..."
    play sound "audio/ep6/eff/letter.mp3"
    narration "띠링"
    show phone lock at center :
        zoom 0.65
        ypos 970
    bomi "팀장~"

    bomi "나 이제 나갈건데"

    bomi "같이 가자!!"

    e "(어...? 보미 집은 여기 근처가 아닌데...?)"

    e "(뭐라고 답장해야...)"
#전화울리는소리
    hide phone with dissolve
    play sound "audio/ep6/eff/call.mp3"
    narration "([player_name]의 전하기가 울린다)"
    show bomi smile
    stop sound
    bomi "[player_name]! 준비 다 했어?"

    e "어...? 어..."

    bomi "우왕! 타이밍 짱이다~! 나 지금 너네집 앞에 막 도착했는데!"

    e "어...? 우리 집에...? 왜...?"

    bomi "무슨소리야~ 이유가 어디있어! 보고싶으니까 왔지!!"
    show bomi hello
    bomi "빨리 내려와~!"
    play sound "audio/ep6/eff/calloff.mp3"
    hide bomi with dissolve
    narration "(뚝)"
#화면 페이드아웃
    scene black with dissolve
    e "(보미가 왜 여기까지..? 일단 빨리 내려가자)"
#식당 on
    scene sikdang :
        zoom 3.2
    show bomi smile at left

    narration "보미와 같이 식당에 간 [player_name]."
#노랑이 웃으면서 등장
# (기싸움 구간)
#겨울이 화난표정
    #!!!중얼거림 ->중얼중얼
    #!!!bomi nighttime
    show bomi smile at left , nighttime
    show ep6_gyeoul angry at right
    gyeoul "...내 연락은 받지도 않더니.."
    $ love[2] -= 3 #!!! 겨울호감

#!!!가을 앵그리로 바꿈
    show ep6_gyeoul angry at right , nighttime
    show gaeul angry at center
    gaeul "뭐야...? 둘이...? 무슨 사이야...?"
    show gaeul angry at center , nighttime
    show ep6_gyeoul angry at right , nighttime2
    gyeoul "[player_name] 너 설마 둘이..."
    $ love[0] -= 3 #!!! 


# <선택지>

# 1. ….그냐 오는 길에 만났어
# 2. … 우린 친구야
# 3. …(얼굴 붉히기)
#보미 웃으면서
    show ep6_gyeoul angry at right , nighttime
    show gaeul angry at center , nighttime
    show bomi smile at left , nighttime2
    bomi "아! 몰랐구나! [player_name]이랑 나랑 어릴때부터 친구였어!"
    
    bomi "이제는 아니게 될 수도 있지만 ㅎㅎ"
#겨울 놀래면서
    show bomi smile at left , nighttime
    show ep6_gyeoul angry at right , nighttime2
    gyeoul "그게 무슨 소리야?"
#보미웃으면서
    show ep6_gyeoul angry at right , nighttime
    show bomi smile at left , nighttime2
    bomi "너가 신경쓸 만한 일은 아니야."
    show bomi smile at left, nighttime
    e "(분위기가 이상하다... 이게 무슨 일이지...?)"
#가을 화내면서
    show gaeul angry at center , nighttime2
    gaeul "자, 다들 뭐 먹을래? 주문부터 하자."
    show gaeul angry at center , nighttime
    e "그...그래 주문하자!"
#화면페이드아웃
    scene black with dissolve
    e "(잠깐 무슨 일이 있었던 것 같지만)" 
    
    e "(이후 우리는 밥을 먹으며 과제에 대한 이야기를 진행했다.)"
    scene cluster :
        zoom 3.2
#페이드인
#가을디폴트
    show gaeul at left
    gaeul "그럼 이 부분은 이렇게 풀면 될 것 같은데?"
#겨울디폴트
    show gaeul at left , nighttime
    show ep6_gyeoul at center
    gyeoul "응 그럼 난 DFS부분 짜올게."
#보미디폴트
    show ep6_gyeoul at center , nighttime
    show bomi at right
    bomi "좋아! 그럼 난 파일입출력쪽 해올게!"
#가을디폴트
    show bomi at right , nighttime
    show gaeul at left , nighttime2
    gaeul "그럼 내일까지 각자 맡은 부분 해서 다시 모이자!"
#화면 페이드아웃
    scene black with dissolve
    e "(정신을 차려보니 과제는 어느덧 거의 완성되어 있었다...)"

    e "(내가 너무 아무것도 한게 없는 것 같은데… 이래도 될까...?)"

    e "(클러스터에서 더 많이 공부해 봐야겠다...)"

    narration "다음날..."
    scene home :#!!!!zoom
        zoom 2.8
    narration "과제 제출날"

    e "드디어 제출이다...!"

#시스템창 과제 제출하기 누르면 퀴즈 뜸
    show ep6_quiz at center :
        zoom 0.63
        ypos 900
    menu :
        "정답을 골라주세요!{fast}"
        "1번":
            show bomi smile at right
            bomi "역시 [player_name]이야! 정말 대단해!"

#놀래는겨울
            show ep6_gyeoul smile at left
            gyeoul "잘했어 [player_name]. 이번에 좀 했네."
            $ love[2] += 20 #!!! 겨울호감
            scene black with dissolve
        "2번":
            show gaeul at left
            gaeul "그래도 좋은 경험이었어...!"
            show ep6_gyeoul at center
            gyeoul "...역시 너무 과대평가 한걸까?"
            show bomi sad at right
            bomi "괜찮아~! 그래도 재미있었잖아!"
            scene black with dissolve
        "3번":
            show gaeul at left
            gaeul "그래도 좋은 경험이었어...!"
            show ep6_gyeoul at center
            gyeoul "...역시 너무 과대평가 한걸까?"
            show bomi sad at right
            bomi "괜찮아~! 그래도 재미있었잖아!"
            scene black with dissolve
        "4번":
            show gaeul at left
            gaeul "그래도 좋은 경험이었어...!"
            show ep6_gyeoul at center
            gyeoul "...역시 너무 과대평가 한걸까?"
            show bomi sad at right
            bomi "괜찮아~! 그래도 재미있었잖아!"
            scene black with dissolve
    jump ep7_start
# # 퀴즈 성공시 -
# #놀래는보미
#     show bomi smile at right
#     bomi "역시 [player_name]이야! 정말 대단해!"
# #놀래는겨울
#     show ep6_gyeoul smile at left
#     gyeoul "잘했어 [player_name]. 이번에 좀 했네."

# # 실패시.
# #가을아쉬워하며?혹은디폴트
#     show gaeul at left
#     gaeul "그래도 좋은 경험이었어...!"
#     show ep6_gyeoul at center
#     gyeoul "...역시 너무 과대평가 한걸까?"
#     show bomi sad at right
#     bomi "괜찮아~! 그래도 재미있었잖아!"
