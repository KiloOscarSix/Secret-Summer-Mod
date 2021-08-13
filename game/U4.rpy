label U4:

    "After your all night gaming session with Coral, you’re suddenly woken up hours later when your door bursts open."

    WO "[p_name]! Wake up, [p_name]!"

    P "Hmm, just five more minutes… *mutter*"

    WO "You can sleep later, silly! This is way more important!"

    "You grunt and are finally able to crack your eyes open after a short while."

    scene d1 #cam on C excited in panties
    with dissolve
    #play music "CTS2 - Upbeat-Pop-Theme.mp3"

    P "(Coral? And she’s in her underwear…)"

    P "*yawn* You don’t seem to be on fire, so what’s the emergency?"

    C "I got an email from Immortal Fighting!"

    scene d2 #cam sit up
    with dissolve

    "You sit up a bit more."

    P "Seriously? What’d it say?"

    C "Come on, I’ll show you!"

    P "*laugh* (Her excitement is contagious.)"

    P "Alright, you got my full attention."

    "And even though you try not to show it, her lack of pants has your attention too."

    P "(I guarantee she ran in here all excited without even realizing what she was wearing. Or rather not wearing.)"

    menu:

        "Tease her a little [CoralPath]":

            $ Cpanties = True

            P "You know, Coral, you didn’t have to go all out to get me to wake up. A simple shake would have done the trick."

            scene d3 #C neu
            with dissolve

            C "Am I supposed to know what you’re talking about? Because I’m totally lost."

            P "*smile* I’m just saying, white is my favorite color, and you already know that, so I appreciate you going the extra mile."

            scene d4 #C frown
            with dissolve

            C "Can you stop speaking crazy, and speak norm…"

            scene d4-2 #C eyes go wide
            with dissolve

            P "(Haha. I think she finally noticed.)"

            scene d5 #C looks down at panties
            with dissolve

            P "(Yep, she definitely noticed, alright.)"

            scene d6 #C embarrassed
            with dissolve

            C "*blush* D-Do you think I’m going to react like some anime character and frantically run out of the room while calling you a 'baka'?"

            P "(No matter the situation, Coral refuses to look like the one on the losing side, like the time she insisted she ate a cup of wasabi on purpose, thinking it was an appetizer.)"

            P "*smirk* So, you’re saying you’re not even a little embarrassed?"

            C "Th-That's right, what’s the big deal? You’re my [rel_b] and have probably seen me in my underwear before anyway."

            P "(I haven’t since you really started to fill out, and damn do you look good.)"

            C "So just hurry up and come to my room."

            scene d8 #C walk out of room
            with dissolve

            "Coral doesn't wait for your response and walks away, though you can see her steps are quicker than usual."

            P "(Haha. I couldn't help but tease her a little… And I did want to sleep in a bit more, but can’t complain about what I woke up to.)"

            jump U4PAN

        "Don’t say anything":

            scene d9 #C run away
            with dissolve

            C "Okay, hurry, [p_name]! I’ll be waiting for you!"

            jump U4PAN

label U4PAN:

    scene bs
    with dissolve
    stop music
    "You throw on some clothes and head to Coral's room."

    scene a127 #cam at C door
    with dissolve
    #play music "CTS2 - Upbeat-Pop-Theme.mp3"

    P "Coral, I’m here. Can I come in?"

    C "Of course, slowpoke! Come on!"

    P "*laugh* Okay."

    scene d10 #cam walk to C looking at him on couch
    with dissolve

    C "I’m so excited!"

    P "*smile* Really? I couldn’t tell by the way you practically dragged me out of bed."

    scene d11 #cam closer
    with dissolve

    C "Hehe, sorry. I did stop myself from waking you up a couple of hours ago, so I should definitely get some brownie points for that."

    P "Ha, in that case, absolutely. Thank you. I think I really did need those extra two hours."

    scene d12 #cam sit on couch look at C exc
    with dissolve

    C "Good thing I waited, then. But now it’s time to get down to business!"

    if Cpanties == True:

        P "(Coral is really still in her panties, but she’s either pretending not to be embarrassed anymore or totally forgot.)"

        P "(I sure as hell am not going to spoil the moment by saying anything though. Just sit back and enjoy. Hehe.)"

    else:

        P "(I think Coral still doesn't realize she's in her underwear.)"

        P "(I sure as hell am not going to spoil the moment by saying anything though. Just sit back and enjoy. Hehe.)"

    P "*smile* Right, so what does the email say?"

    scene d13 #C look down at laptop
    with dissolve

    C "Ummm, it says…"

    C "'Congratulations on reaching the top 1,000 players,' and blah blah blah…."

    "Coral’s eyes quickly scan the email."

    scene d14 #C exc
    with dissolve

    C "Okay, here’s the good part!"

    C "'To commemorate your ranking, we are gifting you a secret prize that you can go claim by solving the following...'"

    C "'I am not alive, but bring to life, love, laughter, beauty, and strife. Though I don't speak, I never fail to captivate you with a tale.'"

    P "So we have to figure out this riddle and go to wherever the answer is?"

    scene d15 #C neu look at cam
    with dissolve

    C "Yep. I tried to figure it out, but I got a big fat goose egg so far. I even searched on Moogle."

    P "*smile* You are such a cheater."

    scene d15-2 #C smi look at cam
    with dissolve

    C "Hey, there’s no rules in love and video games."

    P "Haha, I'm pretty sure it’s love and war, but I don’t blame you anyway."

    P "How do you know your answers are wrong, though?"

    scene d15
    with dissolve

    C "There’s a site they provide where you can type the answer, but it keeps telling me I'm wrong."

    P "Hmm…"

    P "Can you please read the riddle one more time?"

    C "Sure."

    scene d13
    with dissolve

    C "I am not alive, but bring to life, love, laughter, beauty, and strife. Though I don't speak, I never fail to captivate you with a tale."

    scene d15
    with dissolve

    C "Any clue what it could be?"

    P "(Ehh… might as well take a stab at it.)"

    menu:

        "Song":

            P "Maybe it’s a song? A song can bring laughter and love, and often times does have a story, so that's it for the tale part."

            scene d12
            with dissolve

            C "Ohhh, you’re right! That has to be the answer."

            scene d14
            with dissolve

            C "Okay, let’s type in 'song.'"

            scene d16 #C frown
            with dissolve

            C "Ugh, that’s not the answer either…"

            P "Shit, my bad."

            scene d15-2
            with dissolve

            C "Nah, that was better than any of the answers I had."

            P "*smile* Thanks."

            jump CH4RID

        "A joke":

            P "How about a joke?"

            C "Do you really think now is the best time? We need to focus on solving the riddle."

            P "*laugh* I mean that maybe the answer is a joke."

            P "Think about it, it can make you laugh, obviously, and have a tale, and some jokes have strife and a bunch of other stuff."

            P "(Not really sure about the part that says it doesn't talk, but can a joke technically talk…? Worth a guess anyway.)"

            scene d12
            with dissolve

            C "Ohhh, you’re right! That has to be the answer."

            scene d14
            with dissolve

            C "Okay, let’s type in 'joke.'"

            scene d16
            with dissolve

            C "Ugh, no dice. That’s not the answer either…"

            P "Shit, my bad. Some parts of the riddle didn’t fit correctly for it."

            scene d15-2
            with dissolve

            C "Nah, that was better than any of the answers I had."

            P "*smile* Thanks."

            jump CH4RID

label CH4RID:

    scene bs
    with dissolve
    stop music
    "You and Coral spend the next few hours trying to solve the riddle, but the result is the same."

    scene d17 #C sleeping in cam lap
    with dissolve

    P "(Huh…? Why is Coral laying on my lap?)"

    P "*yawn* (Oh, must have fallen asleep. Guess we still needed a bit of rest after that all-nighter, and then racking our brains for the riddle answer.)"

    P "*smile* (I have to say though, she looks so cute just sleeping like that.)"

    "Seconds go by as you watch your little [rel_s], and other thoughts soon enter your mind.)"

    scene d18 #cam on C body
    with dissolve
    #play music "SEN - Hip-Hop-Jazz-Groove.mp3"

    P "(I wonder how it would feel to just… touch?)"

    menu:

        "Touch her":

            scene d19 #cam hand reach out to touch
            with dissolve

            P "(I only want to see how it feels for two seconds, that’s it.)"

            jump CH4DREAM

        "Don’t do anything":

            P "(Even though I am BEYOND tempted, I don’t want to cop a feel while she’s innocently sleeping.)"

            jump CH4DREAM

label CH4DREAM:

    scene d20 #C turn face up
    with dissolve

    C "Mmmm, no…"

    P "(Huh?)"

    C "I know… I do too… *mutter*"

    P "*smile* (And here I thought I was the only one who sleep talked.)"

    scene d21 #C touch boobs
    with dissolve

    C "*moan* You know… I can’t resist when… you touch me like that… *mutter*"

    P "(Uh, what?)"

    C "Uhhnn, wait… The others are home…"

    P "(Is Coral legit having a sex dream? Right on my LAP? I don’t know whether this is the biggest gift or curse.)"

    scene d22 #C smile
    with dissolve

    C "Do you really… want to do it that bad…?"

    C "*giggle* Okay, okay… you don’t have to stare like… a dog begging for a bone… *mutter*"

    scene d23 #C touch puss
    with dissolve

    C "Mmm… *moan*"

    C "You’re… inside me… again…"

    scene d25 #different angle C masturbate
    with dissolve

    "As if you’re hypnotized, all you can do is watch your younger [rel_s] play with her pussy."

    "Coral rubs her lips in a slow circle before plunging her fingers back into her little hole over and over again."

    "With her panties on, the juices leaking out of her can easily be seen."

    scene d26 #different angle C masturbate 2
    with dissolve

    C "Oh my god… *moan*"

    "Coral starts fingerfucking herself even faster as her moans get louder, pushing her fingers deep into the thin cloth. A part of you is concerned Zoe or your [rel_m] might hear, but you can’t take your eyes off Coral."

    C "Yes… yes…! *moan*"

    C "You can do it inside... I do want to have your baby…"

    scene d27 #C bites lip and cum close up face
    with dissolve

    "A visible tremor makes Coral shake from head to toe as an orgasm hits."

    P "Wow…"

    "You can’t stop yourself from saying out loud."

    scene d28 #C eyes open a bit
    with dissolve

    "But your voice wakes her up."

    "Your brain shoots warning signals, but all you can do again is watch her."

    scene d29 #C smile
    with dissolve

    C "Mmm, hey, you perv."

    P "(What??? So she knows I was watching her the whole time?!)"

    P "H-Hi?"

    C "*giggle* Why are you acting all shy…"

    scene d30 #C eyes open wide
    with dissolve

    "Coral blinks a few times before her eyes go wide."

    C "[p_name]…?"

    P "Uh, yeah. It’s me."

    scene d31 #C sit up and stare
    with dissolve
    stop music
    C "Y-You’re real, right?"

    P "*laugh* Yeah, I think so. Are you… okay?"

    scene d32 #C nerv look away
    with dissolve

    C "O-Of course."

    C "I guess we fell asleep there, huh? All that riddle stuff after our gaming session really took it out of us."

    scene d33 #C looks down at panties
    with dissolve

    "Coral looks down at herself."

    C "Oh my god! *mutter*"

    scene d32
    with dissolve

    C "A-Anyway! I need to go to the bathroom…"

    P "(I have no doubt you do. I didn't even know women could get so wet. It’s like there was a rainstorm in her panties.)"

    P "*smile* To change or something? Did you wet yourself like when we were younger? Thought you got over that."

    C "*blush* R-Right now is not the time for jokes! Just try and figure out the riddle while I’m gone!"

    scene d34 #C running away ***Add stain
    with dissolve

    "Coral makes her mad escape, but you catch a glimpse of dark stains on her underwear."
    $ renpy.end_replay()
    scene d35 #C gone
    with dissolve

    P "(That was definitely an interesting event. Coral was really having a sex dream right on my lap…)"

    P "*laugh* They do say reality is stranger than fiction."

    "Your laughing dies as you realize something."

    scene d36 #cam look at floor
    with dissolve

    P "(Wait… When she woke up, she acted like she was still dreaming, and asked me if I were real…)"

    P "(So I’M the one she was fantasizing about?)"

    "The idea of Coral having sexual or romantic feelings for you bounces in your head."

    P "(I know we’ve always gotten along super well, but actually LIKING ME? That’s… insane, right?)"

    P "(But… is it? I'm pretty much attracted to all the girls, no matter how crazy that sounds too.)"

    P "*shake head* (I don’t have time to think about all of this right now, but I definitely plan to figure out what the hell all this means with Coral.)"

    scene bs
    with dissolve

    "She soon returns, and changed, but you decide not to tease her again as you have your own conflicted emotions."

    scene d37 #C lean back on couch
    with dissolve
    #play music "CTS2 - Upbeat-Pop-Theme.mp3"

    "And you two resume the search for the riddle’s answer."

    C "Ugh, at this point, I’m seriously ready to give up."

    P "As the older one, I should probably encourage you to keep going, but fuck me, man. I'm starting to think there's not even a correct answer."

    scene d38 #C look at cam
    with dissolve

    C "*sigh* Maybe we should just take a break and come back to it with fresher minds?"

    P "(I hate to let Coral down after she was so excited, but we have been at this for hours now.)"

    P "That might be a good idea. And hey, if we can’t find the answer, we’ll just hack the site or something."

    scene d39 #C smile
    with dissolve

    C "You may be joking, but I have picked up a few skills in the last year."

    P "What happened to my sweet little Coral?"

    C "Muahaha."

    "*knock* *knock*"

    scene d40 #C turn head to door. Cam look at door
    with dissolve

    N "It’s me, my dumplin's. Can I come in?"

    P "Sure, [m_nik]. Come in."

    scene d39
    with dissolve

    C "Hmm? Did this suddenly become your room when I was in the bathroom? Because there’s a big C on the wall over there, and it sure as heck doesn’t stand for cuck."

    P "*laugh* Cuck?"

    C "Yeah, I think it’s a funny word. ‘Cuck.’"

    scene d41 #N walk in room
    with dissolve

    P "Sure, but are you forgetting the Gummy Pact we made when we were kids? We agreed that half of everything you own is mine if I gave you the last gummy worm."

    C "Oh my god, you’re invoking the pact? You are so evil. And I didn’t even know what a pact was back then!"

    scene d42 #N near looking at them
    with dissolve

    P "*grin* Heh, I know."

    C "God… I’m surprised you haven’t actually already taken advantage of it yet."

    P "I’m waiting for the opportunity to claim your most precious thing. Muahaha."

    scene d43 #C awkward slightly look away
    with dissolve

    C "S-Suuure."

    P "(Oof. After what just happened that statement definitely hits different.)"

    N "I’m so happy y'all are two peas in a pod again. *giggle*"

    P "Of course. Batman can only go without Robin for so long."

    scene d45 #cam on C annoy
    with dissolve

    C "Ugh, whatever. Batman isn't even a real superhero."

    P "I told you not to joke about that, Coral!"

    scene d42
    with dissolve

    C "*giggle* God, I almost forgot how serious you take your comic book stuff."

    P "Superheroes are no joke, Coral."

    C "Yeah, yeah, Bat Boy."

    scene d47 #C look at N, vice versa
    with dissolve

    C "So what brings you to my dungeon, [m_nik]?"

    N "Just wanted to let y’all know that lunch is ready."

    C "Thanks. We were actually about to take a break anyway, so this is good timing."

    N "I heard y’all up pretty late last night. Playin' yer video games like you used to?"

    scene d42
    with dissolve

    P "Yup, and we were able to get a high enough rank on the game to receive a special prize, but we need to figure out a dumb riddle to actually claim it."

    P "That’s why we've been cooped up in here all day."

    scene d49 #N sad & C look at her
    with dissolve

    N "Oh, I’m so sorry y’all are havin' trouble. Would you like me to take a crack at it?"

    P "*shrug* Sure, but we’ve pretty much tried out every answer."

    C "Are you ready, [m_nik]?"

    scene d42
    with dissolve

    N "Sure, puddin', but don’t you need to grab yer computer or phone to look at the riddle?"

    scene d49-2 #C annoy
    with dissolve

    C "Ugh, unfortunately, no. I’ve recited it in my head so freaking much the past few hours, I can give it to you without even looking."

    N "*giggle* Okay, baby girl. Hit me."


    scene d50 #C neu
    with dissolve

    "For what seems like the millionth time that day, you hear the Immortal Fighting riddle."

    C "I am not alive, but bring to life, love, laughter, beauty, and strife. Though I don't speak, I never fail to captivate you with a tale."

    scene d51 #N thinking and pose
    with dissolve

    "Several seconds go by while you wait for Norah."

    scene d52 #N smi looks at cam
    with dissolve

    N "Maybe they’re talkin' about a book?"

    P "A book…?"

    scene d53 #C eyes open at cam
    with dissolve

    C "A book…"

    "You and Coral have the same reaction as you think about the answer."

    P "(It matches every part of the riddle. Even the bit about 'not speaking.’ This has to be it!)"

    scene d54 #C excited typing
    with dissolve

    "In the blink of an eye, Coral snatches her laptop nearby and types the answer."

    scene d55 #C throw up hands, look at comp still
    with dissolve

    C "Hahaha, yes!!! It worked!"

    P "Hell yeah!"

    scene d56 #N look at cam, C look at N
    with dissolve

    P "*smile* You are a bonafide genius, [m_nik]."

    C "Seriously, [m_nik]. You rock so hard."

    N "Heh, now I don’t know about all that, but I'm happy I could help y'all out."

    scene bs
    with dissolve
    stop music
    "After reminding you about lunch, she makes her exit."

    scene d15-2
    with dissolve
    #play music "CTS2 - Upbeat-Pop-Theme.mp3"

    P "Talk about a lifesaver, huh? I almost forgot how many times she’s bailed us out of something."

    C "Haha, I know. Not to mention keeping Zoe off our backs whenever we thought of something crazy like filling those balloons full of jello."

    P "*smile* Ah, good times, good times."

    P "Anyway, what does the website say now? Does it tell you our prize???"

    P "(Not gonna lie, I’m getting pretty excited too. Maybe it’s a secret character or something?)"

    C "Hehe, looks like I’m not the only one who’s excited now."

    scene d14
    with dissolve

    C "It says that…"

    scene d16
    with dissolve

    C "Ugh, are you freaking kidding me?"

    P "What’s wrong?"

    scene d15
    with dissolve

    C "The site is saying we have to go to the library downtown, and there’s a computer waiting in the backroom that we’re supposed to use."

    P "*sigh* Seriously?"

    C "If I’m lying, then I’m dying."

    P "*laugh* Considering you’re not dead, I guess you’re not messing with me."

    P "But… you know what? This might actually be a good thing."

    scene d57 #C confused, move
    with dissolve

    C "How is having to solve more crap that makes our heads hurt 'good' in any way?"

    P "If this was just a simple prize, there’s no way they’d be going through all this trouble, right?"

    scene d58 #C realize exp
    with dissolve

    C "Yeah… Immortal Fighting is big all over the world, so them having something set up in our city probably means they’re doing stuff in other cities, too."

    scene d14
    with dissolve

    C "Holy crap! What do you think it is???"

    P "Your guess is as good as mine, but I sure as hell plan to find out."

    scene d59 #cam reach hand out
    with dissolve

    P "You with me, partner?"

    scene d60 #C put hand in cam, still look at him
    with dissolve

    C "Hell yeah, let’s kick this whole puzzle thing’s ass!"

    scene bs
    with dissolve

    "You and Coral skip lunch, much to the disappointment of Norah, but explain the situation and head straight to the city’s library."
    stop music
    scene d61 #C smi walking look forward
    with dissolve
    #play music "CTS2 - Upbeat-Pop-Theme.mp3"

    C "Just follow me. The backroom is right up here."

    P "Surprised they still even have libraries anymore with practically everything digital these days."

    C "True, but I know a couple of girls that LOVE reading real books. People like them keep it alive."

    P "Well, I do think that’s pretty cool they’re trying to keep the old stuff alive. New doesn’t always mean better."

    scene d62 #C smi at cam
    with dissolve

    C "Spoken like a true grandpa."

    P "You’re joking, but I’m pretty sure I found a gray pube the other day."

    C "Oh my god, ew, [p_name]. *giggle*"

    P "*smile* Sorry, too much info."

    C "Ya think?"

    scene d63 #cam on A & M playing comp
    with dissolve

    "You and Coral soon reach the backroom of the library as promised, but there are two girls already there."

    P "(Oh, they’re both pretty cute. And the blonde's tats are something you definitely don’t see every day.)"

    scene d64 #cam on C worried look at girls
    with dissolve

    C "*whisper* Shit, there are already people on the Immortal Fighting computer… Do you think they beat us to the prize?"

    P "(Damn, I wasn’t even thinking about that. Guess us guys really do think with our penises sometimes.)"

    scene d65 #A neu look at M, M smi look at A
    with dissolve

    TG "Alright, Munchkin. We’re on the last one. What do you think we should do here?"

    BG "I-I think that we should check the painting."

    P "(Oh, the brunette has a pretty noticeable stutter.)"

    C "Wait… Is that Miracle?"

    scene d64
    with dissolve

    P "Miracle?"

    C "Yeah… The brunette."

    scene d66 #C look at cam
    with dissolve

    C "She and her best friend were the first friends I made when I started college out here."

    P "What about the tatted one?"

    C "That’s Sasha, her older sister. And before you get any ideas, she’s just as likely to rip your penis off as she is to say hello."

    P "Ha… Guess those tattoos aren’t just for show."

    A "Fuck yeah, it worked."

    scene d63
    with dissolve

    A "You and that big brain of yours is going to get us far."

    M "*giggle* I-I'm just glad it worked."

    "The girls wrap up on the computer and approach you."

    scene d67 #A&M walk to cam look at each other
    with dissolve

    C "Hey, Miracle."

    scene d68 #M confused when they stop, A neu
    with dissolve

    M "Huh?"

    A "Friends of yours, Munchkin? Sabrina isn’t going to be happy about this at all."

    scene d69 #M smi
    with dissolve

    M "*giggle* C-Coral is friends with Sabrina too."

    A "What about this dude?"

    P "(Man, Coral wasn’t lying about this Sasha girl. I feel like if I say the wrong thing, she WILL rip my dick off.)"

    scene d70 #M conf
    with dissolve

    M "O-Oh, I don’t really know him…"

    scene d72 #A smi
    with dissolve

    A "Ah, I see. I thought you were just as innocent as the vampire twins, Coral. But looks like you got yourself a pretty boy toy over here."

    scene d74 #cam on C flustered look at A&M
    with dissolve

    C "Wh-What? Boy toy? No, he’s…"

    menu:

        "You’re her boyfriend [CoralPath]":
            $ Cbf = True
            $ cpts = cpts + 1
            P "(Heh, let’s have a little fun.)"

            scene d75 #cam put arm around C, she flustered, look at cam wide eyed
            with dissolve

            P "*laugh* Boy toy makes it sound like I’m a piece of meat. But I know that Coral values my mind."

            P "Isn’t that right, babe?"

            scene d76 #C embarrassed looks down
            with dissolve

            C "U-Um, yes…"

            P "(Ha, she’s actually going with this? I thought for sure she would have shoved me away and told me to stop playing around.)"

            "Her behavior makes you think of the sex dream earlier."

            P "(Maybe… maybe it WAS really about me, no matter how crazy that sounds.)"

            scene d77 #A&M smile at them
            with dissolve

            A "Well, isn’t that just the sweetest thing that makes you want to throw up."

            M "Hehe. I-I think it’s really romantic."

            M "D-Do you want to come over tomorrow, Coral? I-I bet Sabrina will want to hear about your new boyfriend too."

            C "Oh, uh, yeah. That’s cool, I guess..."

            jump CH4BF

        "Don’t say anything":

            C "Just my [rel_b]."

            M "O-Oh, I didn’t know you had a [rel_b]. It’s, u-um, nice to meet you. I’m Miracle."

            A "Ditto. I’m Sasha."

            P "*smile* It’s nice to meet you too, Miracle and Sasha. I’m [p_name]. And thanks for looking out for Coral. She may be a handful, but she means well."

            C "*laugh* Whatever."

            jump CH4BF

label CH4BF:

    C "I know you guys are on your way out, but… Can I ask why you came here in the first place?"

    scene d69
    with dissolve

    A "Ah, I almost forgot. You’re pretty into video games, aren’t you, Coral? So I’m guessing you’re here for the Immortal Fighting promotion."

    C "So you ARE here for that… Even Miracle?"

    M "Y-Yeah. Sasha forced me to play, even though I told her I just wanted to read. But she said she would buy me books whenever I wanted for the next month."

    scene d77
    with dissolve

    A "Yep. At first, I just wanted someone to practice some moves on, but it turns out the munchkin over here is good with the sticks, and we were able to get a top ranking."

    P "(Ha. These two sisters certainly seem interesting.)"

    P "Wait… Does that mean you took the promotional prize?"

    scene d69
    with dissolve

    A "I don’t think so. We had to play some sort of game, but I think you should be able to access the computer and play too."

    "You hear Coral take sigh of relief."

    C "What’d you guys win, if you don’t mind me asking?"

    scene d77
    with dissolve

    A "Hey, now. Where’s the fun in that? And I have a sneaking suspicion you’ll have it soon enough anyway."

    C "*smile* Thanks for the vote of confidence, Sasha. We’ll try not to let you down."

    A "Good luck."

    scene d79 #A walk away
    with dissolve

    A "Let’s go get that ice cream for all your hard work, Miracle."

    scene d79-1 #A gone
    with dissolve

    M "G-Good luck, guys. S-See you both soon."

    scene d80 #cam face neu C look down
    with dissolve

    P "You have some pretty interesting friends."

    C "Hmm…"

    P "What’s wrong?"

    scene d81 #C look at cam
    with dissolve

    C "Nothing, just thinking… Miracle said she would see us BOTH again."

    P "I think she just meant around town or something."

    C "*shrug* I guess. Just thought it was weird she included you."

    P "Aww, are you jealous your friend might like me? Even if she did, it won’t happen anyway. That would be NTR."

    P "And we all know NO ONE likes that."

    scene d82 #C break eye contact embarrassed
    with dissolve

    C "P-Please. Why in the world would I be jealous who likes you or not?"

    if Cbf == True:

        C "And I have no idea why you thought it was funny to tell them you were my boyfriend. Now I have to actually follow through with that lie to Miracle and Sabrina."

        P "What, are you saying I’m not boyfriend material? I WAS joking around before, but now I’m actually offended. I would rock your world, Coral."

        scene d83 #C smi at cam
        with dissolve

        C "You are such a goofball…"

        P "*grin* You bring out the best in me."

        P "But hey, you can just tell your friends how much of a goofball that I really am like you said and that my sense of humor is… an acquired taste. *smile*"

        scene d82
        with dissolve

        C "I don’t think they would actually freak out that much, even if you were my real boyfriend…"

        P "What? What do you mean?"

        scene d84 #C look around
        with dissolve
        stop music
        "Coral suddenly starts looking around as if she's searching for something."

        P "Coral?"

        scene d85 #C grab cam hand to lead him away
        with dissolve

        C "Come on, let’s get away from here."

        "Coral grabs your hand."

        P "(What in the world is going on?)"

        scene d86 #C sit at computer table
        with dissolve

        P "What’s up, Cor'? You practically ripped my arm off dragging me over here."

        C "I’m going to tell you something, and you have to SWEAR never to say ANYTHING to ANYONE."

        P "You’re kinda freaking me out here, Coral."

        scene d87 #C mad
        with dissolve

        C "SWEAR!"

        P "Alright, alright. I swear. Now just tell me what's going on. I'm about ready to explode over here."

        scene d88 #C deep breath
        with dissolve

        "Coral takes a deep breath."

        scene d86
        with dissolve

        #play music "NERV - Smooth-Lounge-Background.mp3"
        C "*whisper* So, I’ve known Miracle since I started college here almost a year ago, and I started going to her house to hang out with her and Sabrina."

        C "One time, I overhear her talking to Sabrina about a time where Miracle's [rel_f] peeked up her shirt, and she responded by opening her legs so he could see better and stuff."

        "You almost don’t understand the words your 18-year-old [rel_s] just spoke."

        C "And that’s all I was able to get before I panicked and moved away."

        P "Whoa."

        scene d90 #C sheepish
        with dissolve

        C "I know…"

        P "So… is she in that type of relationship with him?"

        scene d86
        with dissolve

        C "Heck if I know, but… What else are you supposed to think? That’s just plain crazy."

        P "(Is it? Maybe. But I feel some type of way towards Coral, and I think she feels SOMETHING for me after witnessing her dream earlier this morning.)"

        P "Now I get your comment about them not thinking us dating would be a big deal."

        scene d91 #C smile
        with dissolve

        C "*laugh* See?"

        P "And… what do you think about them being in that type of relationship? If they were?"

        scene d86
        with dissolve

        C "Well… I don’t know. I know that it does happen in real life, and Miracle was giggling while she was remembering what happened…"

        C "So… it’s fine if you like the person? And it’s consensual. But I can see it being creepy in some situations. I don’t know."

        "You stare at Coral."

        P "(I keep thinking about what happened earlier, and Coral’s possible feelings toward me.)"

        P "The… thing about me being your boyfriend. Is it creepy to you?"

        P "(I don’t even know what kind of question that was, but I can’t think straight right now and my heart is pounding.)"

        scene d92 #C confused
        with dissolve

        C "What...?"

        scene d93 #C uncomfortable back up
        with dissolve

        "Coral seems to recognize how close you two are and leans back."

        P "Like… If I were your actual boyfriend or something. Is that creepy in your mind? Or weird?"

        scene d94 #C uncomfortable look away
        with dissolve

        C "What… I don’t know…"

        scene d93
        with dissolve

        C "Why are you even asking me something like that?"

        "Sweat starts to form on your forehead and your throat gets dry."

        scene d95 #cam on floor
        with dissolve

        P "(I can tell her about my feelings here or… not. I don’t know what to do!)"

        "Half of you just wants to confess, but another part of you reminds that this is not just a girl and doing so could damage your relationship for life."

        C "I… had a dream about you this morning…"

        scene d94
        with dissolve

        "Your head snaps up so fast, you hear it crack in the silent room."

        C "We were like… doing stuff."

        "Your heart starts beating even faster, but not because of fear like before."

        P "(Holy shit! I can't believe she actually admitted that!)"

        P "You mean… sexual stuff?"

        scene d96 #C angry
        with dissolve

        C "*blush* No, I mean riding unicorns and eating cotton candy."

        P "(Haha. I can tell this is not easy for her, obviously going through the same emotions myself.)"

        scene d94
        with dissolve

        C "I-I'm sorry, [p_name]… I’m honestly not trying to be a jerk… This is just kind of hard. I've never had to say any of this out loud before."

        C "Heck, I haven't even really thought about it. I would just start to freak out whenever I did."

        P "(So does that mean she has had feelings for me for a while?)"

        P "I think about you too, Coral."

        scene d97 #C smi
        with dissolve

        C "You do?"

        P "*smile* Yeah, I do. You’re my best friend, and obviously pretty, so it wasn’t very hard to start having those type of feelings for you."

        C "Hehe."

        scene d93
        with dissolve

        C "I’m happy to hear that, but this is all so much right now… My brain feels like it's about to explode or something…"

        P "(I don’t blame her. We just literally told each other of our mutual feelings.)"

        P "Hey, you’re not alone. I know this is a lot to process right now, and we still have to solve this Immortal Fighting puzzle."

        P "So let’s just focus on this for today, and then we can digest everything else at our own pace?"

        scene d97
        with dissolve

        C "Yeah, I’m good with that… Thanks for being so cool about all of this. I thought you would be, so it made confessing a bit easier."

        C "Though that crap was not easy. *laugh*"

        P "*laugh* No kidding."

        P "So, ready to get this shit over with?"

        C "Sooo ready."
    else:
        P "*laugh* I get it, I get it."

        P "Anyway, you ready to get this shit over with?"

        scene d83
        with dissolve

        C "I was ready yesterday."

    scene d98 #C on comp and see screen of living room
    with dissolve
    #play music "CTS2 - Upbeat-Pop-Theme.mp3"


    "You and Coral start up the game and test out the controls."

    C "Okay… So all we can do is move the camera around. Not very exciting."

    P "And it looks like we’re just in a regular house, but the door that says exit won’t open. I'm going to guess this is an interactive type of game."

    C "And we need to figure out how to get that door open."

    P "Yep. Time to start rearranging some furniture."

    jump M2

label M2:

    menu:

        "[gr]Check bathroom":

            $ op5 = True
            $ con5 = True

            scene d99 #check bathroom
            with dissolve

            "You study the bathroom as Coral moves the camera all around."

            P "The tub is full. Can you try emptying it or something?"

            C "Sure."

            "Coral does as suggested and is able to empty the tub."

            "*click* A green check mark shows up next to two grayed out ones in the corner of the screen."

            P "Ohh, looks like we’re on the right track. Let’s keep going."

        "[gr]Check living room":

            $ op2 = True
            $ con2 = True

            scene d98
            with dissolve

            P "Are you spotting anything out of the ordinary?"

            C "Hmmm, Oh, yeah. The painting on the far side wall is kind of crooked. Let's see if I can interact with it..."

            "*click* You get a green check mark, but still need more."

            P "*smile* Making progress."


        "Check kitchen":
            $ op3 = True

            scene d101 #kitchen
            with dissolve

            "Your eyes search for anything out of the ordinary."

            P "I don't really see anything."

            C "Hmmm… Me neither."

            P "Well, on to the next thing then."

        "[gr]Check bedroom 1":
            $ op4 = True
            $ con4 = True

            scene d102 #bedroom
            with dissolve

            "Coral immediately begins trying to interact with every object and soon finds an out of place picture frame on the left side of the room."
            "*click* You receive a green check mark, alongside the other check marks."
            P "Awesome."


        "Check bedroom 2":
            $ op1 = True

            scene d103 #bedroom 2
            with dissolve

            "Coral checks the bedroom for anything out of place or interactive objects, but finds none."

            C "Ugh."

            P "Just keep searching. We’ll get it..."


    if not (con2 and con4 and con5):
        P "(Need to keep searching.)"
        jump M2

    else:
        "*ring*"
    scene d105 #C smi and face vam
    with dissolve

    C "Awesome, we got it!"

    P "This was way easier than the riddle, which we needed [m_nik]'s help to even get."

    C "Seriously."

    scene d107 #comp screen has message
    with dissolve

    P "Oh, the game is saying something."

    scene d108 #C face screen, winner text
    with dissolve

    C "Ohhh, this must be about our prize!"

    P "(Better be worth all the trouble.)"

    C "'Congratulations on solving the riddle and puzzle of the Immortal Fighting promotion 2020...’"

    C "'You and your partner are now cordially invited to participate at one of the following locations for a chance to win $10,000… And an exclusive trip to our studios where you will be involved in creating a new character for our upcoming DLC...'"

    "You and Coral stay still for a while, almost as if time is frozen."

    scene d109 #C face cam excited
    with dissolve

    C "Oh my goddd, so freaking cool!"

    "You’re a bit worried about Coral making so much noise in the quiet library, but your excitement makes you forget about it instantly."

    P "Haha, hell yeah. All that trouble was so worth it. 10k? Helping create a new character at their studios? Dude."

    C "This means we have to practice even harder. There are going to be some heavy hitters since this is a worldwide tournament."

    P "Definitely. We need to turn it way up to compete with the best."

    C "True, but we’re no scrubs either. I seriously think we can make a dent in the tourney if we’re serious."

    P "*smile* Hell yes we can."

    P "And hey… Now I think I understand what your friend Miracle meant by seeing us again soon."

    C "Oh crap, you’re right, haha. I do like her and Sasha and all, but there's no way I'm going to let them get in the way of OUR prize."

    P "*smile* I’m with you."

    P "(Today was completely nuts with everything that happened between me and Coral, and now this sudden tournament. And there’s so much to think about, not even including the dating sim we still plan to make.)"

    P "(But I’m glad to be doing all this with her. And I think we’re even closer now than before the divorce. It’ll be really interesting to see how our relationship develops from here.)"

    scene bs
    with dissolve
    stop music
    "You and Coral spend the rest of the day strategizing and figuring out the game plan for the upcoming video game tournament."

    "And while that has suddenly become a priority for you, Leanne and her behavior at your welcome back meal has not left your mind."

    "So you visit her home the very next day for some answers."

    scene d110-1 #MC stand in front of L door
    with dissolve

    P "(Okay, this is it. I’m just going to go in there and confront Leanne about her playing footsie with my dick when she’s the one who hasn’t even let me touch her since we made our deal.)"

    P "(And I know she’s going to try and change the conversation and make everything nonchalant, but I'm not going to let her control anything this time.)"

    P "(But when I do get her to tell me what’s up, do I even want to continue how we’ve been?)"

    P "(No… Something has to change. I just don’t know which direction I want to go right now, or even what she’ll want to do.)"

    P "*deep breath* Alright, enough talking, [p_name]. Let’s do this."

    scene d110-2 #***MC knock
    with dissolve

    "You go to knock on the door, but pause."

    scene d110-3 #MC open door
    with dissolve

    P "(Ah… How’d I know the door would be unlocked? Again. I’m going to talk Leanne’s ear off about her carelessness too.)"

    P "(Some perv who wants to screw her could easily get in…)"

    "You realize immediately that you fit the description."

    P "(B-Besides me, obviously.)"

    scene bs
    with dissolve

    "You finally enter her house and head straight upstairs."

    scene d110-4 #L sit on edge of bed look out window
    with dissolve

    "You expect to find Leanne passed out, but she’s already awake, and you go to call her out, but pause again."
    #play music "Sad - Reflective-Piano-Theme.mp3"

    P "(Leanne… I don’t think I’ve ever seen that look on her face before… Almost like she’s depressed?)"

    "You’ve known the free spirit your whole life and have never once seen her down, so the shock is plausible."

    P "(What in the world is going on with her?)"

    "You think back to her recent behaviors, like quitting the job Zoe got for her, becoming distant with everyone, and of course the reason you came over in the first place."

    "That’s when an idea pops into your head."

    P "(Of course I want to figure out why she broke our number one rule and what it means going forward, but trying to clear her head first might be the solution to that.)"

    P "(And of course I'm worried about her anyway.)"

    scene bs
    with dissolve
    stop music
    "You quietly sneak back out the house and set up arrangements for an outdoor getaway before returning the very next day."

    scene d110-4
    with dissolve

    P "(She’s literally in the same spot as yesterday… With that same empty look…)"

    P "*shake head* (No need to dwell on that anymore. Time to put my plan into action!)"

    P "I’m starting to think you WANT to get sexually assaulted with how much you leave your door unlocked."

    scene d111 #L smile and face cam
    with dissolve
    #play music "LTS2 - Sweet-Juice.mp3"
    L "[p_name]."

    L "Are you saying you would be the one doing the assaulting? You know no touching allowed…."

    scene d113 #L lay closer to face cam
    with dissolve

    L "But I guess I wouldn’t be able to do anything about it."

    P "*dick twitch* (Is she challenging me here? Maybe she’d let me touch if I were more forceful…)"

    P "(No! Clear your head, man. We’re not here for that right now.)"

    P "*clear throat* You shouldn’t joke like that, Leanne. Especially in 2020 with all this social justice warrior stuff going on."

    L "Always so seriousss."

    P "And you’re always joking. Ever thought about becoming a clown?"

    L "Hahaha. Do you think I’d be cute? I’ve always wanted one of those red, round noses."

    P "*smile* Zoe would blow her top if that’s what you wanted to do."

    L "Mmm, now you’re really tempting me."

    P "Ha, of course. I should have known that."

    P "Anyway, enough chitchat. We need to get going while it’s still early."

    scene d114 #L sit pose
    with dissolve

    L "And where would that be, little [rel_b]? I don’t remember us making any plans."

    P "That’s because I just made them. We’ll only be gone overnight, so just throw on some street clothes for the day."

    scene d115 #L lay back to look at ceiling
    with dissolve

    L "Mmm… But I don’t wanna. Let’s just watch a movie or something. You can even pick which one."

    P "Hell yeah I am. I am NOT watching another one of those cheesy horror flicks."

    L "Hehe. But you used to watch them all with me when we were younger. Don’t you remember?"

    P "I remember you sweet-talking me into watching them with you, sure. But I’m not that same kid anymore."

    scene d113
    with dissolve

    L "Oh, trust me. I think that no one knows that more than me."

    "Your heart beats a little faster under her knowing gaze."

    P "(She’s starting to dictate the convo like always. I need to get us back on track.)"

    P "Exactly. I’m much bigger and stronger. Which means that I can make you come hang out with me, but I want to give you a chance to keep your dignity."

    "Leanne watches you in amusement before letting out a short laugh."

    scene d114
    with dissolve

    L "Fine, you win, [p_name]. Can you at least tell me where we’re going?"

    P "Nope. Go get dressed and make sure to wear sports shoes."

    P "(Leanne almost never does what others want, so I think I should try to hold on to what little power I seem to have if I really want to change things and get through to her.)"

    P "(The softer approach has never worked, and I doubt it ever will.)"

    "Yet again, silence fills the room as she watches you."

    P "(What goes through her mind when she looks at me like that? I would honestly pay money to know.)"

    scene d117 #L walk to bathroom
    with dissolve

    L "I should go shower, then."

    scene d118 #L further and drop robe
    with dissolve

    L "Try not to peek, though I know that’s a little difficult for you."

    "Your eyes involuntarily scan every inch of her glorious body as she heads for the bathroom."

    scene bs
    with dissolve
    stop music
    "Your 23-year-old [rel_s] soon gets ready and you head out to the chosen place to clear her mind."

    scene d119 #L face cabin
    with dissolve
    #play music "LTS2 - Sweet-Juice.mp3"
    L "A tent in the woods? I admit I do like my horror movies, but not THIS much."

    P "*laugh* Come on, you’re telling me you’d rather do something boring like go shopping?"

    scene d120 #L smi face cam
    with dissolve

    P "Out here we can be one with nature and pee on trees and stuff."

    L "*laugh* You have a unique definition of bonding with nature… But I guess taking in some fresh air and sunshine every now and then isn’t bad."

    L "And at least you got us a luxurious tent with a bed. Not sure if I could do the full-on camping thing."

    P "*laugh* I figured, but remember, I’m a city boy too. Sleeping on the ground isn't really my thing either, so I paid a local camping service to set this all up just for you."

    P "Don’t you feel all special? *grin*"

    L "*giggle* Indeed I do. You are so sweet."

    scene d121 #L inside checking out bed
    with dissolve

    "You two enter the tent."

    P "What do you think?"

    L "The bed seems actually pretty comfortable. Not too hard or soft."

    P "That’s what she said."

    scene d122 #L sit and face cam
    with dissolve

    L "*giggle* You know, I’ve always wondered who 'she' is, but definitely a slut. Right?"

    P "*smile* Huge slut."

    L "Haha. So, I’m guessing we’re going to be sleeping on the same bed?"

    P "I’ll be a gentleman and offer to sleep on the ground, but I reaaally don’t want to."

    L "Do you honestly think I would let you sleep on that hard ground? Of course you’re sleeping on the bed. All I need to know is that you’ll behave."

    P "(As much as I would love to cop a feel or two 'accidentally,' the whole reason I brought Leanne out here was to see if I could do something about her depression or whatever else she has going on.)"

    P "Do you really need to ask that?"

    scene d123 #L change pose
    with dissolve

    L "Mhm. I think I do."

    P "(I don’t blame her. I have broken the no touching rule a few times throughout the years.)"

    P "Keep my hands to myself. Got it."

    L "Hehe. Good."

    P "Now that we got that out of the way, follow me. I want to show you something."

    L "You’ve already dragged me all the way out here, so I guess I have no choice."

    scene d124 #L soldier salute
    with dissolve

    L "Lead the way, sir."

    P "*smile* (Even though this trip is for her benefit, I have missed just hanging out with Leanne, just like with the other girls.)"

    scene d125 #L hiking tired look at ground
    with dissolve

    "You and Leanne set out."

    P "(I know Leanne isn’t exactly an outdoorsy type, but she's struggling more than I thought. Well, that's what happens when you're cooped up in a house all day.)"

    scene d126 #L look at cam
    with dissolve

    L "How much further do we have to go?"

    P "Still got a bit. You good?"

    scene d127 #L smi
    with dissolve

    L "Right as rain."

    P "*smile* I never understood that saying."

    L "*laugh* Then we can both agree it’s stupid, but I like how it sounds."

    P "(Leanne may not like doing certain things, but she doesn't whine or complain when she's actually in it, like right now even when she's really struggling.)"

    menu:

        "Offer a piggyback ride":

            $ lpts = lpts + 1

            scene d128 #cam go to ground, L surprised
            with dissolve

            P "(It wouldn’t hurt to save a damsel in distress, so to speak.)"

            L "Hey, you okay?"

            P "Right as rain."

            scene d129 #L smile
            with dissolve

            L "Hey, that’s mine."

            P "*smile* Sorry. I’ll give you a piggyback ride to make up for it."

            L "That’s sweet, but you don’t have to force yourself."

            P "It’s not a big deal. Besides, this is your only chance aboard the [p_name] Express. Are you really going to pass this opportunity up?"

            L "Hahah. You make an excellent point."

            scene d130 #L piggyback MC look back 3rd
            with dissolve

            P "Alright, ready to go?"

            L "Mhm, but can you choo-choo one time?"

            P "I WILL drop you, Leanne."

            L "*giggle* Okay, okay. I’ll shush and enjoy the ride."

            scene d131 #MC start walking 3rd
            with dissolve

            "You start walking."

            L "I know you’re 20 now, but it’s hard to believe you can carry me like this. I’m not too heavy?"

            P "Actually, no. I thought you would be heavier."

            L "*laugh* I appreciate the honesty."

            P "(Most girls might get offended at that statement, but Leanne really doesn't mind honesty.)"

            scene d132 #L rests Head on MC back
            with dissolve

            "Leanne rests her head on your neck with her soft warm, sweet breath tickling you."

            L "I missed you, you know."

            P "(She did? Sometimes I don't know how she feels. No, a lot of the time. Though I might know her better than… anybody, I guess.)"

            P "That makes me happy to hear, Leanne. You’re one of my best friends."

            "She snuggles her head into to you even more."

            jump CH4HIKE

        "Keep going":

            P "(And we aren't that, that far anyway. She’ll be fine.)"

            jump CH4HIKE

label CH4HIKE:

    scene d133 #L look at waterfall lake
    with dissolve

    "You reach your destination."

    P "And ta-daaa. What do you think?"

    L "This is gorgeous..."

    scene d134 #L face cam
    with dissolve

    L "I’ll admit, I was expecting an ass-shaped tree or something."

    P "Come on, Lee. Give me a little credit as an adult now. I plan to show you the ass tree AFTER."

    L "*giggle* My, my. Apologies to you, good sir. I won’t underestimate you again."

    scene d135 #L undress pose shirt
    with dissolve

    L "But this place is too good to pass up."

    scene d136 #shirt gone
    with dissolve

    P "What are you doing?"

    scene d137 #L take off pants pose
    with dissolve

    L "I’ve always wanted to go take a dip in a place like this."

    scene d138 #L pants gone
    with dissolve

    P "I see… And nude?"


    scene d139 #L face cam
    with dissolve

    L "Well, since you showed me such a nice place, I figured you should get to see something nice too. Do you approve?"

    P "*smile* I think you already know the answer to that."

    L "Heh. I think I do. Now, why don’t you get undressed and we can get have a little swim together?"

    P "(Since we made our deal, she’s always been the one to strip… But I guess it’s my turn now. Good thing I’m confident in my body.)"

    P "Ah, so this is your true aim. You’ve been thinking of a way to get me out of my pants all these years."

    L "*giggle* Ohh, yes. You’ve completely figured me out. And here I thought I was being subtle."

    scene d140 #cam look down
    with dissolve

    "You laugh and quickly undress, trying not to show your slight embarrassment with Leanne’s eyes never once leaving you."

    scene d141 #L look at cam junk
    with dissolve

    P "Okay, you ready to…"

    P "*awkward smile* You’re just going to openly stare at my junk?"

    L "Would you rather I pretend not to like most girls?"

    P "(She has a point there. I think pretty much every girl would sneak a peek out of curiosity. But Leanne’s always been honest too, which I will always appreciate.)"

    scene d139
    with dissolve

    L "Okay, I’m done."

    P "Ha… You gonna tell me your verdict?"

    L "Oh, I guess you’re the type of guy who likes a little vocal recognition."

    "You grin and put both hands on your hips."

    P "You know me so well."

    L "Haha. Okay, then."

    scene d141
    with dissolve

    L "[p_name], you have the biggest dick I’ve ever seen, and it’s not even hard. So god only knows how amazing your erection looks."

    P "(I was totally expecting a goof answer, but hearing her talk like that turns me on…)"

    P "Ha, uh, I guess that’s a pretty good review if I’ve ever heard one. Thanks."

    scene d139
    with dissolve

    L "You are quite welcome, my big dick little [rel_b]."

    scene d142 #L run to lake
    with dissolve

    L "Now, enough stalling! Let’s get in that water!"

    scene d143 #L cannon ball
    with dissolve

    L "Yahooo!"

    scene d144 #L disappeared
    with dissolve

    P "(Ha. She wasn't lying about being excited to swim out here.)"

    scene d145 #L face cam in water wave hand
    with dissolve

    L "Come on, Moby Dick!"

    P "(Yeah. It was definitely a good idea to bring her out here. Now I just need to figure out how to get her talk… Which is WAY easier said than done.)"

    scene bs
    with dissolve
    stop music
    "You think about the dilemma as you join her."

    scene d146 #cam face L in water
    with dissolve
    #play music "LTS2 - Sweet-Juice.mp3"
    P "The water's warmer than I was expecting."

    L "Sorry. I really had to go."

    P "WHAT? You peed?"

    L "Hehe, I’m joking. I just think you make the cutest faces when I tease you."

    P "*laugh* Ugh. You know I’m going to have to get you back now, right?"

    scene d147 #L swim back on side of cam
    with dissolve

    L "You can try, but all I have to do is flash you my pussy and make you forget."

    P "You act like your pussy is that Men in White pen."

    L "Hehehe. Same concept. They actually consulted me."

    P "*laugh* I guess I’ll have to take your word for it."

    scene d148 #L swim on other side
    with dissolve

    L "Sooo, I guess I wouldn’t be a proper big [rel_s] if I didn’t ask how all that fun stuff like how work is going?"

    P "It’s going… You know, same old, same old."

    L "I see. And you said you were down here for business or pleasure?"

    scene d147
    with dissolve

    P "*smile* For business, but of course seeing you girls was a priority for me."

    L "Just when I thought you couldn’t get cuter you go and say something like that."

    L "And you’ve been good while on your visit?"

    P "(The definition of 'good' regarding our deal means basically not perving out on the girls.)"

    menu:

        "I did peek on Zoe [gr]\[Zoe Peek\]":

            $ Zpeek = True

            $ lpts = lpts + 1

            P "(I did peek on Zoe that one time when I had arrived, but hell, can you blame me after almost a year of separation?)"

            P "(But… I don’t want to lie to Leanne about it. Because I actually feel I can be honest with her. She knows my biggest secret, after all.)"

            P "I… did peek on Zoe once when arriving here, but that’s literally the first time I’ve ever done that."

            scene d148
            with dissolve

            L "Am I not good enough for you?"

            P "What? No… I just… *shrug*"

            P "I don’t know. I wasn't really thinking at the time."

            P "(She doesn’t seem mad, but you can never tell with Leanne.)"

            scene d146
            with dissolve

            L "Okay."

            P "O… kay? That’s it?"

            L "Yes. You were honest with me, and I appreciate that. Even felons get three strikes before they’re out."

            P "Ha… Lucky me, then."

            jump CH4PEEK

        "I didn’t peek":
            $ lpts = lpts + 1
            P "I haven’t given into wicked, carnal temptation, if that's what you mean."

            scene d146
            with dissolve

            L "*giggle* That is what I meant, yes. And I’m proud of you for being so strong. I'll let you get it a peek at my pussy later, okay?"

            P "Haha… I am okay with that. Yes."

            jump CH4PEEK

label CH4PEEK:

    P "And what about you and work?"

    scene d149 #L float in front of cam on back
    with dissolve

    L "Yeeeah, still figuring that out, ya know?"

    P "I’m sure Zoe would be delighted to hear that."

    L "No, she’d be totally pissed."

    P "*smile* You know I was being sarcastic."

    P "But what’s up with flaking out on the job she gave you?"

    scene d150 #L switch to right or left swimming
    with dissolve

    L "Nothing really, just didn’t like it."

    P "(Leanne doesn’t straight up lie, but she sure as hell doesn’t always tell the truth.)"

    P "So you’re telling me nothing made you quit that job?"

    "…"

    L "It’s a boring story."

    P "Lucky for you I happen to LOVE boring stories!"

    L "Hehe. Do you now?"

    scene d146
    with dissolve

    L "Fine, I’ll tell you since you wanna know sooo bad."

    L "So, I started working at the marketing office and it took like a week for the boss to start acting like a creep."

    P "Creep?"

    scene d151 # L move hand
    with dissolve

    L "Sure, you know the usual. Staring at my tits and ass without batting an eyelash, and telling me I had a nice body."

    P "*frustrated breath* (Just dealt with this with Buster Himen and Irene, so I can picture it pretty well.)"

    L "Ohh, save your sighs. It gets better."

    L "The boss calls me in that same week and offers me a future higher position if I fuck him. Or be fired."

    P "Are you fucking kidding me?"

    scene d146
    with dissolve

    L "I kid you not, my dear [rel_b]."

    P "So that’s when you quit…"

    L "No, I fucked him."

    P "YOU WHAT?"

    scene d151
    with dissolve

    L "Haha. Oh yeah. I told him to meet me at a hotel and handcuff himself to the bed, and wear some sexy panties I had laid out for him, because that’s just the kind of freaky stuff I was into."

    L "Then I came out of the bathroom and took the video camera I had set up beforehand, and told him if he ever so much as looked at another woman the way he did me, his wife and everyone else in that marketing building would see him playing dress up."

    "A smile slowly creeps on your face."

    P "You definitely did fuck him good."

    scene d146
    with dissolve

    L "Just giving the old boss what he asked for. Wanna see the video? He is a pig, but the way he slipped into those panties has to be a talent."

    P "Hahaha. You don’t even have to ask."

    P "For a second there, though…"

    L "What? You think I'm the type to just fuck anyone?"

    P "No! Of course not, Leanne…"

    scene d152 #L hug up to cam
    with dissolve

    L "Hey, you’re not the only one who’s been good. I haven’t let anyone else touch or even see me since we made our deal."

    P "(What? Seriously?)"

    "You want to immediately start asking a million question, but stop your onslaught of thoughts."

    P "(Not yet, [p_name]. There’s plenty of time for that. No need to rush things. Just keep unwinding her like you planned.)"

    P "*smile* You know my dumb male brain is super happy to hear that, right?"

    L "*giggle* I know. That’s why I told you."
    $ renpy.end_replay()
    scene bs
    with dissolve
    stop music
    "You and Leanne spend the rest of the day together, taking in the surroundings and just relaxing."

    scene d153 #L rotating marshmallow look down
    with dissolve

    L "We’re actually roasting marshmallows. Now we’re really hardcore camping."

    P "*smile* Well, they are gluten free, so I don’t know how hardcore we really are."

    L "*giggle* Probably shouldn’t tell people that. If anything, we almost got mauled by three bears."

    P "*laugh* Three bears?"

    scene d154 #L look at cam
    with dissolve

    L "Mmmm, you’re right. Two sounds more believable."

    P "*laugh* Two it is, then."

    L "Hey, you know what really go great with these marshmallows?"

    scene d155 #L raise booze
    with dissolve

    L "Alcohol!"

    P "What? Where did you even sneak that?"

    L "Hehehe. A gal's gotta have her secrets, [p_name]."

    scene d156 #L drink
    with dissolve

    "Time passes as you and Leanne take turns drinking, and the mood really starts to loosen up as you both get buzzed."

    scene d157 #L dancing
    with dissolve

    "And Leanne starts playing music on her phone and dancing without prompt."
    #play music "Dance - Chill-House-Lounge.mp3"

    P "*laugh* What are you doing?"

    L "Don’t you ever just feel like danciiing the night away?"

    P "Sure, if I didn’t dance like a paraplegic. And the fact that you can even dance at all is impressive with how buzzed we are."

    L "Ha. If these little moves impress you, then what do you think of this?"

    scene d158 #L dance ballet
    with dissolve

    "Leanne starts doing a series of ballet-like moves that makes your jaw drop."

    scene d159 #L face cam, dance normal pose
    with dissolve

    L "What do you think about that?"

    P "What do I think? I think holy shit, Leanne. Where and when did you learn how to dance like THAT?"

    P "I saw a professional ballet dancer on the finals of a talent show the other day, and I swear you look even better, while basically drunk."

    P "(I knew she could dance, but not on a professional level.)"

    L "It’s nothing, really. Just a few moves I picked up."

    P "*laugh* What you just did is not what I would call 'nothing.’ You had to do some serious training for that or something. No?"

    scene d160 #L stand normal
    with dissolve
    stop music
    L "Nope."

    L "Anyway, I do think that alcohol is starting to hit me, and that nice tent bed is calling my name."

    scene d161 #L walk away
    with dissolve

    L "You must be tired too. Come to bed as soon as you’re ready."

    P "Ah… right."

    scene d162 #L gone
    with dissolve

    P "(Is it me or did that conversation have an air of uncomfortableness at the end?)"

    "You think for some seconds, but soon realize there's nothing you can do about it either way, and join Leanne in bed."

    scene d163 #L sleep
    with dissolve

    P "Leanne?"

    "The only response is her steady breathing."

    P "(Shit… she looks so beautiful. I know I promised to leave the sexual stuff alone for right now, but maybe a small kiss wouldn't hurt?)"

    menu:

        "Kiss her [LeannePath]":
            $ lpts = lpts + 1
            P "(Yeah, just a peck.)"

            scene d164 #cam move close to L lips
            with dissolve

            "You quickly push your lips against Leanne’s moist and soft ones."

            scene d163
            with dissolve

            P "(Fuck, that felt so good. Maybe just one more and I will stop.)"

            scene d164
            with dissolve

            "You lean in for a final kiss."

            scene d165 #L open mouth
            with dissolve

            L "I think that’s enough, [p_name]."

            scene d166 #L open eyes
            with dissolve

            L "Don’t you think?"

            P "Y-Yeah! Totally. I’m going to sleep right now. Goodnight, Leanne. Love you."

            scene bs
            with dissolve

            "You close your eyes at once."

            P "(Shit, she caught me. I think this is only the second time she ever has since we started this whole thing.)"

            L "*giggle* I love you too, my naughty little [rel_b]."

            P "(At least she doesn’t sound mad.)"

            "Is your last thought before sleep overtakes you."

            jump CH4KISS

        "Don’t kiss her":

            P "(Mmm… But maybe it isn’t such a good idea. And I am supposed to be controlling myself during this trip.)"

            scene bs
            with dissolve

            "You soon fall asleep."

    jump CH4KISS

label CH4KISS:

    "You don’t know how long you slept, but you suddenly wake up."

    P "*yawn* (What time is it? Still looks pretty dark.)"

    scene d168 #cam on L side empty
    with dissolve

    P "(Huh?)"

    P "(Did Leanne have to go pee or something? I don't like her being out in the middle of the night here even for a minute.)"

    scene bs
    with dissolve

    "You hurriedly put on some shoes and go searching, but don’t have to go far."

    scene d170 #L sitting near campfire look at phone
    with dissolve

    P "(Leanne? She’s looking at her phone with that same empty look that made me bring her out here on this nature retreat in the first place.)"

    scene d171 #cam closer look down at L
    with dissolve

    P "Leanne? You okay?"

    scene d172 #L smi up at cam
    with dissolve

    L "Right as rain."

    P "You reaaally like saying that, don’t you? Seriously, though. What are you doing out here in the middle of the night?"

    L "Nothing much. Just watching the hilarious video of my boss. Wanna see again?"

    P "…"

    P "(Then why did you have such a serious look on your face?)"

    P "No, Leanne. You weren’t."
    #play music "Sad - Reflective-Piano-Theme.mp3"
    "Your [rel_s] continues to watch you without changing expression before breaking eye contact."

    scene d173 #L look down
    with dissolve

    L "I guess it’s only fair you caught me doing something at least once."

    P "*smile* Now we’re even."

    scene d172
    with dissolve

    L "*laugh* Indeed we are."

    P "So… what WERE you watching?"

    scene d174 #L look down neu
    with dissolve

    "Leanne doesn’t speak for several seconds."

    P "(I’ve never in my life seen Leanne hesitate. What in the world could she have been watching?)"

    "More time goes by, and she doesn't seem to be on the verge of answering your question."

    P "Leanne… You don’t have to answer if it makes you uncomfortable, but I really would like to know."

    scene d176 #L neu at cam
    with dissolve

    L "Why do you care so much?"

    P "*raise eyebrow* Is that a trick question? Obviously I’m trying to show concern in hopes of getting in your pants once day."

    scene d172
    with dissolve

    L "Hehe. Playing the long game, eh? Not an easy road, but I respect it."

    P "*smile* I care because I care about you. Not much more to it than that."

    "Leanne's eyes don’t leave yours for a short while."

    L "Watching old videos from when I used to do ballet. Seriously do ballet. For years."

    P "What…? Why am I only learning this now?"

    L "John made sure to keep us all busy. I’m sure there’s plenty I don’t know about you or the other girls when we were young."

    P "*nod* Yeah… Everything I remember from childhood is mostly about the company, learning the ins and outs, or a bunch of crazy life lessons."

    P "So, I’m guessing you were pretty good by the display I just saw earlier… And do you still dance now?"

    scene d174
    with dissolve

    L "No, I don’t."

    P "Why?"

    L "…"

    P "Leanne?"

    L "John told me I was wasting my time, that I was good, but not good enough."

    "For the second time on the short trip, a wave of anger washes over you."

    P "Fuck him! What does he know?!"

    scene d172
    with dissolve

    L "As much as I would love to agree with you, little [rel_b], he was right."

    L "I tried out for a prestigious dancing program coming out of high school and failed miserably. All four judges voted no."

    L "So you see? Just not good enough. That’s when I quit and left it all behind."

    "You’re quiet for a moment."

    P "Why are you out here?"

    scene d177 #L confused
    with dissolve

    L "What?"

    P "You’re out here in the middle of the night looking at old videos of yourself, why?"

    scene d174 #L neu
    with dissolve

    L "..."

    P "Because you still love it, Leanne. Because you still want to dance."

    scene d176
    with dissolve

    L "Even if that’s true, I failed once already. Remember?"

    P "The greatest basketball player in the history of the world failed to make the varsity team his sophomore year. But he sure as hell didn’t give up."

    P "I’m not saying I have all the answers, Leanne. But I think you should do what you love. Period."

    P "So this is the only thing I’m going to ask you."

    P "What do you want to do?"

    scene d177
    with dissolve

    L "I…"

    scene d172
    with dissolve

    L "...want to dance."

    P "*smile* Then there’s nothing else to talk about."

    P "(Never would I have thought this plan will work so well. But I actually got Leanne to open up in a huge way.)"

    L "You are the best thing that ever happened to me. Do you know that, little [rel_b]? I don’t deserve you."

    "You’re a little surprised by Leanne’s sudden affection."

    P "(Figuring out your path in life is a pretty big deal, so I guess she feels grateful.)"

    P "Yes, you do. And I'm going to be here for you every step of the way."

    scene bs
    with dissolve
    stop music
    "You two return to the tent after."

    scene d180 #L snuggled up to cam
    with dissolve

    P "(Oh wow. Leanne is cuddling up to me.)"

    "She usually forbids such contact, but you don’t feel any lust from it."

    P "*smile* (Still feels pretty damn nice, though.)"

    L "I’ll admit I wasn’t gung-ho about this whole trip, but I’m really happy you brought me out here. Thanks again, [p_name]."

    P "*smile* I’ll drag your ass out into the woods any time you need."

    L "*giggle* I’m counting on it."

    "You wonder how Leanne will restart her dancing career, but you'll be here for any help that she needs."

    scene bs
    with dissolve

    "You two catch a few hours of sleep before returning to the city in the morning."

    jump U5
