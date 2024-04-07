image ep7_etc notice_hidden = "images/ep7/etc/sys_hidden.png"
image ep7_etc quiz = "images/ep7/etc/sys_quiz.png"
image ep7_etc success = "images/ep7/etc/sys_success.png"
image ep7_etc failed = "images/ep7/etc/sys_failed.png"

image ep7_bomi smile = "images/ep7/bomi/bomi_smile.png"
image ep7_bomi default = "images/ep7/bomi/bomi_default.png"

image ep7_gaeul smile = "images/ep7/gaeul/gaeul_smile.png"
image ep7_gaeul default = "images/ep7/gaeul/gaeul_default.png"
image ep7_gaeul standing = "images/ep7/gaeul/gaeul_standing.png"

image ep7_gyeoul down = "images/ep7/gyeoul/gyeoul_down.png"
image ep7_gyeoul smile = "images/ep7/gyeoul/gyeoul_smile.png"
image ep7_gyeoul smile2 = "images/ep7/gyeoul/gyeoul_smile2.png"
image ep7_gyeoul surprised = "images/ep7/gyeoul/gyeoul_surprised.png"

label ep7_start:
    scene black with dissolve
    play music "audio/ep7/bgm/ep7.mp3"
    # 지금까지 퀴즈 3개 2중 두개 이상 맞췄을 때 시스템 창으로
    show ep7_etc notice_hidden at center :
        zoom 0.9
    narration "축하합니다! 조건을 충족하여 히든 에피소드가 열렸습니다."

    narration "<히든 에피소드 - BSQ>"

    narration "bsq를 성공하면 특별 보상이 주어집니다."
    $ choice_position = "bottom"
    menu:
        narration ""
        "네!":
            hide ep7_etc with dissolve
            narration "BSQ 진행을 선택하셨습니다."
        "싫어요..":
            return
    show ep7_bomi smile at left :
        zoom 0.8
    show ep7_gaeul smile at center :
        zoom 0.8
    show ep7_gyeoul down at right :
        zoom 0.8
    menu:
        narration "누구와 함께 bsq를 진행하시겠습니까?{fast}"
        "윤보미":
            hide ep7_bomi
            hide ep7_gaeul
            hide ep7_gyeoul
            jump select_bomi
        "서가을":
            hide ep7_bomi
            hide ep7_gaeul
            hide ep7_gyeoul
            jump select_gaeul
        "한겨울":
            hide ep7_bomi
            hide ep7_gaeul
            hide ep7_gyeoul
            jump select_gyeoul


label select_bomi:
    narration "윤보미와 함께 bsq를 진행합니다."
    show bomi smile
    bomi "bsq? 좋아!!"
    show bomi default
    bomi "그거 되게 어려워 보이던데 역시 ㅇㅇㅇ! 넌 자신 있구나!"

    bomi "나 너만 믿는다~!"

    e "…잘 부탁할게!"
    hide bomi with dissolve
    narration "bsq 문제가 공개되었습니다!"
    $ choice_position = "right_bottom"
    show ep7_etc quiz at center:
        zoom 0.8
        ypos 800
    menu:
        narration "정답을 선택하세요!{fast}"
        "1번":
            show ep7_etc failed at center:
                zoom 0.8
                ypos 800
            narration "아쉽게 틀려 성공하지 못했습니다..."
            hide ep7_etc
            show bomi default
            bomi "괜찮아~! 그래도 ㅇㅇㅇ 너랑 같이해서 재미있었어"
            #호감도 +10
            e "…노력했지만 역시 bsq는 쉽지 않은 도전이었나 보다…"
            e "…보미에게 미안하다…"
        "2번":
            show ep7_etc failed at center:
                zoom 0.8
                ypos 800
            narration "아쉽게 틀려 성공하지 못했습니다..."
            hide ep7_etc
            show bomi default
            bomi "괜찮아~! 그래도 ㅇㅇㅇ 너랑 같이해서 재미있었어"
            #호감도 +10
            e "…노력했지만 역시 bsq는 쉽지 않은 도전이었나 보다…"
            e "…보미에게 미안하다…"
        "3번":
            show ep7_etc success at center:
                zoom 0.8
                ypos 800
            narration "정답을 맞추어 BSQ를 성공했습니다!"
            hide ep7_etc
            show bomi smile
            bomi "역시 ㅇㅇㅇ이야! 믿고 있었어!"
            #호감도 +30
            e "어려웠지만 그동안 열심히 공부한 덕분에 잘 풀수 있었다."
            e "아니 보미와 함께라서 할수 있었던 걸까?"

        "4번":
            show ep7_etc failed at center:
                zoom 0.8
                ypos 800
            narration "아쉽게 틀려 성공하지 못했습니다..."
            hide ep7_etc
            show bomi default
            bomi "괜찮아~! 그래도 ㅇㅇㅇ 너랑 같이해서 재미있었어"
            #호감도 +10
            e "…노력했지만 역시 bsq는 쉽지 않은 도전이었나 보다…"
            e "…보미에게 미안하다…"
    return


label select_gaeul:
    narration "서가을과 함께 bsq를 진행합니다."
    show ep7_gaeul standing
    gaeul "응? bsq같이 하자고?"
    show ep7_gaeul default
    gaeul "그래! 좋아!"

    gaeul "우리 열심히 잘 해보자!"

    e "…잘 부탁할게!"
    hide ep7_gaeul with dissolve
    narration "bsq 문제가 공개되었습니다!"
    $ choice_position = "right_bottom"
    show ep7_etc quiz at center:
        zoom 0.8
        ypos 800
    menu:
        narration "정답을 선택하세요!{fast}"
        "1번":
            show ep7_etc failed at center:
                zoom 0.8
                ypos 800
            narration "아쉽게 틀려 성공하지 못했습니다..."
            hide ep7_etc
            show ep7_gaeul standing
            gaeul "할 수 있을 것 같았는데! 아쉽다.."
            #호감도 +10
            e "…노력했지만 역시 bsq는 쉽지 않은 도전이었나 보다…"
            e "…가을이에게 미안하다…"
        "2번":
            show ep7_etc failed at center:
                zoom 0.8
                ypos 800
            narration "아쉽게 틀려 성공하지 못했습니다..."
            hide ep7_etc
            show ep7_gaeul standing
            gaeul "할 수 있을 것 같았는데! 아쉽다.."
            #호감도 +10
            e "…노력했지만 역시 bsq는 쉽지 않은 도전이었나 보다…"
            e "…가을이에게 미안하다…"
        "3번":
            show ep7_etc success at center:
                zoom 0.8
                ypos 800
            narration "정답을 맞추어 BSQ를 성공했습니다!"
            hide ep7_etc
            show ep7_gaeul default
            gaeul "와! ㅇㅇㅇ! 대단해!"
            #호감도 +30
            e "어려웠지만 그동안 열심히 공부한 덕분에 잘 풀수 있었다."
            e "아니 가을이와 함께라서 할수 있었던 걸까?"

        "4번":
            show ep7_etc failed at center:
                zoom 0.8
                ypos 800
            narration "아쉽게 틀려 성공하지 못했습니다..."
            hide ep7_etc
            show ep7_gaeul standing
            gaeul "할 수 있을 것 같았는데! 아쉽다.."
            #호감도 +10
            e "…노력했지만 역시 bsq는 쉽지 않은 도전이었나 보다…"
            e "…가을이에게 미안하다…"
    return


label select_gyeoul:
    narration "한겨울과 함께 bsq를 진행합니다."
    show ep7_gyeoul down
    gyeoul "나랑..?"
    show ep7_gyeoul surprised
    gyeoul "아..아니 싫은게 아니라!"

    gyeoul "너도 나랑 같이 하고싶어 할 줄은 몰라서....!"
    show ep7_gyeoul smile
    gyeoul "좋아! 너랑 함께해서 너무 좋다!"
    e "…잘 부탁할게!"
    hide ep7_gyeoul with dissolve
    narration "bsq 문제가 공개되었습니다!"
    $ choice_position = "right_bottom"
    show ep7_etc quiz at center:
        zoom 0.8
        ypos 800
    menu:
        narration "정답을 선택하세요!{fast}"
        "1번":
            show ep7_etc failed at center:
                zoom 0.8
                ypos 800
            narration "아쉽게 틀려 성공하지 못했습니다..."
            hide ep7_etc
            show ep7_gyeoul smile2
            gyeoul "난 괜찮아..! 결과보단 과정이 중요하니까."
            gyeoul "너랑 같이 해서 즐거웠어!"
            #호감도 +10
            e "…노력했지만 역시 bsq는 쉽지 않은 도전이었나 보다…"
            e "…겨울이에게 미안하다…"
        "2번":
            show ep7_etc failed at center:
                zoom 0.8
                ypos 800
            narration "아쉽게 틀려 성공하지 못했습니다..."
            hide ep7_etc
            show ep7_gyeoul smile2
            gyeoul "난 괜찮아..! 결과보단 과정이 중요하니까."
            gyeoul "너랑 같이 해서 즐거웠어!"
            #호감도 +10
            e "…노력했지만 역시 bsq는 쉽지 않은 도전이었나 보다…"
            e "…겨울이에게 미안하다…"
        "3번":
            show ep7_etc success at center:
                zoom 0.8
                ypos 800
            narration "정답을 맞추어 BSQ를 성공했습니다!"
            hide ep7_etc
            show ep7_gyeoul smile
            gyeoul "ㅇㅇㅇ 너 정말 대단하다! 고마워!"
            #호감도 +30
            e "어려웠지만 그동안 열심히 공부한 덕분에 잘 풀수 있었다."
            e "아니 겨울이와 함께라서 할수 있었던 걸까?"

        "4번":
            show ep7_etc failed at center:
                zoom 0.8
                ypos 800
            narration "아쉽게 틀려 성공하지 못했습니다..."
            hide ep7_etc
            show ep7_gyeoul smile2
            gyeoul "난 괜찮아..! 결과보단 과정이 중요하니까."
            gyeoul "너랑 같이 해서 즐거웠어!"
            #호감도 +10
            e "…노력했지만 역시 bsq는 쉽지 않은 도전이었나 보다…"
            e "…겨울이에게 미안하다…"
    return
