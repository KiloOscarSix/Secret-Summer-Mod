label U6:

    scene bs
    with dissolve

    "A little more time passes as you spend time with the girls, trying secretly to uncover the problems they've got going on."

    scene f1 #cam sitting over edge of bed. Show his body
    with dissolve

    "It's early morning, but you're wide awake, thinking about the situation."

    P "(I know what's going on with Leanne now. She and her career in dancing never being explored.)"

    P "(So now all I actually have to do is help her… Which is a lot easier said than done, but at least I have somewhere to start.)"

    P "(And of course I still plan to figure out why she was all touchy feely back at my welcome back lunch when she's strictly forbidden that for years.)"

    scene f2 #cam look up
    with dissolve

    P "(Then there's Zoe and the blackmailing by her colleague. Well, technically not blackmail, fortunately.)"

    P "(But he's still a threat to her romance blog, so I'll come up with a tighter plan to deal with him.)"

    if zroute == True:
        P "(Still hard to believe she has a website like that, though, and now I'm even participating in it.)"
        P "*smile* (But it's the perfect way to cross the boundaries in our relationship.)"

    scene f3 #cam look to side
    with dissolve

    P "(After that is Coral. She hated me when I first got here, but finally forgave me, and now we're tighter than ever.)"

    P "(She doesn't exactly have a problem like the others, but there's still plenty we have to work on.)"

    P "(Like our dating simulator and the Immortal Fighting tournament. Which is still freaking awesome!)"

    if Cbf == True:

        P "(Another big thing that happened was us revealing our feelings for each other, which totally caught me by surprise.)"

        P "*smile* (But I couldn't be happier. We didn't discuss anything in detail, so I'm still anxious to see where everything goes.)"

    scene f4 #cam look to other side
    with dissolve

    P "(The only problem of the girls I don't know is still [m_nik]… But I think I'm getting closer and closer to finding out what it is.)"

    P "(I just have to keep spending time with her, like with the computer lessons.)"

    if nroute == True:
        P "(And with us officially dating now, it might be easier to pry the truth from her.)"
        P "*smile* (I still can't believe we are, but our date recently just proves that fact.)"
        P "(And let's not forget about the kiss at the end. I know she's still plenty hesitant about intimacy, but that shows that she isn't totally against it.)"

    scene f1
    with dissolve

    P "(And of course I have my own crap to deal with, having to secure the Buster Himen contract or be reeled back home.)"

    P "(That would obviously mean leaving the girls high and dry again, so there's no way I can fail.)"

    scene f4
    with dissolve

    P "(Good to have Irene on my side now. No freaking clue why she decided not to rat on me, but I'm sure as hell not going to complain.)"

    P "(I don't know if I should fully trust her, though. There's no doubt that she's a smart woman, so who knows what plans she could have up her sleeve.)"

    scene f2
    with dissolve

    "*ring*"

    P "(The front door? Who could be visiting so early?)"

    scene bs
    with dissolve

    "You throw on some clothes and go check who it is, with everyone else out of the house."

    scene f5 #Irene at front door
    with dissolve

    P "(Speak of the devil.)"

    P "Irene?"

    I "That's what some people call me, yes."

    P "*laugh* (Not really used to her joking. I guess our relationship really has changed.)"

    P "You're visiting pretty early. I'm not in trouble, am I?"

    scene f6 #I raise eyebrow, shift pose?
    with dissolve

    I "Have you done anything to think you would be in trouble? Well, besides being here in the first place and all."

    "You can't help but bark out a laugh."

    P "Hey, that's a very sensitive topic, you know."

    scene f5
    with dissolve

    I "I know, I know. You haven't gotten a call from John telling you to come back home, right?"

    P "That I haven't."

    I "See? I know how to keep a secret."

    P "*smile* I do see. Thank you, Irene."

    scene f7 #I clap
    with dissolve

    I "Okay! Now to get to the reason I'm here. You do know what today is, don't you?"

    P "Uhhh… Happy Birthday?"

    scene f5
    with dissolve

    I "*laugh* My birthday was last month, actually. And now that we're on good terms, I totally expect a belated present."

    P "(Irene probably has everything under the sun, dealing with my [rel_f]. So what could I possibly get her that she doesn't already have?)"

    P "*smile* I'll see what I can do."

    I "Thank you."

    scene f8 #I shift pose
    with dissolve

    I "But today is actually Buster Himen's party. So this is the day we close the deal and you show John how capable you are."

    I "Are you ready?"

    P "(Damn, I had totally forgotten with me so focused on all of the girls, but I can't let Irene know that.)"

    P "Of course. I got it in the bag."

    scene f9 #I look inside. Maybe raise hand?
    with dissolve

    I "*laugh* I'm sure you do, but do you mind if I come in to talk a bit more?"

    P "Ah, sorry. Where are my manners? Come in, please."

    scene f8
    with dissolve

    I "Thank you."

    scene bs
    with dissolve

    "You lead Irene to the living room."

    scene f10 #I smi on looking around
    with dissolve

    I "I didn't mention it last time I was here, but this really is a beautiful home."

    P "Zoe was actually the one to pick it out, so you can thank her."

    scene f11 #I look at cam
    with dissolve

    I "That does make sense. Norah certainly isn't a weak woman, but Zoe likes to take charge, doesn't she?"

    P "*smile* Like a rhino."

    I "*laugh* So, anyway, I came here to pick you up."

    P "Pick me up?"

    scene f12 #I move hand
    with dissolve

    I "Mhm, I've been doing a little research and it turns out there are supposed to be some big wigs at the party tonight."

    I "So we need to go all out in terms of appearance. You don't have a tuxedo or anything here, correct?"

    P "Ah… nope. I've never worn one anyway. Just regular suits."

    scene f11
    with dissolve

    I "That's what I thought. You don't exactly seem like the flashy type."

    P "*raise eyebrow* What type do I seem like?"

    scene f13 #I raise hands
    with dissolve

    I "*laugh* I swear I didn't mean that as a slight."

    scene f12
    with dissolve

    I "I actually prefer the casual style myself."

    P "(I think she said something similar back at Himen's office.)"

    P "Then… why do you dress the way you do?"

    scene f14 #I neu look down to side
    with dissolve

    I "Well… John says that I should use what I have, and there's no shame in it."

    menu:

        "Don't say anything":

            jump U6agree

        "Say something [IrenePath]":

            $ ipts = ipts + 1

            P "To be honest, I'm not sure if he's right or wrong about that. He's obviously more experienced and business savvy than me…"

            scene f15 #I slight surpris look at cam
            with dissolve

            P "But you don't HAVE to do anything like dressing flashy. You're smart enough to get whatever you need done."

            I "…"

            scene f11
            with dissolve

            I "Heh… Not easy to make me blush, [p_name]. Thank you for saying that."

            jump U6agree

label U6agree:

    scene bs
    with dissolve

    "Of course you're not exactly gung-ho to go tuxedo shopping for a party you don't even want to be at."

    "But you do understand how important it is to impress people like Buster Himen who only respect wealth and power."

    scene f16 #I looking at suit
    with dissolve

    I "Oh, what about this color, [p_name]? I think you would look really good in it."

    P "*shrug* Sure."

    scene f17 #face cam
    with dissolve

    I "You know, if you looked any more disinterested, I would actually start thinking you didn't want to be here."

    P "Ha, sorry. Just never been much of a clothes shopper. Like you said, I like to keep it simple."

    P "So I will humbly let you pick what tux I should get. I'm sure you know what you're doing."

    I "*laugh* You're real smooth, you know that?"

    scene f16
    with dissolve

    I "Lucky for you, I'm the typical woman who loves shopping. Even for other people…"

    I "Oh! This is so cute. I think it'd look great on you."

    P "*smile* (Guess I'm starting to learn more and more about the real Irene.)"

    scene f18 #I move down a bit to reach for more clothes
    with dissolve

    "You follow her as she checks out more clothes."

    P "So today's shopping trip is about some big names attending the party, right? How big we talking?"

    I "Well, plenty big. Though the ones we need to worry about impressing are who we can get in bed with. Or show our muscle to."

    P "What do you mean show our muscle?"

    scene f19 #I face cam neu
    with dissolve

    I "Phil Lowry who owns a very popular clothing brand is rumored to be trying to get into the video game scene, too."

    P "Ah… I know plenty about him… Or at least how much my [rel_f] hates him for always stealing contracts. *laugh*"

    I "Certainly. Not only is he a hindrance when it comes to business, but that worm of a human being is a sexual assault waiting to happen."

    scene f20 #I switch pose
    with dissolve

    P "Damn. Is he really that bad?"

    I "Let's just say he makes Buster Himen look like a firefighter who volunteers at an orphanage in his free time."

    P "*laugh* Okay, that's REALLY bad."

    scene f21 #I smile
    with dissolve

    I "No kidding."

    scene f18
    with dissolve

    I "That's exactly why you're going to be my husband."

    P "*blink* Come again?"

    I "You know how John likes to keep to himself. Most people don't even know what he looks like."

    scene f21
    with dissolve

    I "That's why you're going to pretend to be the head of the Perving Company. Which isn't too far a stretch, considering you'll inherit it one day."

    menu:

        "Disagree":
            $ ipts = ipts - 1

            P "I don't think that's really necessary, is it, Irene? And I doubt they would think I'm really your husband."

            scene f20
            with dissolve

            I "Clearly you've forgotten how Buster Himen treated you like a fly in the room on our very first meeting?"

            I "It is known that I'm married to the CEO of our company, so they don't have a choice but to believe I'm there with a man none other than him."

            I "Or do you like being treated as a fly?"

            P "Ah… That I don't. I guess you're right."

            scene f21
            with dissolve

            I "Heh. Of course I am. As the saying goes, 'boys go to Jupiter to get more stupider.'"

            "You laugh out loud, not expecting her joke."

            P "Touché."

            jump U6husband

        "Agree [IrenePath]":

            $ ipts = ipts + 1

            P "I guess you do have a point. Buster Himen treated me like a fly on the wall last time."

            I "Exactly. So this time, you'll be treated with some dignity instead of an errand boy sent out by his [rel_f]."

            P "But do you think they'll really buy we're married?"

            scene f22 #I change pose
            with dissolve

            I "What, am I too old for you?"

            P "*laugh* Quite the opposite. I was thinking I'm too young for YOU."

            scene f23 #I look at cam body
            with dissolve

            I "You should give yourself more credit, [p_name]. You're a handsome MAN in great shape."

            "You feel a little nervous with Irene openly checking you out."

            I "I saw a woman surely older than me ogling you when we were walking through the food court."

            scene f22
            with dissolve

            P "Really?"

            I "Mhm. So you're going to be my young stud husband for the evening."

            P "And you'll be my sugar mama?"

            I "Hahaha. Don't push it."

            jump U6husband

label U6husband:

    scene bs
    with dissolve

    "You and Irene continue shopping… Or rather you watch her shop until heading to the dressing rooms to try everything on."

    scene f24 #cam dressing self
    with dissolve

    "But having never worn a tuxedo before, the task is a lot more difficult than you imagined."

    P "*mutter* I swear it'd be easier to put on a suit of armor than this shit."

    "You blow out a frustrated sigh."

    scene f25 #stall door
    with dissolve

    I "[p_name], is everything okay?"

    P "Ah… yeah. I'm good."

    I "You don't sound very good. I'm coming in."

    P "Wha –"

    scene f26 #I look at cam body
    with dissolve

    P "I-I'm half naked here, Irene."

    I "You definitely are, which means you're not good after all."

    scene f27 #I hug up to cam, look down
    with dissolve

    I "Look, you have this all wrong. Let me help."

    "She starts fiddling with your pants, dangerously close to your crotch."

    P "I-Irene."

    I "One second, [p_name], I almost got it."

    scene f28 #f27 different angle
    with dissolve

    "All you can do is try to control yourself from getting an erection as she continues to help you dress."

    I "And… there!"

    scene f26
    with dissolve

    I "How do they feel? Not too tight or too big?"

    "You lift your legs."

    P "Nope. They fit perfect, actually."

    scene f30 #I smile at cam
    with dissolve

    I "Good."

    scene f31 #I look around
    with dissolve

    I "Now where's your jacket?"

    I "Ah, there it is."

    scene f32 #I reach for jacket super clothes to cam
    with dissolve

    "Irene reaches for it before you can even ask."

    "And you get a good whiff of her sweet scent as she does."

    scene f33 #I putting jacket on cam
    with dissolve

    I "This part goes here… and you attach this…"

    P "(Guess I have no choice again, but to let her dress me. I WAS struggling anyway, so the help is appreciated.)"

    P "You know, you're kinda scary good at this. I just realized you didn't even ask my size, but everything looks to be fitting perfectly."

    P "Are you a witch, Irene?"

    scene f34 #I close to cam face fixing shoulder
    with dissolve

    I "*laugh* I've been called something fairly similar to that, but no, I assure you I'm completely human."

    P "So you're just like the Michael Jordan of shopping?"

    I "Heh, not quite."

    scene f35 #I switch to other shoulder
    with dissolve

    I "I worked as a seamstress up until a few years ago."

    P "(I gotta say, I was not expecting to hear that.)"

    P "Really?"

    scene f36 #I look at cam
    with dissolve

    I "Is it so surprising? I wasn't born with a silver spoon in my mouth."

    P "Ah, I didn't mean to sound like an ass or anything. You just seem so…"

    P "*shrug* I don't know. Like a princess or something. Like you come from royalty."

    I "*giggle* That's very cute of you to say, but I promise I'm no one special."

    scene f26
    with dissolve

    I "Okay! Let's take a look at you."

    "You stand awkwardly as Irene studies you."

    P "So? What's the verdict?"

    scene f30
    with dissolve

    I "If anything, you're the princess with how regal you look right now, [p_name]."

    P "Ha! I think I'll take that as a compliment."

    I "Hehe. It was."

    scene f39 #I brush hair out face
    with dissolve

    I "Oh, just a sec! Just a little lint in your hair."

    "Irene starts messing with your hair."

    scene f40 #I still close hands on cam face
    with dissolve

    I "There, now you're perfect."

    P "*smile* Thanks."

    I "…"

    P "Irene?"

    scene f41 #I surprise
    with dissolve

    I "Oh!"

    scene f30
    with dissolve

    I "Heh, sorry about that."

    P "Are you okay?"

    I "Yes, of course…"

    scene f42 #I shy look away
    with dissolve

    I "It's just that I think this is nice, us spending time together. You might not know, but I don't have any children."

    I "And obviously I'm not your mother and I wouldn't dare try to be, but I want you to think of me as someone you can rely on."

    I "*shake head*"

    scene f30
    with dissolve

    I "*laugh* I don't even know what I'm saying right now. Just forget that crazy ramble."

    I "I treat you like a stranger for the past year, and now I'm suddenly telling you to treat me like a mother figure."

    I "What nerve I must have, right?"

    menu:

        "No [IrenePath]":
            $ Imf = True
            $ ipts = ipts + 2

            P "You're wrong."

            scene f43 #I surprise
            with dissolve

            I "I'm wrong?"

            P "Yes. I treated you just as much of a stranger since you married my [rel_f], so I'm just as much to blame."

            P "And we haven't spent much time together, but it's been a lot of fun hanging out with you recently."

            P "Plus assaulting me in the dressing rooms is totally something a mom would do."

            scene f30
            with dissolve

            I "*giggle* I wasn't even thinking, sorry about that. I just wanted to help you."

            P "*smile* I know, which is why I'm not pressing charges."

            I "Hehe. Thank you."

            scene f44 #I hugs cam
            with dissolve

            P "Oh."

            I "Since you're saying me acting more like a mom to you is okay, I'm going to be taking more liberties from now on."

            P "*laugh* Like random hug attacks?"

            I "Exactly."

            P "Maaan, just what have I gotten myself into?"

            scene f40
            with dissolve

            I "*laugh* Too late to take it back now. You're all mine. Muahaha."

            P "You might have to fight Norah if that's the case."

            I "She's actually the one who suggested I act more like a mother to you."

            P "Really?"

            scene f45 #I drop hands
            with dissolve

            I "Mhm. I was definitely hesitant at first and figured we should have more of a friendship…"

            I "But, I understood what she was trying to say the more I thought about it "

            scene f46 #I look around
            with dissolve

            I "And now here we are in a dressing room together."

            P "*laugh* We've definitely come a long way in a short time."

            scene f45
            with dissolve

            I "We have."

            P "(So [m_nik]'s the reason for Irene's sudden change in attitude. She's always helping me, even when I don't realize it.)"

            P "(I'm seriously lucky to have her… And Irene now too, I guess.)"

            jump U6no

        "Yes":

            P "*awkward laugh* I'll pretend it didn't happen, no problem."

            scene f42
            with dissolve

            I "Thank you…"

            jump U6no

label U6no:

    "You hear vibrating."

    scene f47 #I look at phone. f30 base
    with dissolve

    I "Excuse me a moment, sweetie. John is calling."

    "You involuntarily twitch."

    scene f48 #I turn slight to side
    with dissolve

    J "Were you able to secure the Himen contract?"

    "The dressing room is quiet enough to hear the other side of the phone."

    P "(Those are literally the first words out of his mouth? Jesus.)"

    scene f49 #I face other way Worried
    with dissolve

    I "Well… not exactly. The initial meeting did go well, so we're hoping to close tonight at his party."

    scene f50 #I smile at cam
    with dissolve

    I "[p_name] and I are actually out right now, and I have to say he cleans up quite well."

    "You smile back at Irene."

    J "Just make sure you get the contract. Even if [p_name] fails."

    P "…"

    scene f49
    with dissolve

    "Irene breaks eye contact with you."

    I "I understand."

    scene f48
    with dissolve

    I "But you know, there really are some nice tuxedos at this shop, honey. I saw this blue one you might –"

    WO "John, are you ready?"

    scene f51 #I neu face cam head down
    with dissolve

    I "Who was that?"

    J "I have a meeting I need to get to. I'll talk to you later."

    I "But you don't have any meetings planned for today…"

    J "Look, I'm already late enough as it is. I will talk to you later, Irene. Bye."

    scene f52 #I neu look down at phone. f47 base
    with dissolve

    "*click*"

    "There's a heavy and awkward silence as Irene stares at her phone."

    P "(Should I say something here?)"

    scene f30
    with dissolve

    I "Okay! So I guess we're all good to go get rung up."

    I "I just need to run to the ladies room and I'll be right back to help you take everything off."

    scene f25
    with dissolve

    "She practically runs out before you can respond."

    P "(I have a feeling she doesn't need to use the bathroom at all.)"

    scene bs
    with dissolve

    "But you have no choice but to wait for her until she does return to help you remove the tuxedo."

    "You then purchase it and leave the store."

    scene f54 #I neu walking
    with dissolve

    "As you walk through the mall to leave, you can see the recent phone call with John really has effected her."

    P "(I'm used to her having a poker face, but it's not her usual one… Like, I can tell it's forced right now.)"

    P "(The party is right around the corner, and having a depressed Irene is not a good thing any way you look at it.)"

    "You think of how to cheer her up."

    scene f55 #I stop walking to face cam
    with dissolve

    P "Hey, Irene."

    I "Yes, is something wrong?"

    P "Nope. Just figured we could have a little fun before we left. There's an ice skating rink here. Wanna check it out?"

    scene f56 #I smile
    with dissolve

    I "I used to beg my parents to take me as a child, but never got the opportunity. *laugh*"

    scene f57 #I look away
    with dissolve

    I "But I… I think I'm a bit too old for such things now."

    P "Ohhh… I think I know what it is."

    scene f58 #I confused look at cam
    with dissolve

    P "You were just trying to be nice by saying you liked spending time with me."

    P "You're actually super embarrassed to be seen with me right now, aren't you? That really hurts, Irene."

    scene f58-2 #I gone. f56 base
    with dissolve

    I "*giggle* You're so silly. That couldn't be further from the truth."

    P "*smile* Well then, prove me wrong."

    I "I truly feel sorry for the girls your age. They don't stand a chance with that reverse psychology of yours."

    scene f59 #I look down at self
    with dissolve

    I "But I can't exactly go skating in this getup, can I?"

    P "*smile* Good thing we're in a mall filled with clothing shops."

    scene bs
    with dissolve

    "You follow Irene back to the store where you bought the tuxedos."

    "And wait for her to pick out her new outfit."

    scene f60 #I look at self. Embarrassed smile
    with dissolve

    I "How do I look…? It's been a while since I've worn casual clothes, to be honest."

    I "I can't tell if I look good or bad, or what."

    P "Irene, you look amazing. You could probably wear a trash bag and still turn heads."

    scene f61 #I look cam
    with dissolve

    I "*laugh* I'd definitely be turning heads if I wore a trash bag out, but I get what you're saying. Thank you, sweetie."

    I "But… I'm still a little hesitant to go skating. This will be my first time, and I run the risk of looking like a total buffoon."

    P "*laugh* Well, I've skated plenty of times, so I promise I won't let you look like one."

    scene f62 #cam put hand on I shoulder
    with dissolve

    P "Trust me, alright?"

    I "*nod* Okay, I'm in your hands, [p_name]."

    scene bs
    with dissolve

    "You and Irene head to the rink and rent the skates to take the ice."

    scene f63 #I freakout look at ice. Hold on to cam. Arms out
    with dissolve

    I "I don't know if this was such a good idea after all…"

    P "*smile* I think you're overthinking it, Irene. And you're way too tense. Try to –"

    scene f63-2 #I hug up to cam
    with dissolve
    I "I-I'm falling, [p_name]!"

    P "No, you're not, I got you. Just try and relax, okay?"

    scene f63-3 #diff angle
    with dissolve

    I "A-Are you sure, honey?"

    P "Yes."

    I "Super duper sure?"

    P "*smile* Yes, I'm super duper sure."

    scene f64 #I look at cam
    with dissolve

    "You separate from her again as Irene timidly looks up."

    P "*laugh*"

    I "Wh-What's so funny?"

    P "I'm just so used to you being in control."

    scene f65 #I pout
    with dissolve

    I "I hope you're enjoying this moment because I am so going to get you back."

    P "Haha. There's no need for threats. I'm not trying to make fun of you or anything, just the situation."

    P "But I'll make it up to you by turning you into an Olympic figure skater by the time we finish…"

    P "Or at least good enough to not fall on your butt every five seconds. Deal?"

    scene f66 #I smile
    with dissolve

    I "I guess that's a fair trade for me not totally getting you back."

    P "*laugh* Then let's start. The first thing were going to do is called 'gliding.' So just lift one leg at a time, almost like your marching."

    scene f67 #I worried look down. F63 base
    with dissolve

    I "Okay…"

    P "Ah, you shouldn't look down either. That's actually how some accidents happen because you're not looking where or who you might run into."

    scene f64
    with dissolve

    P "Perfect. Now let's try the gliding."

    scene f68 #Diff angle, I marching
    with dissolve

    "Irene does as instructed and starts picking up one leg after the other."

    "She's slow at first, but starts to pick up confidence."

    P "Not so bad, right?"

    scene f66
    with dissolve

    I "Actually, no, it's not."

    I "So, what's next, sensei?"

    P "*laugh* Next is the real deal, and not that much different from gliding. The only difference is extending your legs and leaning forward a bit."

    scene f69 #cam get side of I, hold hand. I worry look at cam
    with dissolve

    P "But let me get right on your side, so you don't depend on me too much."

    I "A-Are you really sure you should be letting me go by myself already, sweetie?"

    P "I'm holding your hand, don't worry. I got you. You have to pay attention to where you're going right now."

    scene f70 #I look forward surprised
    with dissolve

    I "Oh, right!"

    "Irene moves forward slowly, but consistently."

    P "Try to keep your balance more, Irene."

    scene f71 #cam grab waist from behind
    with dissolve

    "You get behind her."

    P "(She's slim and busty at the same time. I can't believe I'm just casually touching such a gorgeous woman like this.)"

    "But you try to keep your lewd thoughts to the side to focus on teaching her."

    scene f72 #diff angle
    with dissolve

    P "Think of a penguin and how it waddles, shifting your weight from one leg to the other as you move."

    "Your advice seems to help her."

    scene bs
    with dissolve

    "So you return to holding her hand, but you eventually let go as you two spend more time going over the basics."

    scene f73 #I skating. Cam directly in front skating backwards
    with dissolve

    P "I have to say, I'm pretty impressed, Irene. An hour ago you were like Bambi walking for the first time."

    P "And now you're a graceful gazelle gliding through the grassy fields of the safari."

    I "*laugh* That almost sounds like a backhanded compliment, but I'll take it. I did look pretty bad at first."

    scene f74 #I shift pose, mirror. Look down
    with dissolve

    I "And I would say you're way more impressive. You're skating backwards right now."

    P "You should see Leanne. That girl can skate circles around anyone."

    scene f75 #I surprised
    with dissolve

    I "Really? I don't mean to offend, but she just doesn't seem like the… energetic type from the brief interactions I've had with her."

    P "(Can't exactly blame Irene for thinking that way, but Leanne's finally getting her life back on track with dancing.)"

    P "And what type are you? It dawns on me that I really don't know that much about you."

    scene f73
    with dissolve

    I "Well, there's not really much to tell. What do you want to know?"

    P "You said you didn't grow up with the silver spoon when you were helping me with the tux. What did you mean by that?"

    I "It's not a very exciting story, but since you're asking…"

    scene f76 #cam move to side of I look at cam
    with dissolve

    "You move closer to hear."

    I "My parents were immigrants that came to this country with nothing but the clothes on their back when I was fourteen."

    P "(Oh wow, I wouldn't have guessed Irene was an immigrant.)"

    I "So, I grew up pretty poor and didn't know much English, which isn't exactly the best combination for public school."

    scene f77 #I look forward
    with dissolve

    I "They would say I stink and make fun of the same few pair of clothes I wore every week."

    I "Mocking my accent was another favorite game my schoolmates liked to play."

    "Your mouth hangs open, you not expecting to hear even more of what her childhood was like."

    scene f78 #I move hand and smile
    with dissolve

    I "I hated those kids, for making my life so hard. I even hated my parents for a while because it was their fault."

    I "But I soon realized I was being selfish and weak. It wasn't anybody's fault."

    scene f76
    with dissolve

    I "Excuse my language, but life is just a bitch sometimes. So I stopped crying and complaining to God to make everything better."

    I "And started learning how to make my own clothes, and getting rid of my accent."

    scene f79 #I hold out hands
    with dissolve

    I "And voilà. Now you have me as I am now. Non stinky and no accent."

    if Imf == True:
        "You stop skating, forcing her to."
        P "You know we weren't exactly fond of each other at first, but I respected your strength."

        scene f80 #I mouth open listening, stop skating
        with dissolve

        P "I don't know how many times I'd wake up in the morning to see you sleeping at a chair with your laptop open or a mountain of paperwork."

        P "Now I understand why. You had a rough life, and instead of giving in, you just worked hard. No tricks or shortcuts."

        P "So I honestly think you're incredible for that, Irene."

        "She stares at you for a moment as if she's trying to figure out a difficult math problem."

        scene f81 #I turn around, wipe tears
        with dissolve

        I "*laugh* You are a jerk, you know that? Making a girl cry."

        P "(She's actually crying? Never thought I'd see the day.)"

        P "*smile* I swear that wasn't my intention, but why did you turn around?"

        scene f82 #I look down, hands down
        with dissolve

        I "I promised myself long time ago that I would never let anyone see me cry. See me weak…"

        I "Because that's when people take advantage."

        P "I wouldn't do that, Irene. I promise."

        "…"

        scene f83 #I smile crying face cam. F80 base
        with dissolve

        I "There… are you happy?"

        P "*smile* I am."

        scene f84 #cam wipe away tears
        with dissolve

        "You wipe Irene's tears."

        P "Would it be weird of me to say that I like seeing you like this?"

        I "*laugh* It would be totally weird."

        scene f85 #cam lower hand
        with dissolve

        P "It's just because I feel like I'm seeing the real you. No poker face where I can't tell what in the world you're thinking."

        I "It took me years and years to perfect that face, and you shatter it in no time at all. You really are a jerk."

        scene f86 #I shy look away
        with dissolve

        I "But… you're not making fun of my crying like the kids at my school used to do, so I guess it's not a big deal…"
    else:
        "She stops skating, forcing you to."
    scene f87 #I poke cam chest. F85 base
    with dissolve

    "Irene pokes you in the chest."

    I "And what about you, huh? It's time for you to reveal your deepest secrets and be vulnerable."

    P "(I think the only thing Irene doesn't know about is the fact I'm still trying to develop games… But is it really smart to tell her everything?)"

    menu:

        "Tell her [IrenePath]":

            $ ipts = ipts + 1

            scene f88
            with dissolve

            P "*laugh* I guess that would only be fair, but you pretty much know everything about me already… Even that I used to develop video games as a hobby."

            I "Mhm. John did inform me of that."

            scene f89 #cam look away
            with dissolve

            "You rub the back of your head."

            P "Well, uh… It's not so past tense anymore."

            I "So… you're still working on them, despite his insistence that they are a distraction?"

            scene f90 #I neu. F85 base
            with dissolve

            P "(Shit. Maybe telling Irene WAS a mistake.)"

            P "Yeah…"

            scene f88
            with dissolve

            I "I think it's fine."

            P "S-Seriously?"

            I "*nod* I might've said different if this was just weeks ago… But after spending time with you… I don't know. I just have a different perspective on things."

            I "You should do what makes you happy. And it's only a hobby, right?"

            P "(I eventually do want to make it fulltime, but I don't think I should divulge that yet, especially with me not even knowing how to handle my [rel_f].)"

            P "Thanks for being cool about it, Irene."

            scene f92 #I cross arms
            with dissolve

            I "Mhm. Remember how nice I am the next time you decide to make me cry."

            P "Haha. You're really not going to let me forget about that any time soon, are you?"

            I "Nope… Though I might develop a slight case of amnesia if you buy me some of that delicious looking ice cream in the food court."

            P "Hahaha. I think I can make that happen."

            if Imf == True:
                scene f93 #I hug cam. Use base f44
                with dissolve

                P "Irene? Is this another random hug attack?"

                I "*laugh* Yes, but not so random."

                scene f94 #I put hand on side of cam face. Use bsse f41
                with dissolve

                I "I know you were trying to cheer me up by making me come skating."

                P "Ah… I guess I wasn't so subtle after all, was I?"

                I "*giggle* Not quite. But I really do appreciate it, honey. I'm not used to people helping me for no reason at all."

                P "(It's true that I didn't want a depressed Irene at the party, but I really am starting to care about her.)"

                P "Well, I'm really starting to care about you, Irene. It really does feel like I have a second mom now."

                scene f95 #I excited
                with dissolve

                I "Do you really mean that?"

                P "*smile* Of course. I don't just go around telling women they can be my mom. Not really into that kink."

                I "*laugh* You're so silly."

                scene f93
                with dissolve

                I "And you're also really sweet."

            jump U6secret

        "Don't tell her":

            P "*smile* You pretty much know my whole life story at this point. Even my dirty little secret, so nothing else to tell."

            scene f88
            with dissolve

            I "Hehe. I guess that's true."

            I "And thank you for forcing me to come skating. It was really fun, [p_name]."

            P "*smile* Anytime."

            jump U6secret

label U6secret:

    scene bs
    with dissolve

    "You and Irene spend a little more time skating before leaving."

    "And before you know it, the time for Buster Himen's party arrives."

    scene f96 #I smiling in hall
    with dissolve

    I "This is it, are you ready?"

    P "Even if I'm not, I damn sure won't let them know that."

    I "*laugh* Good answer."

    if Imf == True:
        scene f97 #I walk up to cam
        with dissolve

        "Irene walks up to you and puts both her hands on your chest."

        I "But you're going to be fine, honey. You know what you're doing."

        P "(Hearing her say that does give me a little confidence boost.)"

    scene bs
    with dissolve

    "You and Irene spend time mingling with the other partygoers, and you do your best to act like the CEO of the company."

    scene f98 #I turn to cam, but not looking at him
    with dissolve

    I "Oh god."

    P "What's wrong?"

    I "I stupidly made eye contact with Phil Lowry and now he's on his way over here."

    P "(I understand Irene's hesitation if even one percent of what she says about him and his sexual harassing ways is true.)"

    scene f100 #PL close, look at I
    with dissolve

    PL "Hello there, Irene. I must say, you are looking absolutely delicious this evening."

    "The hungry look in the man's eyes makes you want to punch him."

    I "Thank you."

    scene f101 #I turn to cam
    with dissolve

    I "*whisper* Can we please go? I already feel warts forming from being around this overgrown toad."

    P "*whisper* No kidding. I'm not even who he's directing his attention at, and I feel violated."

    scene f102 #PL look at cam
    with dissolve

    PL "And who might this… boy be? An intern of yours?"

    scene f100
    with dissolve

    I "Try CEO."

    PL "Hahaha! I didn't know you were trying your hand in comedy, Irene."

    PL "If this child is the CEO of the Perving Company, that would make him your husband."

    PL "Or is it the babysitting business you're actually trying your hand at. Hahaha!"

    menu:

        "Tell him off":
            $ ipts = ipts + 1
            scene f102
            with dissolve

            P "That's pretty funny, Mr. Lowry. Almost as funny as the drop in your company's stock last quarter."

            scene f103 #PL surprised. I smile at cam
            with dissolve

            P "And it is definitely funnier than the lawsuit you're going through involving tax fraud."

            scene f104 #PL angry
            with dissolve

            PL "…"

            scene f105 #I grab cam arm. Cam focus on her
            with dissolve

            I "Honey, I think it's time we say hello to the host."

            P "*smile* Me too."

            scene bs
            with dissolve

            "You can practically feel the heat pouring off Phil Lowry as you stroll past him."

            jump U6kiss

        "Kiss Irene [IrenePath]":
            $ Ikiss = True

            P "*smile* Well, I do admit I'm young, but there's not much I can do about that."

            scene f106 #I surprise close to cam. PL neu
            with dissolve

            "You pull Irene close."

            P "What I can do, however, is prove just how much we love each other."

            scene f107 #cam kiss surprised I
            with dissolve

            "You kiss Irene and feel her tense up in surprise."

            P "(Maybe… this wasn't the best idea?)"

            scene f108 #I close eyes and kiss
            with dissolve

            "Irene kisses you back after a moment."

            "And you want that moment of feeling her moist and soft lips to last forever, but realize you need to pull away."

            scene f109 #I hugged up to cam. I look at PL
            with dissolve

            I "As you see, my husband can be quite bold when challenged."

            I "But if you'll excuse us, we need to greet the host of the party."

            scene bs
            with dissolve
            "You leave a speechless Phil Lowry and make your way to Buster Himen."

            jump U6kiss

label U6kiss:

    scene f110 #BH hands out. With drink
    with dissolve

    BH "Ah, so you did end up coming. Welcome, my esteemed guests of the Perving Company."

    "You and Irene greet him."

    I "As much as we would like to stay and mingle, we really did come here on behalf of business."

    scene f111 #BH hands down. Look at cam
    with dissolve

    BH "Man, she really doesn't waste any time, does she?"

    P "*smile* No, she doesn't."

    scene f112 #BH look at I
    with dissolve

    "So you all begin discussing the potential of the two companies working together, with Irene letting you take the lead."

    scene f111
    with dissolve

    BH "I was still a bit on the fence after our initial meeting, but you've convinced me, kid. I'm on board. *laugh*"

    P "(Yes! Now I don't have to worry about being shipped home early.)"

    BH "Now all you need to do is convince my partner."

    P "Partner?"

    scene f112
    with dissolve

    I "What are you talking about? Are you not the sole owner of your company?"

    BH "I was until recently when I sold a percentage to my longtime colleague, Carl Morrison."

    scene f113 #I head down look away towards cam
    with dissolve

    I "You've gotta be kidding me. *mutter*"

    P "(I don't blame Irene for getting annoyed. He should have mentioned this crap from the beginning.)"

    P "Can you not convince your partner that it would be in his benefit to work with us?"

    scene f111
    with dissolve

    BH "Carl is what you would call 'old school.' He likes to hear what's what from the horse's mouth."

    "You hold back a sigh."

    P "So where can we speak to Mr. Morrison? Is he here tonight?"

    BH "That would be quite the surprise, considering I haven't talked to him in months."

    scene f112
    with dissolve

    I "Excuse me?"

    P "(This just keeps getting better and better.)"

    BH "Carl is a rolling stone, always traveling, and getting up to God knows what. And you can never reach the man. I can give you his current location, though."

    scene f111
    with dissolve

    BH "That way you can go find him, or you can always wait for him to come back."

    BH "And before you ask, no. I have no idea when he's coming back. Sometimes it takes weeks, or months."

    scene f110
    with dissolve

    BH "So, what'll it be folks?"

    "There's no question in your mind on what needs to be done."

    scene f114 #I turn to cam
    with dissolve

    "And by the hard gaze Irene is giving you, she's on the same page."

    P "(I'm going to get that contract. No matter what I have to do.)"

    scene bs
    with dissolve

    "You spend a little more time talking to Buster Himen to figure out where exactly you'll be going."

    scene f115 #f96 base. I neu
    with dissolve

    P "Well, that didn't go exactly as planned, did it? Now we have to fly to another country just to convince someone else."

    I "It certainly is an annoyance, but things like this aren't uncommon in our line of work."

    P "I get that, but if we find out there's ANOTHER partner, I'm stabbing Buster Himen with the nearest sharp object."

    scene f96
    with dissolve

    I "*giggle* That might be slightly bad for business… but I might hand you a pen or something anyway."

    P "See? We're turning out to be such good partners. That is the definition of teamwork."

    I "Heh. I guess we do make quite the duo."

    scene f116 #I face bathroom, hand up
    with dissolve

    I "Now that we know our objective, we can leave. But I just need to use the restroom. Would you mind waiting for me, honey?"

    P "Nah, take your time. I won't leave without you."

    I "*laugh* What a gentleman. Thank you for not abandoning me."

    scene bs
    with dissolve

    "You post up to wait."

    "*MEANWHILE*"

    scene f117 #I washing hands in bathroom
    with dissolve

    I "(Like [p_name] said, today didn't go as planned… but it wasn't the worst thing in the world.)"

    I "(We'll be spending more time together.)"

    I "*laugh* You're like a schoolgirl, Irene. Looking forward to spending time with a boy."

    WW "What's so funny? I want to laugh."

    scene f118 #I angry facing PL 3rd Stand straight
    with dissolve

    I "What in the hell are you doing in the women's bathroom? You need to leave RIGHT NOW."

    PL "Why all the hostility? I just came to check on you."

    scene f119 #I neu
    with dissolve

    I "…"

    I "I'm fine as you can see. Please leave."

    PL "You know, I've been really patient over the past year, but how long are we going to play this game?"

    scene f120 #I Arms crossed
    with dissolve

    I "I have no clue what you're talking about."

    PL "It's clear I'm attracted to you, so how much is it going to cost me? You know money's no object. Just name the price."

    scene f120-2 #I surprised f119 base
    with dissolve

    I "What…?"

    scene f121 #I smile
    with dissolve

    I "*laugh* I admit your boldness is commendable, but I wouldn't sleep with you, even if it meant saving my own life."

    scene f122 #I neu walk past PL. PL turn to her mad
    with dissolve

    I "Now if you'll excuse me –"

    PL "You conceited bitch…!"

    scene f123 #PL pushing I against wall
    with dissolve

    I "Wh-What do you think you're doing?! Let me go or I'll scream!"

    scene f124 #PL cover I mouth
    with dissolve

    "Irene carries through with her threat, but her screams are muffled."

    PL "Did you really think I'd let you do that? You're pretty, but boy are you stupid. You should have called for help the second I stepped in here."

    I "([p_name]…! Save me!)"

    scene bs
    with dissolve

    "*BACK TO PRESENT*"

    scene f125 #cam in empty hall look at floor
    with dissolve

    P "(Wonder how long Irene's going to take? Might as well play some games on my phone in the meantime.)"

    "You hear a 'bang' as you go to retrieve your phone."

    scene f126 #cam in direction of bathroom
    with dissolve

    P "(Did I just hear something come from the bathrooms?)"

    "You strain your ears to hear for more."

    "..."

    P "(Guess it was nothing.)"

    scene f125
    with dissolve

    "You go to take your phone again, but pause."

    scene f126
    with dissolve

    P "(I'm probably being silly, but let me just go check and see if Irene's okay.)"

    scene f127 #cam knock on bathroom
    with dissolve

    P "Hey, Irene. Sorry to be a creeper, but I just wanted to see –"

    "*BANG*"

    scene f128 #cam hand down
    with dissolve

    P "*mutter* What the hell…?"

    P "Irene??? Are you okay???"

    "…"

    P "I'm coming in!"

    scene f129 #cam see PL pressing I to wall. PL guilty look at cam. I terrified
    with dissolve

    "At seeing what's going on, a fire lights inside you."

    scene f130 #closeup I eyes. PL face cam
    with dissolve
    PL "H-Hey, its not what you think. I swear. She told me she likes it rough."
    "Seeing the pure fear on Irene's face, you rush forward."

    P "...YOU MOTHERFUCKER!!!"


    scene f131 #cam punch PL
    with dissolve

    "And smash your fist into his face."

    scene f132 #PL knocked out
    with dissolve

    "Instantly knocking him out cold."

    "But that isn't enough for you, so you start for him again."

    I "[p_name]!"

    scene f133 #I covering face burried in cam chest
    with dissolve

    I "I-I was so scared."

    "She starts crying harder and shaking as you wrap your arms around her."

    scene f133-2 #cam arms around I
    with dissolve

    P "It's okay, Irene... I'm here and I'm not going to let anything happen to you. I promise."

    P "(I can't believe that fucker was really going to try and rape her or something!)"

    P "We need to call the police and let them know what –"

    scene f134 #I look at cam
    with dissolve

    I "N-No, please… I just want to go back to the hotel."

    P "(Is that really the best thing to do? We should report this piece of shit.)"

    I "P-Please, [p_name]…"

    P "*smile* Okay, Irene… We'll just go back before deciding anything."

    "Her phone starts ringing."

    scene f135 #I look at it
    with dissolve

    I "I-It's John… I don't think I can talk right now…"

    "She starts shaking more as fresh tears come down."

    scene f136 #I look at cam
    with dissolve

    P "It's okay. We'll let him know everything that happened back at the hotel."

    "Irene timidly nods, but she's shaking so much that she accidentally answers the phone."

    scene f135
    with dissolve

    J "Hello?"

    "…"

    J "Irene, what the hell are you doing? Answer me."

    "You think about what to do with a frozen Irene."

    scene f137 #cam reach the phone
    with dissolve

    "And decide to answer yourself."

    scene f138 #I holding self, looking at floor
    with dissolve

    P "Hey…"

    J "Why are you answering the phone? Where is Irene?"

    P "We're at the party for Buster Himen and she just got attacked in the bathroom by some guy."

    J "What? Is she hurt?"

    scene f132
    with dissolve

    P "No… I stopped it before anything could happen."

    J "Good."

    J "Were you able to secure the contract?"

    scene f139 #cam look to side
    with dissolve

    P "What?"

    J "You know I don't like repeating myself, boy. I asked if you were able to secure the Himen contract."

    P "The con… the contract? I just said your wife was ATTACKED."

    J "And you said she wasn't physically hurt, correct? She'll be fine. Just file a police report."

    "There's another surge of anger inside you."

    scene f132
    with dissolve

    P "You're almost as bad as that piece of shit that attacked her! You don't even give a fuck about her! All you care about is your shitty company!"

    J "..."

    J "I appreciate seeing some fire in you, boy. But if you EVER grow enough balls to direct it at me again, I'll –"

    "You hang up."

    scene f138
    with dissolve

    P "(I don't have time for that asshole. I'm worried about Irene right now.)"

    "The phone starts ringing again, but you ignore it and start trying to reassure Irene everything is going to be okay."

    scene bs
    with dissolve

    "You then take her back to the hotel as promised and she seems to regain a little life along the way."

    scene f140 #I sad cross arms look down hotel hall
    with dissolve

    I "Thank you for walking me all the way up, [p_name]… And obviously for saving me."

    I "I really don't know would have happened if you didn't come."

    P "*smile* The good thing is that we'll never have to find out, right?"

    scene f141 #I smile at cam
    with dissolve

    I "You're exactly right."

    menu:

        "Offer to come inside [IrenePath]":

            $ ipts = ipts + 2

            P "Listen… I know you might not want to be bothered right now, and be left to your own thoughts…"

            P "But it would really make me feel better if I stayed with you tonight. I can just crash on the floor."

            I "You wouldn't be bothering me in the slightest…"

            scene f142 #I look down
            with dissolve

            I "Actually, I would really like if you stayed with me tonight. I'm just not used to relying on others so much…"

            scene f141
            with dissolve

            I "But I just feel safe with you around… And comfortable."

            if Imf == True:

               P "Well yeah, I have seen you cry after all."

               I "*laugh* That is very true. My dignity is basically non-existent around you at this point."

            I "And also, you have another thing coming if you think I'm going to let you sleep on the floor, mister."

            jump U6hotel

        "Leave":

            P "Okay, so make sure to call me if you need anything at all, alright? I'll make sure to keep my phone near me."

            scene f140
            with dissolve

            I "Oh…"

            scene f141
            with dissolve

            I "Right, of course. Thank you again for everything tonight, honey."

            scene bs
            with dissolve

            "And with that, you leave and return home to the girls' house."

            jump U7

label U6hotel:

    scene bs
    with dissolve

    "Irene changes into her night clothes, while you strip to your shirt and boxers, and you two settle into bed, despite you offering to sleep on the floor again."

    scene f143 #cam face I back
    with dissolve

    P "Now that I see how comfy this bed is, I'm kind of glad you forced me to sleep with you. *laugh*"

    P "You know how people always take things like soap and towels from hotel rooms? You think they'd notice a missing bed?"

    "…"

    P "Irene?"

    scene f144 #I crying looking up at celling
    with dissolve

    I "*sniff* John doesn't give a fuck about me, does he? I heard everything he said in the bathroom."

    I "And it's total bullshit that he had a meeting when we heard that woman's voice on his phone earlier today."

    scene f145 #I wipe tears
    with dissolve

    "Irene tries to wipe her flowing tears, but they just keep on coming, like a broken dam."

    I "I tried to convince myself that he would change back into the man I first met, but I realize now that man never existed."

    scene f144
    with dissolve

    I "From the start, he would only use me to handle business for him and did the bare minimum to keep me around."

    I "I truly see that now after everything that's happened."

    scene f146 #I look at cam, smile
    with dissolve

    I "But I've also realized how amazing of a man you are. Everything I was wishing John to be."

    I "Kind, thoughtful and most certainly courageous."

    scene f147 #I put hand on cam face
    with dissolve

    I "You know, you were the first person I thought about when I got attacked. You were the one I mentally called out to."

    I "And you came. You saved me."

    "Irene starts stroking your face."

    I "My knight in shining armor."

    scene f148 #I kisses you
    with dissolve

    "Your eyes shoot open at the unexpected kiss."

    P "(Is this really happening right now???)"

    scene f149 #I surprised
    with dissolve

    "And Irene expression matches yours after a moment."

    scene f150 #I sit up
    with dissolve

    I "Oh my god, honey! I'm so sorry. I shouldn't have done that."

    scene f151 #cam sit up
    with dissolve

    P "It's okay…"

    scene f152 #Hands cover face
    with dissolve

    I "*laugh* No, it's not. You offer to stay with me because I got attacked, and now I'm attacking you."

    I "We've just been getting along so well, and I'm not used to being treated like a human being instead of a piece of ass."

    I "And after you saved me… *shake head*"

    scene f153 #I sad at cam
    with dissolve

    I "Is it possible for you to forgive me, [p_name]? I promise I'll never do anything like that again."

    I "I know we've only just started our relationship, but it really scares me to think about losing it now."

    I "I… I love you, sweetie. I really do."

    menu:

        "It's fine":

            P "*smile* Don't worry about it at all, Irene. We can just forget about what just happened."

            P "Wait, what are we talking about again?"

            scene f156
            with dissolve

            I "*laugh* Thank you, [p_name]…"

            scene bs
            with dissolve

            "You hang out with Irene a little the next morning before returning home to the girls' house."

            jump U7

        "You love her too [IrenePath]":

            $ iroute = True

            $ ipts = ipts + 3
            label galleryScene6:
            P "*smile* There's nothing to forgive because I love you too, Irene… "

            scene f154 #I surprised
            with dissolve


            I "Nothing to forgive… So you mean… You love me as a... woman?"

            P "Yes. I really do."

            P "(All this time we've been spending together like she said has made me realize how much I do care about this woman.)"

            P "(And after she was attacked tonight, all I want to do is hold and protect her…)"

            scene f155 #I smile look forward
            with dissolve

            I "I know that I should be objecting to that type of relationship after just trying to basically be your mother…"

            scene f156 #I smile at cam
            with dissolve

            I "But thinking about you being my man… It makes me happy."

            I "So… will you make me your woman, [p_name]? Right now?"

            P "(Oh... Oh! She's asking me to…)"

            scene f157 #cam kissing I
            with dissolve

            "You respond by pushing your lips against hers and she eagerly responds, and presses her Double D tits into you."

            P "(They're so damn big. I need to touch them.)"

            scene f158 #MC on top, grab tits
            with dissolve

            "You gently push Irene down and grab a handful of her chest while rubbing her curvy thigh with your free hand."

            I "Mmmmm."

            "She moans into your mouth as you continue to kiss."

            scene f159 #closeup of boob playing
            with dissolve

            "And you start playing with her boob by squeezing and feeling its firmness, molding it to your touch."

            scene f160 #closeup of crotches
            with dissolve

            "Irene pushes her hot crotch into yours as you do and your hard-on presses into her soft pussy, with only your clothes separating direct contact."

            P "(We're both wearing shorts and I can still feel how hot her pussy is.)"

            scene f159
            with dissolve

            "You refocus on her magnificent tits and bring up your other hand to play with both by squeezing and kneading them."

            "Irene's nipples get even harder as you do, letting you know you're doing the right thing."

            scene f161 #I rub MC package. F158 base
            with dissolve

            "But she abruptly breaks off your kiss and starts rubbing your dick."

            I "[p_name], I can't wait anymore… I want your hard cock inside me."

            P "(Irene doesn't seem like the shy type when it comes to sex, so I'm not surprised by her forwardness.)"

            scene f162 #closeup I face
            with dissolve

            P "(But she also has a really sweet side. Let's see how she reacts to me taking the lead.)"

            P "Yeah? You want my hard cock? How bad?"

            scene f163 #I bite lip
            with dissolve

            I "Really, really bad. Or I think I might go crazy…"

            "She never stops rubbing you while you talk."

            P "*smile* We wouldn't want that, now would we?"

            scene bs
            with dissolve

            "You two quickly undress and get in position."

            scene f164 #missionary 3rd
            with dissolve

            "And you waste no time by slowly pushing your big dick into Irene's wet, hot pussy."

            I "Oh… oh my god…"

            "She wraps her legs and arms around you tighter."

            scene f163
            with dissolve

            I "I didn't expect you to be so big, honey…"

            P "And I didn't expect your pussy to be so damn tight. It's like it doesn't want to let me go."

            P "*smile* But don't worry. We'll take it slow."

            scene f164
            with dissolve

            "You start fucking Irene and make sure to keep your strokes slow and even as you shove yourself into her."

            "Easily separating her mushy insides before taking yourself out again, though her pussy's grip makes it a challenge."

            P "Your pussy really does love me, doesn't it?"

            scene f164-2 #diff angle
            with dissolve

            I "*moan* Yes, honey… Please don't stop for anything."

            "So you don't stop. You keep burying your swollen cock into her over and over."

            "And it gets easier to move inside as her pussy becomes even wetter."

            scene f164-3 #whisper in ear
            with dissolve

            I "So this is what a real man feels like…?"

            "Irene's hot breath hits your ear as she moans into it."

            I "You're so much better, [p_name]… You're twice the man he could ever be..."

            "It's clear who Irene is referring to, which makes your erection even bigger."

            scene f163
            with dissolve

            "Irene moves to look at your face."

            I "Yes… My big, strong man… I love you inside me so much. I don't ever want this to stop."

            P "And it won't. Because your pussy belongs to me now."

            scene f164-2
            with dissolve

            I "*moan* Yes… It's all yours, as long as you promise to always love me."

            "For the next several minutes, you fuck Irene, still making sure to go slow, which helps you in lasting."

            "But only for so long."

            P "*grit teeth* I'm about to cum, Irene!"

            scene f167
            with dissolve

            I "Please cum inside me, [p_name]!"

            "With her legs holding your hips down, you have no choice in the matter and blast your load deep inside her pussy."

            scene f168 #I pussy creampie. Cam dick still close
            with dissolve

            I "Mmmm. There's so much. *laugh*"

            P "*smile* The fact that you're so nonchalant about me cumming inside means you're on birth control."

            I "You shouldn't assume, you know. I'm not on anything."

            scene f168-2 #I face
            with dissolve

            P "WHAT?"

            I "Come here, I want to cuddle with my man."

            scene f169 #I face . base f149
            with dissolve

            "You're still trying to register the fact that Irene isn't on any contraception, and you just came inside of her."

            I "You don't have to worry, you won't be a dad any time soon. I've never been able to get pregnant."

            I "My eggs just aren't suitable for a million and one reasons a slew of doctors have explained to me."

            P "(So that's why she wasn't worried.)"

            scene f170 #I close eyes and head on chest
            with dissolve

            "Irene puts her head on your chest."

            P "I'm really sorry, Irene. That seriously sucks."

            I "It's okay. I made peace with it a long time ago."

            scene f169
            with dissolve

            I "You're… okay with the fact that I can't have children, right?"

            P "*smile* Of course. There's always adoption and all that. YOU are what I care about."

            I "…"

            scene f170
            with dissolve


            "Irene buries her head back in your chest."

            I "Okay…"

            "..."

            I "[p_name]?"

            P "Yeah?"

            I "I love you. I really do."

            P "*laugh* And I love you even more."

            scene bs
            with dissolve

            "The night passes and you slowly open your eyes when morning comes."

            scene f171 #I smi at cam
            with dissolve

            "To see Irene staring at you."

            P "Irene?"

            scene f172 #I look away
            with dissolve

            I "Well, this is embarrassing... You caught me watching you sleep like a total creeper."

            P "Not total, just a slight one. And I do understand I'm easy on the eyes, so it's not your fault."

            scene f171
            with dissolve

            I "*giggle* I’m glad to have such an understanding man."

            "Her declaration of you being her 'man' makes you think about the current situation."

            P "Hey, can I ask you something?"

            I "Mhm. Anything."

            scene f173 #cam look down at her body
            with dissolve

            "You look away."

            P "(Damn is she sexy... Seriously...)"

            P "(No, focus, [p_name].)"

            scene f171
            with dissolve

            P "Last night… do you regret it at all?"

            I "I do understand all of this is a bit sudden, but you saving me just made everything click in my head."

            scene f174
            with dissolve

            I "It made me realize John's true nature. Even back when you told me about the contract he forced on you."

            scene f171
            with dissolve

            I "And I’m the kind of person that is all in when I see something good. And you’re good, [p_name]. I don’t need months or years to figure that out."

            I "Even by just watching your interactions with Norah or the other girls shows how much they love the man you are."

            I "And I love that man, too."

            scene f174 #I worry look down
            with dissolve

            I "But I understand not everyone is as impulsive as me, and I did kind of throw myself at you."

            I "Are you… having second thoughts?"

            P "Irene, look at me."

            scene f175 #I neu mouth open
            with dissolve

            P "Having sex with you is something I’ll NEVER regret."

            P "*smile* And you’re not too bad to hang around either."

            scene f171
            with dissolve

            I "*giggle* Well, I'm glad you can tolerate my personality."

            P "The things I do for love, right?"
            $renpy.end_replay()
            scene bs
            with dissolve

            "You and Irene have breakfast, and you hang around a bit before going home."

            jump U7
