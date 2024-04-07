# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.

image exam_screen = "images/ep4/characters/exam_screen.png"
image exam_screen_successs = "images/ep4/characters/exam_screen_success.png"
image ep4_exam = "images/ep4/etc/quiz_exam.png"

image background cluster = "images/ep4/backgrouds/cluster.png"
image background cherry_blossom = "images/ep4/backgrouds/cherry_blossom.PNG"
image background oasis = "images/ep4/backgrouds/oasis.PNG"
 
image bambi = "images/ep4/characters/bambi.png"

image ep4_gaeul exam = "images/ep4/characters/gaeul/gaeul_exam.png"
image ep4_gaeul nolram = "images/ep4/characters/gaeul/gaeul_nolram.png"
image ep4_gaeul simoo = "images/ep4/characters/gaeul/gaeul_simoo.png"
image gaeul default = "images/ep4/characters/gaeul/gaeul_normal.PNG"
image gaeul backshot = "images/ep4/characters/gaeul/gaeul_backshot.PNG"
image gaeul upset_smile = "images/ep4/characters/gaeul/gaeul_disappoint.PNG"
image gaeul embarrass = "images/ep4/characters/gaeul/gaeul_diificulty.PNG"
image gaeul smile = "images/ep4/characters/gaeul/gaeul_smile.PNG"
image gaeul big_smile = "images/ep4/characters/gaeul/gaeul_bigsmile.PNG"
image gaeul sad = "images/ep4/characters/gaeul/gaeul_sad.PNG"
image ep4_gaeul happy = "images/ep4/characters/gaeul/gaeul_defult.png"
image bomi default = "images/ep4/characters/bomi/bomi_normal.png"
image bomi greet = "images/ep4/characters/bomi/bomi_greet.png"
image bomi smile = "images/ep4/characters/ep4/bomi/bomi_smile.png"
image bomi backshot = "images/ep4/characters/ep4/bomi/bomi_backshot.png"
image bomi sad = "images/ep4/characters/ep4/bomi/bomi_sad.png"
image bomi surprise = "images/ep4/characters/bomi/bomi_surprise.png"

transform nighttime:
    matrixcolor BrightnessMatrix (-0.5)

transform nighttime2:
    matrixcolor BrightnessMatrix (0)

label  ep4_start:
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
    play music "audio/ep4/bgm/double.mp3"
    play sound "audio/ep4/eff/typing.mp3"
    scenter "Episode.4"

    scene background cluster :
        zoom 3.0
    e "(오늘은 대망의 exam날이다.)"

    e "(과연 내가 잘 할 수 있을까?)"
    show bambi
    bambi "지금부터 시험 시작하겠습니다!"

    bambi "다들 exam계정으로 로그인하세요!"
# 시험컴퓨터화면
# id는 입력되어있고
    hide bambi
    show exam_screen at center :
        zoom 0.9
        ypos 1200
menu:
        "{size=+30}다음 중 올바른 패스워드는 무엇일까요?\n{/size}"
        "1. 42gyeongsan":
            stop music fadeout 6.0
            jump bad_ending
        "2. forty_two":
            stop music fadeout 6.0
            jump bad_ending
        "3. exam": 
            jump answer_question

# 로그인 실패하면
label bad_ending :
    bambi "시험 시간 10분 경과했습니다! 아직까지 로그인 못 한 분들은 퇴실해주세요!"

    scene black with dissolve
    e "(역시 난 안되는 걸까...)"

    e "(무거운 걸음으로 집에 돌아왔다...)"

    e "(침대에 누운 채로 하루, 이틀...)"

    e "..."
    return
# 게임 종료

# #로그인 성공 시
label answer_question :
    hide exam_screen
    play sound "audio/ep4/eff/correct.mp3"
    show exam_screen_successs at center :
        zoom 0.9
        ypos 1200
    e "(된건가..? 열심히 해보자!)"
#화면어두워짐
#벚꽃화면으로
    hide exam_screen_successs with dissolve
    scene black with dissolve
    e "(하 드디어 끝났다...)"

    e "(4시간이 마치 40분처럼 느껴질 만큼 내가 가진 모든 것을 쏟아낸 시간이었다.)"

    e "(5문제... 기대했던 만큼은 아니지만)"
    
    e "(그 동안 노력했던 시간에 대한 보답으로는 충분한 점수다.)"

    e "([e]. 나도 하면 되는 거였구나.)"

    e "(시험을 처음 치는 것도 아닌데 어쩐지 홀가분한 마음이 든다.)"

    e "(아! 시험 끝나고 오아시스에서 도시락을 준다고 했었지?)"
    play sound "audio/ep4/eff/foot.mp3"
    narration "발걸음을 돌려 오아시스로 향했다." 
    scene oasis
    narration "오아시스에 가까워질수록 웅성이는 소리가 커져왔다."

    narration "그리고 그 사이에 혼자 앉아있는.."
#가을이뒷모습
    show gaeul backshot
    e "넌 그때...골목길...?"
#가을이 속상한데웃는표정
    hide gaeul backshot
    show gaeul default
    gaeul "어? 이름이..."
    
    gaeul "[e]이었나...?"

    e "기억...하는구나..."
#가을이 살짝웃음(없으면 활짝웃음)
    hide ep4_gaeul nolram
    show gaeul default
    gaeul "당연하지. 내가 그때 얼마나 미안했는데..."

    gaeul "너도 지금 라피신 중이면 오늘 시험 친 거야?"
    
    e "어..? 응..."
    
    e "생각보다 잘 친 거 있지. 그때 너 덕분에 지금 라파신을 할 수 있게 됐어."
#가을당황하는표정
    gaeul "아냐! 네가 열심히 한 덕분에 잘 한 거겠지."
#가을 웃으며#!!!가을웃으며
    show gaeul smile
    gaeul "잘 적응하고 있는 것 같아 보기 좋다."
    $ love[0] += 3 #!!! 가을호감 13

    e "(갑자기 생각지도 못한 칭찬을 들어버렸다.)"

    e "...너는? 시험 잘 봤어...?"
#가을 울먹이는표정
    show gaeul embarrass
    gaeul "...아 나는...그냥..."
    $ love[0] -= 5 #!!! 가을호감 8

    e "(어떡하지...? 내가 눈치없게...)"

    e "...그...그러니까..."

#봄 인사하며등장
    hide gaeul embarrass
    show bomi greet with vpunch
    bomi "어! [e]!"

    bomi "시험 잘봤어?????"
 
    e "그 봄아...! 잠깐...!"
    show bomi smile
#봄웃으면서
    bomi "나 이번 시험 진짜 엄청 잘 친 거 있지!"
#격앙된표정?살짝좋으면서 홍조가 올라옴
    bomi "혹시 나 천재가 아닐까?"
#살짝슬퍼짐
    show bomi sad
    bomi "근데 5번 문제에서 막혀서 너무 아쉬워..."
#궁금해하는표정
    show bomi default
    bomi "[e] 넌 몇 개나 풀었어?"

    e "...그게 난 ...5...개..."
#완전 놀래는봄
    # show bomi surprise
    show bomi surprise
    bomi "뭐야! 너 엄청 잘했잖아!!"
    $ love[1] += 6 #!!! 봄 호감

    bomi "그럼 너 5번문제 어떻게 풀었는지 알려주면 안 돼?"

    e "어..? 으...응..."
    show ep4_exam at center :
        zoom 0.63
        ypos 900
    
# <퀴즈>

menu:
        "다음 중 올바른 것은?"
        "1. 1번":
            jump down_likeability
        "2. 2번":
            jump down_likeability
        "3. 3번" : 
            jump down_likeability
        "4. 4번" :
            jump up_likeability
# 맞추면
#보미놀래는표정
label up_likeability :
    hide ep4_exam
    show bomi surprise at right
    bomi "와! [e]! 너 진짜 짱이다!!" #호감도 + 7
    $ love[1] += 7 #!!! 봄호감

#가을놀래는표정
    show bomi surprise at right , nighttime
    show ep4_gaeul exam at left
    gaeul "너 엄청 잘 하는구나...! 멋지다..." #호감도 + 9
    $ love[0] += 18 #!!! 가을호감

    jump return_epi

# 틀리면
#봄 무표정
label down_likeability :
    hide ep4_exam
    show bomi default at right
    bomi "음... 역시 어려운 문제인가 보네. 괜찮아 그래도 시험 때는 맞췄잖아?" #호감도 + 5
#가을무표정
    show bomi default at right , nighttime
    show gaeul default at left
    gaeul  "...생각보다 잘 못하는구나..." #호감도 -3
    $ love[0] -= 9 #!!! 가을호감하락

    jump return_epi

label return_epi :
    show bomi default at right , nighttime2
    hide ep4_gaeul
    show gaeul default at left , nighttime
    bomi "그러고보니 너는 서가을...? 맞지?"
#땀흘리면서 당황하는 표정
    hide ep4_gaeul happy
    show bomi default at right , nighttime
    show gaeul default at left , nighttime2
    gaeul "어? 응..."
    show bomi default at right , nighttime2
    show gaeul default at left , nighttime
    bomi "너도 엄청 열심히 공부하던데! 시험 잘 봤어?"
    show bomi default at right , nighttime
    show gaeul default at left , nighttime2
    gaeul "아...난..."
    show gaeul default at left , nighttime
    narration "갑자기 분위기가 싸해졌다."

    e "...음! 이러지말고 우리 시험도 끝났는데..."
    
    e "나가서 ...도시락 먹을까...?"

    e "(순간 어디서 그런 용기가 났는지 모를 일이다.)"

    e "(어떡하지? 지금이라도 실수라고 할까?)"
    show bomi smile at right
#보미 웃는모습
    show bomi default at right , nighttime2
    show gaeul default at left , nighttime
    bomi "그래! 진짜 좋은 생각이다! 지금 벚꽃도 피고 날씨도 좋고! 지금 바로 나가자!"
#가을이도 웃는모습
    hide gaeul
    show bomi smile at right, nighttime
    show ep4_gaeul happy at left , nighttime2
    gaeul "...좋아! 기분 전환도 되고 좋겠다!"
    show bomi smile at right , nighttime2
    show ep4_gaeul happy at left, nighttime
    bomi "그래. 사람이 많으면 더 재미있으니까!"
    show bomi smile at right , nighttime
    e "(다행히 둘다 기분이 나쁘진 않은가 보다.)"
#벚꽃배경
    scene black with dissolve
    scene background cherry_blossom with dissolve
#봄,가을 놀라는표정 양쪽으로
    show bomi surprise at right
    bomi "우와아아~!"
    show bomi surprise at right , nighttime
    show ep4_gaeul happy at left
    gaeul "예쁘다...!"
#가을뒤에서보이는이미지
    hide bomi surprise
    show ep4_gaeul simoo at center
    gaeul "있잖아 [e]. 오늘 사실 많이 힘들어서..."

    gaeul "아까 거의 울 뻔 했는데..."
    show ep4_gaeul happy at center
#가을활짝웃음
    gaeul "너 덕분에 기분이 훨씬 나아졌어!"

    gaeul "고마워!"
    $ love[0] += 6 #!!! 가을호감
    
    show ep4_gaeul happy at center , nighttime
    e "(그냥 당황해서 나가자고 한 것 뿐인데...)"

    e "(나 덕분이라니... 이런 기분은... )"
    
    e "(처음이다.)"

    e "그렇게 말해줘서..."
    
    e "고마워..."
    
    # show gaeul surprise
#가을놀라는표정
    show ep4_gaeul happy at center , nighttime2
    gaeul "무슨 말이야 내가 더 고맙지!"
#가을일반표정
    hide ep4_gaeul nolram
    show gaeul default at center
    gaeul "그런데 [e]. 혹시 넌 좋아하는 계절이 뭐야?"

#발자국소리,봄이무표정등장,좌가을,우봄
    e "응? 특별히 생각해 본 적은..."
#보미가 웃으면서
    show gaeul default at left , nighttime
    show bomi default at right
    bomi "아~ 계절? [e]이는 봄을 제일 좋아해."

    bomi "가을이 너는? 어떤 계절 좋아해?"
#가을썩표정
    show bomi default at right , nighttime
    show gaeul default at left , nighttime2
    gaeul "나?? 나도 특별히 좋아하는 계절은 없는데."
#가을웃음
    hide gaeul
    show ep4_gaeul happy at left
    gaeul "아! 봄은 별로야. 황사가 심하잖아~ ^^"

    gaeul "너는 무슨 계절 좋아하는데?"
#봄은웃는데화난표정
    hide ep4_gaeul happy
    show bomi default at right , nighttime2
    show gaeul default at left , nighttime
    bomi "나? 글쎄, 나도 특별히 싫어하는 계절은 없는데...?"
    hide gaeul
    show bomi default at right , nighttime
    show ep4_gaeul happy at left , nighttime2
    gaeul "에이~ 그래도 제일 좋아하는거 하나는 있을거 아니야~"
    hide ep4_gaeul happy
    show bomi default at right , nighttime2
    show gaeul default at left , nighttime
    bomi "글쎄… 좋아하는건 아무래도... 봄? 예쁘잖아~"
#보미웃으면서
    show bomi smile at right
    bomi "아! 근데 가을은 별로더라."
    show bomi smile at right , nighttime
    e "..그래? 봄이 너가 싫어하는 것도 있었나..?"
    show bomi smile at right , nighttime2
    bomi "그러게~ 근데 싫어하는데 이유가 어디 있겠어~ 안그래?"
    show bomi smile at right , nighttime
    e "(뭘 까, 이 이상한 기류는…)"

    e "(…무사히 돌아갈 수 있을까?)"
    hide ep4_gaeul
    hide bomi
    scene black with dissolve
#화면 페이드아웃
    narration "걱정과는 달리 그 이후로는 별일 없이 도시락을 먹고 산책을 즐길 수 있었다."
#보미활짝
    show bomi smile
    bomi "오늘 너무 즐거웠어~ 내일 클러에서 보자!"
#가을인사하는장면
    hide bomi
    show ep4_gaeul happy
    gaeul "[e]아 잘 가! 내일 보자!"
    
    e "..그래! 내일 보자!"
    hide ep4_gaeul
    narration "나 생각보다 잘 하고 있는 것 같다. 이대로라면 나쁘지 않을지도…"
    stop music fadeout 3.0
    jump ep5_start
# 에피 4 끝

