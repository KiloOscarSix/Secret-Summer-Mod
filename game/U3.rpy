label CH3:

     "Some time passes as you wait for the pizza Coral wanted for lunch, and you go to wash up as it arrives."
     #play music "GTS-Uplifting-Acoustic-Background-No-Vocal-Edit.mp3"
     scene c1 #cam looking down at sink in bathroom, wash hands
     with dissolve

     if nshower == True:

         P "(I still can’t believe [m_nik] and I just showered together…)"

         P "(Her body is even more amazing than I’ve been imagining, and I didn’t even have to spy on her, so my deal with Leanne is still good.)"

         P "(Speaking of which, I still definitely plan to discuss what was up with her behavior at my welcome back party.)"

         P "(A lot of things are happening right now… But I’m glad to be entangled back in the girls' lives.) *smile*"

     else:

        P "(I still can’t believe [m_nik] asked me to SHOWER with her…)"

        P "(Well, maybe that isn’t totally true. It was a bit extreme, but she just wanted to feel close to me again after our little separation.)"

        P "*smile*(Well, she doesn’t have to worry about that. I’ll make sure we get along like we used to.)"

     "*bzzzt!*"

     P "(Oh, someone’s calling.)"

     scene c2 #MC looking down at phone. 3rd
     with dissolve

     P "*mutter* Hmm, don’t recognize this number, but it has the same area code as back home."

     scene c3 #MC answer phone. 3rd
     with dissolve

     P "Hello?"

     I "Where are you?"
     stop music
     P "What? Irene?"

     I "The one and only."
     #play music "Shut Up.mp3"

     P "(Wh-Why in the world is she calling?)"

     P "Um... Why are you asking where I am?"

     I "Because I’m at your hotel and the clerk says you’re not here. So that begs the question, WHERE ARE YOU?"

     P "(I have no clue why she’s all the way in this city, but this is VERY BAD!)"

     P "I, uh, I just stepped out and am enjoying the city. Can I ask why you’re at my hotel?"

     I "Because I’m your partner on the Buster Himen contract."

     P "WHAT?"

     I "Yes, your [rel_f] thought that it would be better for you to have a little guidance, so he sent me out."

     I "I’ve already set the meeting for an hour from now, and am going to text you the address now, so do not be late. I'm sure you know how important is meeting is."

     "The phone call ends."

     scene c2
     with dissolve

     P "Oh."

     P "This is not good."

     P "(If [rel_f] finds out l breached the terms of our deal, I have no doubt he would follow through on his threat.)"

     P "(And it would completely screw up everything the girls have going on. Hell, might even ruin their LIVES.)"

     scene c4 #MC look up
     with dissolve
     stop music
     P "(There’s no way in fucking hell I’m going to let that happen.)"

     scene bs
     with dissolve

     "You take a deep breath to calm down and go make an excuse to everyone about needing to step out."

     "Of course they give you suspicious looks like they did when you chose to be separated from them, but they don’t question you, unlike the first time."

     "Then you quickly drive back towards the other side of the city to meet Irene."

     scene c5 #cam walking in office hallway
     with dissolve

     P "(I still can’t believe Irene is in this city! And worse than that, she’s my partner on the contract!)"

     "You remember her very clear threat before you left home."

     scene c6 #Flashback of her threatening
     with dissolve

     I "You can pretend to be innocent, but I know you’re plotting something."

     I "And I promise you I’m going to find out exactly what that is."

     scene c5
     with dissolve

     "You blow out a stressful breath."

     P "(It’s going to be tough dealing with her, but at least I know she’s out to get me.)"

     P "(I’m not going to let her ruin the little time I have with [m_nik] and the girls. Just gotta play smart.)"

     "With one more deep breath, you calm your nerves and enter the meeting room."

     scene c7 #I sitting at table, not looking at MC
     with dissolve

     P "(There she is.)"

     P "(She may be my enemy… but damn does she look good as ever.)"

     P "(No, focus, [p_name]!)"

     scene c8 #cam sit next to her, still not looking at cam
     with dissolve

     P "Hey Irene…"
     #play music "ITS - Mr-Debonair.mp3"
     I "You’re late."

     P "What? I’m literally right on time."

     I "If you’re not 10 minutes early, then you’re late. I’m sure that’s something you know by now."

     P "(It certainly is. Just like a million other lessons, I had to learn that one the hard way after getting locked out of the house at 6, and then having to sleep outside.)"

     P "(Of course [m_nik] threw a fit, but she was never a match for his coldness. No one ever has been.)"

     P "(Though Leanne did give our [rel_f] a run for his money a few times.)"

     menu:

         "Be friendly [IrenePath]":

             $ ipts = ipts + 1

             P "Sorry about that. I guess maybe I was a bit nervous about this whole meeting and walked slower than I intended."

             P "(That is the actual truth. If I’m not able to close this contract, I’ll be sent packing, and my secret summer will be ended before it can even really start.)"

             scene c9 #I look at cam
             with dissolve

             I "As long as you remember what John's taught you, there’s nothing to be nervous about."

             P "(What? Is she actually trying to make me feel better? Irene?)"

             P "(Then again… her name is on this deal too, so of course she wants it to go well.)"

             P "Thanks."

             jump c1

         "Brush her off":

             P "What’s the big deal? I’m on time, and the guy isn’t even here yet."

             scene c9
             with dissolve

             I "That 'guy' as you call him will be our biggest contract to date, if we’re able to agree to terms."

             I "So for both our sakes, I hope you don’t have such a laissez-faire pitch to convince him to join the company."

             P "(Of course she’s only worried about how she comes out looking in all of this.)"

             P "I got it."

             I "We’ll certainly see."

             jump c1

label c1:

     I "So, where exactly are you coming from? I can’t help but recall your flustered reaction when I called."

     P "(She’s just as smart as she is hot, though I know [rel_f] would never choose a partner less than.)"

     P "Well, yeah… I think that’s the first time you’ve ever called me on the phone, so I was a bit surprised."

     I "You still didn’t answer my question. Where were you?"

     P "(Shit, where did I say I was again?)"

     menu:

         "Watching a movie":

             P "I was, uh… just out watching a movie."

             I "Movie? Didn’t you say you were out on the town?"

             P "O-Oh, yeah… I WAS, but then I went to watch a movie."

             scene c10 #I smile
             with dissolve

             I "You’re not as smart as you think, kid. I’ve been playing this game a lot longer than you have, and it’s clear as day you’re lying."

             scene c11 #I stand up
             with dissolve

             I "You know what? I don’t even need to find out what you’re lying about."

             I "Your [rel_f] actually believed you were stepping up like he’s always wanted."

             I "But he did tell me to keep an eye out for any suspicious behavior, and you can only be up to no good with this little lie about where you’ve been."

             P "(Fuck, what do I say here?!)"

             scene c12 #I walk away
             with dissolve

             I "Goodbye."

             P "Irene, wait!"

             scene bs
             with dissolve

             "The meeting with Buster Himen goes horribly as you fumble your rehearsed pitch several times."

             "But it doesn’t matter as Irene follows through on her threat, and you are forced to return home early."

             "GAME OVER."

             return

         "[gr]Out on the town":

             P "Oh… uh, yeah. I was just checking out the city since it’s so nice."

             P "There’s actually this really nice restaurant I found that seems like they have some good sushi."

             P "You do like sushi, right? You’re always ordering it at home."

             I "…Before we go making any dinner plans, how about we focus on this contract?"

             P "(Good, got her off my back.)"

             P "(At least for now anyway.)"

             P "*smile* Right."

             jump c2

label c2:

     "*door open*"

     BH "Alright, let’s make this quick."

     scene c13 #BH walk in room
     with dissolve

     BH "I have somewhere else to be soon, and I can’t afford to be late."

     I "*mutter* What you can’t afford is another donut."

     "You hold in a laugh."

     P "(Normally I don’t find it cool talking behind people’s backs like [m_nik] says, but I know Buster Himen is your typical corporate asshole.)"

     scene c14 #BM look at MC in suit & Irene smile 3rd
     with dissolve

     BH "So? What is this about?"

     P "(He doesn’t even know what the meeting's about…)"

     scene c15 #BH smile at I
     with dissolve

     BH "I hope a blind date because I think I’ve fallen in love at first sight. *laugh*"

     BH "Zeus Almighty. How are you doing, sweetheart?"

     I "I’m fine. Thank you, Mr. Himen. Though I’m sorry to tell you we’re here for business, not pleasure."

     BH "Hey, nothing says you can’t have a little pleasure too. Hahaha!"

     I "*laugh* Right."

     I "Well, why don’t we at least discuss the business part, so you’re not late for your other engagements?"

     I "*mutter* Pig."

     P "(I think now is my cue to step in.)"

     P "I think you’ll be really excited for what we have to offer you today, Mr. Himen."

     BH "I’m trying to figure out why I’ve never run into such a stunning woman such as yourself when I virtually know everyone that matters in this city."

     P "Mr. Himen, sir?"

     scene c16 #BH neutral at MC. 3rd
     with dissolve

     BH "Huh?"

     P "Ah, yes… I was just saying -"

     BH "Who are you?"

     P "(Always be professional, even if you feel like stabbing the person with the nearest sharpest object.)"

     P "Yes, sir. My partner Irene whom you’ve been getting acquainted with, and myself are here on behalf of the Perving Company."

     P "We have a business offer that we think could greatly benefit us both."

     scene c17 #BH dismissive hand wave
     with dissolve

     BH "You and a million others."

     scene c16
     with dissolve

     BH "Well, I might as well hear it before turning it down since I came all the way out here."

     P "(Isn’t this the office you commute from?)"

     P "Yes, sir. So it’s obvious you have the hottest thing around – a website devoted to beautiful girls streaming video games."

     P "A.k.a. 'e-girls.’"

     P "Which frankly, I’m surprised hasn’t been done until now. There’s only one thing players love more than games – a hot girl playing those games."

     P "If I could’ve watched Mass Erect being playing by a virtual supermodel that actually knew what she was talking about, I would’ve been your first subscription."

     scene c18 #BH smile
     with dissolve

     BH "Ha. What does a young punk like you know about Mass Erect?"

     P "(I know that it’s your favorite game, and I made sure to research like hell on it before coming here, and even did an all-nighter playing it.)"

     scene c19 #BH standing and arms up, excited
     with dissolve

     "You and Buster Himen go back and forth about the characters, levels and everything else for several minutes."

     P "(Okay, time to steer the conversation back on track.)"

     scene c20 #BH standing normal smile
     with dissolve

     P "And do you remember the party mission where Commander Leopard is wearing the sci-fi outfit?"

     P "The Perving Company wants to give your e-girls the option to try a new brand of the same type of clothes, specifically geared towards them."

     P "Hot, but still stylish and practical."

     BH "You had me at hot. Hahaha."

     BH "Show me the goods, kid."

     P "(Awesome, he seems interested, unlike before. This is going way better than I expected, but I really have been trained for this.)"

     P "Of course."

     scene c21 #MC turns towards I look at him. 3rd BH look at I
     with dissolve

     P "Irene, can you please show him the sample?"

     I "It would be my pleasure."

     scene c22 #I stand to show outfit to BH. MC stand too
     with dissolve

     I "Not only are the clothes stylish and attractive as my partner mentioned, but we also have plans to implement several features."

     I "For example, headphones jacks directly into the clothes and Wi-Fi compatibility, which we can discuss further, provided you’re interested, of course."

     BH "*whistle* Big shit. But I can’t just stare at the outfits. I gotta see 'em in action."

     I "Oh, absolutely. My apologies. We’ve brought several pictures of our models -"

     BH "I’m sorry, gorgeous, but that ain’t gonna cut it. I need to see them up close and personal."

     BH "So unless you got a model lying somewhere around here, we’re gonna have to postpone this meeting."

     P "(No, no, no. That’s not good at all! Postponing this meeting would kill all the momentum we built up today.)"

     menu:

         "Don’t ask":

             P "(There’s no way she would agree to modeling for this sleazeball, so I’m not even going to put myself through the embarrassment of asking.)"

             scene bs
             with dissolve
             stop music
             "You and Irene manage to convince Buster Himen to check out a model on a video call, and that seems to satisfy him."

             scene c53 #from c51 with original clothes for I, MC and I facing BH smiling
             with dissolve
             #play music "ITS - Mr-Debonair.mp3"
             BH "Alright, I admit that this idea doesn’t seem too bad."

             BH "So, I’m throwing a shindig very soon, so feel free to come and we can talk more."

             I "That sounds great, Mr. Himen. My partner and I would be honored to attend your party."

             P "Definitely. Thank you, Mr. Himen. We look for to discussing the particulars of our proposed contract."

             scene c54 #BH looks at I 3rd from c52
             with dissolve

             BH "Hopefully I get to see you in an outfit just as sexy as the one you showed me here today."

             I "I’ll have to see what I have lying around."

             BH "Hell, I’m sure you would look incredible in a towel, sweetheart. And I sure as hell wouldn’t complain if you decided to go that route. Hahaha!"

             I "*laugh* I wouldn’t want to cause a scene, so I’ll pass on that for the time being."

             "You talk a little more before he finally leaves."

             jump ch3help


         "Ask her to model [IrenePath]":

            $ ipts = ipts + 1

            scene bs
            stop music
            "You quickly excuse yourself and Irene to talk outside."

            scene c23 #cam facing Irene outside
            with dissolve
            #play music "ITS - Mr-Debonair.mp3"
            I "What is so important that you needed to practically drag me out of the meeting?"

            P "It won’t be for much longer if we don’t find a model."

            I "Well, I’m not much of a magician, so if you’re betting on me pulling one out of my magic hat, then you’re out of luck."

            P "(I NEED this meeting to go well. The more it does, the higher my chances of staying here and being with the girls.)"

            P "How about pulling yourself out of your hat?"

            I "What? I have no idea what that means."

            P "I was… trying to… use your…"

            P "*cough* Never mind."

            P "What I’m trying to say is, you can be the model."

            scene c24 #I smile
            with dissolve

            I "*laugh* That’s pretty funny. You almost looked serious there for a second."

            P "Because I was – I am."

            scene c25 #I frown and change pose
            with dissolve

            I "What do you think I am? Some piece of ass to just parade around?"

            P "No, you’re my partner, and I’m asking for your help right now."

            I "…"

            scene c26 #I looks to the side
            with dissolve

            I "Did you see the way that lummox was ogling me? And you expect me to practically strip naked in front of him."

            P "You’re a beautiful woman, Irene. You gotta be used to creeps checking you out by now."

            I "That doesn’t mean I like it, [p_name]. There’s no getting used to being treated like a a walking ass with tits attached."

            P "I… understand."

            P "(Then why does she dress like she does? Unless it’s because of [rel_f]…)"

            P "Then for making you go through this, I’ll let you get whatever you want at that fancy restaurant I was talking about earlier."

            scene c24
            with dissolve

            I "*laugh* You’re actually trying to bribe me?"

            P "No, of course not!"

            P "Well… maybe a smidge."

            P "*smile* Did I mention they had sushi, your favorite?"

            I "*laugh* Alright, alright, kid. You butter me up any more and I’m going to need to be served alongside some coffee."

            I "You’re lucky I really do like my sushi."

            scene c23
            with dissolve

            I "But I’m going to need your help to squeeze into the outfit. It’s a couple sizes small."

            P "(She feels comfortable enough to let me see her in her underwear? Maybe she trusts that I don’t look at her like a piece of ass…)"

            P "(Which isn’t saying much, since I basically look at her like my enemy, and I’m sure she knows that.)"

            P "Uh, sure. No problem."

            scene bs
            with dissolve
            stop music
            "You two inform Buster Himen of your impromptu model, and he lets you use the meeting room to get ready."

            scene c27 #cam looking at door or window
            with dissolve
            #play music "ITS - Mr-Debonair.mp3"
            I "Alright, you can turn around. I’ve gotten as far as I can myself."

            "(You can’t help but be a little nervous about helping such an attractive woman – your [rel_f]'s wife into a skimpy outfit.)"

            P "(At least Mr. Himen let us use the meeting room to get ready. I guess he’s not a total asshole when doing business he's interested in.)"

            P "(Or… he might really just want to see Irene in the gamer girl outfit.)"

            P "Alright, I’m turning around now."

            scene c28 #I half dressed
            with dissolve

            "Your dick twitches at the sight of the blonde bombshell barely dressed."

            "…"

            I "Are you going to help me, or do you need an invitation?"

            P "Ah, sorry… I’m just trying to figure out the best position to help get the outfit on."

            P "(Total lie. Though I really am thinking about that now.)"

            I "The bottom’s still a bit loose. Just yank them up while I hold onto you."

            P "Yeah, the simplest way may be the best way."

            scene c29 #Mc grab I waist. I put hand on his shoulders 3rd
            with dissolve

            P "Ready?"

            I "Yes, go ahead."

            "You put a moderate amount of force into pulling the outfit up, but it barely moves over Irene’s voluptuous butt."

            "So you grit your teeth and pull even harder, but you only make little progress."

            scene c30 #MC move head back to look at I 3rd
            with dissolve

            P "Do you mind if I get closer to get a better grip?"

            I "*sigh* Just do what you have to do."

            P "Thanks."

            scene c30-1 #MC press against I to pull up short
            with dissolve

            "You try to ignore the amazing sensation of Irene’s double D tits pressed against you, and the incredible scent of her lavender perfume."

            P "(Think of grandma vaginas! You CANNOT get hard here!)"

            "With the might of 100 men, you endure your lust and refocus on getting the e-girl outfit past Irene’s ass."

            "But to no avail."

            scene c30
            with dissolve

            P "I can’t do it in this position after all, Irene."

            I "First time a guy’s ever told me that."

            P "*laugh* I believe that."

            scene c31 #I smile and raise eyebrow 3rd
            with dissolve

            I "Do you, now?"

            P "*cough* Um, anyway…"

            P "I’m thinking we might have better luck if you lean over the table and I get behind you."

            scene c28
            with dissolve

            I "You want me to lean over the table?"

            P "I do think it’ll help. But I totally understand if you’re too uncomfortable."

            I "…"

            I "Let’s just get this over with, please."

            "You two get in position."

            scene c34 #cam on I backside
            with dissolve

            P "(Remember, this is for business, so try not to be a typical 20-year-old and perv out.)"

            P "*deep breath* (Okay.)"

            scene c35 #MC holding I waist. Underhanded
            with dissolve

            P "I’m going to pull now."

            "You don’t wait for a response and put all strength into your arms, and you do manage to get some of the outfit further passed her bubble butt."

            scene c36 #MC crotch pressed and lean more I. 3rd
            with dissolve

            I "H-Hey -"

            P "*grit teeth* I… think… it’s working…"

            "Irene groans uncomfortably as you focus on getting the rest of the outfit on."

            P "Ah, I think I got it!"

            scene c37 #cam back away
            with dissolve

            "You back up."

            scene c38 #i looking down at self
            with dissolve

            I "Hmm… I was really starting to doubt this whole thing, but I guess that position did do the trick."

            scene c28
            with dissolve

            I "What now?"

            P "(I guess she trusts my methods now… Though I’m not so sure she’s going to like this one.)"

            P "Getting the top on is a tricky because we’re basically on the same level."

            I "Which means you need to go higher, or I need to go lower."

            P "Yeah… Like on your knees?"

            "You try to keep your nervousness from showing."

            scene c40 #I mad
            with dissolve

            I "What? There is no way I am getting on my knees in front of you. I don't care if we have to postpone this meeting."

            P "(I can’t say I don’t understand her reluctance, but shit. How can I convince her? I've already bribed her.)"

            P "What did you want to be growing up?"

            scene c41 #I confused
            with dissolve

            I "What are you talking about now?"

            P "Like a princess or something? Maybe even a queen?"

            scene c28
            with dissolve

            I "…"

            I "Sure, but I really don’t get where you’re going with this."

            P "Well, just pretend you’re a knight getting knighted on their knees or something."

            P "Yeah, I got it. You’ve just come back from slaying a dragon, and are being knighted. Knight Irene!"

            scene c42 #I smile
            with dissolve

            I "*snort* What… I don’t even…"

            I "Don’t you think that’s a bit of a reach from wanting to be a princess?"

            P "*smile* Ah, well, a little. But I figure you’re the type to want to be a strong knight instead of a princess. Now, anyway."

            I "Well, I won’t say you’re wrong there."

            I "What’s so glorious about sitting around all day while you get fat? When you want a stone turned, it’s often better to do it yourself."

            P "(I believe her. She’s always working alongside [rel_f] and accompanying him on his business trips instead of just lazing around the house, or taking it easy.)"

            P "Like my attempt at convincing you to get on your knees, this whole situation is a bit silly."

            P "But we’re literally half way done, and having this meeting go well greatly benefits us both."

            scene c28
            with dissolve

            "Irene blows out a defeated breath."

            scene c43 #I look to side on knees
            with dissolve

            "She doesn’t seem like she’s going to say anymore, giving you the cue to proceed."

            scene c44 #cam closer
            with dissolve

            P "(I seriously had my doubts she would continue to go along with any of this, but it really isn’t a huge deal if we don’t make it.)"

            scene c45 #cam hands on top. 3rd
            with dissolve

            I "Why don’t you have a girlfriend?"

            scene c45-2 #cam hands on top
            with dissolve

            P "What?"

            "Her unexpected question makes you pause on the pulling, but you soon start again."

            I "Obviously, I haven’t been around for an extended period of time, but I’ve never seen you go out or bring any girls home."

            I "Are you not interested in women?"

            menu:

                "Answer her [IrenePath]":
                    $ ipts = ipts + 1
                    P "*laugh* Do I give off gay vibes to you?"

                    scene c46 #I look at cam
                    with dissolve

                    I "Gay vibes?"

                    P "Sure, like the typical 'gay voice' some might call it."

                    P "*clear throat* Ohhh myyy gooddd, that outfit is sooo cuuute!"

                    scene c47 #I smile
                    with dissolve

                    I "That was so well done that I’m starting to think that’s the real [p_name] just wanting to 'come out.’"

                    P "*laugh* Nice play on words there, but I’m straight."

                    P "(But I like the wrong girls, and it’s getting way harder to control myself around them everyday…)"

                    I "That’s what I thought, so why no dating?"

                    P "*shrug* You know how [rel_f] keeps me busy, so I’ve just been kinda focusing on the job right now."

                    I "He just wants the best for you."

                    P "You don’t know anything."

                    "You snap back without thinking."

                    scene c46
                    with dissolve

                    I "…"

                    P "(Shit, let’s not can get on her bad side after coming this far.)"
                    jump ch3help2

                "Don’t answer":

                    P "(Why is she asking me that?)"

                    P "I’m sorry, but I can’t really talk and focus on doing this at the same time."

                    jump ch3help2

label ch3help2:

    scene c45
    with dissolve

    "You manage to pull the top half over her tits after a bit more."

    scene c48 #cam back up
    with dissolve

    P "Alright, we did it!"

    scene c49 #I smile stand
    with dissolve

    I "I suppose we did."

    scene c50 #I modeling for BH 3rd
    with dissolve

    "You call Buster Himen back, and he checks out the e-girl outfit."

    BH "Alright, I admit that this that I’m interested in discussing this endeavor further."

    BH "So, I’m throwing a shindig very soon, so feel free to come and we can talk more."

    I "That sounds great, Mr. Himen. My partner and I would be honored to attend your party."

    P "Definitely. Thank you, Mr. Himen. We look forward to discussing the particulars of our proposed contract."

    scene c52 #I stand straight.  3rd
    with dissolve

    BH "I hope to see you in something just as sexy there."

    I "I’ll have to see what I have lying around."

    BH "Hell, I’m sure you would look incredible in towel, sweetie. And I sure as hell wouldn’t complain if you decided to go that route. Hahaha!"

    I "*laugh* I wouldn’t want to cause a scene, so I’ll pass on that for the time being."

    scene bs
    with dissolve
    stop music
    "You talk a little more before he finally leaves, and you wait outside until Irene changes back into her dress."

    jump ch3help


label ch3help:

    scene c55 #cam face annoyed I
    with dissolve
    #play music "ITS - Mr-Debonair.mp3"
    I "Ugh, I feel like I need to take a shower – no, 2 showers after dealing with that creep."

    P "Ha, yeah… I’m kind of disgusted for you. There were a few times I wanted to tell him to chill out, but that obviously would’ve screwed everything up."

    scene c56 #I neutral
    with dissolve

    I "It certainly would. Sometimes you have no choice but to deal with his type to get anywhere."

    P "(Sounds like she’s talking from experience. And with how attractive she is, I’m sure plenty of guys like Buster Himen have harassed her.)"

    I "Anyway, good work today. I was hesitant about sitting back and letting you take point, but you handled everything pretty well."

    I "We’ll talk again soon and strategize for the party."

    P "Sounds good. Thanks."

    scene bs
    with dissolve
    stop music
    "You separate with Irene from there and return to the girls' house."

    scene c57 #cam look at house door
    with dissolve
    #play music "GTS-Uplifting-Acoustic-Background-No-Vocal-Edit.mp3"
    P "(I seriously was nervous for today, and the while everything didn't go off without a hitch, we’re still in line to get the contract, and that's all that matters.)"

    P "*smile* (I think things will turn out okay after all. And Irene's suspicions seemed to have gone down a bit too.)"

    I "So, this is where you’ve been spending your time."
    stop music
    "Time seems to freeze as you suddenly break out in a cold sweat."

    I "I’m sure your [rel_f] would be VERY, VERY interested to know too."

    "Almost like a robot being activated for the first time, you mechanically turn towards the voice."
    #play music "PENSIVE - Black-And-White-City.mp3"
    P "(Irene…)"

    "You almost expect to see no one there, as if you were just imagining things."

    scene c59
    with dissolve

    "But you aren’t that lucky."

    I "So, this is the reason you wanted to come out here. Just for a vacation with your [rel_fam]."

    P "(What do I say here?! She totally caught me!)"

    P "I-Irene, please, you can’t say anything."

    I "And why not? I’ll admit you showed some skills back at the meeting, but it’s clear the whole speech to John about taking over the company was a false one."

    I "When there’s no incentive like this in it for future contracts, do you really think you’ll be as motivated?"

    I "We both know you’re not interested in the logistics of the business, which is fine. But let’s not pretend you are."

    I "Trust me. I'm doing you a favor in the long run. You’d just end up miserable later."

    P "Y-You don’t understand."

    I "I think I’m the one who should be saying that, but you’re a smart kid. I’m sure one day you’ll figure it out."

    scene c60 #I walk away
    with dissolve

    I "Goodbye."

    P "(N-No, I can’t let her leave!)"

    scene c61 #cam grab I arm
    with dissolve

    P "W-Wait!"

    scene c62 #I mad face cam
    with dissolve

    I "Who do you think you are grabbing me like that?"

    P "(Damn, I was kinda forceful. I seriously need to calm down.) *deep breath*"

    P "I’m sorry, Irene. I was just trying to stop you from leaving, but I had no right to grab you like that."

    P "Can you please just hear me out for a minute?"

    scene c59
    with dissolve

    I "…"

    I "I’m listening."

    P "*deep breath* (The truth shall set you free.)"

    P "I know that you think I just wanted to come out here for a vacation, but I swear that isn’t true."

    P "My [rel_m] and [rel_s] have been going through some things, so I just wanted to be there for them."

    I "I’m not finding the correlation between that and you using the contract as an excuse to be here."

    P "You know that my [rel_f] wouldn’t want me to come down."

    I "Because you’re in the middle of training, and he doesn’t want you distracted, which I admit is a bit strict, true."

    I "But if you were just upfront about coming out for a week or two, I’m sure it would’ve been fine."

    P "*laugh* Yeah? Then why did he make me sign a contract that states if I were to ever even VISIT the girls, he would cut off all financial aid to them immediately."

    P "So Coral being in college and Zoe being in law school, or whatever else they wanted to do would be impossible because they don’t have a penny that his name isn’t attached to."

    P "(Which he purposely made that way. Bastard.)"

    scene c58
    with dissolve

    I "Ha. And you expect me to believe John would go that far to keep me from seeing your [rel_fam]?"

    P "Yes, he says they make me too soft. Too weak."

    I "This is ludicrous. Do you even hear what you’re saying? A contract not to see your own [rel_fam]?"

    P "*grit teeth* (She has to believe me!)"

    P "You’re obviously a smart woman, Irene. Do you think that what I’m saying is above the man you’re married to?"

    P "Honestly, really think about it."

    P "(I’m taking a huge gamble here, but he’s had to shown her his psychotic side in their time together, even if it hasn't been that long.)"

    scene c59
    with dissolve


    I "…"

    P "(She isn’t saying anything… So… he has?)"

    "*door open*"

    N "Oh…"

    N "I thought I heard voices out here."

    scene c63 #cam on N smiling at him
    with dissolve
    stop music
    P "[m_nik]…"

    N "Hi, puddin'. I was just fixin' to call you with you bein' gone fer so long."

    P "Ah, yeah… I’m really sorry about that. Traffic was a bit more than I expected."

    N "It’s fine, darlin'. I’m just so happy yer back."

    scene c64 #N look at I & I neu look at N
    with dissolve

    N "Though I admit I’m a little confused as to what yer doin' down here with my boy, Irene."

    I "I… just had some business to attend to in this area, and had some things to discuss with him regarding the company."

    N "I see…"

    P "(I think this is literally the first time they’ve ever had a conversation. You could cut the awkwardness with a knife.)"


    N "Would you like to come in for a little pizza? I would’ve cooked somethin' proper if I knew you’d be visitin'."


    I "Oh, no, thank you."

    N "Come on, you tellin' me a big city gal like yerself doesn’t like pizza?"

    scene c67 #I surprised
    with dissolve

    I "Wha…"

    scene c68 #I smile
    with dissolve

    I "*laugh* I guess I’m not. Okay, I’ll take a slice or two."

    P "(What just happened?)"

    scene c68-2 #focus on N
    with dissolve

    P "([m_nik]'s ability to disarm people really should be a superpower. I just hope the rest of this little meeting goes as well.)"

    "And there is still obviously the dilemma of Irene spilling the beans about your visit."

    scene c69 #N & I smiling at table across from each other with pizza
    with dissolve

    "But all you can do is shut up and smile as the 2 women chat over the meal."

    scene bs
    with dissolve

    "Until eventually going off for a walk at your [rel_m]'s request."

    scene c70 #N & I walking side by side,  lookingforward smiilde
    with dissolve
    #play music "GTS-Uplifting-Acoustic-Background-No-Vocal-Edit.mp3"
    I "Thank you again for the pizza, Norah. I wasn’t expecting it to be as good as home, so it was a very pleasant surprise."

    I "Probably shouldn’t have had so many slices, though… My trainer is going to eat ME for lunch when I return."

    scene c71 #N look at I
    with dissolve

    N "*giggle* Oh, I doubt that with how good of a shape yer in. You could stand to gain a few more pounds from where I’m lookin'."

    I "Let’s hope she feels that way."

    scene c70
    with dissolve

    "There’s a lull in conversation as they continue to walk."

    N "You know, I didn’t like you for quite some time durin’ the divorce and everything happenin', but I realized I was bein' childish."

    N "I’ve wanted to talk with you like this for a while, but I was too chicken to reach out and call."

    scene c72 #I neu look at N
    with dissolve

    I "I can’t say I blame you for your dislike. When another woman enters the picture and then there’s suddenly a divorce…"

    scene c72-2 #N look at I
    with dissolve

    N "*shake head* John and I were done for years before you showed, so yer presence only revealed the truth of everything."

    N "So honestly? I’m grateful for you."

    I "Ha. This is definitely a new experience for me. Being thanked by my man’s ex."

    I "But… I’m glad there’s no animosity between us. There’s no real reason there should be."

    I "Unless you want John back?"

    N "*giggle* No, he’s all yers."

    I "*laugh* Then we are golden."

    scene c73 #N smiling, I confused
    with dissolve

    "Norah suddenly stops walking, forcing Irene to do the same."

    I "Is something wrong?"

    N "Oh, no, not at all. I just wanted to say that I appreciate you bein' so cordial with me."

    N "And I hope you can have an even better relationship with [p_name]. I’m sure you know he’s very important to me."

    N "And with you being his new [rel_m], that makes you important to me also."

    scene c74 #N grab I hands. I look at N hands
    with dissolve

    N "So please take care of him for me."

    scene c75 #I hesitate look at N
    with dissolve

    I "I… will…"

    N "Thank you, Irene. This means more to me than you’ll ever know."

    scene bs
    with dissolve
    stop music
    "Norah and Irene soon return to the house and you see her to her car."

    scene c76 #cam on I walking. HDRI?
    with dissolve
    #play music "PENSIVE - Black-And-White-City.mp3"
    P "(I’ve been racking my brain for a way to convince Irene not to snitch, but I haven’t come up with jack shit!)"

    P "(I’m totally screwed, aren’t I…?)"

    I "I can sense you practically ready to jump off a cliff over there, but you can relax."

    I "I’m not going to say anything."

    "Her words stop you dead in your tracks."
    stop music
    P "YOU’RE NOT?"

    scene c77 #I face cam
    with dissolve

    I "That’s right."

    P "What…"

    P "(I don’t understand. She can completely and utterly screw me over with a simple phone call…)"

    P "(So why in the hell isn’t she?)"

    P "But don’t you want the company…?"

    I "No. I just want the next person running it to know what they’re doing. That’s my duty as vice president."

    P "Oh…"

    P "(And like she said earlier, since I haven’t exactly shown the most enthusiasm until now, she wanted to just replace me as the next guy in line.)"

    scene c78 #I look to side, a little nervous. Maybe grab arm
    with dissolve

    I "Listen… I know that we haven’t exactly started off on the right foot, which is my fault as the adult here."

    I "So, I apologize…"

    scene c79 #I nervous reach out hand to shake
    with dissolve

    I "And… um, if you’re willing, I would like to start over."

    menu:

        "Shake her hand":
            $ ipts = ipts + 1

            P "(She’s extending an olive branch and saying she’s not going to tell my [rel_f] anything.)"

            P "(I’d be out of my noggin to not at least pretend to be cool with her.)"

            scene c80 #cam shake I hand
            with dissolve

            P "*smile* We can definitely do that."

            scene c81 #I smile
            with dissolve
            #play music "ITS2-Les-Souvenirs.mp3"
            I "Thank you, [p_name]. I appreciate you being so understanding."

            jump ch3hug

        "Hug her [IrenePath]":
            $ ipts = ipts + 2
            scene c82 #MC hug I surprised. 3rd
            with dissolve

            "Without thinking, you lunge forward."

            I "What are you???"

            P "I’m sorry for being such an asshole too, Irene. From the second you appeared, I blamed you for everything."

            P "But I know that the divorce wasn’t your fault, so again, I am sorry."

            scene c83 #I nervous 3rd
            with dissolve

            I "It’s…"

            scene c84 #I smile and hug back 3rd
            with dissolve
            #play music "ITS2-Les-Souvenirs.mp3"
            I "Okay… I forgive you, [p_name]."

            "You hug for a few more seconds before separating."

            jump ch3hug

label ch3hug:

     scene c81
     with dissolve

     I "So like we planned before, we’ll talk again when Himen contacts us about the party."

     I "I hope it’s okay if I still help you on securing the contract?"

     P "Oh… sure, of course. *smile*"

     P "(Remember, better to play nice with our new relationship being literally less than 5 minutes old.)"

     I "Oh, and before I leave, would you like to take one of the e-girl outfits to give to Coral? She loves video games, doesn’t she?"

     P "That’s like asking if a fat kid loves cake."

     I "*laugh* In that case, I’ll give you a few for her."

     P "Thanks, Irene. That’s really cool of you."

     P "(I have no clue why she suddenly wanted to start over with me, but it’s not a bad thing. I can focus more on the girls this way.)"

     scene bs
     with dissolve
     stop music
     "You do take a couple of the outfits for Coral, and say your goodbyes to Irene for the second time that day."
     "Then change before heading to Coral’s room."

     scene a127
     with dissolve

     P "(I almost feel like I’m dreaming with what just happened, but Irene DID find out about my secret visit, and now we’re… cool?)"

     P "*laugh* They do say reality is stranger than fiction."

     P "(Anyway, I want to check on Coral to see how her research is going.)"

     P "(I thought about giving her the e-girl outfits, but it would be better to hold off till we’re on better terms.)"

     P "(Don’t want her to think I’m trying to buy her forgiveness since I already gave her Immortal Fighting when I arrived.)"

     scene c87 #C open door
     with dissolve
     #play music "CTS - Away-With-You-Loop.mp3"

     C "I thought I heard someone outside my door. What are you doing?"

     P "What does it look like? I was obviously stalking you."

     P "I’m the biggest fan of King Reef! Can you sign my face? I’ll never wash it again."

     scene c88 #C slight smile
     with dissolve

     C "You’re not funny."

     "Despite her words, you see a slight smile tugging at the corners of her mouth."

     P "*smile* How’s the researching coming along?"

     scene c87
     with dissolve

     C "Alright. There’s not a ton of info since the game isn’t even technically out yet, so I’m almost done figuring out which characters are best for tag team mode and stuff."

     scene c89 #cam walk past C
     with dissolve

     P "Awesome, then I’ll practice while you wrap things up."

     scene a143
     with dissolve

     C "Hey, what do you think you’re doing???"

     P "Practicing, remember? I just said it 2 seconds ago."

     "You hear Coral growl behind you, but she doesn’t say anything else."

     P "(This isn’t the first… or second time Coral's been mad at me for something, so I know the best way to wear her down is to hang around.)"

     scene c91 #cam on TV. Mortal Kombat on screen ***use canva***
     with dissolve

     "You fire up the game while Coral lays on her bed with a laptop."

     P "Coral, which character is the best to use for fighting against Scorpio in tag team?"

     C "Uhhh, hold on."

     "…"

     C "They say Jack or Sub One is the best."

     P "Can you please come over here, so I don’t have to strain to hear you?"

     C "But I’m comfortable laying down. And I’m literally a few feet away."

     P "(She’s right. I can hear her perfectly, but I want her near.)"

     P "Alright. But if we lose because you were too comfortable on your bed, don’t blame me."

     C "Ugh, fine."

     scene c92 #C neu at cam with laptop on sofa
     with dissolve

     "Coral comes over."

     C "Happy?"

     P "*smile* A little."

     scene c93 #C typing on laptop
     with dissolve

     "She goes back to researching while you play."

     P "Hey, I was wondering about you being King Reef and everything. Why that pseudonym?"

     C "No reason, really."

     P "Hmm."

     P "(Why does it sound so familiar…)"

     P "Wait, I remember calling you Coral Reef when we were kids. Is that why?"

     scene c94 #C nervous
     with dissolve

     C "N-No. It… was just a name I made up..."

     menu:

          "Tease her":

             $ cpts = cpts - 1

             P "Haha. Come on. It totally is, isn’t? Admit ittt."

             scene c95 #c mad look at cam
             with dissolve
             C "I said no, okay?"

             P "(Ah… maybe it wasn't the best idea to tease.)"

             P "(I know I usually do, but I have to remember she really is upset with me right now.)"

             P "(Better just drop it.)"

             jump ch3tease

          "Don’t tease [CoralPath]":

             "You hold back a knowing smile."

             P "(As much as I would love to tease her like usual, I have to remember she really is upset with me.)"

             jump ch3tease

label ch3tease:

    scene c93
    with dissolve

    "You go back to playing."

    "*hour later*"

    scene c92
    with dissolve

    C "Okay, I’m pretty much done."

    "You pause the game."

    P "Cool, wanna practice a bit?"

    C "*shrug* Why not?"

    scene c97 #C playing
    with dissolve
    stop music
    "You and Coral practice for a couple of hours and realize how in sync you are in tag team mode."

    "So you decide to go online for a few practice matches."

    "Soon, a few turns into a dozen, and a dozen turns into several dozens until you both are playing until the sun comes up."

    P "*yawn* I think we should probably call it a night, Coral… Though I think we can safely say day now."

    P "How long have we been playing?"

    C "Like 9 hours or something."

    scene c98 #C excited
    with dissolve

    C "But that’s besides the point! We only have ONE more match until we crack the top 1,000!"

    P "(Might as well tough it out for another match, even though I feel like passing out.)"

    scene c97
    with dissolve
    #play music "Rock-Party-30-Sec-Intro.mp3"
    "You start the final match, and it comes down to the final round."

    P "Player 1 is going in for the grab, jump over him."

    C "Alright, I’m gonna send a combo at him as soon as I land. Grab him from behind."

    "You try to do as she says, but player 2 attacks you."

    P "Shit, can’t. Can you rejoin me?"

    C "Yeah, hold on."

    "Coral fights her way back to you."

    P "Let’s do our special move."

    C "Now? Don’t you think it's a bit early?"

    P "Yeah, but it’ll throw them off guard."

    "Your opponents do the exact same thing, and activate their special move a split second before you."

    "The results are devastating as your character dies, and Coral is left to fight alone."

    P "*kiss teeth* Are you kidding me?"

    P "Watch out for the pincer attack, Coral. They’re going to try to get you from both sides."

    C "I know."

    scene c99 #C pain and move a bit
    with dissolve

    C "Ah, shit!"

    P "Hey, you okay? What’s wrong?"

    scene c101 #C look at cam
    with dissolve

    C "I have a serious hand cramp!"

    P "(That’s what happens when you play a fighting game for 9 hours straight. Surprised it didn’t happen to either of us sooner.)"

    C "Take the controller from me and play!"

    scene c102 #cam reach to take control
    with dissolve

    "You hurriedly do as she says, but she doesn’t let go."

    P "Coral, let go."

    C "I can’t!"

    P "(Oh boy.)"

    C "Hurry!!! They’re killing me!!!"

    P "Wh-What do you want me to do here?"

    C "Jump behind me and help me play!"

    scene c103 #MC behind C playing. C smile. 3rd
    with dissolve

    "You do, seeing her character on screen getting pummeled and immediately start fighting back."

    C "Yeah, let’s kick that jerkface's butt!"

    P "Coral's excitement makes her wiggle and move around, making her small, firm ass rub against your crotch."

    P "(Well, I have to say, this is not good at all.)"

    "You try to stay calm while focusing on the game, but it gets increasingly more difficult each time she shifts."

    P "(S-Should I just lose, so she stops?)"

    P "(No… I can’t do that to her when she’s so excited. I just have to endure."

    "Even though a part of you is doing it for your little [rel_s], it would be a lie to say you didn’t enjoy the sensations of her practically grinding on you."

    C "Hehehe, yeah!"

    scene c104 #C eyes open and confused
    with dissolve

    C "Huh?"

    P "(Fuck, I got a half chub, and she totally feels it!)"

    scene c105 #C look down nervous
    with dissolve

    "You try to ignore the incredibly awkward situation and focus on the final round of the match as it winds down."

    scene c106 #cam on C nervous
    with dissolve
    stop music
    "A minute later, you are finally able to pull out the narrow victory."

    scene c107
    with dissolve

    "But Coral doesn’t react, simply getting off you."

    P "Um, Coral? I won the match…"

    C "Yeah…"

    P "(I don’t know what to do here. Admit I have an erection or pretend nothing happened!)"

    P "(But I should probably get out of this situation first!)"


    if nshower == True:

        P "(I remember taking a shower with [m_nik] where she saw my erection, but she acted like it was no big deal.)"

        P "(Which made a very awkward moment much less… So maybe I should try to do the same here.)"
    else:
        P "(I think it’d be best to just be nonchalant about the whole thing rather than pretending it didn’t happen when she so obviously felt something.)"

    P "Hey, Coral… I’m really sorry about… my reaction just now. You were just moving around so much, so that caused a bit too much stimulation. *forced laugh*"

    C "But isn’t that weird for you to get 'stimulated' when I’M the one doing it?"

    menu:

        "It isn’t weird [CoralPath]":
            $ cpts = cpts + 1
            $ croute = True

            P "I don’t think so."

            P "I think you’re a pretty girl, even if you are my [rel_s]."

            scene c108 #C smile at cam
            with dissolve

            C "Really?"

            P "*smile* Yeah, I do."

            scene c109 #cam hand touch her hair
            with dissolve

            P "And I’ve been meaning to tell you I like what you did with your hair. Of course I liked the old style too, but this one is really cute."

            C "Thanks… I saw one of my favorite MeTubers have a similar hairstyle, so I just wanted to try it out."

            P "Well, it suits you."

            jump ch3hair

        "It is weird":

            P "Ah, maybe a little… But that doesn’t change the fact that you’re a pretty girl."

            scene c108
            with dissolve

            C "Really?"

            P "*smile* Yeah."

            jump ch3hair

label ch3hair:

    scene c110 #C look at cam neu
    with dissolve

    C "…"

    P "Coral?"
    #play music "SAD-Emotional-Guitars.mp3"
    C "I’m still really mad at you."

    P "I know… And you have every reason to be."

    scene c107
    with dissolve

    C "We planned to develop a dating simulator for almost a whole year."

    C "Figuring out the code, getting assets, building an entire new engine…"

    C "And then poof, you suddenly disappear when the divorce happened."

    P "I didn’t disappear, Coral…"

    scene c110
    with dissolve

    C "You might as well have."

    P "You’re right… You’re right, and I know I’ve apologized a million times, but I AM sorry."

    C "Why did you choose to live with John in the first place?"

    P "(Literally no one calls him what he is to us… Except me, I guess.)"

    P "(And just like [m_nik], Coral is asking the million-dollar question. Hopefully, it goes better this time around.)"

    "You remember your [rel_fam] initially freaking out when you wouldn’t divulge the reason for your abandonment."

    P "To… protect all of you."

    scene c111 #C mad
    with dissolve

    C "What? Did that asshole threaten you or something? Threaten us?"

    C "I bet if we told Zoe or Leanne -"

    P "No, Coral. That’s exactly what I DON’T want. I just told you because I trust you and I owe you some answers, probably more than anyone."

    scene c107
    with dissolve

    C "…"

    P "I promise I’ll figure something out, so you just have to trust me like I trust you, okay?"

    C "Alright..."

    P "And you should totally turn me down right now, but I’m going to ask you anyway…"

    P "Will you work on the dating sim with me again?"

    C "Yeah."

    P "Wh-What? Really?"

    scene c108
    with dissolve

    C "Why are you acting so surprised when you’re the one who asked?"

    P "Ha. I guess I was just expecting you to say no, but this is awesome! Thanks for giving me another chance, Cor."

    C "You’re welcome."

    scene c107
    with dissolve

    C "But if you do something like that again, I’ll never forgive you."

    scene c112 #C crying, but still neutral
    with dissolve

    C "Especially if you just leave without saying goodbye."

    P "(That was another part of the contract, just leaving without the 'weak' and emotional farewells.)"

    P "(But... is Coral crying? I can count on one hand the times I've seen her cry in my entire life.)"

    P "(I’m starting to realize how much I hurt the girls by doing all this.)"

    P "I swear I won’t ever do anything like that again."

    P "*smile* Scout's honor."

    scene c113 #C hug cam
    with dissolve

    P "Oh."

    "After the initial surprise, you smile and hug your little [rel_s] back."

    if croute == True:

        P " (I could literally hold her like this forever. And she smells so damn good.)"

    "You finally separate after several seconds, and Coral wipes her tears."

    scene c108
    with dissolve

    P "How are your hands feeling now?"

    scene c114 #C look at hands
    with dissolve

    C "They’re okay."

    P "Good. We should probably get some sleep before we both pass out, but we’ll talk more about the dating sim later, alright?"

    scene c107
    with dissolve

    C "Alright, sounds good."

    P "I love you."

    scene c108
    with dissolve

    C "*giggle* You’re so sappy sometimes. I love you too, big [rel_b]."

    P "(Getting on good terms with Irene and making up with Coral is not what I expected when I woke up today, but I’m seriously lucky it turned out this way.)"

    scene bs
    with dissolve
    stop music
    "You leave Coral’s room and immediately collapse in your bed."

    jump U4
