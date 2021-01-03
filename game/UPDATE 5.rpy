label U5:

    scene bs
    with dissolve

    "A little time passes, and you make sure to set up another computer session with Norah."

    scene b120
    with dissolve

    P "Alright, now that we got all the boring and technical stuff out of the way, time for brainless entertainment!"

    N "*giggle* I'm finally glad I'll be able to talk with my girlfriends about the latest shows, and whatnot."

    N "But TV sure is different nowadays, ain't it, puddin'? Everything you need seems to be over the gosh darn internet."

    P "Yep. Knowing how to use technology is essential now."

    N "That's why I'm so thankful yer helpin', sugar."

    scene e1 #N kiss cam forehead
    with dissolve

    N "Mwah!"

    scene e2 #N face close and hand on cam face
    with dissolve

    N "Just what would I do without my beautiful baby boy, hm?"

    "You try to think of a witty response, but the way your [rel_m]'s sweet breath hits you makes it hard to think."

    P "(I'm starting to get hard. I can't even keep myself from reacting to these innocent gestures anymore.)"

    P "(Something is going to have to change soon. Whatever it is, but this can't keep going on or I'll go crazy.)"

    P "[m_nik]…"

    "All you can do is look away and enjoy the close contact."

    scene b120
    with dissolve

    N "Oops, hehe. My beautiful MAN."

    N "I know yer not a baby anymore and I shouldn't treat you like one."

    scene e3 #N smi look forward down
    with dissolve

    N "Yes… Yer all grown up and won't need me at all once you find a nice girl to keep you company."

    menu:

        "Brush her off":

            P "*laugh* Come on, it won't be like that. Even when I do get a girlfriend, we'll be fine."

            P "So no dramatics, Norah!"

            scene b120
            with dissolve

            N "Heh… I guess I am bein' dramatic for no reason. Sorry about that, sugar. You know how I get sometimes."

            P "No problem."

            jump U5re

        "Reassure her [NorahPath]":

            $ npts = npts + 1

            P "Huh, did you hear that?"

            scene b121
            with dissolve

            N "What? What are you talkin' about, sugar?"

            P "I thought I heard something crazy like I wouldn't need you anymore. I might need to get my ears checked because you and the girls will always be the most important women in my life."

            scene b120
            with dissolve

            N "I guess I'm the baby because I really want to cry right now. But I'm going to hold it in for your sake."

            N "I've been nothin' but an emotional luney since you came back."

            P "(Like I said before, it really surprised me how much she did seem to miss me, but I can't exactly blame her.)"

            scene e4 ##cam hand on N shoulder
            with dissolve

            P "No, you've just been a [rel_m]. And there's nothing wrong with that."

            P "Just promise to not give me kisses in front of my friends like you did in middle school, and we're golden."

            P "Didn't live that incident down for a whole month."

            N "Hehehe. I promise, but all bets are off when we're alone!"

            scene e1
            with dissolve

            N "Mmmmwah!"

            P "Haha. Not going to fight a losing battle there."

            jump U5re

label U5re:

    scene e5 #use b119 as base. N smi
    with dissolve

    "You and Norah finally start the show called Game of Chairs a little while later."

    "And it soon finishes."

    scene b120
    with dissolve

    P "So? What'd you think? I couldn't help but notice your hyper focus during the show, so I didn't want to talk too much. *laugh*"

    P "I even poked you a few times, but you didn't seem to know notice."

    N "*giggle* Sorry, puddin'. I just didn't want to miss any details when my girlfriend asks me about my review."

    P "I understand. So what is your review, madam? The people want to know!"

    N "Hehe. Well, it was definitely intense and dramatic, even more than I thought."

    scene e6 #N angry
    with dissolve

    N "Like when that man got caught bein' intimate and pushed that boy from the tower!"

    N "I sure wish I could give that fella a piece of my mind! You should NOT push children from towers."

    P "Hahah. I don't think there are too many people who would argue with that."

    P "(She's always been like this, genuinely getting upset at injustice, even if it's a television show.)"

    P "Speaking of that scene, though… What did you think about the guy doing… that with his [rel_s]?"

    P "I bet that was pretty shocking for you."

    P "(I'm interested to know what she thinks about those types of relationships, to begin with. So I kinda do have an ulterior motive for this question.)"

    scene b121
    with dissolve

    N "Hmm… Well, not really."

    P "S-Seriously?"

    P "(I wasn't expecting that answer.)"

    scene b120
    with dissolve

    N "Heh. That's probably a bit of a surprise to hear, but you know that stereotype about the South…"

    P "Ah. *laugh*"

    P "So… it's true?"

    N "It's certainly not common or anything, but there are some places that are more open to it than others."

    N "One of my friends even openly started datin' her [rel_b] back in high school."

    P "Whoa, really?"

    N "Mhm. Of course everyone was surprised at first, but they really seemed to care about each other, so we all quickly got used to it."

    N "And I think if two people genuinely do care about each other and have them feelin's, then they deserve the right to be together."

    P "*smile* I couldn't agree with you more, [m_nik]."

    "A part of you wants to confess your own feelings right then and there, but you control yourself."

    P "(Hearing her say that really makes me think I have a chance… But at what exactly? What exactly is it that I want?)"

    scene e5
    with dissolve

    N "Do you think we can watch another show, puddin'? I kinda zoned out on Game of Chairs, so I want to watch somethin' you like."

    N "Oh, what about this one?"

    N "'A group of strangers feel an uncanny connection and those bonds deepen one fateful day...'"

    scene b120
    with dissolve

    N "Have you seen this one before?"

    P "(Hell yeah I have. They show actual sex scenes between the actors… And there's a ton. You could pretty much call it a porn series.)"

    menu:

        "Watch it [NorahPath]":

            P "Uh… I actually have seen it before… So I should warn you that the sex scenes in this make Game of Chairs look like a family Christmas special."

            scene e7 #N surprised
            with dissolve

            N "Wow, really? I didn't even know shows like this existed."

            scene b120
            with dissolve

            N "*laugh* My mother, God rest her soul, would be havin' a right fit if I even considered watchin' something like this."

            P "(I didn't know Nanny Mable too well before she passed when I was a kid, but I do remember her being pretty strict.)"

            P "(But watching this show with [m_nik] would basically be like watching porn together.)"

            "That thought makes your dick twitch."

            P "Do… you want to maybe check it out together? If the scenes make you too uncomfortable or anything like that, we can just stop and choose something else."

            if npts >= 5:
                $ nporn = True
                "***You were able to access this scene because you do have enough points***"
                scene e8 #N nervous, thinking
                with dissolve

                N "Mmm…"

                "Norah groans in contemplation."

                N "I guess it wouldn't hurt anything to take a peek… And if it does get a little cuckoo, then we can just stop."

                P "You sure? Speak now or forever hold your peace."

                scene b120
                with dissolve

                N "*giggle* I'm sure, sugar. Thank you for askin', but like I said, I know yer not a little boy anymore, so it's fine if we do more… adult things together."

                P "(I DEFINITELY like the sound of that.)"

                P "*smile* Awesome. I'm really happy our relationship is growing."

                N "Me too, pumpkin."

                scene e5
                with dissolve

                "So without further ado, you and Norah begin the erotic series called 'Flies on the Wall."

                "*minutes later*"

                N "Wow, puddin'. There's so much happenin' already. It's so excitin'!"

                P "*smile* I know. The story really hooks you in the first few minutes."

                "And it doesn't take long for the very first sex scene to pop up."

                scene e9 #N sur
                with dissolve

                N "Oh my… Those two are really getting' into it, aren't they?"

                "You see the man and woman who are strangers give in to their otherworldly connection and start feeling on each other while making out."

                P "They certainly are…"

                "You respond quietly, knowing what's up next."

                scene e10 #N sur at cam
                with dissolve

                N "D-Did she just tell him to put it in her backside?"

                P "Ha… Yeah. She doesn't want to get pregnant, especially because of her new career, remember? And she doesn't want to wait to find protection either."

                N "Because of the mysterious connection?"

                P "Yup. They pretty much can't control themselves."

                scene e9
                with dissolve

                "Norah quickly goes back to the show. And all you can do is watch her from your peripheral as the anal sex begins."

                N "How in the world can she take him into her backside…? Don't it hurt?"

                P "You'd be surprised at how flexible the ass can be."

                "You say without thinking, but immediately realize your words."

                scene e10
                with dissolve

                P "(Did I seriously just say that out loud with my [rel_m] right next to me?)"

                N "I-It can? But how do you know, sugar?"

                P "(Does she actually want to know… or is she just surprised by my comment?)"

                "You think how to answer."

                P "(If I do want to progress with her, then I have to cross the boundaries of our normal relationship.)"

                P "*clear throat* Well, uh, I've done anal a couple of times and have figured out there are two types of girls."

                "You wait for your [rel_m] to respond, but she only stares at you in anticipation."

                P "Uh… the first type of girl will never mesh well with it, no matter how much you try."

                scene e11 #N smile nervous look to side
                with dissolve

                N "So… even if you… correctly prepare?"

                P "(Yes! She actually seems interested.)"

                P "Right. So, with this girl, Ashley, I played with her butt for a while… Just fingering it gently and trying to get it looser."

                scene e12 #N look at cam
                with dissolve

                P "But even getting it knuckle deep was a problem. So I tried licking and sucking, and all that to get her muscles to relax."

                N "Did it work?"

                P "A bit, yeah. So I kept that up for a while before virtually dumping a whole bottle of lube on her."

                scene b120
                with dissolve

                N "*giggle* I don't blame you…"
                if nshower == True:
                    scene e13 #N glance at cam dick
                    with dissolve

                    N "Yer not exactly the smallest branch on the tree, darlin'."

                    scene b120
                    with dissolve

                    P "(She totally just glanced at my dick.)"

                    P "Ha… That's a bit embarrassing, [m_nik]."

                    P "(She made a similar comment when we first got naked before showering together.)"

                    N "Hehe. Sorry. But you really don't have anything to be embarrassed about. Any girl would be like to have…"

                    scene e13
                    with dissolve

                    N "A man of your impressive size."

                    scene b120
                    with dissolve

                    P "(She totally just peeked again! But I sure as hell am not complaining.)"

                scene e11
                with dissolve

                N "So, puddin'… How did it go with this girl… You said Ashlyn?"

                P "*smile* Close, Ashley. But not well. Even with all the prep and lube beforehand, I wasn't able to put my… penis in passed the head."

                P "And after a couple more times of trying, we gave up."

                scene e12
                with dissolve

                N "I see…"

                P "Yep, so that's the first type of girl when it comes to anal."

                N "Right, you did mention there were two types of girls... What's the second?"


                P "The second type is like a girl I dated named Natalie. She was pretty conservative and more on the 'nerd' side, but we got along great."

                scene b120
                with dissolve

                N "That makes sense y'all got on so well."

                P "Huh?"

                N "Well, you definitely love yer video games and books."

                P "*smile* So you're basically calling me a nerd."

                scene e10
                with dissolve

                N "What? No, never, sugar…"

                scene b120
                with dissolve

                N "Well, maybe a little, but that's why I had to shoo all them girls away when you were younger. You had brain and brawn."

                P "(Ha. I do remember her being a bit more clingy and less welcoming when girls would want to play with me when I was a lot younger.)"

                P "*grin* I'm totally taking that as a compliment."

                N "*giggle* It was, handsome."

                N "But I'm sorry for interruptin'. Please continue."

                P "(I can't believe my own [rel_m] is apologizing for cutting off my sex story. This still feels so surreal.)"

                P "*smile* No problem."

                scene e14 #cam on ceiling
                with dissolve

                P "So where was I? Uuuh…"

                N "I think you were talkin' about how well you and Natalie got along."

                scene b120
                with dissolve

                P "Right, thanks."

                P "So, with her being on the reserved side, we moved pretty slowly when it came to sexual stuff. But eventually, we agreed to try anal on a whim."

                scene e12
                with dissolve

                N "I did hear the quiet ones are usually the freakiest."

                P "Haha. That stereotype may be true."

                P "(I wonder how freaky or conservative [m_nik] is when it comes to sex? Is anal the type of thing she would do? Or maybe has already done?)"

                P "Anyway, all we did was buy a small bottle of lube before trying, and she was able to take all of me."

                scene e10
                with dissolve

                N "R-Really? Yer whole penis fit inside that teensy-weensy little hole? It didn't hurt her at all?"

                P "Nope. As a matter of fact, she told me to go harder after only a few minutes. And it was like that every time we did."

                P "I'm no expert, but like I said, I think there are those two types of girls when it comes to anal sex."

                scene e11
                with dissolve

                N "Heh, I see… That was very informative, puddin'. Thank you…"

                P "(She's obviously not completely comfortable with this conversation, but it was a huge step in… I don't know which direction yet.)"

                scene e5
                with dissolve

                "You and Norah finish the rest of the show, commenting here and there on the scenes, including the sex."

            else:
                "***You missed a scene because you DO NOT have enough points***"
                scene e15 #N uncomfortable
                with dissolve

                N "Oh… I don't know if that's the most appropriate thing, sugar. Maybe it would be better if we watched somethin' else?"

                P "Ah, right. Of course. Let's just look for something else, then. Plenty of good shows and movies on this site."

                P "(Shit! I Totally missed a good opportunity to move our relationship in a different direction.)"

                scene e5
                with dissolve

                "You and Norah finish the rest of the show, commenting here and there on the scenes."

                jump U5anal

        "Don't watch it":

            P "I have, and it's really inappropriate, if I'm being honest. We should probably watch something else."

            N "Oh! Good thing you warned me, sugar. I'll just let you choose what we watch before I suggest somethin' even worse. *giggle*"

            P "Ha, it's not your fault."

            scene e5
            with dissolve

            "You and Norah find another show, commenting here and there on the scenes."

            jump U5anal

label U5anal:

    scene b120
    with dissolve

    N "That was so fun, puddin'. Thank you for spendin' time with me. It makes me so happy."

    P "I wish all women were as simple as you."

    N "Hehe. Well, I'm glad I'm one of a kind."

    P "*smile* You seriously are."

    if nshower == True:

        P "(I think only Coral is home right now, so it should be fine.)"

        P "Do you wanna take a quick shower, [m_nik]? Zoe is still at work, and Coral is going strong on one of her binge sessions."

        scene e16 #N smile with hand to chest
        with dissolve

        N "Gosh, is it Christmas or somethin'? I get to spend so much time with you today."

        N "I half-expected one of the girls to barge and drag you away during our lessons like they used to."

        P "*laugh* Even if they did, I would tell them I'm all yours and they can wait."

        N "Hehe. You should be careful what you tell a woman, they can easily misinterpret such sweet words."

        scene e2
        with dissolve

        N "Yer lucky I'm so understandin'."

        P "*clear throat* H-Haha, yeah…"

        P "(You are killing me here, [m_nik].)"

        scene bs
        with dissolve

        "You and Norah sneak into the bathroom and begin your new pastime of showering, but after a bit, you stop her from washing you."

        scene b157
        with dissolve

        P "Today is your turn to get scrubbed like a queen."

        N "*giggle* I suppose there's no way I can argue when you put it like that. I would be honored to get cleaned by your royal hands, my king."

        P "(Ugh, don't get hard, don't get hard, don't get hard.)"
        label galleryScene5:
        scene e17 #cam washing N back
        with dissolve

        N "Mmm…"

        "Norah lets out a sigh of approval as you start washing her smooth, silky skin."

        P "You have such nice skin, [m_nik]."

        N "Thank you, sugar. I always see fancy commercials with all them creams and lotions full of chemicals."

        N "But eatin' right and little exercise here and there is the key to health, but I'm no doctor, so I might be wrong."

        P "Nah, I totally agree. Natural is always the way to go."

        scene e18 #cam look down to N butt
        with dissolve

        P "(Speaking of natural… She has got to be the perfect fit for the 'milf' body stereotype if there ever was one.)"

        P "(I can only imagine how pumping her from the back and watching that big ass jiggle against my dick would-)"

        N "[p_name]? Did you hear me, sugar?"

        scene b157
        with dissolve

        P "Oh, sorry. What'd you say? Kinda zoned out there for a sec. Focused on your royal scrubbing."

        N "Hehe. I said that I know I'm supposed to be gettin' pampered here and all, but do you think I could wash you a little bit more anyway?"

        P "(She can't help but want to take care of me, even though I really wanted to touch her some more.)"

        P "*smile* Do your thing. I shall stand here like a statue as thy scrubs me down."

        N "*giggle* I appreciate it, my good sir."

        scene b158
        with dissolve

        "A bit into the washing, Norah speaks up again."

        N "I'm so happy you and Coral are gettin' along after so long."

        P "*smile* Me too. It wasn't easy getting her to forgive me, but it was definitely worth it."

        N "Thank you for tryin', puddin'. She would never admit it, but there are times when I could hear her cryin' in her room."

        P "I… didn't know that."

        P "(Now I really feel like shit.)"

        scene e20 #N surprised
        with dissolve

        N "Oh! I wasn't tryin' to make you feel guilty or anything like that. I was just tryin' to say yer [rel_s] missed you somethin' fierce is all."

        N "We all did."

        P "*smile* You don't need to explain, [m_nik]. I understand."

        "You do understand she isn't blaming you, but you feel guilty anyway."

        scene b161
        with dissolve

        "Norah watches you for a short while before returning to what she was doing."

        scene b158
        with dissolve

        N "Coral also tells me you two are makin' yer video games again?"

        N "I know that… John has always been critical of yer hobbies, but it makes me really glad yer still tryin'."

        scene b161
        with dissolve

        N "And now that you've officially made me a computer whiz, maybe I can play without gettin' confused after half a minute. *giggle*"

        P "(Now that I'm older, I can appreciate her taking interest in all of our hobbies, and even trying to participate.)"

        P "Heck yeah you can. And the one Coral and I are working on is a dating sim, so it's pretty straightforward."

        scene e21 #N confused
        with dissolve

        N "A datin' sim?"

        P "Ah, dating simulator. So you basically have an option to date multiple girls and have to earn points with them by doing various activities..."

        P "I promise it's a lot more fun than I'm explaining. *laugh*"

        scene b158
        with dissolve

        N "Sounds plenty interestin' to me. And I know you and Coral will make a downright fun game…"

        P "Hm? What's wrong?"

        scene b161
        with dissolve

        N "Heh, nothin'. Yer game just made me think about somethin' my girlfriend said."

        P "What'd she say?"

        N "Well… that basically I should start datin'."

        scene b158
        with dissolve

        N "I wasn't thinkin' anything about that when she mentioned it months ago, but now that it's been almost a year…"

        N "I don't know. Maybe it is time for me to get back out there. I do think I'm ready."

        scene b161
        with dissolve

        N "And I know that online datin' is how most people meet each other nowadays, so I was thinkin' you could help me with that, sugar? Signin' up for all them websites and whatnot."

        "Your brain tries to process the new information."

        P "(So she wants to start dating… But what about me and my feelings? Our relationship? Or lack thereof…)"

        menu:

            "Say something [NorahPath]":
                $ nroute = True
                P "Y-You can't…"

                scene e21
                with dissolve

                N "Puddin'? What do you mean?"

                "It becomes hard to breathe and your heart starts beating faster."

                P "I don't want to let another man have you. Not when I know I can make you happy."

                scene e22 #N stop washing
                with dissolve

                N "What are you… What are you talkin' about, [p_name]?"

                "You swallow the imaginary brick in your throat."

                P "(Now's not the time to act all timid and shy. I have to at least sound like the capable man I want to convince her I am.)"

                scene e23 #cam grab N
                with dissolve

                P "[m_nik]… *shake head*"

                P "Norah."

                N "Y-Yes?"

                P "I've always thought you were an incredible women and that man is an idiot for letting you go… But I promise I won't make that same mistake…"

                P "*clear throat* And I know this is a lot to take in, so if you need time to think, I completely understand. But… I would like us to date, no matter how crazy that sounds."

                "An infinitely long lapse in the conversation makes your heart beat even faster."

                "Or at least it seems that way to you, but only a few seconds pass as your [rel_m] watches you, like she's trying to figure out what newly discovered creature you are."

                scene e25 #N smile look down
                with dissolve

                N "It don't sound crazy at all."

                P "Huh?"

                scene e26 #N smile at cam
                with dissolve

                N "Remember what I told you just earlier? About my friend and how the South is more open-minded about certain relationships?"

                P "(Ah… right. I was so panicked that I didn't even remember all that.)"

                N "So datin' you isn't such a hard decision. Yer everything I could want in a man. Sensitive, courageous, a downright smarty pants, and so much more."

                P "*laugh* If I was called a smarty pants by anyone else, then I might take it personal. But I know you mean it as a compliment."

                P "So… you're okay with us dating?"

                "You try to keep the hopeful smile from dominating your face, but are failing miserably."

                P "(This is going better than I ever thought!)"

                N "I definitely am, sugar. I've told you a million times that nothin' makes me happier than spendin' time with you and I mean that."

                scene e28 #N sad look down
                with dissolve

                N "But… I don't think we can be together…"

                P "B-B-But why? I… I thought you were okay with us dating?"

                "Your voice cracks despite your attempt to control it."

                scene e29 #N look at cam
                with dissolve

                N "I am, puddin'... But I'm just not sure about the physical side…"

                P "The physical side?"

                scene e28
                with dissolve

                N "Mhm… You know, like… bein' intimate and all that…"

                N "Of course yer a handsome fella, a blind person at night could see that… But it just doesn't come natural to me to think of you in that way…"

                P "(Duh, of course she's not going to be naturally attracted to me like I am her. That would definitely be asking for too much.)"

                N "And yer a young man with all kinds of ragin' hormones and urges… So I just don't wanna tie you down emotionally and leave you hangin' physically…"

                scene e29
                with dissolve

                N "That wouldn't be fair to you, and I want you to be happy, no matter what."

                P "(So that's why she's saying we can't date? For my happiness? …I need this woman.)"

                scene e30 #cam grab N and she slightly surprised
                with dissolve

                P "*smile* Hey, I completely understand where you're coming from, but that's not the most important thing to me."

                P "I won't lie and say I don't want you in that way, because you're a gorgeous woman, but that's not something we need to think about at all right now."

                P "What I do want to think about is taking you on the best date of your life."

                scene e31 #N excited
                with dissolve

                N "Hehe… The best date of my life? Thems is big words, sugar."

                P "*grin* I know, but I can back them up… If you agree to be my date."

                scene e32 #cam hold out arm
                with dissolve

                P "What say you, my queen?"

                scene e33 #N excited grab arm
                with dissolve

                N "*giggle* I wholeheartedly agree, my king… And I'm so dang excited!"

                P "(This did end up going super well, if not totally expected. I can't be… intimate with her… Though I definitely don't plan to give up on that.)"

                P "(But before I can even get to that, I really do need to back up my words of giving her the best date she's ever had!)"

                jump U5co

            "Don't say anything":

                "After a short inner debate, you come to a conclusion."

                P "(You know what? Maybe it is for the best that she start dating and eventually finds happiness. And I can be there to help her along the way.)"

                P "*smile* I'd be happy to help you, [m_nik]. And I'm proud of you for having enough courage to get back out there."

                N "Thank you, sugar… It means a lot to hear you say that."

                jump U5co

label U5co:
    $ renpy.end_replay()
    if nroute == True:

        scene bs
        with dissolve

        "From then on, you spend every ounce of your energy planning the perfect date for Norah."

        "And the day to execute soon arrives."

        scene e34 #N stand by door look down at self
        with dissolve

        N "What do you think, sugar? Is this good enough? You told me to dress for adventure, right?"

        scene e35 #N neu mouth open waiting for answer
        with dissolve

        P "(I'm used to her frilly skirts and dresses, so it's nice to see her like this.)"

        P "You're perfect, [m_nik]."

        P "(She really is dressed perfectly for what we'll be doing to be doing.)"

        scene e36 #N smile
        with dissolve

        N "Good. I was a bit nervous about dressin' like I'm back on the farm."

        P "It suits you. I haven't ever really seen you dress like this. Can you give me a 'yeehaw'?"

        N "*giggle* You might earn one if this date is as good as you say."

        P "Man, you're turning up the pressure even more, huh?"

        scene e37 #N hug up to and grab cam
        with dissolve

        N "Well, I believe in my man."

        "Hearing her declare you're her man so easily makes your dick harden. Though her big tits pressed into your arm may also play a factor."

        P "(So does that mean she considers us boyfriend and girlfriend, and not just 'dating'?)"

        P "(I think I could probably assume that knowing how serious people from the South take relationships.)"

        P "*smile* Good, because I'm going to rock your world today, Norah."

        scene e38 #N excited
        with dissolve

        N "*giggle* I'm so excited!"

        scene e39 #N run past
        with dissolve

        P "(Ha. I think 'excited' is an understatement.)"

        scene bs
        with dissolve

        "You make Norah close her eyes as you get to the date site, and lead her the rest of the way on foot once parked."

        scene e40 #N eyes closed excited
        with dissolve

        N "Oh, sugar, yer killin' me here! Can't I open my eyes yet???"

        P "Hahah, yes. I think I've tortured you long enough. You can open your eyes."

        scene e41 #N look to side
        with dissolve

        "The second you give the okay, her eyes fly open and she checks the area."

        N "We're on a farm?"

        "Butterflies form in the pit of your stomach."

        P "Yeah… At first, I thought about taking you to the fanciest restaurant I could find, but then I really started thinking…"

        P "You've told me so many fun-filled stories about growing up in the South, living on the farm… So I just figured we could have more fun this way."

        scene e42 #N normal smile to cam
        with dissolve

        N "Honey…"

        N "It really means a lot that you even considered all this, and I'm happy you did. Yer definitely gettin' passin' grades so far."

        P "(Wasn't expecting her to be so honest about how I'm doing…. But I guess it's a good thing to hear.)"

        scene e43 #cam close
        with dissolve

        P "Only time I've considered being a teacher's pet."

        N "*giggle*"

        P "So, ready to officially start our day of festivities?"

        N "Ya darn tootin'! I could barely sleep last night thinkin' about it."

        P "Haha, alright. No more suspense."

        scene e44 #cam hold up gun, N sur at it
        with dissolve

        N "Is that a gun?"

        P "Yup. Your dad would always practice on the farm, but said girls should stick to what their good at when you asked him if you could learn."

        scene e45 #N look at cam
        with dissolve

        N "You remember that? I think I told you that once when you were younger."

        P "*smile* Of course I do. I remember everything you say."

        scene e46 #N smile
        with dissolve

        N "Hehe. Handsome and a sweet-talker. It really ain't fair."

        P "Haha. Well, I got some targets you can take that unfairness out on."

        P "What do you say, Norah?"

        scene e47 #N excited
        with dissolve

        N "Hehe, heck yeah! Let's shoot some stuff."

        scene bs
        with dissolve

        "You two get in position."

        scene e48 #cam behind N holding up gun
        with dissolve

        P "(Not gonna lie, [m_nik] looks so hot holding a gun like that.)"

        scene e49 #N smile back at cam
        with dissolve

        N "I think I'm ready, sweetheart. Should I shoot?"

        P "Go for it!"

        N "Hehe. Okay."

        scene e48
        with dissolve

        "You hear Norah take a short breath before squeezing the trigger. A loud bang immediately follows that echoes in the empty surroundings."

        P "(I rented the entire farm and the surrounding acres for the day, so we should be able to make as much noise as we want.)"

        N "Ah, darnit."

        scene e50 #N sad face cam
        with dissolve

        N "Did you see? I wasn't even close to the target? I guess my daddy had a point."

        menu:

            "Encourage":
                $ npts = npts + 1

                P "Come on, [m_nik]. You literally just shot a gun for the first time. I don't think anyone expects you to be a natural gunslinger, right?"

                P "You should've seen me yesterday out here setting all of this up. I couldn't hit any of the targets until my very last try. And trust me, there were plenty before that."

                scene e49
                with dissolve

                N "Heh, really?"

                P "*nod* So, don't give up on yourself so fast. I KNOW you can do it."

                N "Thank you for believin' in me, darlin'. I won't give up until I blow that target sky high!"

                P "Haha. Now that's the Norah I know. Get 'em, girl."

                jump U5sh

            "Show her [NorahPath]":
                $ npts = npts + 2

                P "What? You mean you didn't hit the target your first time shooting a gun, ever? That's unacceptable, Norah. Get your things, this date is over."

                scene e49
                with dissolve

                N "Heh… I guess I am bein' a bit silly, aren't I?"

                P "Not silly. I just think you're too hard on yourself. No one is perfect, even if certain people expect you to be."

                "You both hold eye contact for a moment, knowing exactly what that means."

                P "Besides, you should have seen me out here yesterday when I was setting everything up. I would've made you look like a notorious outlaw."

                P "'Norah the Nutcracker.' She leaves every town she visits shaking in their boots."

                N "*giggle* In that case, I definitely do feel better."

                P "*smile* And I actually did learn some good tips from the owner after he couldn't watch the ‘godforsaken display' I was putting on any longer."

                N "Really? Can you help me, sugar?"

                P "Only 'cause you asked so nicely."

                scene e51 #cam right behind N
                with dissolve

                "You position your [rel_m]."

                P "So your stance is good, but you're way too tense."

                scene e52 #cam hand on N shoulder
                with dissolve

                P "Just try to relax your shoulders a bit."

                "You feel the muscles become slack."

                P "Good. Now when you're aiming, try to shoot a little higher because the bullet is going to fall some."

                scene e53 #N raise gun high
                with dissolve

                N "Like this?"

                P "Hmm… I think that's a bit too high."

                scene e54 #cam put both hands around her to aim
                with dissolve

                P "Let's try to go down little by little."

                "As you try to find the right spot, you realize how close you are as you take in Norah's lavender-smelling hair."

                "And the feeling of her round ass pressed back against your crotch."

                P "(Down, boy. She said she's not comfortable with the sexual stuff, so let's not put her off even more.)"

                "You will your erection away and refocus on the task at hand."

                scene e48
                with dissolve

                P "Okay, I think that's about good."

                scene e49
                with dissolve

                N "Am I ready to shoot now, puddin'?"

                P "*smile* Yeah. I think that should be enough for now. Go ahead and let it rip."

                N "Okay!"

                "You back up as she takes another calming breath."

                jump U5sh

label U5sh:
    if nroute == True:

        scene e48
        with dissolve

        "One more deafening bang sounds in the air as Norah shoots."

        scene e57 #zoom on bullseye's or bottle
        with dissolve

        "And manages to hit her target."

        scene e58 #N face cam excited
        with dissolve

        N "Did you see, sugar! I hit it!"

        P "*smile* I did. Awesome job, [m_nik]. I knew you could do it."

        N "Hehe. Thank you! I wanna shoot some more!"

        P "(Oh… I think I've created a little criminal.)"

        scene bs
        with dissolve

        "It takes some effort, but you're able to pry Norah away and to the next activity where she's forced to keep her eyes closed."

        scene e59 #N excited hand on eyes smiling
        with dissolve

        P "Okay. Promise you're not peeking, young lady?"

        N "*giggle* Cross my heart and hope to die, stick a needle in yer eye."

        P "(That… was a bit morbid.)"

        P "Okay, you can look now."

        scene e60 #N excite look around
        with dissolve

        N "Okay!"

        scene e60-2 #N sur look at animals
        with dissolve

        N "*gasp*"

        P "(It's impressive how well trained these guys are. Didn't even make enough noise to give away their presence.)"

        P "*smile* What do you think?"

        scene e61 #N excited grab one on ground smiling
        with dissolve

        N "I think they're sooo cute!"

        P "Thought you would say so."

        scene e62 #cam close to all animals on N
        with dissolve

        "You and Norah spend a good amount of time playing with the exotic animals before you tell her it's time for the next activity."

        scene e63 #N pout
        with dissolve

        N "Aw, do we really gotta go already? I felt like I barely played with 'em."

        scene e64 #N smile in face of animal
        with dissolve

        N "Ain't that right, cutie pie? Hehe."

        P "*laugh* I don't think two hours qualifies as 'barely.' But I have a surprise for you that's just as good."

        scene e65 #N excited at cam
        with dissolve

        N "Really???"

        P "Mhm."

        scene e64
        with dissolve

        N "Yer papa's draggin' me away, but Mama's gonna be back to visit all y'all babies soon enough. I promise."

        "You know your [rel_m] didn't mean it like that, but you can't but imagine impregnating her and having a child."

        P "(Is it fucked up that vision makes me happy?)"

        scene bs
        with dissolve

        "You let the thought go and move on to the next activity as promised."

        scene e66 #N smile walking
        with dissolve

        N "Come on, sugar. Can't you even give me a tiny hint of what my surprise could be?"

        P "*laugh* Just because you keep asking doesn't mean I'm going to answer. Besides, we're almost there."

        "*neigh* *neigh*"

        scene e67 #N sur look out for sounds
        with dissolve

        N "Huh, what are those sounds…?"

        P "(Good timing.)"

        scene e68 #horses
        with dissolve

        N "*gasp*"

        N "Honey, you couldn't possibly mean…"

        scene e70 #N exc face cam
        with dissolve

        N "The horses are mine??? But these kind are so expensive!"

        P "(No kidding.)"

        P "Don't worry, I made a pretty good deal with the farm, so the caring and maintenance is already paid for, too. And you're only getting ONE. *laugh*"

        P "But you can choose which."

        N "Hehe."

        scene e72 #N hug cam
        with dissolve

        N "This was the last type of gift I was expectin' today, thank you so much, sugar."

        P "*smile* Anything for my cowgirl."

        N "*giggle*"

        "*neigh*"

        P "Oh, looks like they're calling you. Better go choose one before they get more impatient."


        scene e74 #cam stand behind N looking at horses
        with dissolve
        "Norah does slowly walk toward the horses and looks between them."

        P "(Wonder which one she'll pick? The owner said these were two of his best horses, so I guess she can't go wrong either way.)"

        N "I think I'll go with…"

        scene e75 #N hold out hand to horse
        with dissolve

        N "This beauty over here."

        N "How are you doin, huh? Doin' okay?"

        "Norah's voice is soothe and calming as she inches closer and closer."

        P "(Looks like she knows what she's doing.)"

        scene e76 #Horse nudging N and N patting
        with dissolve

        "It doesn't take long for the horse to accept her approach and touch."

        P "*smile* good choice. That really is a beautiful horse, [m_nik]."

        "You walk over."

        scene e77 #cam closer
        with dissolve

        N "You know what?"

        scene e78 #N normal smile at cam
        with dissolve

        N "I want you to choose the name."

        P "Me?"

        N "Mhm. I think it'd be more special that way. Like it'll be both ours in spirit. Whaddya think?"

        P "*smile* I think that's really cool."

        P "Hm… Let me think for a sec… It's a boy, so..."

        scene e79 #ground
        with dissolve

        $ h_name = renpy.input("What is the horse's name? Default will be Stormy")
        if h_name == "":
            $ h_name="Stormy"

        P "(Yeah… [h_name]. I really like that name.)"

        scene e78
        with dissolve

        P "What about [h_name]?"

        N "Oh, I think that is a gorgeous name, puddin'."

        scene e77
        with dissolve

        N "What do you think, [h_name]? Yer daddy chose that special name just for you."

        HH "*neigh*"

        N "*giggle* I think that was a neigh of approval."

        P "(There she goes making me a dad again… And again, I don't hate it.)"

        scene e78
        with dissolve

        N "You ready to ride, darlin'?"

        P "Huh? Ride what?"

        N "*giggle* The horses, silly! You can take the other one."

        scene e80 #cam look at other horse
        with dissolve

        P "(I wasn't really planning to… But I don't want to seem like a spoilsport, especially after promising what I did.)"

        scene e78
        with dissolve

        P "Uh, sure… Sounds like fun. Though I'm sure you know I have no clue how to ride."

        N "Hehe, I know. I'll tell you exactly what to do, puddin'. It'll be safe, I promise."

        P "*smile* Alright, I'm in your care, Norah. Just tell me what to do."

        N "Alright, first thing yer gonna do is approach the horse real careful-like. He don't know you, so you want to establish trust right away."

        P "Just like what you did with [h_name]?"

        N "Mhm, exactly like that. Lead with yer hand and let him smell you."

        scene e81 #cam hold out hand to horse
        with dissolve

        "You do as instructed and carefully make your way to the waiting horse."

        P "Easy there, boy… Don't mistake my hand for an apple and take a chomp out of it or something… *mutter*"

        scene e82 #horse smell hand
        with dissolve

        "The horse starts smelling you as soon as you reach it."

        P "Like it? Just bought a new cologne. Supposedly it's supposed to drive the ladies wild."

        N "*giggle* I think he does like you already."

        scene e83 #horse lick hand
        with dissolve


        P "*smile* I guess he does."

        N "What yer gonna do now is mount him. Make sure you do it with confidence, or he might get antsy if he senses any nervousness from you."

        P "He can actually sense if I'm nervous?"

        N "Mhm. They're big and strong, but horses are also very sensitive. You can almost think of them as big dogs."

        P "*laugh* I can kinda see that."

        scene bs
        with dissolve

        "Calming yourself, you soon mount the horse and Norah does the same, and you take off."

        scene e84 #N exc on horse smile
        with dissolve

        N "You did such a good job! I'm very impressed."

        P "Ha, thanks. Really not as hard as I thought it would be."

        N "That was the hard part for a lot. All we're gonna now is pull on the reigns a bit and just relax."

        P "What, no racing? You're lucky, I sooo would've left you in my dust."

        N "*giggle* I'll take yer word for it. I haven't ridden in a while, so I could use the practice."

        N "But I'll be happy to revisit this conversation in the future if yer still feelin' so bold, puddin'. I used to eat fellas like you for breakfast."

        P "Hahaha. Yes, you're on. When we both get a little more practice in."

        scene bs
        with dissolve

        "Norah continues to give you tips and instructions until you eventually lead her to the next thing on your list."

        scene e85 #N exc looking at picnic basket
        with dissolve

        N "Oh, I wasn't expectin' a picnic here."

        P "I figured we might be hungry at this point, so I had lunch setup."

        scene e86# N look at cam
        with dissolve

        N "Heh, you really thought of everything, didn't you? Thank you, I was actually startin' to get a little peckish."

        scene bs
        with dissolve

        "You and Norah take out all of the food and begin eating, and soon finish."

        scene e87 #N smiling down at food
        with dissolve

        N "Mmm, this is all so good, sugar. I really might need to take some home."

        P "*laugh* Feel free, it's all yours. Just make sure to hide it from Coral. You know she can be like a little hamster and pick at everything."

        N "*giggle* Thanks for the warnin'. You may have a point."

        P "*smile*"

        P "This might sound a little weird… But I want to know more about you. Of course I know the basics, but I'd really like to know more."

        scene e88 #N sur look up
        with dissolve

        N "You really wanna know more about me? It'll probably be borin'."

        P "I like listening to you talk. And I'm not just saying that to be nice. I do."

        scene e88-2 #N smi look down
        with dissolve

        N "Heh… I guess there's no problem then, since you really seem interested…"

        P "(Is she acting shy? That's really unexpected… and cute. But more importantly, she's reacting as if she were on an actual date.)"

        P "(Good!)"

        scene e89 #N smile at cam
        with dissolve

        N "You know that I grew up on a farm where I learned to ride horses and take care of a buncha animals and stuff."

        "Your [rel_m] goes on to explain her strict parents and the grittiness of the South."

        N "Then I met John…"

        scene e88-2
        with dissolve

        N "He was like a lighthouse to a ship out in a blindin' storm…"

        P "(Wow, I didn't know she felt that way about him.)"

        N "He saved me from all that and we moved away from the South as far as we could."

        P "Right… He's from the South too, but why doesn't he have an accent like you?"

        scene e89
        with dissolve

        N "He hated where we came from and everything about it, so he changed as much of himself as he could."

        N "It did worry me, but I figured we were in new surroundings and that it made sense, but as the years passed…"

        scene e90 #N look down sad
        with dissolve

        N "I realized I didn't know him anymore… And the way he treated you kids…"

        N "*shake head* It wasn't right. I understand he wanted y'all to be as tough as him for the world, but he forgot about bein' a [rel_f]…"

        scene e91 #N sad look at cam
        with dissolve

        N "I'm sorry I didn't stop him, baby… I swear I am. And if I could, I would go back and change everything."

        menu:

            "Don't say anything":

                "…"

                jump U5da

            "Say something [NorahPath]":
                $ npts = npts + 1
                P "Hey, don't think for even a second that any of what happened when we were kids was your fault. It's HIM who decided to act crazy, even now. You have nothing to do with that."

                P "And I remember plenty of times you tried to speak up or help, like the time you snuck me food when I wasn't allowed to eat for a whole day."

                P "I remember him finding out and yelling at you too, but you told him you would do it again."

                P "(And then Leanne gave him a piece of her mind... Good times.)"

                P "*smile* So I want you to smile, okay? Seriously. I wouldn't be the man I am today without you."

                jump U5da

label U5da:
    if nroute == True:

        scene e89
        with dissolve

        N "It's funny… You're a lot like he used to be when I fell for him… And I can easily say yer a better man."

        N "More kind, charmin', funny. I may be in trouble if I don't watch myself."

        P "*wink* That's the plan."

        N "*giggle* Yer so bad."

        P "(But it feels pretty awesome that she thinks of me in that way. Maybe I do have a chance to eventually do intimate things with her. Here's hoping.)"

        scene bs
        with dissolve

        "You two eventually clean up and engage in a few other activities on the farm until returning home."

        scene e92 #night/darker N in front of door, cam in front of her
        with dissolve

        P "So, the date is officially over! What's the verdict? I still get a passing grade? *grin*"

        N "…"

        P "[m_nik]? Did you actually have that much fun and can't talk?"

        scene e93 #N kiss cam
        with dissolve

        "Your eyes shoot open as she kisses you out of nowhere."

        P "(What? Where? Who? Is this actually happening? This is awesome!)"

        "Her soft lips press into yours for a few seconds."

        scene e94 #N look left
        with dissolve

        P "Wow… I wasn't expecting that. Not that I'm complaining even a little bit, by the way."

        N "Well… you were just such agentleman today that I figured you deserved a little award…"

        scene e92
        with dissolve

        N "Did it feel… good?"

        P "*nod* It felt amazing, to be cliché."

        N "As long as that's how you really feel."

        scene e94
        with dissolve

        N "A-Anyway, I think I'm gonna go clean up a little now, sugar. Thanks so much again for takin' me out."

        scene e95 #N gone
        with dissolve

        P "(She was pretty nervous at the end there and practically ran away. I don't think she was planning to kiss me and did it on the spur of the moment…)"

        P "(But she wasn't freaked out and seemed to enjoy it, and even asked if I did.)"

        P "*smile* (Today want as well as I planned, just gotta keep it up.)"

        scene bs
        with dissolve

        "You follow Norah's suit and get washed up before ending the day."

    scene bs
    with dissolve
    "Not long later, Zoe drags you out of bed for the continuation of readying you for a 'real' career in law like her."

    scene e96 #Z neu standing in office
    with dissolve

    Z "Today, you'll be simulating how it is to work as an intern at a firm."

    P "Ah, basically what you're doing?"

    Z "Precisely. I will be giving you tasks that mirror my own."

    P "I'm not nearly as efficient as you, so take it easy on me. When we were younger some of my friends even thought you might be an android. *laugh*"

    Z "…"

    P "(Okaaay. Tough crowd. Though she seems a lot more serious today than even usual.)"

    P "*clear throat* Uh, anyway… I'm ready to get started."

    scene e97 #Z walk away
    with dissolve

    Z "Good, follow me."

    P "(Man, she really is all about business today. So something tells me this isn't going to be a very fun experience.)"

    "You sigh and follow her."

    scene e98 #Z face cam in messy bedroom
    with dissolve

    Z "The first thing I need you to do is clean up this room."

    P "Thought I'd never see you with a messy room. Now I know anything is possible."

    scene e99 #Z anxious look away
    with dissolve

    Z "I've been… preoccupied with other matters."

    scene e100 #Z smi at cam
    with dissolve

    Z "Which is why it's a good thing you're here, isn't it? Almost like my prayers have been answered."

    P "(She's finally smiling, but it isn't friendly.)"

    P "*raise eyebrow* So I'm your servant boy now?"

    Z "Oh, heavens, no."

    Z "If anything, you could be classified as a maid."

    P "*frown*"

    Z "Hehe."

    scene e101 #Z walk passed
    with dissolve

    Z "Anywho, I'll let you get to work. Have fun."

    P "(Have fun how exactly?)"

    scene e102 #Z gone
    with dissolve

    "You sigh again as soon as she's gone and get to work."

    menu:

        "Start with the left side":

            scene e103 #cam hands out cleaning left side
            with dissolve

            "You spend the next several minutes tidying up the left side of the room."

            scene e104 #cam on right side cleaning
            with dissolve

            "Before switching to the other side."

            jump U5cl

        "Start with the right side [ZoePath]":
            if zpts >= 1:
                $ zsecret = True
                "***You have enough points for this option***"
                scene e104
                with dissolve

                "You start tidying up the room as instructed, but pause when something falls out of the box you were going to move."

                P "(Oof, I better not damage any of Zo's books or I'll be her 'maid' for the rest of my life.)"

                scene e106 #cam open book
                with dissolve

                P "Let's see what's inside…"

                P "'Greg takes his swollen cock and sticks it inside Marie, forcing her to cry out in pleasure…'"

                "Your eyes open wide and you let out an involuntary laugh."

                P "(Zoe's actually into smut?)"

                "Even though the proof is right in front of you, it's still hard to believe."

                P "(No matter how strict or serious she is, she IS still a woman. So of course she's interested in stuff like sex and romance, right?)"

                scene e105
                with dissolve

                "You shake your head and go to put the book away when you spot something else in the box."

                scene e107 #cam hold up dildo
                with dissolve

                P "Whoa…"

                P "(Now THIS, I was not expecting. A dildo?)"

                "You try to envision it lodged into Zoe's pussy, but the image won't come to your mind because of how impossible it seems."

                P "(Maybe I don't know my lawyer [rel_s] as well as I thought…)"

                jump U5cl

            else:
                "***You DO NOT have enough points for this option***"

                jump U5cl

label U5cl:

    scene bs
    with dissolve

    "It doesn't take long for Zoe to return and inspect what you've done."

    scene e108 #Z back to cam
    with dissolve

    Z "Well, it isn't as clean as I would like, but I suppose it's sufficient for the time being…"

    scene e109 #Z look to where her secret box was
    with dissolve

    Z "How could I have possibly forgotten… *mutter*"

    P "Zoe?"

    scene e109-2 #e98 clean
    with dissolve

    Z "[p_name]… Did you by any chance move a box that was on the right side of the room?"

    if zsecret == True:

        P "(From the way she's all fidgety, she has to be talking about her little sex box.)"

        P "(Heh, let's have a little fun.)"

        P "*grab chin* Hmmm, did I?"

        "Zoe's eyebrow twitches."

        P "I think I did. I'll go and get it for you. You want it, right?"

        scene e110 #Z flustered and hold out hands to stop cam
        with dissolve

        Z "No, no, no! Y-You've done enough here. I require your services somewhere else now."

        P "You sure? Its really no problem."

        Z "Y-Yes, I am quite positive. Let us move on."

        "You hold in a laugh and finally stop moving."

    else:
        P "*grab chin* (Did I?)"

        "…"

        P "Sorry, not that I can remember. Is it important or something?"

        scene e110-2 #e99 clean
        with dissolve

        Z "Erm… Not at all."

        P "(Is it me or is she acting weird?)"

        scene e109-2
        with dissolve

        Z "*clear throat* Anyway, it's time to move on to the next task I have for you."

        P "(Great, more work. Wonder what she'll have me doing this time?)"

        "Whatever seemed to bother Zoe quickly goes away before you have too much time to think about it."

    scene bs
    with dissolve

    "From there, you follow her into the office again."

    scene e96
    with dissolve

    Z "Alright, what you'll be doing now is calling a few people that have made payment plans to the firm, but have been late."

    "You hold back a sigh."

    P "So from maid to bill collector, huh? Guess I'm moving up in the world."

    scene e111 #Z smi
    with dissolve

    Z "I wouldn't quite say that yet. I need you to go pick up a few drinks, as I usually do on my mornings at the internship."

    P "Oh… sure. Let me just grab my phone really quick to write-"

    scene e96
    with dissolve

    Z "No time. You'll just have to remember."

    P "But-"

    Z "The first order will be a tall latte with a dash of cinnamon and caramel drizzle. Don't forget to make it non-fat."

    Z "The second is a medium-sized iced, vanilla latte with almond or soy milk. Doesn't matter which."

    Z "And the third is a double, venti half-sweet caramel macchiato."

    scene e97
    with dissolve

    Z "You can go pick them up after you make the calls over at the desk."

    "All you can do is stare with an open mouth as your [rel_s] briskly walks out of the room."

    P "(What have I gotten myself into?)"

    scene e112 #cam at desk look at blurry computer
    with dissolve

    "The only thing you can do is get to work as instructed."

    P "(Alright, looks like the first person I gotta call is a woman named Mrs. Rooney.)"

    scene e113 #cam look down at desk
    with dissolve

    "You pick up the phone to call and an elderly woman answers."

    P "*smile* Hello, Mrs. Rooney. I'm sorry to bother you. I'm calling on behalf of the Gaping Firm about your late payments?"

    RR "Oh my, am I late?"

    P "Yes, ma'am."

    RR "I'm so sorry. I've just been so preoccupied with my family. I haven't seen my grandkids in a few months."

    RR "You end up having an extra glass of wine and call your daughter-in-law a no-good, money grubbing whore, and bye-bye grandkids. *laugh*"

    P "I-I see…"

    RR "But thank you for calling and I'll make sure those payments are on time from now on. Bye now, sweetie."

    P "*laugh* (That was interesting.)"

    scene e112
    with dissolve

    P "(So the second person is a guy named Mr. Walnuts…)"

    "Once again, you call the number and a man with a New York accent picks up."

    WW "I AM YOUR WORST FUCKING NIGHTMARE, PAL."

    scene e113
    with dissolve

    P "E-Excuse-"

    WW "I TOLD YOU PEOPLE A MILLION FUCKING TIMES THAT I'LL PAY YOU YOUR DAMN MONEY WHEN I GET IT."

    WW "WHAT THE FUCK DO YOU WANT ME TO DO UNTIL THEN, PULL IT OUT MY ASS?"

    WW "WHY DON'T YOU GO TAKE IT FROM MY EX-WIFE WHO'S BLEEDING ME LIKE A PIG IN ALIMONY?!"

    P "(I've always thought debt collectors take too much blame, and I feel like giving this guy a piece of my mind, but I have to remember I'm representing Zoe here.)"

    P "Sir…"

    WW "SIR, MY ASS! DO YOU KNOW HOW IT FEELS TO WALK IN ON YOUR WIFE GETTING RAMMED BY THE POOLBOY?"

    WW "*sniff* A-And then she divorces YOU…"

    "The man starts bawling."

    WW "Oh goood, I miss you, Cheryl, please come back to me!"

    scene e112
    with dissolve

    "You manage to calm down the man eventually, and he promises to start making payments again."

    P "(That went well. Geez.)"

    "You call several more people until finally reaching the last name on the list."

    P "Mrs. Norton… *mutter*"

    P "(Okay, let's get this over with. I am beyond done.)"

    scene e113
    with dissolve

    "You make the final call and a woman with a husky voice answers."

    P "(You can basically see how hot this woman is. Probably a milf.)"

    P "Good morning, ma'am. I'm calling for the Gaping Company and your late payments?"

    WO "*giggle* Come on, do I sound so old that you need to call me ma'am? Please, call me Vanessa."

    P "*laugh* I'm really sorry about that, Vanessa. I just didn't want to come off as rude or anything like that."

    scene e114 #cam look somewhere else
    with dissolve

    WO "You're fine. And I am sorry about being late with those payments. I've just been caught up redecorating."

    WO "But you know… If I had a big sounding strong man like yourself, I'm sure it would go a lot faster."

    WO "Maybe just a weekend or two? I promise make it worth your while. *giggle*"

    P "(Is… this really happening? It's like I'm in a porno, so wouldn't I be insane to pass up an opportunity like this?!)"

    menu:

        "Accept the offer":
            $ zpts = zpts - 1
            P "*smile* You know what, Vanessa? I think I might be able to help a damsel in distress, such as yourself. And then we can talk about my little reward."

            WO "Oh, fancy yourself a knight in shining armor, do you? If anything, I would say you're more akin to a maid as we deduced."

            P "(Did she just diss me?)"

            P "*eyes open* Wait…"

            WO "That's right."

            scene e115 #Z smi by desk with phone
            with dissolve

            "You slowly turn your head to the voice."

            P "You're..."

            Z "Mhm. 'Vanessa' in the flesh."

            Z "May I inquire as to why you were agreeing to go to this woman's premises when all you were required to do was confirm future payments?"

            "Your mouth opens, but no words come out as you try to quickly think of a valid excuse."

            scene e116 #Z neu phone down
            with dissolve

            Z "I didn't think I had to explain that you are representing me today, so your poor decisions reflect badly on me."

            "You rub the back of your head in embarrassment and offer an apologetic smile."

            P "Sorry about that, Zo'."

            Z "*nod* Time for you to go get those drinks."

            jump U5ca

        "Don't accept [ZoePath]":
            $ zpts = zpts + 1
            P "Ah… I would really love to help you, Vanessa, but I would probably get in trouble and I don't want you to feel guilty or anything like that."

            P "(Shit, I can't believe I really just turned down a clear come on from a milf, but Zoe is more important. I need to focus on her right now.)"

            "*clap* *clap*"

            P "What…"

            scene e115
            with dissolve

            P "Zoe?"

            WO "Yes."

            P "She answers, but you hear Vanessa's voice instead."

            P "Ha… you were testing me."

            Z "That I was. And you pass."

            scene e116
            with dissolve

            Z "Now it's time for you to go out and get those drinks."

            jump U5ca

label U5ca:

    P "(Right back down to business…)"

    "A part of you wants to quit or complain, but you know that is a sure-fire way to disappoint Zoe, and it'll screw my chances of finding out what's going on with her."

    P "(I'll suck it up for now… But I don't know how much longer I can a hold out.)"

    scene bs
    with dissolve

    "You're forced to drive an hour for the drinks and Zoe admonishes you for the wrong orders when you return."

    "She then puts you through several more jobs, each more difficult than the last."

    scene e96
    with dissolve

    Z "Are you ready for the next assignment I have for you?"

    "You go to say 'no,' but pause."

    P "(Don't give up yet. You can stick this out a little longer.)"

    scene e117 #Z think pose
    with dissolve

    Z "Hmm… It seems I've underestimated you. Either that or you're a glutton for punishment."

    P "What?"

    Z "I've been doing my best to make you quit since our first day together."

    "You think back to Zoe putting you through a different kind of torture not long ago, like forcing you to drink that disgusting green smoothie."

    "As you do, you let her words sink in."

    P "(I never could get anything passed her when I was a kid.)"

    P "How long have you known?"

    scene e118 #Z smi
    with dissolve

    Z "Not long after you declared your interest in choosing a similar career to me."

    Z "At first, I was ecstatic, but then I started to wonder why the sudden change of heart. And that wonder soon turned into doubt."

    Z "So I purposely made you do all those things the other day when I dragged you out of bed. I thought you might falter and give your true motivations, but you didn't."

    Z "So I inquired about it from the other girls and Coral mentioned you two had started your… venture once more."

    P "Geez, way to snitch, Coral. *mutter*"

    P "(Though I have no doubt that Zoe was asking questions in a roundabout way, so Coral didn't even know she was giving me up.)"

    scene e96
    with dissolve

    Z "So that begs the question, [p_name]. Why in the world go through all of this? What exactly is your aim here?"

    Z "Because it's abundantly clear that my pleas for you to attend college have fallen on deaf ears."

    P "(The only thing I can do now is tell the truth, which I maybe should have done from the beginning…"

    P "(Though going through all this crap might show that I really am serious about finding out what her problem is, and helping.)"

    P "The truth is, I'm worried about you, Zoe."

    scene e119 #Z surprised
    with dissolve

    Z "Concerned over me? Why?"

    P "Just like you're able to see through me, I can tell something is going on with you."

    P "Maybe you can hide it better with the others, but I haven't been back long and I can already tell you're not yourself."

    Z "…"

    scene e120 #Z smi look down
    with dissolve

    Z "I suppose we've reached a stalemate then…"

    P "*smile* Looks like it. Ready to call a truce or do you want to go a few more rounds?"

    scene e121 #Z throw up hands
    with dissolve

    Z "I am prideful, but I know when to concede. And it's clear you'll go to dire ends to get what you want."

    P "(Looks like doing all of this crap did pay off.)"

    P "*laugh* You definitely didn't make it easy, but you're right. I'm willing to go through whatever for you, Zoe. So please talk to me."

    scene e119
    with dissolve

    P "I can't promise to help with whatever problems you have, but I will try. All I'm asking for is the chance."

    Z "…"

    scene e118
    with dissolve

    Z "*laugh* I know I've said it before… But you really aren't a boy anymore."

    "It's more of a statement, so you don't answer."

    scene e122 #Z look away
    with dissolve

    "Zoe suddenly gets serious."

    Z "As you've deducted, I do have a dilemma of sorts, and the origin is work. I found one of the lawyers at the firm acting suspiciously."

    P "Suspiciously? How?"

    scene e96
    with dissolve

    Z "Taking random lunch breaks and acting very secretive when taking certain phone calls."

    Z "So I followed him during one of his breaks and spotted him meeting with two men in black suits and sunglasses."

    P "That doesn't sound shady at aaall."

    scene e111
    with dissolve

    "Zoe huffs out a short laugh through her nose."

    Z "Precisely. So I planned to confront him, but never got the chance."

    P "What happened?"

    scene e96
    with dissolve

    Z "Just as I had noticed him acting suspiciously, he noticed my interest and threatened to reveal my secret to my university."

    scene e122
    with dissolve

    Z "*sigh* And I would no doubt be expelled for it."

    P "(I know Zoe's university is strict to the point it makes private schools look like a Saturday night at a strip club.)"

    Z "I suppose you want to know the secret."

    P "Yes, I do. I need the whole picture to properly help. But you know you can trust me, right?"

    scene e96
    with dissolve

    Z "*stare* …"

    Z "Yes. I know."

    P "*smile* Good. Besides, remember that time I told you my biggest secret?"

    scene e111
    with dissolve

    Z "I hope you're not talking about your candy stash when we were mere children?"

    P "Hey, I would've died for it back then. Don't underestimate a kid and his love for candy."

    Z "*giggle* You are so silly."

    P "*grin*"

    Z "[p_name]?"

    P "Yeah, Zo'?"

    Z "Thank you for trying to help me."

    P "You're welcome, Zo'."

    scene bs
    with dissolve

    "Zoe leads you from the office to her bedroom, so you two don't get any surprise visitors."

    scene e124 #cam behind Z on laptop
    with dissolve

    "You focus on the screen as Zoe finally goes to a website."

    scene e125 #Z nerv look back at cam
    with dissolve

    Z "*nervous breathing*"

    P "(Whoa… I have to say this is the absolute last thing I was expecting her secret to be.)"

    if zsecret == True:

        P "(But maybe I shouldn't be so surprised with her little goodies I found earlier while cleaning.)"

    P "This website... and blog…"

    scene e126 #cam look at Z
    with dissolve

    P "It's yours?"

    Z "Y-Yes? Is it so shocking?"

    P "Ha, well… If I'm being honest, yeah. You just don't seem like the type to be interested in sexual stuff."

    scene e127 #Z more flustered
    with dissolve

    Z "I-It's not sexual, okay?! I admit there's a fair amount of that at first glance, but I just like to give advice on romance and of course that accompanies intimacy…"

    Z "So I chat with those subscribed to my site about everything that encompasses that from date night ideas to… not safe for work ideas."

    P "(Wow. Zoe is really running a romance/sex blog. No wonder she doesn't want her university to find out.)"

    P "Now I understand why your university can't find out. They're no-nonsense, right?"

    scene e128 #Z sad look away
    with dissolve

    Z "Yes, but that does not matter anymore. I can't risk being exposed, so I'm shutting the website down."

    P "(It's clear as a day she enjoys this and doesn't want to give it up.)"

    "You quickly come to a conclusion."

    P "You don't have to shut anything down."

    scene e129 #Z surprised
    with dissolve

    Z "Wh-What are you talking about? Didn't you hear anything I said? I simply cannot risk getting expelled, and thus putting a stain on my future as a respectable lawyer."

    P "I hear you loud and clear, but I have a plan so that your school never catches a whiff of this."

    Z "H-How?"

    "Zoe's voice is full of desperation, so you're intuition about her really wanting to keep the site was right."

    P "We kill him."

    scene e130 #Z eyes wide
    with dissolve

    Z "WHAT???"

    P "*laugh* Sorry, couldn't resist."

    Z "What…"

    scene e131 #Z neu
    with dissolve

    Z "…"

    Z "If I were any less mature, I would give you a good smack at this moment."

    P "*smile* Good thing for me you are, big [rel_s]."

    P "But seriously, I'm going to follow this douche threatening you and find out what the hell he has going on. And then I'm going to give him a simple choice."

    P "Either he can promise to keep his mouth shut about your website or I can expose him too."

    scene e129
    with dissolve

    Z "What? That's ludicrous, [p_name]! I couldn't possibly let you put yourself in harm's way like that."

    P "You're not, and honestly, even if you tell me not to do it, I'm going to anyway. I'm sorry, but I just can't let anybody screw with you."

    P "Call it stupid or foolish if you want, but that's just how I feel."

    Z "…"

    scene e132 #Z smile
    with dissolve

    Z "It is neither stupid or foolish... It is brave and caring."

    scene e133 #Z kiss cam forehead
    with dissolve

    P "smile* (One of Zoe's kisses. That's super rare.)"

    scene e134-2 #Z sit smile
    with dissolve

    Z "As you just stated, I know that nothing I say is going to convince you otherwise, so I will be joining you on your mission."

    P "(What? No, I can't let her do that.)"

    Z "And before you protest as I can clearly see you are posturing yourself to do, I will not back down either. So either we will do this together or not at all."

    P "…*laugh* I guess we're all pretty stubborn, eh?"

    Z "*laugh* That we are."

    scene e134 #Z nerv look away
    with dissolve

    Z "But, erm, now that we've established that… I wanted to inquire about something else…"

    P "(I can't say I'm used to Zoe acting all shy and timid like she has been today, but I get she's out of her comfort zone with having had to reveal everything.)"

    P "Shoot."

    Z "Well… I've really been meaning to acquire a male's perspective regarding various relationship topics for a podcast series on my website."

    scene e134-3 #N nerv at cam
    with dissolve

    Z "And since you know my secret now… I was wondering if you would be interested by any chance to share your views?"

    P "(The surprises keep coming, huh? This may be the perfect opportunity to get… closer to Zoe in another way.)"

    P "(But is that really what I want? And even if it is, am I ready to cross that line in our relationship? It could ruin everything.)"

    menu:

        "Help her [ZoePath]":
            $ zpts = zpts +2
            $ zroute = True

            "You think for a moment."

            P "(Yeah… yeah. It is what I want, and I am ready.)"

            P "*smile* I would love to participate with your website."

            scene e135 #Z excited
            with dissolve

            P "And I actually think it's pretty cool you have a secret hobby like this. I thought all you did was work, work and more work. *laugh*"

            Z "Thank you so much, [p_name]! I'm going to make preparations for the podcast right away and we can get started tomorrow."

            P "Haha. No problem. But aren't you worried about your voice? It doesn't matter if people recognize mine, but you obviously want to stay anonymous."

            scene e134-2
            with dissolve

            Z "Aren't you forgetting earlier when I so easily tricked you into thinking I was that woman named Vanessa Norton?"

            P "Ah, you're totally right. Haha. If the whole lawyer thing doesn't work out, you should seriously think about doing voice acting because that was damn impressive."

            Z "Heh. I'll keep that in mind."

            scene bs
            with dissolve

            "After a little more conversation, you leave an excited Zoe."

            jump U5po

        "Don't help her":

            P "(No… I don't think I am ready for this and the possible consequences.)"

            P "I'm sorry, Zo', but I just don't think I would be good at that kind of thing. I hope you understand?"

            scene e134-4 #Z sad at cam
            with dissolve

            Z "Oh…"

            scene e134-2
            with dissolve

            Z "I understand. And thank you again for helping me keep my website, [p_name]. I really do appreciate it."

            P "*smile* Anything for you. I just expect the same kind of favor when I need something."

            Z "*laugh* I'll see what I can do."

            scene bs
            with dissolve

            "You leave Zoe's room and think about how you're going to catch her colleague."

            jump U6

label U5po:

    if zroute == True:

        "It doesn't take long for Zoe to summon you the next day."

        scene e137 #Z with laptop smi
        with dissolve

        Z "Thanks again for agreeing to help me with this, [p_name]. Having a man's point of view of several subject matters is crucial in giving out constructive advice to all my female subscribers."

        P "I think you're awesome for even doing it in the first place. This way there is no biases, and people can get honest advice."

        Z "Hehe. Thank you."

        P "So, I just speak into the mic clipped on my shirt and all your listeners will hear me?"

        Z "Correct. I'll be monitoring the questions and the chat and will relay everything to you."

        P "*nod* Roger that. I'm ready."

        scene e138 #Z look down at laptop
        with dissolve

        Z "Great! I'm starting the podcast now."

        Z "Hey, everyone! I know I've been gone for a little while, but what better way to say sorry than to give you that long-awaited podcast you all have been begging for, right???"

        P "(Wow, Zoe really can sound like a completely different person when she wants to. I'm learning a lot about her this trip.)"

        "She talks for a little while before introducing you as a special 'friend,' and you two get into the first topic."

        scene e137
        with dissolve

        Z "The first topic is one that has been hotly debated amongst everyone in the forum."

        Z "Who should lead the relationship, the man or the woman? I'm sure all of the lovely ladies in this chat would love to hear your perspective on it."

        P "*smile* No pressure at all."

        Z "*laugh* Maybe a little, but whatever you think is what we all want to know. Real, raw truth about such an important dynamic. No answer is right or wrong."

        P "*nod* To be honest, it's something I've thought about before and have struggled with in my own relationships."

        scene e138
        with dissolve

        P "Let's just take both scenarios from my experience. I was set up with this girl who was much more wealthy and she would buy me everything I wanted and pay for all of our dates."

        P "Maybe it's a silly primal feeling, but I just felt inferior that I wasn't providing, despite our younger age. And I noticed that she would have an attitude every time she did shell out cash."

        scene e137
        with dissolve

        Z "So you're saying she didn't enjoy having to take care of you, despite having the means to do so?"

        P "Right."

        Z "And why do you think that is?"

        P "I had thought about that question a lot at the time and I came to the conclusion that women just like to be taken care of by their man. And I enjoyed taking care of her."

        P "So I stopped letting her buy me things and our relationship got way better."

        P "Of course this is just a very small sample, but just having the man be equal or in charge financially is something that I think some women want."

        scene e138
        with dissolve

        Z "Oh! Your comments definitely sparked the chat. We have a good number agreeing with you and a good number disagreeing."

        P "*smile* It is a pretty touchy subject so I understand."

        "You and Zoe go over more topics until it's time for the question and answer portion."

        scene e139 #Z look down flustered
        with dissolve

        "And everything goes smoothly at first until a chosen subscriber asks an explicit question."

        Z "H-Hey, behave now, ladies. Let's keep it PG for our guest."

        P "I'm totally cool with it. *whisper*"

        scene e140 #Z look at cam
        with dissolve

        Z "R-Really? *whisper*"

        P "*nod*"

        scene e138
        with dissolve

        Z "Ha, well… it looks like you're going to get your wish granted after all, princess233."

        scene e141 #Z smi cam avert eyes
        with dissolve

        "You and Zoe start answering a slew of sexual questions that only get more heated."

        Z "This time we have a question from Honey69 who would like to know how to get her husband in the mood."

        P "(This could be a fun question… Let's see if Zoe is willing to play ball.)"

        P "I get keeping the passion alive for a new relationship can take work, but that's what it is 'work.' You have to try, so that's awesome that you're asking that question, Honey."

        P "But I would like to hear it from LawlessLove's perspective on how she would turn me on if I was her boyfriend, and I can critique or comment."

        scene e142 #Z mad at cam
        with dissolve

        P "(LawlessLove, Zoe's online identity… But shit, did I take it too far? She does not look happy at all.)"

        Z "'WHAT ARE YOU DOING?'"

        "Zoe mouths."

        P "'It's fine.'"

        "You smile and mouth back, trying not to show your regret and nervousness at asking the question in the first place."

        scene e139
        with dissolve

        P "(Is she… actually thinking about it?)"

        scene e143 #Z avert eyes shy
        with dissolve

        Z "Thank you for the question. I'm sure my audience is interested how I would approach the situation myself."

        Z "So to answer your question… I would come home and see you sitting on the couch watching TV and would walk right up to you..."

        Z "Then slide off the panties I had masturbated with earlier…"

        Z "While looking directly into your eyes. And I would just give them to you without a word before going into the kitchen to make dinner."

        scene e144 #Z shy look other way
        with dissolve

        Z "What do you think about that so far?"

        P "(It's clear Zoe isn't totally comfortable because she can't even look me in the eye… but I can tell a part of her likes it too.)"

        P "(And what she just said she would do to me is hot as fuck. I almost believe those words didn't come from her mouth.)"

        P "I'm very pleasantly surprised, Lawless. In that situation, I would be so confused…"

        P "But in the best way possible and then forget whatever the hell I was doing to follow you into the kitchen."

        scene e145 #Z open mouth mesmerized at cam
        with dissolve

        P "Then as quietly as you gave your dirty panties to me, I would bend you over and…"

        P "(I don't want to push my luck here with this being our very first podcast together. Shouldn't take it too far.)"

        P "*laugh* Well, you get the idea."

        Z "What…"

        scene e147 #Z surprised
        with dissolve

        Z "O-Oh! Right!"

        scene e138
        with dissolve

        Z "Hehe, that was some demonstration, wasn't it, girls?"

        "You two spend a little bit more time talking before the podcast finally ends."

        scene e137
        with dissolve

        P "That was… fun. *awkward laugh*"

        Z "Yes… Quite… And if you're willing, I would enjoy having you back very soon."

        "You try to hold off the huge smile that wants to form on your face."

        P "(Not only was she okay with that little sexual roleplay, but she wants me back? Hell yes.)"

        P "I'll check my schedule and I'll have my secretary let you know. And since I don't have a secretary, my answer is yes."

        Z "*giggle* I well let you know of the next occurrence then. Thank you, [p_name]."

        scene bs
        with dissolve

        "You leave Zoe's room and think about how you're going to catch her colleague."

        jump U6

label U6:

    "OKAY, PEOPLE. THIS IS THE END OF UPDATE 5 FOR SECRET SUMMER."

    "IF YOU WANT TO SEE MORE. PLEASE CONSIDER SUPPORTING MY PATREON. EVERY DOLLAR HELPS, SERIOUSLY."

    "SEE YOU NEXT UPDATE!"
