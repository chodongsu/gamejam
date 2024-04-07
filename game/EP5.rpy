# image home = "images/ep5/background/자취방사진 2.png"
image seecat = "images/ep5/characters/집가는 길 고양 발견.PNG"
image gohome = "images/ep5/backgrounds/gohome.png"
image ep5_gyeoul talk = "images/ep5/backgrounds/talk_gyeoul.png"

image gyeoul = "images/ep5/characters/후드째려보는겨울 2.PNG"
image gyeoul glare = "images/ep5/characters/gyeoul_glare.png"
image gyeoul angry = "images/ep5/characters/angly.png"
image gyeoul silmang = "images/ep5/characters/약간 실망한 겨울.PNG"
image gyeoul sad = "images/ep5/characters/gyeoul_cry.png"
image gyeoul sad2 = "images/ep5/characters/gyeoul_cry2.png"
image gyeoul sad3 = "images/ep5/characters/gyeoul_cry3.png"
image ep5_gyeoulcall = "images/ep5/characters/gyeoul_call.png"

# image gyeoul sad4 = "겨울 눈물 리본 제거.PNG"
image gyeoul eyecontact = "images/ep5/characters/gyeoul_eyecontact.png"
# image gyeoul = "후드 째려보는 겨울2.PNG"
# image bambi = "bambi.png"
# image gyeoul smile = "웃는 겨울3 2.png"
# image gaeul sad = "가을_슬픔.PNG"
# image gaeul angry = "가을_화남.PNG"
# image gaeul = "가을_무표정.PNG"
# image gaeul = "가을_디폴트.PNG"
# image bomi smile = "보미_행복.PNG"
# image bomi = "보미_디폴트.PNG"
# image bomi hello = "보미_인사2.PNG"
# image bomi sad = "보미_우울.PNG"
image cat1 = "images/ep5/characters/cat1.png"
image cat2 = "images/ep5/characters/cat2.png"
image cat3 = "images/ep5/characters/cat3.png"


label ep5_start :
    define print_ep5 = Character(None,
    what_size=50, #폰트 사이즈
    what_xalign=0.5, #창 내에 텍스트를 중앙에 배치
    window_xalign=0.5, #창을 가로로 중앙에 배치
    window_yalign=0.5, #창을 세로로 중앙에 배치
    what_text_align=0.5, #창 내에 텍스트를 중앙에 배치 (만일을 대비해서)
    window_background=None,#창 제거, 글자만 보이기
    what_outlines=[(3, "#000000", 2, 2), (3, "#ffffff", 0, 0)],#경계선 보이기
    what_slow_cps=3 #텍스트 보이는 속도 조절
    )
    play sound "audio/ep5/sound/typing.mp3"
    play music "audio/ep5/bgm/ep5_bgm.mp3"
    print_ep5 "Episode.5"

    scene gohome :
        zoom 0.6

    narration "친구들과 헤어지고 집에 가는 길"

    e "아... 맞다! 에ㅇ팟!"

    e "아... 챙겨...와야겠지...?"

    e "(혼자 거리를 걷다 보니 생각이 많아진다.)"

    e "(오늘 시험은 생각보다..잘했지만...)"
    
    e "(앞으로도 잘할 수 있을까?)"

    e "(오늘은 그냥 운이 좋았던 게 ...아닐까?)"
    # play sound cat#!!!고양이울음소리
    show cat2 with hpunch
    play sound "audio/ep5/sound/cat.mp3"
    cat "야-옹"

    e "어? ...야옹이?"

    # scene seecat

    # play sound cat
    cat "야옹"
    
    e "야옹아~ 헤헤 귀여워라."

    cat "야옹"

    e "야옹아. 오늘 형아가 기분이 좋다?"

    cat "야옹?"

    e "사실 있잖아..."
    
    e "내가 여기서 뭘 하고 있는 건지 혼란스러웠거든..."
    # play sound cat

    hide cat2
    show cat3
    cat "야옹..."
    
    e "난 원래 코딩을 하고 싶었던 것도 아니었고..."

    e "겨울이처럼 나보다 잘하는 애들도 훨씬 많고..."

    e "그런데 이번에 시험을 치고 나서..."
    
    e "물론 운이 좋았던 것도 있지만..."
    
    e "뭐랄까 약간 자신감이 생긴 기분이야..."

    e "..."

    e "..."

    e "그런데 겨울이는 날... 싫어하는 걸까?"

    e "미움받는 건 익숙하지만..."
    
    e "그래도 항상 힘든 건 어쩔 수 없나 봐..."
    # play sound cat
    hide cat3
    show cat1 with vpunch
    play sound "audio/ep5/sound/cat.mp3"
    cat "야옹!"

    e "..위로해 주는 거야..?"
    
    e "너한테라도 이야기하니까 훨씬 기운이 난다."
    
    e "고마워..."
    hide cat1
    narration "갑자기 고양이가 옆으로 뛰어간다."
    scene black with dissolve
    e "어? 야옹아??"
    scene ep5_gyeoul talk 
    show gyeoul sad2
    narration "야옹이를 따라가니 그곳에는 울고 있는 겨울이 있었다."
    show gyeoul sad
    e "(...어쩌지 지금이라도 못 본 척 가야겠...)"
    show gyeoul eyecontact
    e "헉 눈을 마주쳐버렸다...!"
    show gyeoul sad3 with vpunch
    gyeoul "...꺼져"
    $ love[2] -= 3 #!!! 겨울호감하락

    e "아...그게..."

    show gyeoul glare with vpunch

    gyeoul "못 들었어? 꺼지라니까?"

    gyeoul "왜 너도 내가 웃겨???"

    gyeoul "잘난척하던 애가 시험 망치고 있는 게 웃기냐고!"

    gyeoul "너 같은 애들이 제일 싫어. 간절함도 없고,"
    
    gyeoul "코딩이 뭔 줄도 모르고, 직접 찾아볼 용기도 없으면서"
    
    gyeoul "주변 도움받아서 쉽게 가려고만 하는 너 같은 애들"
    
    show gyeoul glare with vpunch
    gyeoul "다 꺼져버렸으면 좋겠다고!"
    $ love[2] -= 7 #!!! 겨울호감하락

# <선택지>

# 1. …. 미안… -> 호감도 + 3
# 2. ..너가 왜 멋대로 날 판단해? 호감도 -5 -> 핑뚝 째려봄

# …
# menu :
#     "... 미안..."
#     jump second_y
#     "...너가 왜 멋대로 날 판단해?"
#     jump second_n

# label second_n :
#         show gyeoul jjz
#         narration "[째려보는겨울이"
# label second_y :
#1번선택시
    #겨울 호감도+3
    narration "어색한 침묵이 돌았다..."

    e "...그 혹시... 내가 ... 도와줘도... 괜찮을..까...?"

    show gyeoul angry with vpunch
    gyeoul "니가 나를??"
    $ love[2] -= 1 #!!! 겨울호감하락

    e "아니 그게... 그러니까..."

    e "우리는 동료...학습...을 하는 거잖아..."
    $ love[2] += 10 #!!! 겨울호감
    
    e "같이 공부한다면... 그 다른 사람을 가르쳐 줄 때"
    
    e "학습효과가 가장 좋다는 말도 있고 그러니까..."
    $ love[2] += 10 #!!! 겨울호감

    e "(내가 뭘 말하고 있는 거지? 겨울이가 날 얼마나 한심하게 볼까...)"

    narration "..."

    narration "..."

    e "왜 아무말이 없지...?"

    gyeoul "..."

    e "(역시 주제 넘었던 걸까...)"
    show gyeoul glare
    gyeoul "...래... 아..."

    e "...뭐라고?"
    hide gyeoul
    show ep5_gyeoulcall with hpunch
    gyeoul "그래!!!! 좋다고!!!!!!"
    $ love[2] += 15 #!!! 겨울호감


    gyeoul "너 생각보다 쓸모 있는 것 같으니 같이 해도 좋겠다고!!"

    e "...!" 
    
    e "정말? 고마워!!!"

    gyeoul "..."
    hide ep5_gyeoulcall
    show gyeoul sad3
    gyeoul "...뭐라는거야..."

    gyeoul "… 그리고 ...그땐..ㅁㅣ안ㅎ..."

    e "(뭐라고 한거지?)"

    e "…미..미안 못들었어..한번만 더..."
    hide gyeoul sad3
    show gyeoul glare with vpunch
    gyeoul "아 못 들었으면 듣지 말던가!!"
    $ love[2] += 7 #!!! 겨울호감

    hide ep5_gyeoulcall
    narration "(갑자기 겨울은 화를 내며 먼저 가버렸다.)"
    
    e "(내가 뭘 잘못한 걸까?)"

    e "..."
    
    gyeoul "아 뭐하는거야! 안 따라오고!"
    $ love[2] += 13 #!!! 겨울호감

    e "..어..! 어.. 갈게...!"
    scene black with dissolve
    e "(겨울의 마음은 정말 알 수 없다...)"

    e "(하지만 이제... 날 싫어하지는 않는 것 같다...)"

    e "(무사히 시험도 끝났고 겨울이와도 나름의 화해를 한 듯하다.)"

    e "(오늘은 정말 보람찬 하루였다...)"
    stop music fadeout 3.0
    jump ep6_start