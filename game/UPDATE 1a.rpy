define P = Character('[p_name]', color="#00a8f3")
define J = Character('John', color="#ffffff")
define BH = Character('Buster Himen', color="#ff6666")
define sc = Character('Store Clerk', color="#ffffff")
define s = Character('Stern Female Voice', color="#ffffff")
define Z = Character('Zoe', color="#ff471a")
define rfv = Character('Raspy Female Voice', color="#ffffff")
define L = Character('Leanne', color="#ff6666")
define uf = Character('Unknown Female', color="ffffff")
define WO = Character('Woman', color="ffffff")
define RR = Character('Old Woman', color="ffffff")
define WW = Character('Man', color="ffffff")
define N = Character('Norah', color="#ff0000")
define C = Character('Coral', color="#e6e600")
define I = Character('Irene', color="#cc00cc")
define A = Character('Sasha', color="#ffffff")
define M = Character('Miracle', color="#ffffff")
define TG = Character('Tattooed Girl', color="#ffffff")
define BG = Character('Brunette Girl', color="#ffffff")
define HH = Character('[h_name]', color="#ffffff")
define PL = Character('Phil Lowry', color="#ffffff")
define RO = Character('Robot', color="#ffffff")
define RV = Character('Robotic Voice', color="#ffffff")
define SG = Character('Sarah Green', color="#ffffff")
define GI = Character('Little Girl', color="#ffffff")
define ML = Character('Miguel Lopez', color="#ffffff")
define MA = Character('Man', color="#ffffff")
define DD = Character('Dealer', color="#ffffff")
define CC = Character('Carl', color="#ffffff")
define MI = Character('Maid', color="#ffffff")
define HO = Character('Hostess', color="#ffffff")
define YA = Character('Yakuza', color="#ffffff")
define PI = Character('Pilot', color="#ffffff")

default con1 = False
default con2 = False
default con3 = False
default con4 = False
default con5 = False
default skip1 = False
default op1 = False
default op2 = False
default op3 = False
default op4 = False
default op5 = False
define Cbf = False
define Cpanties = False
define Cbf = False
define Zeek = False
define Imf = False
define Ikiss = False



jump start

label start:
    default ipts = 0
    default zpts = 0
    default lpts = 0
    default npts = 0
    default cpts = 0
    define nshower = False
    define nroute = False
    define iroute = False
    define lroute = False
    define croute = False
    define zroute = False
    define nporn = False
    define zsecret = False
    define Lraw = False
    default timeout = 1.0
    default timeout_label = None

    "Before you play Secret Summer, you have to define some relationships. I know it's annoying, but better to get it out of the way now so that you can focus on the game."
    scene bg
    show mc
    with dissolve

    $ p_name = renpy.input("What is the name of the MC?")

    if p_name == "":
        $ p_name=""
    hide mc
    show j
    with dissolve

    $ rel_f = renpy.input("The oldest man of the house is the MC's ??? (Default will be landlord. 1/7)")


    if rel_f == "":
        $ rel_f ="landlord"
    hide j
    show c
    with dissolve

    $ rel_s = renpy.input("This is 18-year-old Coral. She is your ??? (Default will be roommate. 2/7)")

    if rel_s == "":
        $ rel_s ="roommate"
    hide c
    show lz
    with dissolve

    $ rel_b = renpy.input("This is 23-year-old Leanna, the redhead and 22-year-old Zoe with the black hair. You are their ??? (Default will be roommate. 3/7)")

    if rel_b == "":
        $ rel_b ="roommate"
    hide lz
    show i
    with dissolve

    $ rel_sm = renpy.input("This is 37 year-old Irene, the new wife of the landlord. And also your ??? (Default will be landlady. 4/7)")


    if rel_sm == "":
        $ rel_sm ="landlady"
    hide i
    show n
    with dissolve

    $ rel_m = renpy.input("This is 41-year-old Norah, the ex-wife of the landlord. And also the MC's ??? (Default will be landlady. 5/7)")
    if rel_m == "":
        $ rel_m ="landlady"

    $ m_nik = renpy.input("What does the MC call her? (Default will be her name.)")

    if m_nik == "":
        $ m_nik ="Norah"
    hide n
    show fam
    with dissolve

    $ rel_fam = renpy.input("What are the people of this household called together? (Default will be unit. 7/7)")

    if rel_fam == "":
        $ rel_fam ="unit"

    jump start1

    label start1:
        #play music "GTS - Hawaiian-Fun-Time-Loop.mp3"
        scene a1
        with dissolve

        P "Ok, this level design looks good so far, but I’m still not sure which concept I should go with for this game."

        P "How about two twin brother warriors that switch places?"

        P "…Nah. That’d never work."

        "*ten minutes later*"

        P "Argh! I have a serious case of writer’s block. Maybe I’ll just work on the character models for now."

        "*bzzzt*"

        P "(Oh, someone’s calling me.)"

        scene a2
        with dissolve

        N "Hello? Can I speak to the most handsome and sweet boy in the whole wide world, please?"

        P "*laugh* Hey, [m_nik]. I thought you had forgotten about me."

        N "Why, pigs would start flyin' before that happened. *giggle*"

        N "How is my beautiful baby doin' this evenin'?"

        P "(For whatever reason, I always notice her country accent more over the phone than in person.)"

        P "Same as usual, [rel_f] forcing me to do company work all day."

        P "(He’d have a fit if he knew I was still trying to make video games.)"

        N "I’m so sorry, sugar… Are you sure you don’t want me to talk to him?"

        P "N-No, you can’t!"

        N "Oh… I apologize, sweetie. I wasn’t tryin' to upset you or nothin'."

        P "(I already know how that conversation would go, so there’s no reason to put her through that stress.)"

        P "(And I promised him to keep her off his back as part of the deal anyway.)"

        P "I, uh, I just don’t want you to go through all that trouble, and end up arguing and stuff."

        N "Well… as long as you’re sure. But you say that word and I’ll talk to him. Okay?"

        P "Thanks, [m_nik]."

        P "(It’s been about a year since I was forced to leave the girls, but at least we all keep in contact pretty often.)"

        P "(Well… except for Coral. No matter how much I call or text, she refuses to talk to me. Not that I blame her.)"

        P "(Just like her, all the girls were more than confused when I chose [rel_f] over them after the divorce, and never even gave them a real answer why.)"

        P "(But there is one...)"

        P "And how about you? How was work? You’re calling pretty late today."

        N "Yes, I’m sorry about that, too, puddin'. It was just a bit hectic at the bakery today."

        P "That’s a good thing, right? Better than sitting around doing nothing. *smile*"

        N "*laugh* Right. A good thing..."

        N "*sniffle*"

        stop music

        P "(I-Is she crying?)"

        scene a3
        with dissolve
        #play music "PENSIVE - Nomadic.mp3"
        P "H-Hey, are you okay? What’s going on? Did something happen today? Can I help somehow –"

        N "*clear throat* I’m fine, I’m fine! Really, sugar."

        N "It's just my hormones goin' all wacky with it bein' that time of the month."

        P "Oh, um, I see."

        P "(I seriously can’t remember her ever crying, even when things got really bad between her and [rel_f]. Not even when I told her I wanted to live with him.)"

        P "(So what in the world could be enough to make her cry now?)"

        N "*laugh* Didn’t mean to make things so awkward."

        N "I better get off the line before I make a fool out of myself even more. I love you, baby. Sweet dreams."

        P "I… love you too. Goodnight."

        scene a4
        with dissolve

        P "(Is she really okay? Maybe I’m thinking too much and I should take her at her word. Work at the bakery just must be stressing her out a bit.)"

        P "Wait… What the hell are you thinking, [p_name]?"

        P "(I promised to protect all the girls and I thought by leaving that I was, but [m_nik] crying shows me that I obviously made a mistake.)"

        P "(Something is hurting her, and I can’t even help!)"

        P "(And its not only that. In the past year that I've been gone, I can tell that every single one of the girls has some sort of problem.)"

        P "(But no matter how much I ask or try to find out what's going on, they refuse to tell me anything…)"

        P "(Maybe they don’t think I really care anymore because of how I left…?)"

        P "(But that couldn’t be further from the truth! Everything I did was for them!)"

        P "I still can’t stay with them, but I can at least go back and fix whatever’s happening."

        P "Yeah… I’ve decided."

        P "I'm going back to the girls, at least for a little."

        P "(But that’s way easier said than done.)"

        P "(I basically have a freaking mountain in my way.)"

        P "*deep breath* Time to go see [rel_f]."


        scene a5
        with dissolve
        stop music
        P "(I’m lucky that he’s actually home today.)"

        scene a6
        with dissolve

        P "(Stop being such a wuss, [p_name]. Just knock!)"

menu:

    "Knock already!":

        "*knock*"

        J "Enter."

        jump knock1

    "Just stand there like a dolt":

        J "Enter."

        "You jump at your [rel_f]'s voice."

        P "(S-Shit, how the hell does he always know I’m nearby?)"

        jump knock1

label knock1:
        #play music "PENSIVE - Black-And-White-City.mp3"
        P "Yes, sir."

        scene a7
        with dissolve

        "*silence*"

        P  "(I’ve learned the hard way to stay quiet until I’m spoken to when he’s working. All the girls and [m_nik] too.)"

        J "Do you consider me an unreasonable man?"

        P "(Oh! He finally said something.)"

        P "Um, well, not particularly, sir."

        P "(I can’t help but feel like a little kid every time I’m around him.)"

        P "(Dammit.)"

        J "That’s what I thought. And what’s my only rule?"

        P "(I've heard it so many times that I don't even need to think about the answer.)"

        P "Don’t bother you while you’re working... unless I’m on fire."

        J "And?"

        P "...And even then, I should try to put the fire out myself."

        J "Correct. So unless my senses fail me or I’m going senile, you don’t seem to be on fire."

        J "That then BEGS the question, what possible reason you could have for disturbing my vital work."

        P "*clench jaw* I apologize, sir."

        J "Don’t insult me with a fake apology. You knew what you were doing by coming here."

        P "..."

        J "You’re trying my patience."

        J "Leave."

        scene a8
        with dissolve

        P "(This was a bad idea.)"

        scene a9
        with dissolve

        P "(But what about [m_nik] and the girls? Are you going to abandon them?)"

        P "(AGAIN?)"

        scene a8
        with dissolve

        P "(Fuck! If you don’t stand up for yourself here, then when the hell will you?!)"

        P "*inhale deep*"

        scene a7
        with dissolve

        P "I want the Buster Himen contract."

        scene a12
        with dissolve

        J "What?"

        P "The new clients you’ve been trying to join your company. Let me be the one to close the deal."

        P "You’ve been having trouble, right?"

        J "*stare*"

        J "Why?"

        P "(Because they’re located only an hour or two from the girls, so visiting will be just a drive away.)"

        P "Because I’ve been working on the lower tier of the company for a while and I think it’s time you gave me an opportunity to prove myself."

        P "You want me to eventually take over when you die, right?"

        P "(Shit, maybe that was a bit TOO confident.)"

        scene a13
        with dissolve

        J "Hahaha!"

        P "(I-I honestly can’t ever remember him laughing, but it’s scarier than when he’s mad.)"

        scene a14
        with dissolve

        J "This is the fire I’ve been waiting to see inside you since you were a boy. And I was starting to lose hope, but it seems you’ve had an epiphany."

        P "I have."

        P "(But not for the reason you’re thinking.)"

        J "But I’m not just going to hand over such an important contract. You can start on the Ben R. Over contract –"

        P "I want the Buster Himen contract. I can close it."

        P "(I have to sound like I can get the contract – no, I have to BELIEVE, because I will actually have to if he allows me to pursue it.)"

        J "*stare*"

        P "(Show no weakness, just like he taught you.)"

        P "*stare*"

        J "…"

        J "Fine, you can have it."

        P "Really?!"

        P "*clear throat* I mean, uh, thank you."

        J "If you fight me."

        P "Come again?"
        stop music
        J "If you beat me in a fight and win, the contract is yours."

        P "(He wants me to physically FIGHT him?)"

        P "(I’m used to his weird ass lessons and punishments growing up, but this one might take the cake.)"

        P "C-Come on, you can’t be serious?"

        J "I’m always serious. You should know that."

        scene a15
        with dissolve

        J "So, what’s it going to be?"

menu:

    "Tuck your tail and run":

        P "T-This is crazy! I’m not fighting you!"

        scene a8
        with dissolve

        "*run*"

        J "What a pussy."

        scene bs

        "From then on, you became depressed because of your cowardice and had a miserable life."

        "Thanks for playing, I guess."

        return

    "[gr]Sack up and fight him!":

        P "(This is absolutely crazy!)"
        #play music "Action-Drums-Sport.mp3"
        P "(But if I have to fight him to see the girls, then I will!)"

        scene a17
        with dissolve

        P "I-If that’s what it takes. I’m ready."

        scene a18
        with dissolve

        J "Ha! That’s what I like to hear, boy."

        scene bs

        "He quickly moves the desk out of the way."

        scene a19
        with dissolve

        J "No point in wasting time. Let’s go."

        P "(I'm ready to fight, but I have no clue how!)"

        scene a20
        with dissolve

menu:

    "[gr]Dodge":

        scene a21
        with dissolve

        "*dodge*"

        J "Aren’t you a quick little rabbit?"

        J "Well, let's see if you can dodge this!"

        jump fight1

    "Block":

        scene a22
        with dissolve

        P "(Shit! That punch made my arms go numb! I can’t hold them up!)"

        scene a22-2
        with dissolve

        J "Guess you weren’t ready after all."

        scene a23
        with dissolve

        "..."
        stop music
        scene bs

        "I’m sure you can guess what happened next. Should’ve dodged, son."

        return

label fight1:

        scene a24
        with dissolve

menu:

    "[gr]Dodge":

        scene a24-2
        with dissolve

        P "(I dodged it again!)"

        J "How long do you plan to run?"

        jump fight2

    "Block":

        scene a22
        with dissolve

        P "(Shit! That punch made my arms go numb! I can’t hold them up!)"

        scene a22-2
        with dissolve

        J "Guess you weren’t ready after all."

        scene a23
        with dissolve

        "..."

        scene bs

        "I'm sure you can guess what happened next. Should’ve dodged, son."

        return

label fight2:

       P "(I’ve been avoiding having my face bashed so far, but [rel_f] is right. I can't keep running forever.)"

menu:

    "[gr]Counter":

        P "(I have to fight back! For all the girls!)"

        scene a27
        with dissolve

        J "Shit!"

        scene a28
        with dissolve
        stop music
        P "(Shit, I think I actually hurt him!)"

menu:

    "Finish him off Mortal Kombat style":

        "Geez, it was a joke. Did you really want to rip out his spine or something?"

        "Maybe next update. =D"

        jump ok1

    "Ask if he’s okay":

        label ok1:

        P "Uh, are you okay?"

        scene a29
        with dissolve

        J "Even when you punch someone in the face, you’re nice. *sigh*"

        J "But Rome wasn’t built in a day as they say. You’ve shown me today that you have fire inside you and that’s exactly why I offered you that deal."

        P "(‘The deal.’)"

        P "(The reason why I chose to live with him over the girls.)"

        J "You may hate me now, but you’re going to see that forcing you to live with me and rise to your full potential was to your benefit."

        J "To our legacy’s benefit."

        P "..."

        P "(His name living on is the only thing he truly cares about.)"

        J "Pack your bags. You leave on the jet at the end of the week."

        P "(It worked…? It worked!)"

        P "(Wait for me, girls. We’ll be together again soon.)"

        P "Thank you, sir."

        scene a30
        with dissolve
        #play music "ITS - Mr-Debonair.mp3"
        P "(Oh, great… It’s Irene.)"

        P "(The second [rel_f] was divorced, she showed up, so he had probably been having an affair with her for who knows how long? Irene might've even been the cause of the divorce in the first place.)"

        P "(If that didn't make me dislike her off the bat, the way she treats me like an unwanted accessory to [rel_f] is.)"

        P "(Anyway, just greet her and move on, like always.)"

        P "Hello."

        scene a31
        with dissolve

        P "What are you doing? Can you please move?"

        I "I heard your little conversation in there."

        P "..."

        I "Why do you want the Buster Himen contract?"

        P "(Why does she care? Probably wants me to stay a grunt forever so she can take the company for herself one day.)"

        P "You said you heard the conversation, right? I’m just looking for more opportunity."

        scene a32
        with dissolve

        I "Come on, kid. It’s obvious as a hooker in church that you don’t want the company. So, what’s the real reason?"

        P "*heart beat faster*"

        P "(Relax, she’s just throwing out a line to see if you bite. Don’t be that unlucky fish, [p_name].)"

        P "Do you know the definition of insanity?"

        scene a31
        with dissolve

        I "No, but I’m guessing you’re going to tell me."

        P "It’s doing the same thing over and over again, and expecting different results. So I think it would be crazy not to try something different."

        P "Don’t you?"

        I "*stare*"

        P "(Shit, I hope that wasn’t too condescending. I don’t need to be on her bad side, especially right now.)"

        scene a32
        with dissolve

        I "You can pretend to be innocent, but I know you’re plotting something."

        I "And I promise you I’m going to find out exactly what that is."

        I "Enjoy the rest of your day."

        scene a35
        with dissolve
        stop music
        P "(No, no, no. This is not good! What if she finds out?!)"

        scene a36
        with dissolve

        P "*quick breathing*"

        P "(Relax, man. How would she find out? You’re going to be hours and hours away, while she’s stuck here. As long as you’re careful, she or [rel_f] won’t suspect a thing.)"

        P "(Yeah, I’ll be fine.)"

        P "*smile* Better go pack."

        scene bs
        with dissolve

        "After a plane ride and short Uber drive some days later, you reach the girls' house."

        scene a37 #Standing in front of door. **Use pose when MC returns from Autumn hike***
        with dissolve
        #play music "GTS - Hawaiian-Fun-Time-Loop.mp3"
        P "(I’m finally here!)"

        P "(But I’m still kinda lost on how to go about finding out the girls' problems...)"

        P "(Maybe I should just be more subtle in my approach? Try to find out what’s going on without asking directly like I’ve been doing?)"

        P "*smile* Yeah. That might be the ticket."

        P "(I can’t forget about the Buster Himen contract, though. I promised to secure it, so I at least have to make an attempt or I’ll blow my whole cover and get sent back early.)"

        P "(He didn’t give any instructions yet, but I’m fine with taking it easy. This way I can focus on the girls.)"

        P "(There’s still one more problem, though, and it might be the biggest...)"

        P "(Ever since I hit puberty, I’ve been sexually attracted to [m_nik], Coral, Leanne, and Zoe.)"

        P "(My brain knows how INSANE that is… but I just can’t deny it anymore.)"

        P "(I feel like such a creep, but if I just ignore it, I’m sure it’ll go away… probably. And the year-long separation might have cleared it up, anyway.)"

        P " (But man, I still can’t believe I’m actually here!)"

        P "(My original flight was canceled, so I had to take a much earlier one, so that means all the girls are probably asleep right now.)"

        P "(It’s a good thing [m_nik] gave me a key to let me know I was welcome whenever. This way I don't have to wake anyone up.)"

        scene a38 #Norah falling back **Use pose
        with dissolve

        N "Ah!"
        stop music
        P "O-Oh shit!"

        scene a39 #Norah on floor***
        with dissolve

        P "(Oh, [m_nik]! Wow, she looks… really good.)"

        P "(I guess my theory about the separation clearing my sexual feelings is out the window.)"

        P "(But I should probably stop ogling her now…)"

menu:
    "Or… look a bit closer":
        scene a40 #Zoom in on panties***
        with dissolve

        N "What…?"

        scene a41 #Zoom out again to see her surprised exp
        with dissolve

        N "[p_name]?"
        jump peekn1

    "Focus on helping her up [NorahPath]":
        $ npts = npts + 1
        jump peekn1

label peekn1:
        P "Oh!"
        scene a42 #Offer hand down***
        with dissolve

        P "So sorry about that! I didn’t see you coming."

        scene a43 #Hugging N from 3rd***
        with dissolve

        P "(Damn, she is so gorgeous.)"

        P "(I'm going to be in some serious trouble if I don't calm down a bit.)"

        scene a44 #Close-up of N face. Worried exp***
        with dissolve
        #play music "REU - Home-Again.mp3"
        N "I feel like my mind is playin' tricks on me."

        N "Please tell me I'm not dreamin,' and my baby boy is really here."

        P "*laugh* You’re not dreaming and your baby boy is here."

        scene a45 #N starts crying. Find tear add-on
        with dissolve

        N "Then… you’re real."

        scene a46 #N puts head on his chest
        with dissolve

        P "H-Hey, what’s with the waterworks?"

        N "I know I’m bein’ a crybaby… But I just can’t believe you’re here."

        scene a45
        with dissolve

        N "It’s been ten months and three days since you left. *sniffle*"

        P "(She’s actually been counting the days I’ve been gone…?)"

        P "I’m sorry that I haven’t visited you guys in all this time… I’ve just been… busy with the company back home and everything."

        P "(Liar.)"

        N "I wasn’t tryin' to accuse you or anything, darlin'."

        N "I’ve just really missed you, is all."

        P "Then you should be smiling! This is a good day, right?"

        scene a47 #she smiles while still crying
        with dissolve

        N "You’re right."

        scene a46
        with dissolve

        N "*sniffle*"

        P "[m_nik]…"

        P "(I think she just really missed me... I had no clue it was this much.)"

        scene bs
        with dissolve
        stop music
        "Your [rel_m] calms down after a little while."

        scene a48 #N sitting on couch with surprised exp
        with dissolve
        #play music "NTS - Optimistic-Acoustic-Guitar-Loop.mp3"
        N "But what in the world are you doing here already? I thought your flight was all the way at two?"

        P "Yeah, but it got cancelled, so I was offered a different flight."

        P "I hope it’s okay that I came a bit earlier than expected?"

        scene a49 #N smile
        with dissolve

        N "Are you kiddin’? Of course it is!"

        P "*laugh* Just making sure."

        N "*stare*"

        P "Uh, is there something on my face? Or do you still think you're dreaming? *smile*"

        N "*giggle* Sorry, didn't mean to stare. I just can't believe how handsome you’ve gotten over the past ten months."

        P "*laugh* Come on, [m_nik]… That’s a little embarrassing."


        P "(I am twenty now, but I doubt that I've physically changed much from nineteen. And we’ve video chatted a bunch of times since then.)"

        N "I know I’ve practically hugged you enough for a lifetime already… but do you mind if I give you another?"

        P "Are you kidding? Your hugs are the only reason I came back."

        N "*giggle* I’m honored they’re worth so much to you."

        scene a50
        with dissolve

        N "You must think I’m outta my noggin maulin' you like this the second you get back."

        P "If you’re crazy, then I’m crazy too. *hug tighter*"

        P "(I’m so happy that I did come back. I should’ve snuck out here ages ago.)"

        N "We’re just a bunch of crazy fools, then, huh? *giggle*"

        P "(I didn't notice before, but her big boobs are squished right against me… Shit.)"

        P "(I’m getting a hard-on. Please end the hug soon…)"

        scene a51
        with dissolve

        N "Thank you again, sugar. That felt really nice."

        P "(Phew, that was close.)"

        P "Hey, anytime you want to hug me, go ahead. Even if I’m taking a shower or something. *smile*"

        P "(Wait, what?)"

        P "Er, I mean…"

        N "Even while yer showerin', huh? *giggle*"

        P "Um, Sure... I think we should all be proud of our bodies."

        scene a52 #N looks down at MC crotch
        with dissolve

        P "(Huh?)"

        scene a51
        with dissolve

        N "I, um, yes. I agree. We should all be proud of our bodies."

        P "(Did she just look at my privates for a second…? No way. I’m just imagining things.)"

        N "Anyway, now that yer here early, I really should be headin' out like I planned to buy the groceries for your welcome back meal."

        P "(Now that I think about it, she was headed out when I arrived, which is why we bumped into each other in the first place.)"

        P "Do you mind if I come with you?"

        N "Oh, you don't have to bother yourself, baby."

        P "Really, it’s no bother. And I’m sure all the girls are asleep anyway, right?"

        P "([m_nik] always used to wake up hours before anyone to clean the house or prepare breakfast, and I'm sure that hasn't changed.)"

        P "Unless you’re secretly embarrassed to be seen with me?"

        scene a54 #N surprised exp
        with dissolve

        N "Oh my stars! Puddin', I would never think that! You believe me, don’t you? You and yer [rel_s]s mean the absolute world to me."

        P "(Ha. I almost forgot how much of a worrywart she can be. I bet she’d even blame herself if I robbed a bank, and probably even offer to do my jail time.)"

        P "(But that’s just one of the things I love so much about her.)"

        P "I’m sorry. I’m totally kidding, [m_nik] *laugh*"

        P "I forgot how easy it was to tease you."

        scene a51
        with dissolve

        N "Yer such a meanie. *giggle*"

        N "I guess I’ll have to take it, but I’m a big gal. I can handle it."

        P "(Oh man, why’d she have to say it like that? I’m already struggling to control myself around her as it is!)"

        P "*clear throat* Um, that’s good."

        N "Oh, actually, now that you’re taggin' along, do you think you could help me look for a computer?"

        P "A computer?"

        scene a56 #N worried exp
        with dissolve

        N "Mhm. You know I’m a bit… technologically challenged. But hearin' my girlfriends talk about all the shows they watch online, news they get, and social media and all that makes me feel left out."

        N "I figured I could at least make the effort to live in the twenty-first century. And it might help me keep better organized with the bakery too."

        P "Aw, that’s cool you’re trying. And of course I’ll help you find one."

        N "Thank you, baby… Though I admit I might need a little more help once I actually GET the computer."

        N "But if that’s too much of a bother, I totally understand –"

        P "Of course I’ll help! What kind of guy would I be if I left a stunning damsel in distress like yourself in… Well, distress."

        P "(Maybe I got too excited there, but this is actually the perfect opportunity to find out a bit more of why she was crying a earlier this week!)"

        P "(While I’m helping her learn, I can dig into what happened.)"

        scene a51
        with dissolve

        N "You’re such a charmer today. Thank you so much, honey. I don’t know what I’d do without you. *giggle*"

        scene bs
        with dissolve
        stop music
        "You two head out a few minutes later. And after picking up the items for your meal, you visit an electronic shop."

        scene a58 #N looking at computer neutral exp***
        with dissolve
        #play music "NTS - Optimistic-Acoustic-Guitar-Loop.mp3"
        N "Oh, this one looks kinda nice, dont'cha think?"

        P "Oh no! This one is VERY bad."

        scene a59 #N looks at him surprised
        with dissolve

        N "It is?"

        P "Yes. This brand is very unreliable. Most of their laptops heat up fast and take FOREVER to charge. I’ve learned that the hard way."

        P "And the RAM on this model is pretty low, too. You want at least a few gigabytes."

        scene a60 #N neutral exp
        with dissolve

        N "Oh, well, then how do you know if a computer is good or not?"

        P "Hmm… there are a few factors, and it really depends on what you want to do, too. You said to watch movies and basically surf the internet, right?"

        scene a61 #N smile
        with dissolve

        N "Yes. My friend was just talkin' about this show called Game of Chairs. Fantasy isn’t usually my thing, but she says I HAVE to give it a try. And she says there’s plenty of romance too, so I’m willin'."

        P "(Game of Chairs? The one with the dragons and murdering, and taboo sex scenes? Oh boy.)"

menu:
    "Don’t warn her about the show":

        jump warn1

    "Warn her about the show [NorahPath]":

        $ npts = npts + 1

        P "I don’t know if that’s a good idea, [m_nik]… *awkward laugh*"

        scene a62 #N confused
        with dissolve

        N "Huh, why not?"

        P "Well, that show is known for having a lot of violent and… risqué scenes, if I’m putting it lightly."

        scene a61
        with dissolve

        N "Thank you for the warnin', sugar. My friend did mention that to me also, but sometimes showin' the ugly aspects of the real world makes a show more believable and engagin', ya know?"

        jump warn1

label warn1:

    P "Yeah. I’ve actually watched every episode up until now. *smile*"

    scene a59
    with dissolve

    N "You have?"

    P "Yeah. It took me a while to give it a watch, but I’m so glad I did."

    P "Would you like to maybe watch the first episode together?"

    scene a65 #N excited
    with dissolve

    N "Really? That would be wonderful, puddin'."

    scene bs
    with dissolve
    stop music
    "You go back to explaining the nuances of computers to her, until eventually picking one."

    scene a66 #N smiling and smiling clerk looking at each other***
    with dissolve
    #play music "NTS - Optimistic-Acoustic-Guitar-Loop.mp3"
    sc "So, you guys are getting a Banana laptop. Good choice. You know, the upgraded version is only a hundred more dollars and comes with a major upgrade to the CPU."

    scene a67 #N looks at MC, confused
    with dissolve

    N "The CPU… What’s that thingamajig again?"

    scene a68 #N looks at clerk
    with dissolve

    sc "Ah… I see. Nevermind, then. You know, ma’am. We have a lot more user-friendly computers than this near the front of the store."

    N "User-friendly computers?"

    sc "Sure, there are a lot less 'thingamajiggs' that you don’t have to worry your little head over. *laugh*"
    stop music
    P "(What? Why the hell is he being so rude to her?)"

    N "That’s not very polite…"

    sc "Just trying to help, ma’am."

    P "(I should at least say something.)"
    #play music "Shut Up.mp3"
    P "No, you were trying to be rude. And you succeeded, congratulations."

    scene a69 #clerk mad looks at MC and drops hands
    with dissolve

    sc "Excuse me? Who do you think you are talking to me like that?"

    scene a70 #N worried turns to MC fully
    with dissolve

    N "S-Sweetie, it’s fine. Let’s just go, okay?"

    P "No, it’s not, [m_nik]. This man was being rude to you, and if he doesn’t apologize in the next five seconds, we’re going to get managers involved, and start sending emails, followed by strongly-worded letters."

    P "Do you want that, SIR?"

    scene a71 #clerk worried exp
    with dissolve

    sc "I..."

    scene a72 #clerk looks at N
    with dissolve

    sc "I’m sorry… It’s just that my dog recently passed and I’ve been having a rough time."

    scene a73 #clerk on floor***
    with dissolve
    stop music
    sc "Why did you have to leave me, Mr. Toodles?!"

    P "(Wh-What? What is happening right now?)"

    scene bs
    with dissolve

    "You and Norah manage to calm the clerk, and leave."

    scene a73-2 #N smiling in car
    with dissolve
    #play music "NTS - Optimistic-Acoustic-Guitar-Loop.mp3"
    N "I know I said it before, but I didn’t expect to console a man about his deceased dog today. *laugh*"

    P "Yeah, no kidding. And now I’m the one that feels like a jerk for making him cry."

    N "Aw, it wasn’t yer fault, honey. You can never know what someone is goin' through just by lookin' at them."

    P "I guess you’re right, though I’ll be more careful next time and ask a rude person if they have any recently deceased pets before I threaten their whole livelihood."

    N "You’re so silly. *giggle*"

    N "I gotta say though, I didn’t expect you to react the way you did back there."

    P "(I didn’t expect it either... But I can’t say I regret it. I came back here to protect everyone, and that’s what I’m going to do.)"

    P "You must think I’m pretty childish for that."

    scene a74 #N surprised
    with dissolve

    N "Oh no, baby. Not at all."

    scene a73-2
    with dissolve

    N "It may be childish for ME, but… it felt nice havin' a man defend me like that. It made me feel safe. YOU made me feel safe."

    P  "(Shit, when she looks at me like that, I can almost physically feel how much she loves me… And it just makes my own emotions go haywire.)"

    P "I’m really happy you feel that way, because I’ll ALWAYS protect you. Come rain, sleet or snow."

    scene a76 #N caress cheek
    with dissolve

    N "My knight in shinin’ armor. *giggle*"

    P "(I know I’ll have to leave when summer ends, but I’m going to cherish the little time we do have together.)"

    "*bzzzt*"

    scene a77 #N looks down
    with dissolve

    N "Oh, I think that’s my phone. Excuse me, honey."

    scene a78 #N on phone & smile
    with dissolve

    N "Hi, Ron. How are you?"

    P "(Ron… Who’s Ron?)"

    P "(Oh yeah. Her manager down at the bakery.)"

    scene a78-2 #N confused
    with dissolve

    N "What? But…"

    N "…"

    scene a78-3 #N neutral
    with dissolve

    N "I understand, but I told you I needed this day off because my baby boy was comin'."

    N "…"

    scene a78-4 #N angry
    with dissolve

    N "But I haven’t seen him in almost a year!"

    P "(Sounds like the conversation is starting to get a little heated. The last thing I want is her to get fired because of me. I know how much she loves working down at the bakery, especially when she doesn't have to.)"

    scene a79 #MC put hand on N shoulder
    with dissolve

    P "Hey, [m_nik]."

    scene a80 #N faces him confused, still on the phone
    with dissolve

    N "Please, wait a moment, Ron."

    scene a81 #N lowers phone and smiles
    with dissolve

    N "Don’t worry, sweetheart. I'm not going to let anything ruin this special day."

    P "I seriously appreciate how much you planned into welcoming me back, but it would make me feel horrible if you got fired because of it."

    P "And we have plenty of days up ahead, remember?"

    P "I’m here for the whole summer."

    P "(At least that’s how long I'm planning on staying, assuming nothing goes wrong.)"

    scene a82 #N worried
    with dissolve

    N "But…"

    P "Seriously, I swear it’s fine. I'll be home when you get back. I'll even wait in front of the door for you like a loyal dog."

    scene a81
    with dissolve

    N "*giggle* You don’t have to go that far…"

    N "But are you positive? I just want you to feel special."

    P "I do, [m_nik]. Just showing how much you missed me makes me feel that way. *smile*"

    N "Aw, I love you, darlin'."

    P "I love you too."

    scene bs
    with dissolve
    stop music
    "After driving home, Norah leaves and you decide to make breakfast for your [rel_s]s for when they wake up."

    scene a83 #Breakfast table
    with dissolve

    P "You’ve outdone yourself this time. *grin*"

    P "The cooking lessons with [m_nik] really paid off."

    Z "I certainly do remember you two making a mess during those lessons."

    scene a83-2 #Zoe neutral standing far left of door
    with dissolve
    #play music "ZTS - Acoustic-Dream-Underscore.mp3"
    P "(Fuck, it’s happening again. Just like with [m_nik]. The first thing I want to do is go over and kiss her.)"

    Z "Why are you staring at me like you’re trying to test out your laser vision?"

menu:
    "Make a joke":

        P "H-Ha, no. I was actually testing out my X-RAY vision. And I have to say, blue is my favorite color."

        Z "I don’t remember you aspiring to be a comedian, though I would suggest you quit while you’re ahead."

        P "(Shit! Maybe that wasn’t the best thing to say.)"

        P "C-Come on, I was just trying to attempt a little morning humor."

        Z "Be that as it may, I for one could certainly do without it."

        jump menu1

    "Be honest [ZoePath]":

        $ zpts = zpts + 1

        P "S-Sorry, it’s just I forgot how beautiful you were."

        Z "What?"

        P "(Why would you actually say that?! Quick, think of something else!)"

        P "I just mean, uh, you're pretty, so guys must be nervous around you all the time."

        P "(Smooth.)"

        Z "..."

        P "(Wh-Why isn’t she saying anything? Does she somehow know I’m attracted to her?! What if they all know?!)"

        Z "I don’t know how I feel about my own [rel_b] saying that, but I guess I should thank you for the compliment."

        P "You're welcome. *sigh of relief*"

        P "(Maybe not.)"

        jump menu1

label menu1:

    Z "But what in the world are you doing here already? Our [rel_m] told me your flight wasn't for another four hours or so."

    P "Yeah, had to switch flights because of a cancellation."

    Z "I see."

    scene a84 #Zoe smiles
    with dissolve

    Z "Well, are you waiting for a special invitation? Come over here and give your elder [rel_s] a hug."

    P "*laugh* Right, my bad."

    scene a85 #Z and MC hug***
    with dissolve

    Z "Mmm."

    scene a84
    with dissolve

    Z "What a handsome gentleman you’re turning out to be."

    P "*laugh* Come on, we've video chatted almost every week since I've been gone."

    P "Man, the women in this house really know how to embarrass a guy."

    Z "Hey, I just call it like I see it. *giggle*"

    Z "And by women, I’m guessing you mean [m_nik]?"

    Z "I know she wanted to run a few errands this morning. Did you run into her?"

    P "I did, actually, but she got called into work."

    Z "Ah, such a shame. But you’re here for the duration of the summer, correct?"

    Z "We’ll all have plenty of time to catch up."

    P "*smile* That’s true."

    scene a87 #Z looks at table with neutral
    with dissolve

    Z "What’s with all the food, though?"

    P "Oh, I figured I would make breakfast. *smile*"

    scene a88 #Z look at him with surprised
    with dissolve

    Z "You’re telling me you got up early just to make breakfast for everyone?"

    P "Yeah. I just wanted to do something nice for you guys."

    scene a84
    with dissolve

    Z "Well, I have to say that’s very thoughtful of you, but I planned to get an early start at work today."

    P "(I know how serious Zoe is about becoming a lawyer, so she’s working at a law firm, while going to school.)"

    P "But it’s not good to skip breakfast. *frown*"

    P "Just sit down and I’ll serve you."

    scene a83
    with dissolve

    Z "*laugh* My, my, so pushy. Fine, I suppose I could use the energy."

    scene a91 #Z sitting at table smiling***
    with dissolve

    Z "Even though I was the reluctant one, I’m glad you made me eat. This is quite good."

    P "You’re welcome. And, um, I really have no trouble cooking for you every morning."

    Z "Oh, you really don’t have to bother yourself -"

    P "It's no trouble, really!"

    scene a92 #Z neutral
    with dissolve

    Z "I can’t help but feel the suspicion that you might be plotting, my devious little [rel_b]."

    P "Wh-What me? Plotting? No way. Actually, I’m doing the opposite of plotting."

    Z "Which is?"

    P "Um, not plotting?"

    Z "Right…"

    P "(Plotting is exactly what I’m doing. I know something big at school or the law firm has been stressing her out, and I intend to find out what.)"

    P "(But it’s time to deflect!)"

    P "I just want to help you any way I can, just like you and everyone did for me when we were younger. It’s the least I can do."

    scene a93 #Z surprised
    with dissolve

    Z "My..."

    scene a91
    with dissolve

    Z "You are incredibly cute right now. Thank you, [p_name]. That’s quite thoughtful."

    P "You’re welcome. *smile*"

    P "(Just having Zoe smile at me like that makes coming back worth it.)"

    scene a92
    with dissolve

    Z "I know you’ve just arrived… but I would like to discuss your future."

    P "(I already know what she’s going to say. It was literally the last conversation we had last week.)"

    Z "I know that you have chosen to take over that… ‘man’s’ company, which I still don’t understand, but I’ve given up pressing you on that issue."

    P "(I hate to keep secrets from them, but it’s better this way.)"

    Z "What I’m more concerned with now is that you would be making a dire mistake if you don’t have a degree or skill to fall back on."

    P  "(I’ve already told her a million times that it’s not necessary.) *sigh*"

    P "(Wait…)"

    P "(Maybe I can get closer to Zoe and find out what's going on with her if I go along with her plans?)"

    P "(Of course my ultimate goal is to make videos games, and I hate to lie, but this could be my only chance.)"

    P "You know… I’ve been thinking, and you’re right. College might be the best thing for me."

    scene a96 #Z excited
    with dissolve

    Z "Oh! You don’t know how happy that makes me! Come give me a hug!"

    scene a97 #Z hug
    with dissolve

    Z "I know I’ve been annoyingly insistent, but it’s only because I think you’re a very intelligent young man with a bright future."

menu:

    "Smell her hair":

        P "(Shit, I have to smell.) *smell*"

        Z "What are you doing? *giggle*"

        P "J-Just returning your surprise attack."

        scene a98 #Z backs up and is smiling
        with dissolve

        Z "I suppose I did kind of maul you there. Sorry, I’m just happy you’ve decided to take my counsel. *laugh*"

        jump menu2

    "Don’t do anything, like a true gentleman (boring)":

        scene a98
        with dissolve

        Z "Sorry about the surprise attack. I’m just happy you’ve decided to take my counsel."

        jump menu2

label menu2:

    P "It’s all thanks to you for putting it in my head in the first place. *smile*"

    Z "If only certain people would share your newfound attitude."

    P "(She’s talking about Leanne…)"

    "You and Zoe sit again."

    scene a91
    with dissolve

    Z "I know you’ve just come to the decision to pursue your higher education, but do you have any idea as to what kind of career path you’d like to take?"

    P "(Maybe it might be better to go along with everything she wants? Hope I don’t regret this later.)"

    P "I was actually thinking of the legal field… kind of like you."

    scene a96
    with dissolve

    Z "Really?"

    Z "I think that’s a splendid decision. There are so many jobs and opportunities in law..."

    scene a92
    with dissolve

    P "Is something wrong?"

    Z "I actually need to start getting ready to head out."

    P "Oh, that’s no problem. We can just talk when you get back."

    Z "Yes… but this is a very important conversation, as it pertains to your future."

    P "It’s ok. It’s not like I’m going anywhere."

    P "Well, unless aliens come down and abduct me as a test subject or something *smile*"

    Z "You may be joking, but I know how easily a twenty-year-old can change his mind. You’re like a prepubescent schoolgirl in love."

    Z "…"

    scene a103 #Z frown
    with dissolve

    Z "That sounded a lot better in my head."

    P "(I think I understood that, but her analogies could use some work. Ha.)"

    scene a91
    with dissolve

    Z "Oh, I know. Why don’t you just stand outside my bedroom door while I get ready?"

    P "Outside your bedroom door?"

    Z "Yes, that way we can carry on with the conversation. Life is not just about working hard. It’s about working smart. This way we kill two birds with one stone, right?"

    P "Ha, I guess you’re right."

    Z "Of course I am. *giggle*"

    Z "And I’m going to make sure you’re just as capable. It’s my job as your elder [rel_s] after all."

    scene a105 #Z door closed
    with dissolve

    "After cleaning up, you and Zoe go up to her room, and you wait outside while she gets ready for work."

    Z "…and then you… pivotal…"

    P "(I can hardly hear anything she’s saying.)"

    P "I’m sorry, Zoe. Can you please repeat that? I didn’t catch it."

    Z "What?!"

    P "Um, can you please repeat what you were saying!"

    "..."

    scene a106 #Z show up at door, neutral***
    with dissolve

    Z "I forget most of the doors in this house are basically soundproof. *sigh*"

    P "It’s honestly ok, Zoe. We can continue this conversation later -"

    scene a107 #Z angry
    with dissolve

    Z "No!"

    P "Wh-What?"

    scene a108 #Z worried
    with dissolve

    Z "Oh, I’m sorry for that outburst. It’s just that it would be on my mind all day if we just leave it open."

    P "(I know how anal she is about everything, and she even has some OCD. So her needing to finish the conversation doesn’t surprise me.)"

    P "What do we do then?"

    scene a109 #Z closes eyes, neutral
    with dissolve

    Z "Hmm..."

    scene a106
    with dissolve

    Z "I’m going to leave the door open enough so that we can hear each other. I’m not going to regret that, am I? *stare*"

    P "Not at all!"

    P "(…Though I’d be a total liar to say that peeking on her while she changes isn’t somewhere in the back of my mind.)"

    Z "…"

    scene a111 #Z smile
    with dissolve

    Z "Good."

    scene a112 #Z door cracked open
    with dissolve

    Z "So like I was saying before, you have many options as to what you’re able to focus on in the legal field. But you should also take into account your strengths and weaknesses. That’s a pivotal factor."

    P "I understand… Although, I’m still unsure what’s even available. What would you suggest?"

    Z "I have to admit that you can create some compelling points during an argument. God knows I’ve experienced enough of them firsthand in your rebellious teenage years."

    P "Ah... I’m really sorry about that. *awkward laugh*"

    Z "Apology accepted. I’m just happy you’re taking your future serious."

    P "(I can hear her changing…)"
    stop music
    P "(Aw, man… Am I really thinking about spying on my own [rel_s]?!)"

menu galleryScene1:

    "Don’t peek":

        jump donepeek

    "[gr]Peek":
        #play music "SEXY - Smooth-Hip-Hop-Background-Intro.mp3"
        scene a113 #Z without bra facing dresser and pants
        with dissolve

        P "(Oh my gosh! She’s not wearing a bra! If she turned around, I’d be able to fully see her breasts… Though that would also be very, very bad for me.)"

        Z "I’ve pretty much known I wanted to be a lawyer since childhood, but I know that’s a rarity. Not many people are quite put together as I am."

        P "(I’ve been looking for a short while now, but maybe it’d be better to back off now?)"

menu:

    "Take the win and get outta there!":
        stop music
        P "(Yeah, smarter to back away now.)"

        scene a112
        with dissolve

        jump donepeek

    "[gr]Continue to be a deviant":
        P "(Well… maybe a little more wouldn’t hurt.)"

        scene a115 #Z without bra and in panties
        with dissolve

        Z "But as I mentioned before, you have natural debate skills that many lawyers covet."

        scene a116 #Zoom on ass hands on hips
        with dissolve

        P "W-Wow."

        Z "I understand why you would react like that, but becoming a lawyer is completely within your grasp. Why, we could even form a duo, just like the movies!"

        P "(Ha, didn’t expect a childish statement like that from her.)"

        P "(But okay… I’m really tempting fate. Time to retreat?)"

menu:

    "[gr]Yeah, better to play it safe":
        stop music
        P "(Yeah, that's enough.)"

        scene a112
        with dissolve

        jump donepeek

    "Go all in, baby!":
        P "(Well… maybe a little more wouldn’t hurt. Man, I’m the worst right now.)"

        scene a116
        with dissolve

        P "(She’s going to take off her panties!)"

        Z "It would definitely be better than being teamed up with that Misty O'Ryan, that’s for sure. *annoyed huff*"

        Z "Every time I see that girl, it takes a good amount of willpower not to stab her with the closest sharp object."

        scene a119 #Zoom out to see Z looking at door and smiling***
        with dissolve

        Z "Anyway, I’ve been talking your ear off. What do you think?"

        scene a120 #Z surprised
        with dissolve
        stop music
        Z "What..."

        scene a121 #Z grabs towel and angry
        with dissolve

        "Zoe snatches a towel from nearby."

        Z "What the hell do you think you’re doing?! I suppose I was a fool to actually trust you!"

        scene bs

        "GAME OVER."

        "At least you got to look at something nice."

        return

label donepeek:
    $ renpy.end_replay()
    #play music "ZTS - Acoustic-Dream-Underscore.mp3"

    Z "It would definitely be better than being teamed up with that Misty O'Ryan, that’s for sure. *annoyed huff*"

    Z "Every time I see that girl, it takes a good amount of willpower not to stab her with the closest sharp object."

    Z "Anyway, I’ve been talking your ear off. What do you think?"

    P "(This might be another good opportunity to spend more time with her.)"

    P "You mean about becoming a lawyer? I know you said it’s something I can achieve, but I’m not sure if that’s what I want to do."

    P "(I know I’m already deep, but I can’t have everyone thinking I’ve decided to become a lawyer, too.)"

    Z "Oh…"

    Z "I understand. Well, there are still plenty of other options."

    P "I’m, uh, not ruling it out or anything, though. I was actually hoping you could help me do some research whenever you’re free? I know that’s asking a lot -"

    Z "Are you kidding? I would love nothing more! How about tomorrow? I don’t have any classes or work since it’s the weekend."

    P "(She really does sound excited, haha. I have such an awesome [rel_s].)"

    P "Sounds like a date to me."

    Z "A date it is, then. *laugh*"

    scene bs
    with dissolve
    stop music
    "Even though it takes some more willpower, you patiently wait for Zoe to finish getting dressed, and you both head downstairs."

    scene a122 #Z standing by door, smiling. Dressed in suit
    with dissolve
    #play music "ZTS - Acoustic-Dream-Underscore.mp3"
    Z "Okay, I’m off. I’ll see you later."

    P "Okay…"

    P "(Everyone is busy.)"

    scene a123 #Z confused
    with dissolve

    Z "What’s wrong?"

    P "Sorry, didn't mean to look so sullen. It’s just that I’m happy we’re together again, and I’ll miss you…"

    scene a122
    with dissolve

    Z "I’ll be back in a few hours, you silly boy.*giggle*"

    scene a125 #Z holds his arms**
    with dissolve

    Z "But I’ll miss you too. And we’ll have plenty of time to talk later. Right?"

    P "Right. *smile*"

    Z "Thank God you’ve seen the light. Now it’s imperative more than ever that I put my time and energy into making sure that you reach your full potential."

    Z "I hope you’re ready! *giggle*"

    scene a125-2 #Z in car
    with dissolve

    P "(I’m excited to spend some quality time with Zoe… and also a little scared.)"

    P "(So, I’ve seen her already and [m_nik] when I first arrived.)"

    scene a126 #Z gone
    with dissolve
    stop music
    P "(So that just leaves Coral and Leanne.)"

    P "(I know Leanne lives on her own, so I should probably go visit her after checking up on Coral first.)"

    scene bs
    with dissolve

    "…"

    scene a127 #In front of Coral’s door
    with dissolve

    P "(Alright, here goes.)"

    scene a128 #MC fist at door to knock
    with dissolve

    C "What the hell are you doing?"

    scene a127
    with dissolve

    P "(Wh-What? Did she hear me coming?)"

    C "No, don’t go charging in like that! We should flank them or we’re going to get destroyed."

    P "(Oh, it sounds like she’s playing video games. Haha. And she’s still fiery as ever when she does.)"

    P "(I think she's literally the most competitive person that I've ever met.)"

    P "(Alright, time to man up and knock.)"

    scene a130 #MC knock
    with dissolve

    P "Coral? It’s [p_name]…"

    scene a127
    with dissolve

    "…"

    P "Coral? Do you hear me -"

    C "I don’t want to talk to you."

    C "Leave me alone."

    P "*sigh* (That’s about the response I expected after what I did to her.)"

    P "(Luckily, I came prepared.)"

    P "I understand. I just wanted to give you a present."

    C "Are you stupid? What makes you think I would want ANYTHING from a traitor like you?"

    C "You can eat it, play with it, or stick it up your butt for all I care."

    P "(I see her mouth is fiery as ever too.)"

    P "It’s an early copy of Immortal Fighting."

    "…"

    C "…You’re lying. I’m not going to fall for your childish tricks."

    P "*laugh* I swear that if I’m lying, you can punch me in the face."

    C "Don’t tempt me."

    "…"

    P "(If this doesn't get her to come out and talk to me, nothing will.)"

    C "Guys, I’m going AFK. Don’t start the next dungeon without me."

    P "(Ha, it worked!)"

    C "Alright, alright, I’ll be back in a sec. Calm your balls."

    scene a132 #C shows up at door, neutral
    with dissolve
    #play music "CTS - Away-With-You-Loop.mp3"
    C "Let me see the game."

    P "(Coral's refused to talk to me since I’ve left, so it’s so damn good to see her.)"

    C "Have you gone deaf in the last year? LET ME SEE THE GAME."

    P "Alright, alright."

    scene a133 #MC holds out game
    with dissolve

    P "Here."

    scene a134 #C looks down at it after she takes i with excited smile
    with dissolve

    C "Holy shit! You actually have it. And it doesn't even come out for a few days."

    P "*laugh* I’m really glad you like it so much."

    P "(She’s so cute when she gets excited like this.)"

    scene a135 #C arms are straight and she looks at MC with neutral
    with dissolve

    C "It’s okay. And don’t go thinking we’re suddenly cool just because you brought me a video game that's going to come out in like 2 days anyway."

    P "(Hah… Didn’t think it was going to be that easy.)"

    C "Where’d you steal this from?"

    P "*laugh* It’s more like I got stolen FROM."

    P "Remember Derek who lives at the end of the street back home?"

    C "Yeah. The lummox who always makes a sexual comment when any girl is around."

    C "He finally snap and rape someone?"

    P "Haha… no."

    C "I’ll give it another year."

    C "But what about him?"

    P "He has some connections down at the company who makes Immortal Fighting, and got an early copy for me, so I virtually had to pay him an arm and a leg."

    P "Hell, a hand too."

    C "So you just gave me an illegally acquired gift."

    P "(Oof. Maybe I didn't think this through all the way...)"

    P "Uh… It’s the thought that counts?"

    C "..."

    C "I’m far from a saint, so whatever."

    C "Thanks for the gift, I guess."

    scene a136 #C turns around
    with dissolve

    C "See ya."

    P "W-Wait, Coral!"

    scene a135
    with dissolve

    C "Yes, we both know who I am. You don't have to keep saying my name."

    C "What?"

    P "I was just hoping that maybe I could come in for a sec?"

    C "Why?"

    P "Just to talk."

    C "Like I said before, I don’t want to talk to you."

    C "Bye, sir."

    P "T-Then how about we fire up the new game and go a few rounds?"

    C "I’m busy right now. And I don't want to play with you anyway."

    C "Can I go now, or is there anything else?"

    P "(Shit, how can I make her play?)"

menu:

     "Bait her [CoralPath]":

          P "Ohhh, I get it. Alrighty, then. Talk to you later."

          C "What? What the hell is that supposed to mean?"

          scene a138 #MC face C and she’s frowning or annoyed
          with dissolve

          P "Oh, it was nothing much."

          C "Stop it!"

          P "*hide smile* Stop what?"

          C "You know I hate when people do that. Just say what you want to say before I bite you."

          P "*laugh* There doesn’t need to be any biting. I’ll tell you."

          C "Grrr. Just say it already."

          P "It’s just that I know how you used to hate losing whenever we played Immortal Fighting. It was the only game I could ever beat you at."

          P "(Literally. I think it's a little unfair how good she is at video games.)"

          scene a139 #C laughing
          with dissolve

          C "Haha!"

          P "What’s so funny?"

          C "Hahaha!"

          P "…"

          scene a140 #C smiling normal
          with dissolve

          C "You have no freakin' clue."

          C "Fine, let’s play."

          P "(Can’t show any happiness.)"

          P "Oh, why the sudden change of heart?"

          scene a138
          with dissolve

          C "Just get in before I change my mind."

          jump u1_bait

     "Beg":
        $ cpts = cpts - 1

        P "Please, Coral? I just really have missed you and want to spend some time with you?"

        P "Seriously. Please. I’ll do anything."

        C "Alright, dude. Geez. I’m starting to get embarrassed for you."

        C "We can play, but only a round or two."

        P "*grin* Alright, that’s good with me!"

        C "Ugh."

        jump u1_bait

label u1_bait:

    scene a142 #MC #walking behind C into room
    with dissolve
    stop music


    #play music "CTS - Away-With-You-Loop.mp3"
    C "I have to log out of this MMO really quick."

    P "Sure."

    scene a143 #MC look at room. C out of camera
    with dissolve

    P "(I’ve obviously seen the house and some of the rooms on video calls, but everything is much more impressive up close.)"

    P "(If I can say anything good about [rel_f], it’s that he's a man of his word.)"

    P "(Now the girls don’t ever have to worry about money.)"

    C "Guys, I gotta log off for a bit."

    scene a144 #MC looks to see C bending over desk
    with dissolve

    P "(Shit, I've resisted looking at Coral before… But am I really going to be able to keep that up?)"

    scene a145 #Zoom on ass
    with dissolve

    P "(How does she have such a good figure when she pretty much stays inside all day?)"

    scene a144
    with dissolve

    C "I suck? That’s funny, because your mom does too."

    C "My nickname for her is The Vacuum."

    "..."

    C "Whatever, just be on tomorrow at the usual time. Bye."

    scene a147 #C faces him with neutral
    with dissolve

    C "Okay, let’s go."

    P "(Whoa, almost got caught!)"

    P "Ha… right."

    scene bs
    with dissolve
    stop music
    "..."

    scene a149 #Playing video games. MC in 1st looking at C. She has neutral
    with dissolve
    #play music "CTS - Away-With-You-Loop.mp3"
    P "So your favorite character is still Sub-One."

    scene a150 #C smiles
    with dissolve

    C "He’s still the best, isn’t he?"

    P "Ha. I’d say that depends on the skill of the one controlling him."

    C "Hm, I suppose you’re right."

    C "Hehehe."

    P "(Coral seems confident today. Maybe she got a little better in the last year. But I really am good at this game, so it’ll be interesting to see what she can do now.)"

    P "(Coral gets super focused when she plays, so I know I won’t hear a peep until after the round.)"

    P "(Alright, the fight is starting.)"

    P "(I’ll charge her with a kick.)"

    P "(Oh, she dodged. I’ll follow up with an uppercut.)"

    P "(She blocked, and then grabbed me and slammed me. Damn.)"

    "*A few moments later*"

    scene a152 #C excited smile and looks at MC
    with dissolve

    P "You won, and I didn’t even touch you…"

    C "Hehehe."

    C "Now you see. I’ve gotten wayyy better, so sorry, big [rel_b], but you're going to have to hand your Immortal Fighting king title over to me."

    P "…We’ll see about that."

    P "(I’d like to think that I'm a nice guy, but I definitely don't like losing. Time to really turn up the heat.)"

    "*A few more rounds later*"

    scene a149
    with dissolve

    P "(Finally, I won a SINGLE round, but she’s still been wiping the floor with me.) *sigh*"

    P "I admit, Coral. You are officially the king of -"

    scene a154 #Focus camera on her neutral face
    with dissolve

    C "Play again."

    scene a154-2 #C mouth open
    with dissolve

    C "NOW."

    P "(Hmm? She seems annoyed. Guess she really wants her revenge after I beat her so many times in the past. Haha.)"

    scene a149
    with dissolve

    "*More rounds later*"

    P "(Oh, I’m finally starting to win again. It has been a while since I last played, so I'm starting to get my groove back a bit.)"

    scene a155 #C gets up and faces him angry. hands balled
    with dissolve

    C "You’re not supposed to win!"

    C "You’re cheating somehow!"

    P "*laugh* How?"

    scene a156 #C worried, hands normal again
    with dissolve

    C "I-I don’t know!"

    scene a157 #C hand down and angry
    with dissolve

    C "But somehow!"

    P "I don’t understand the big deal. You never used to get this upset when I won before."

    P "(Sure, annoyed, but never upset.)"

    scene a158 #***C frown, sits and holds out her phone. Shrink an image for phone screen of a Twitter page.
    with dissolve

    P "(Her phone?)"

    P "(Guess she want to me to look at something.)"

    scene a159 #***focus on phone
    with dissolve

    P "(It’s King Reef's social media page.)"

    P "(He’s one of the biggest gamers in the world and holds top ten rankings in almost every competitive game that matters. And he's actually pretty high in Immortal Fighting too.)"

    P "(But why is Coral…)"

    scene a158
    with dissolve

    P "Wait."

    P "YOU’RE King Reef?"

    P "(I know that he’s anonymous, but… but that’s insane!)"

    scene a161 #MC look at C frown
    with dissolve

    C "Yes, and I was 69 and Oh, until you just beat me."

    scene a162 #C bites him
    with dissolve

    C "Grrr!"

    scene a161
    with dissolve

    P "*laugh* Are you crazy, Coral!"

    P "Why did you bite me?"

    C "Because you’re annoying…"

    C "I work my butt off trying to get better all these last months, and you just walk in here and take a big shit right on me."

    C "I hope you’re happy, jerk."

    P "(She really is upset about losing. Making her upset is the last thing I want to do when I'm already in deep shit with her.)"

    P "I’m really not trying to brag, but no one’s ever been able to get the best of me at that game."

    P "And you know I suck in plenty others."

    C "Mmm…"

    scene a164 #C neutral
    with dissolve

    C "This new Immortal Fighting is introducing a tag team mode for the first time, and rumor has it that there’s going to be a secret prize for the top ranking online duos."

    P "(So she wants to pair up with me, even though I’m definitely not her favorite person right now.)"

    P "You want to team up?"

    C "No, I don’t WANT to team up with you, but you know I hate people."

    P "Of course I’ll be your one and only partner. *grin*"

    C "You’re not cute."

    C "We need to start practicing to get a feel for the new tag team mode."

    C "I’ll do some research online and find out which characters work together and stuff, so we can just start tomorrow or after tomorrow."

    P "Sounds like a plan."

menu:

    "Tell her you missed her [CoralPath]":

        $ cpts = cpts + 1

        P "And I know you probably don't want to hear it, but I really did miss you, Coral."

        C "You’re right. I don't want to hear it."

        scene a165 #C look away
        with dissolve

        C "Dummy…"

        P "(It’s going to take a little time to win her trust back, but I just have to keep showing that I really do care and love her.)"

        jump u1_vg

    "Don’t tell her":

        jump u1_vg

label u1_vg:

    scene a164
    with dissolve

    P "I’ll let you get started on your research, but I wanted to first ask you if you talked to Leanne recently?"

    P "I’ve been calling her since last week, but she hasn't answered any of my calls."

    P "(Or responded to my texts.)"

    C "You should feel lucky. We MIGHT hear from her twice a month."

    C "[m_nik] never gives up trying to get in touch with her, though."

    P "I know Leanne's pretty much always done her own thing, but I don’t remember it being like this."

    P "Did something happen in the last few months?"

    C "*shrug* I don’t know."

    P "(I know Leanne and Zoe used to get into it… But that doesn’t explain why she keeps disappearing.)"

    C "You can try going over to her house, but don’t be surprised if she’s not there, or just doesn’t answer."

    P "Alright, thanks for the heads up, Coral."

    P "I think I am going to try to go over there."

    C "Bye."

    scene bs
    with dissolve
    stop music
    "After remembering to tell Coral you made breakfast, you leave and take an Uber to Leanne’s."

    scene a167 #L house
    with dissolve

    "…"

    scene a168 #MC knock
    with dissolve

    "*knock*"

    "*minute later*"

    P "(I don’t think Leanne is coming to the door, but I saw her car outside."

    P "(I really want to see her.)"

    scene a169 #MC hand on doorknob
    with dissolve

    P "(Maybe I should try calling her again?)"

    P "(Oh! The door's open.)"

    scene a170 #L living room
    with dissolve

    P "(I’m glad that Leanne is able to live in such a nice place too.)"

    P "(I know I’ve thought it a million times, but the deal really was worth it.)"

    P "Leanne?"

    P "Leanne, it’s [p_name]. Are you here?"

    "…"

    P "(Maybe she just stepped outside or something?)"

    P "(I’ll check the bedroom, and if she’s not there, I’ll just call.)"

    scene bs
    with dissolve

    "…"

    scene a171 #L sleeping on bed facedown, only panties
    with dissolve

    P "(Ah, there she is.)"

    scene a172 #L zoom in on entire body
    with dissolve
    #play music "SEX - The-Greatest-Desire.mp3"
    P "(Half naked.)"

    P "(You need to control yourself.)"

    P "*deep breath*"

    P "(Okay. I’ll just take my mind off her…)"

    scene a173 #L zoom in on ass
    with dissolve

    P "(Amazing ass, by just making her something to eat, like I did with Zoe and Coral.)"

    P "*stare*"

    P "(That’s enough [p_name]! Go!)"

    scene bs
    with dissolve
    stop music
    "…"

    scene a174 #MC in kitchen at stove. Show pot.
    with dissolve

    P "(Leanne didn’t have much to work with, but I did what I could with what little ingredients there were.)"

    P "(Now that we’re done cooking, let’s see how it tastes.)"

    scene a176 #L finger goes to pot to taste
    with dissolve

    P "(What the?)"

    scene a177 #Cam on L and she smiling with finger in or near mouth
    with dissolve

    L "Needs more salt."

    P "*frown* Don’t complain about other people’s cooking…"

    scene a178 #L lowers hand
    with dissolve
    #play music "LTS - Minor-Funk-Theme.mp3"
    L "Hi, little [rel_b]. Did you know that it's illegal to enter someone’s home without permission?"

    L "Though I don’t think I mind robbers that break in and cook for me."

    P "*laugh* I didn’t break in. Your door was open."

    L "Was it? I knew I was forgetting something before I went to sleep last night."

    P "*sigh* I wish you would be more careful, Leanne. You’re always doing stuff like that."

    L "Aww, you’re so cute worrying about me."

    P "Yeah. And you just make fun of me when I do…"

    L "I can’t help it. You’re just so cute that I can’t help but tease you."

    P "Ha… More like torture."

    L "Tomato, tamoto, as they say."

    scene a179 #L zoom in on her body
    with dissolve

    P "(She’s barely wearing anything…)"

    P "(Maybe it would be okay this once?)"

menu:

    "[gr]Kiss her":
        scene a180 #MC kiss her. L neutral, just staring
        with dissolve

        P "(Her lips are so soft.)"

        L "…"

        scene a181 #Cam on L neutral
        with dissolve

        P "(S-Shit, what the hell am I doing?!)"

        P "I’m so sorry, Leanne!"

        L "…"

        L "What was rule number one?"

        P "That I wouldn’t touch…"

        P "Are you mad at me?"

        scene a178
        with dissolve

        L "Your adorable face makes that nearly impossible."

        L "But you have to behave from now on. Do you understand?"

        P "*smile* I will. Thanks, Leanne."

        P "(Seriously, if I screw up with Leanne, then OUR deal will be broken, which is a totally different one from me and [rel_f]'s.)"

        jump u1kiss

    "Don’t kiss her":

        P "(No, I've promised her that I wouldn't touch or make any inappropriate physical contact.)"

        jump u1kiss

label u1kiss:

    L "But I have to say this is a pleasant surprise. I was beginning to think I would never see you again, dear [rel_b]."

    L "Why don’t you turn off the stove and we can catch up a bit."

    P "*smile* Sure. I’d really like that."

    scene bs
    with dissolve

    "You sit and explain you’re down to visit."

    scene a183 #cam on Leanne sitting on couch. Smiling
    with dissolve

    L "I find it hard to believe that after almost a year, you suddenly decide to visit us all just like that."

    L "That 'man' wouldn’t just let you come down here without some sort of a catch."

    P "(Of course the other girls had their suspicions that our [rel_f] was manipulating me into living with him, but I convinced them all it was my choice, because I wanted to run the company.)"

    P "(But just like Leanne, I don't think a single one of them believes that.)"

    P "(I just want to keep it to myself for now, though.)"

    P "No… there’s no catch."

    L "*stare*"

    P "(Man, I always feel like she can see right through me!)"

    L "*laugh* I get it. I won’t ask any more questions."

    L "So, I’m guessing you’ve seen the others already?"

    P "(Thanks for changing the subject, Leanne.)"

    P "Yeah. I told them all I was coming earlier this week, and I did try calling you a few times, but you never answered."

    scene a184 #L shifts on couch. Lay down on back and looking at ceiling
    with dissolve

    L "Ahhh, you know how it goes. I am but a tumbleweed blowing by, going whereever the wind takes me."

    P "Haha. I guess you kinda have always been a free spirit."

    L "See? You’re the only one who gets me, unlike OTHER individuals."

    L "What would I ever do without you, hmm?"

    P "(She’s totally talking about Zoe.)"

    P "*laugh* I’m glad to be so needed."

    P "(I do want to ask her why she’s been distant lately, but I know for a fact that I'm not going to get a straight answer from her.)"

    P "(Finding out what’s going on with Leanne is by far going to be the hardest, compared to the other girls.)"

    P "(So for now, maybe it would be better to just be more subtle like I planned.)"

    P "But I think [m_nik] and the others are going to have a small get-together for me later today."

    L "And you want me to come."

    P "Of course I do."

    P "I missed you."

    L "Have you now?"

    scene a185 #L turn head to him
    with dissolve

    L "Or is it my pussy you’ve missed?"

    P "*swallow*"

    L "I was thinking last night about how our deal started before I fell asleep. And now you’re suddenly back. Isn’t that funny?"

    P "Haha… Yeah, that is kinda funny."

    L "Do you remember how it started?"

    P "I, uh, do. Yes."

    scene a186 #L with a towel drying off BW. Neutral
    with dissolve

    L "It was about two years ago when we were all still living together back home."

    L "I had just finished taking a shower."

    scene a187 #L looks to door, angry, serious face
    with dissolve

    L "And noticed that the door was just so slightly cracked open."

    L "I’d had suspicions that the same thing happened only a week before, so I called whoever was there to show themselves or they would be in big trouble."

    scene a188 #MC gets closer. L surprised
    with dissolve

    L "And imagine my surprise when you walked in."

    P "(I was pretty surprised myself… I had no clue what to do. ‘Deer in headlights' had never been a more appropriate expression than in that moment.)"

    scene a190 #L angry
    with dissolve

    L "I asked you why the hell you would spy on your own [rel_s]? And you said…"

    P "Uh, I said that I thought you were beautiful and even though I knew it was wrong… I said that I couldn’t help seeing how everyone else saw you..."

    L "*laugh* Almost word for word there."

    L "That’s when I asked you if you felt the same way about the others in our [rel_fam], and you said yes."

    L "And that’s when we made our deal."

    L "You wouldn’t spy on any of them as long as I let you see me from then on."

    P "But I could only look… Never touch."
label galleryScene2:
    scene a191 #L opens her towel for him, smiling or just drops it
    with dissolve

    L "And you certainly did look. You made me stand there for 5 whole minutes. *giggle*"

    P "Ha… sorry about that. The situation was just so surreal to me."

    P "(It still is sometimes.)"

    scene a185
    with dissolve

    L "And have you been a good boy, and remained faithful to our deal?"

    P "Yes… You’re the only one I’ve looked at."

    L "Good."

    scene a193 #L sits
    with dissolve

    L "Well, I suppose I better get my errands out of the way before I attend your little party."

menu:

    "Ask to see her naked [LeannePath]":

        $ lpts = lpts + 1

        P "Um, do you… think I can see you naked before you go?"

        L "*laugh* I thought I noticed a look of longing on your face. Like a dog who buried his favorite bone and forgot where."

        L "Didn’t you just see me a week ago on our video call? You even got to see the new panties I bought."

        P "*clear throat* Actually, it’s been 12 days."

        L "*laugh* You’ve been counting the days?"

        P "Of course I haven’t!"

        P "(Kinda…)"

        L "Suuure, little [rel_b]."

        L "Fine. I suppose it has been a little while, and you have been keeping up your end of the deal, so it wouldn't be fair for me to neglect my end, right?"

        P "Ha, right…."

        L "Let me make myself a little comfortable."

        scene a194 #L sits down and spreads legs
        with dissolve
        #play music "SEX - The-Greatest-Desire.mp3"
        L "Is this okay for you?"

        P "It’s perfect…"

        P "Do you think maybe I could take a picture?"

        P "(I’ve always kind of been hesitant to ask, but now that we’re living in two different places, we don’t get to do this as often.)"

        L "Have I ever once denied you when you asked to see my pussy, tits or anything else?"

        P "Well, no…"

        L "Then there’s no need, right?"

        L "Anytime you want to see me, all you have to do is ask."

        L "Consider me your personal model. *giggle*"

        P "(Shit, I have to admit that sounds freaking amazing.)"

        P "*laugh* I have to admit, that sounds wayyy better than any dumb photo."

        L "Ha, see? Now make sure your eyes absorb every inch of me so you can remember this moment until next time."

        P "(You don’t have to tell me twice.)"

        scene a195 #L zoom in on lower half/ vag
        with dissolve

        L "Do you like my pubic hair? I shaved it down from last time."

        P "I do like it."

        L "*laugh* I have a feeling you’d say that regardless, but thank you anyway."

        P "(Fuck, her pussy looks good as ever. I bet it’s super tight too.)"

        P "(What I wouldn't give just for one lick to see how sweet she tastes.)"

        P "(Then stick my tongue in her hot and sweet little hole until she begged me to put something bigger in her.)"

        P "(That’s when I would take my big cock out and stuff her until I reached her womb.)"

        P "(Have her begging for even more as she creamed all over my cock.)"

        P "(Then take it out and make her clean it all up with that beautiful mouth of hers.)"

        P "(Shit, I want to masturbate to her so bad right now, but that isn't allowed either.)"

        P "Lee, show me your ass."

        L "*giggle* You always get so assertive during our little sessions… but I don’t mind."

        scene a196 #L show ass
        with dissolve

        L "As long as you keep your hands to yourself."

        P "(I used to be so shy and timid in the beginning, and while I’m not steel yet, I can’t help but be direct when I'm staring at her gorgeous body.)"

        "*Minutes later*"

        scene a197 #L sit normal
        with dissolve

        L "Are you good now or do you want to keep going?"

        P "(I want to keep going, but I know she has some errands to run.)"

        P "I’m good. Thanks, Leanne. *smile*"

        L "Hey, what are [rel_s]s for? Hehe."

        jump u1show

    "Don’t ask":

        jump u1show

label u1show:
    $ renpy.end_replay()
    scene bs
    with dissolve
    stop music
    "You leave Leanne’s and take an Uber back home."

    scene a198 #MC at front door
    with dissolve

    P "(I’ve seen all the girls now. Today’s been so amazing just seeing them again.)"

    P "(And we’ll all finally be together again in just a few hours.)"

    P "(Of course I still have to worry about the Buster Himen contact, but I’m just going to focus on the girls today like I planned.)"

    P "(Damn it’s good to be back.)"

    jump CH2
