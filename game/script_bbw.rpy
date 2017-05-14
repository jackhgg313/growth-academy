define BBW = Character('Alice', color="#CC33FF")
define Lunch = Character('Lunchlady', color="#CC33FF")
define Francois = Character('Francois', color="#CC33FF")

image BBW neutral = DynamicImage("Graphics/BBW-[globalsize]-neutral.png")
image BBW happy = DynamicImage("Graphics/BBW-[globalsize]-happy.png")
image BBW sad = DynamicImage("Graphics/BBW-[globalsize]-sad.png")
image BBW surprised = DynamicImage("Graphics/BBW-[globalsize]-surprised.png")
image BBW angry = DynamicImage("Graphics/BBW-[globalsize]-angry.png")
image BBW aroused = DynamicImage("Graphics/BBW-[globalsize]-aroused.png")
image BBW haughty = DynamicImage("Graphics/BBW-[globalsize]-haughty.png")

image cg BBW001 = "Graphics/BBW-SC-1.png"
image cg BBW002 = "Graphics/BBW-SC-2.png"

init 2 python:
    datelibrary['BBW_size_6'] = datetime.date(2005, 12, 10)
    datelibrary['BBW_size_5'] = datetime.date(2005, 12, 10)
    datelibrary['BBW_size_4'] = datetime.date(2005, 12, 10)
    datelibrary['BBW_size_3'] = datetime.date(2005, 12, 10)
    datelibrary['BBW_size_2'] = datetime.date(2005, 12, 10)
    
    eventlibrary['BBW001'] = {"name": "BBW001", "girls": ["BBW"], "location": "cafeteria", "conditions": [], "priority": 0}
    eventlibrary['BBW002'] = {"name": "BBW002", "girls": ["BBW"], "location": "cafeteria", "conditions": [[ConditionEnum.EVENT, "BBW001"]], "priority": 0}
    eventlibrary['BBW003'] = {"name": "BBW003", "girls": ["BBW", "PRG"], "location": "cookingclassroom", "conditions": [[ConditionEnum.EVENT, "BBW002"]], "priority": 0}
    eventlibrary['BBW004'] = {"name": "BBW004", "girls": ["BBW", "PRG"], "location": "classroom", "conditions": [[ConditionEnum.EVENT, "BBW003"]], "priority": 0}
    eventlibrary['BBW005'] = {"name": "BBW005", "girls": ["BBW", "PRG"], "location": "cafeteria", "conditions": [[ConditionEnum.PRESET]], "priority": 0}
    eventlibrary['BBW005A'] = {"name": "BBW005A", "girls": ["BBW", "PRG"], "location": "cafeteria", "conditions": [[ConditionEnum.FLAG, "BBW005_ondiet"]], "priority": 0}
    eventlibrary['BBW005B'] = {"name": "BBW005B", "girls": ["BBW", "PRG", "FMG"], "location": "gym", "conditions": [[ConditionEnum.FLAG, "BBW005_workout"]], "priority": 0}
    eventlibrary['BBW006'] = {"name": "BBW006", "girls": ["BBW"], "location": "hallway", "conditions": [[ConditionEnum.EVENT, "BBW004"], [ConditionEnum.GAMETIME, ConditionEqualityEnum.GREATERTHAN, datelibrary["testday"]]], "priority": 0}
    eventlibrary['BBW007'] = {"name": "BBW007", "girls": ["BBW", "PRG"], "location": "cafeteria", "conditions": [[ConditionEnum.EVENT, "BBW006"]], "priority": 0}
    eventlibrary['BBW008'] = {"name": "BBW008", "girls": ["BBW", "PRG"], "location": "musicclassroom", "conditions": [[ConditionEnum.EVENT, "BBW007"]], "priority": 0}
    #eventlibrary['BBW008A'] = {"name": "BBW008A", "girls": ["BBW", "PRG"], "location": "musicclassroom", "conditions": [[ConditionEnum.FLAG, "BBW008_extrascene"]], "priority": 0}
    
label BBW001:
    scene Cafeteria with fade
    MC "Well! That was... a first day. I didn't expect the school to be exactly like my old one, but on a list of unexpected surprises I didn't think..."
    MC "OK, I guess I couldn't have expected it for it to be a surprise."
    extend " But still, if the teacher had ripped off his face to reveal an alien underneath I wouldn't have been more surprised."
    MC "At least food is familiar enough. A nice snack after class is normal, right?"
    UNKNOWN "I'm sorry, you must not know who you're talking to."
    MC "I wonder who that is."
    "Standing near the doors leading to the kitchen itself was the heavyset girl from my class. There was a man in a chef's outfit standing behind her, and she was arguing with an old woman in an apron and hairnet."
    show BBW angry with dissolve
    BBW "The name is Alice Nikumaru."
    BBW "I am sure there was some kind of memorandum circulated among the staff announcing my arrival at this school."
    extend " A missive to let you all know that I am here and that special accommodations to satisfy me would be instituted."
    Lunch "If you have an allergy or other dietary need, I would have been told."
    BBW "You there. Tell... Madame Hairnet here who I am."
    MC "She's a student. She's in my class."
    show BBW haughty
    BBW "I am THE student, as far as you are concerned. You may see hundreds of others passing down your line as you ladle warmed over spaghetti sauce onto rubber pasta, but I am not just another stomach to fill."
    MCT "You didn't hear the part about me being in your class, did you?"
    BBW "The meals you mass-produce for the student body may be satisfactory given the level of culinary talent you possess, but I have greater needs."
    BBW "Francois here studied at the finest institutes in France, Italy and Japan, all for the sake of honing his skills to a level suitable for me."
    Lunch "We make enough food for even the fat kids. Don't worry, you'll get your share."
    show BBW angry
    BBW "I am NOT some 'fat kid'. I am not even obese."
    show BBW neutral
    BBW "And it is not a matter of quantity, but quality. My palate is a delicate instrument that needs to be handled with care. I have certain expectations that you – as qualified for this job as you may be – can not meet."
    BBW "Now, I've already gone to the trouble of ordering the equipment you probably don't have – wood-fire pizza oven, rotisserie, espresso machine, meat smoker; just a few odds and ends..."
    BBW "But he will need, say, 20%% of your workspace emptied out and handed over to him."
    Francois "And deliveries."
    show BBW happy
    BBW "Of course. And he needs to have deliveries made every day, so if you could give him the address and directions to this building, that would be wonderful."
    MCT "Oh, is that all? Your own private chef and special deliveries every day? Just how loaded is this girl?"
    Lunch "Students don't get to bring private chefs with them, princess. Outsiders don't get access to our kitchen or any other facilities on campus. Either you can take what we offer you, or you can make your own meals in the Home Ec classes."
    show BBW angry
    BBW "What? Francois can not perform at his best in a classroom kitchen. He needs a full assemblage of utensils and appliances-"
    Lunch "I said you can make your meals."
    extend " Yourself."
    show BBW haughty
    BBW "Do you really expect me to subject my dainty hands and creamy skin to the raw ingredients that come with making a three-star meal?"
    BBW "Do you have any idea how much this manicure costs? What would handling an ox tongue or a raw Cornish game hen do to it?"
    Lunch "If you don't get out of my kitchen in the next five seconds, you'll be dunking that expensive manicure in cold, greasy dishwater as I have you scrubbing every pot and pan we have."
    show BBW angry
    BBW "You... You wouldn't."
    Lunch "You wouldn't be the first student punished with kitchen duty."
    BBW "Very well, but this is not the end. A Nikumaru does not give up."
    show BBW neutral
    BBW "Did you see that?"
    MCT "Did you forget that you talked to me not two minutes ago?"
    menu:
        "Yeah. Typical hard-ass school employee, being cruel for the sake of it.":
            jump BBW001_c1_1
        "That was kind of harsh. She could at least have tried to work something out with you.":
            jump BBW001_c1_2
        "I've heard of spoiled little girls, but your own private chef? That's a whole new level.":
            BBW "Is it 'spoiled' to have the best that money can buy? I am Alice Nikumaru."
            jump BBW001_c1_after

label BBW001_c1_1:
    show BBW haughty
    BBW "Maybe this is how they do it at lesser institutions, by in my experience schools exist for the betterment of the students."
    extend " If this is a taste of how this place operates, perhaps transferring is the sensible thing. There must be other schools that can handle my needs."
    MC "I guess if you can have a private chef, you can also have a private tutor."
    jump daymenu

label BBW001_c1_2:
    BBW "Absolutely. Life is filled with give and take, and she wouldn't even come to the negotiating table. How is it that so many people can not understand the basics of business deals?"
    MC "Fancy yourself something of a business woman, eh?"
    show BBW happy
    BBW "I know a lot about how the world works. It's an inherited trait."
    jump BBW001_c1_after

label BBW001_c1_after:
    show BBW neutral
    BBW "Perhaps you've heard of my father, Daitaro Nikumaru?"
    menu:
        "Daitaro... Isn't he some sort of businessman?":
            jump BBW001_c2_1
        "Oh, yeah! He's the guy who plays in that traveling jug band, isn't he?":
            jump BBW001_c2_2

label BBW001_c2_1:
    show BBW happy
    BBW "Not just 'some sort' of businessman. He is the leader of the heavy manufacturing and seafood industries in Japan. He is ranked on the list of the richest people in the world."
    MC "Consider me impressed. But if he's so rich, couldn't he just buy this school and install Francois as head chef?"
    show BBW neutral with dissolve
    BBW "Francois is not a garden-variety chef you can put in charge of just any mess of underlings. His talent is best utilized when he can focus on a single diner's menu."
    extend " But you do raise a good point. Perhaps I should have a chat with Father."
    hide BBW
    MC "I- Is she really going to ask her father to buy this school? Just because she doesn't want to eat the cafeteria food?"
    jump daymenu
    
label BBW001_c2_2:
    show BBW angry
    BBW "* scoff * Is there not a single ounce of class or breeding in this place?"
    hide BBW
    MC "I'd settle for an ounce of humor."
    jump daymenu
    
label BBW002:
    scene Cafeteria with fade
    MCT "This place seems kind of quiet for a high school cafeteria. Everyone's so subdued, it's like someone died. Guess I'm not the only one who was thrown for a loop by yesterday's news."
    MCT "We're all probably wondering the same thing: what's going to happen to me? How... big am I going to get? Am I going to end up like one of those people who can't live in normal society?"
    MCT "Ugh, this is too heavy for first thing in the morning. Let's just get something to eat and take the day as it goes."
    MCT "..."
    MCT "Now to find a table. Oh! There's Alice, eating by herself. I don't think she'd mind if I joined her."
    "I found Alice sitting at a table, a few plates and bowls of food in front of her. She looked unimpressed by the spread."
    show BBW neutral with dissolve
    MC "Mind if I join you?"
    BBW "Be my guest. Perhaps you could help me with something."
    MC "Uh, sure! What's on your mind?"
    "Alice held up a fork with a piece of fish on it."
    BBW "This fish. There's something familiar about it."
    MC "It's mackerel. Fish is a common part of Japanese breakfasts."
    show BBW haughty
    BBW "I know that. I've lived here for most of my life. And 'common' may be the best word for what I am eating. I would never have known what this uninspired morsel was if you hadn't told me."
    "She ate the forkful of fish, her face displaying bland disgust."
    BBW "So tell me this: why, when there are literally hundreds of ways of turning even as pedestrian a choice as mackerel into an appetizing entree, did the staff in this kitchen decide to approach their job like they were vulcanizing a piece of rubber?"
    BBW "Is it because they are just that incompetent? What sort of 'cook' treats their ingredients so disdainfully?"
    MC "I don't know. Grilled mackerel's pretty good."
    BBW "I wouldn't mind having mackerel if it was properly prepared. Poach it, bake it in a honey chipotle glaze, something. But I guess that's too much to ask. Just slap it on a grill, turn it after a minute, job's done, right?"
    show BBW neutral
    BBW "Perhaps I should find out who is supplying seafood to this school and have Father undercut them. We could get some decent food in here without profits being too razor thin."
    MCT "Please don't talk about your father influencing the school with his wealth. I don't know if you're joking or if you actually will try it. Or if you even can."
    jump BBW002_prechoice
    
label BBW002_prechoice:
    menu:
        "What do you normally have, if not mackerel?" if not getFlag("BBW002_c1_1"):
            jump BBW002_c1_1
        "Well, they have to make food for a few hundred people, you know? There's only so much you can do when you're preparing so much at once.":
            jump BBW002_c1_2
        "(Change the subject) So, how about that news about why we're here? How are you taking that?":
            jump BBW002_c2_1

label BBW002_c1_1:
    $setFlag("BBW002_c1_1")
    MC "What do you normally have, if not mackerel?"
    BBW "Tuna, usually. Though for breakfast I prefer something more like a French menu with coffee, berries in cream, and a croissant. Maybe a poached egg. I'm very particular about my breakfast; a heavy meal to start the day can leave me feeling lethargic for hours."
    "She picked up her mug and drank from it, showing the same mild disgust."
    show BBW angry
    BBW "And this is not coffee. I'll have to call Mother later, have her send my French press here."
    BBW "I suppose it was foolish of me to think this place would have proper coffee, but I was told this was an exclusive institution. So far the only thing 'exclusive' is the most uninspired menu I have ever encountered. Is this what you eat every day?"
    jump BBW002_prechoice

label BBW002_c1_2:
    MC "Well, they have to make food for a few hundred people, you know? There's only so much you can do when you're preparing so much at once."
    show BBW neutral
    BBW "All the more reason to let me have Francois on hand. It's unnecessary to force every student here to subsist on this food, and to have someone like me – someone accustomed to a certain standard – suffer this it becomes downright cruel."
    MC "It's not that bad. I've had better, but I've definitely had worse."
    MCT "Besides, you managed to clear your plates."
    show BBW haughty
    BBW "You must not have had much better than this, but trust me when I say that offering this to my refined palate is like substituting Mascagni with... think of the name of some vulgar pop diva."
    MCT "I don't know who Mascagni is."
    menu:
        "(Change the subject) So, how about that news about why we're here? How are you taking that?":
            jump BBW002_c2_1
        "Other than the food, what do you think of this place?":
            jump BBW002_c2_2

label BBW002_c2_1:
    MC "So, how about that news about why we're here? How are you taking that?"
    show BBW neutral
    BBW "I have never encountered a problem I could not deal with. Whatever sort of... mutation I am about to experience, I will handle it with grace and composure. You will not see me sobbing or wailing my misfortune."
    MC "Hmm-mmm. You have any idea what it might be? Or if they even know?"
    BBW "I haven't the slightest."
    show cg BBW001
    MC "Yeah, it's a puzzle. Anyway..."
    hide cg
    jump BBW002_c2_2

label BBW002_c2_2:
    MC "Other than the food, what do you think of this place?"
    show BBW neutral
    BBW "I haven't formed an opinion yet, but my expectations are dropping rapidly. First the unwelcome surprise of this school's true purpose, then the matter of the food. And, of course, being denied the privilege of my servants."
    show BBW angry
    BBW "The term has begun with me being hobbled, almost as if they want me to flounder."
    menu:
        "Do you really need someone to carry your books? Is even that beneath you?":
            jump BBW002_c3_1
        "I'm sure you can get by without a butler or whatever.":
            jump BBW002_c3_2

label BBW002_c3_1:
    MC "Do you really need someone to carry your books? Is even that beneath you?"
    show BBW haughty
    BBW "Your jealousy is so transparent. Go ahead and mock my situation, as children always make light of what they don't understand. If you had even the basic conception of culture and breeding you would understand how this all degrades me."
    hide BBW
    MCT "I was just teasing..."
    jump daymenu

label BBW002_c3_2:
    MC "I'm sure you can get by without a butler or whatever. I get that you're used to having... help. I'm going to guess that you've gone to private academies, right? Elite places that take care of fewer students."
    show BBW haughty
    BBW "I have attended only the best schools in America and Japan. Yes, this place is... different from them. There are a lot more people, for one."
    MC "But you're not the only one adjusting. I mean, we've all been thrown into it without warning, and none of us know what the future holds."
    MC "Maybe you should reach out to some of the other students. Someone in our class might help you deal with this upheaval. Listen to your problems, help you navigate the school culture. You don't have to deal with this on your own."
    show BBW neutral
    BBW "You do have a point. The uncertainty we are all experiencing is a common ground I can exploit."
    MCT "Exploit?"
    BBW "Thank you, Hotsure-san. You've given me something to think about."
    hide BBW
    MC "Well that ended abruptly. Maybe if I'd been more direct... Wait, did she actually remember my name?"
    jump daymenu
    
label BBW003:
    scene Hallway with fade
    MC "I think the library is this way? Maybe? Wait, that bulletin board doesn't look familiar... Ah! I was supposed to turn left back there."
    UNKNOWN "Amazing!"
    MC "Oh? I know that voice."
    scene Cooking Classroom with fade
    show BBW happy at Position (xpos=0.25, xanchor=0.5) with dissolve
    show PRG neutral at Position (xpos=0.75, xanchor=0.5) with dissolve
    BBW "Simply superb. Where did you study?"
    PRG "I didn't. I just sort of... taught myself."
    BBW "Don't be so modest. These are fantastic."
    show PRG happy
    PRG "Oh! K-Keisuke!"
    show BBW neutral
    BBW "Hmm? Hotsure-san, what brings you here?"
    MC "I was walking by and overheard you two. What's supposed to be so awesome?"
    show BBW happy
    show PRG neutral
    BBW "This souffle Kodoma-san has prepared. I've seen enough of Japan's attempts to mimic French cuisine to know to lower my expectations, but this is surprising."
    menu:
        "Oh, is it really that good?":
            jump BBW003_c1_1
        "Can I try one?":
            jump BBW003_c1_2
        "Aida, I didn't know you were a cook.":
            MC "Aida, I didn't know you were a cook."
            jump BBW003_c1_3

label BBW003_c1_1:
    MC "Oh, is it really that good?"
    show BBW neutral
    BBW "It's all relative. I wouldn't tell her to open up a bakery, but for a high school student working with the ingredients and facilities on hand, these are almost revelatory. I can see my judgment was sound as ever to invite her into service."
    MC "Invite who?"
    BBW "Kodoma-san, of course. It almost seems destined that my roommate would turn out to be perfectly suited to act as my right-hand woman during my time at this school."
    MC "I think I missed something."
    BBW "What do you mean? It was your own idea that I should seek help among our classmates. And Kodoma-san is all too eager to fill the role of my servants while I'm left to fend for myself here."
    MC "I wasn't really suggesting you find a maid..."
    show BBW happy
    BBW "Nonsense, Kodoma-san is more than qualified to act as my chef, secretary, personal trainer, accountant, media relations manager, bodyguard, chauffeur and interpreter. And she's eager to start right away. Aren't you, Kodoma-san?"
    PRG "Y-yes, ma'am."
    menu:
        "Is she? I guess that's fortunate for you.":
            jump BBW003_c2_1
        "So are you paying her, or... ?":
            jump BBW003_c2_2
        "Aida, do you really just want to be her maid?":
            jump BBW003_c2_3

label BBW003_c2_1:
    MC "Is she? I guess that's fortunate for you."
    show BBW haughty
    BBW "It is. I would have survived had I been left to my own devices, but people like me – those of us who are always looking at the big picture and have so many things to worry about – we benefit from having dedicated subordinates. Having someone to cook for me frees up time and energy I can devote to other things."
    MC "Like what?"
    BBW "Anything. My studies, my hobbies, being the glamorous trendsetter that I am."
    MC "I guess if she's OK helping you, there's nothing wrong with that."
    BBW "Why wouldn't she be okay? I'm giving her focus and direction, at a time when she needs it most. All of us have been blindsided by the news of this school, and I think the best way to deal with it is to carry on as always. It's what I'm doing."
    MC "I can't say you're letting all this get to you. Maybe you have something there."
    show BBW neutral
    BBW "Of course, I could use more help. It's a full-time job being me, and I'm always looking for people I can count on to help me. Would you be interested in a job?"
    MC "I'll... get back to you on that. I need to be somewhere else right now."
    BBW "Very well, but don't complain if I find someone else to fill the position."
    MCT "It'd be nice to make some new friends here, but I'm not looking to be anyone's butler..."
    jump daymenu

label BBW003_c2_2:
    MC "So are you paying her, or... ?"
    show BBW haughty
    BBW "It's not polite to talk about money so plainly. But to answer your question, I have offered Kodoma-san compensation for her services. And let us leave it at that."
    MC "Didn't mean to offend."
    show BBW neutral
    BBW "I'm sure you didn't, but do be careful in the future. Now, Kodoma-san and I have more to discuss, so is there something you need or...?"
    MC "Don't mind me. I have somewhere else to be right now."
    jump daymenu

label BBW003_c2_3:
    show BBW neutral
    MC "Aida, do you really just want to be her maid?"
    PRG "O-Oh no, it's not like that. Alice- M-Madame Nikumaru is very nice, and I enjoy helping others. I'm just happy to have found a f-friend!"
    MC "Okay... I guess that's one way of looking at it."
    BBW "Kodoma-san is happy with her position, as you can see."
    MC "Yeah. Sure. Happy. Well, I need to get going..."
    jump daymenu

label BBW003_c1_2:
    MC "Can I try one?"
    BBW "I suppose. There are more than enough here. Take one, and tell me my assessment was wrong."
    menu:
        "Hey, you're right. These are pretty good.":
            jump BBW003_c3
        "Aida, these are pretty good.":
            MC "Aida, these are pretty good."
            jump BBW003_c1_3

label BBW003_c3:
    $setAffection("BBW", 1)
    MC "Hey, you're right. These are pretty good."
    show BBW haughty
    BBW "Did you think I was being hyperbolic? I don't hand out praise unless it's earned, and even then I'm careful with my words. I have found in Kodoma-san a rare talent, waiting to be nurtured and cultivated. And who better to guide her than someone with a palette as refined as mine? No one else at this school can help her like I can."
    MC "That's pretty generous of you."
    BBW "I know, but it's the least I can do. It's one of the burdens of the wealthy seldom talked about: the need to foster talent wherever it is found. With my help Kodoma-san will become an excellent chef, someone capable of pleasing even my tastes."
    MCT "And now I'm wondering just how altruistic you are. Still, Aida seems happy with herself, so who am I to butt in?"
    jump daymenu


label BBW003_c1_3:
    $setAffection("PRG", 1)
    PRG "Ohnoit'snothingspecial. I-I-I just like to make treats and share them with people."
    MCT "Cripes, is she that unfamiliar with compliments?"
    BBW "Kodoma-san had mentioned that she was thinking of making treats for our classmates, though I think directing her energy to one person, such as myself, is better than any scattershot approach."
    MCT "Better for who?"
    BBW "I'm afraid we can't stop and chat. Kodoma-san has more training to do if I'm to bring her on as my assistant."
    MC "Your assistant?"
    BBW "Naturally I'll need to find someone to help me now that my personal retinue has been barred from the school. And Kodoma-san practically begged me for the position."
    MCT "Why do I believe things played out a little differently outside your head?"
    jump daymenu
    
label BBW004:
    scene Classroom Day with fade
    MCT "After class clean-up. That's normal. Mind-numbingly boring, but right now I'll take dull over surprising."
    MCT "..."
    MCT "?"
    MC "Um, are you planning to help out?"
    show BBW neutral at Position (xpos=0.25, xanchor=0.5) with dissolve
    BBW "I have Aida taking care of my share of the work."
    MC "Aida? Where is she- Why are you down there?"
    show PRG neutral at Position (xpos=0.75, xanchor=0.5, ypos=0.25, yanchor=0.5) with dissolve
    PRG "Oh! H-hello Hotsure-san. I'm just doing what Nikumaru-san said."
    MC "Did she say to scrub the floor? I'm pretty sure we just need to sweep it."
    PRG "I- I know. I just wanted to do a good job."
    MC "But it's not your job. Alice's name was on the roster."
    show BBW haughty
    BBW "And I got Aida to do it for me. It's called delegating. As long as the work gets done, nothing else matters."
    menu:
        "I... guess I can't argue with that.":
            jump BBW004_c1
        "It's not just about getting the work done.":
            jump BBW004_c2
        "Do I have to tell on you? Because that seems like a really childish thing for all of us.":
            jump BBW004_c3

label BBW004_c1:
    MC "I... guess I can't argue with that."
    show BBW neutral
    BBW "Of course not. Aida isn't complaining, so there should be no issue here."
    MC "I'm not saying I agree. I just can't think of a counterargument."
    jump daymenu

label BBW004_c2:
    MC "It's not just about getting the work done. It's about being part of a team."
    show BBW neutral
    BBW "I am part of the team. I'm supplying leadership and direction to Aida. If she's not complaining, is it really any of your business?"
    MC "...You might not want to make a habit of this. That's all I'm saying."
    jump daymenu

label BBW004_c3:
    $setAffection("BBW", -2)
    MC "Do I have to tell on you? Because that seems like a really childish thing for all of us."
    show BBW angry
    BBW "You're threatening to report me? At what point did any of this become your concern, anyway?"
    MC "When I saw someone not doing their share. This is a collective assignment, we all have to carry our weight. You don't get to sit back and take it easy just because you managed to rope someone else in."
    BBW "Are you a figure of authority in this class? No? Then you do not get to tell me that I do not get to do something."
    show BBW haughty
    BBW "As for alerting someone with actual power, go ahead. Play the sniffling toddler, tattle on me. My conscience is clear."
    MC "Guess that's what I'll be doing..."
    jump daymenu

label BBW005:
#INT: Cafeteria
#Keisuke (internal): Things seem a little livelier today. Not as much moping. And at least one person is very happy.
#BBW_Happy: Tres bien! Aida, dear, this is divine.
#Keisuke: Enjoying Kodoma-san's food again, I see.
#BBW_Happy: If you could taste this for yourself you would understand this is less about enjoying and more about experiencing.
#Keisuke: Are you offering to share some with me?
#BBW_Neutral: I... No. We are not on such familiar terms.
#Keisuke: Guess I can't argue with that, though it does look like she went all out. An omelet, fried potatoes, bacon, sausage... and doughnuts? Isn't that a bit heavy for a breakfast? Especially considering how much there is?
#BBW_Neutral: Are you implying something?
#Keisuke: No. I'm just saying that if I ate all that I'd be feeling sleepy by second period.
#BBW_Haughty: Breakfast is the most important meal. All your energy and drive for the day comes from it, so it's better to pack in as many nutrients as possible.
#Keisuke: That's one way of looking at it, I guess.
#BBW_Haughty: Plus, the more dishes I sample the better I can guide Kodoma-san in her job. For instance, this omelet could do with a bit less onions, and maybe more ham.
#PRG_Neutral: Y-Yes, Nikumara-sama.
#Keisuke (internal): That's some nice rationalization there.
#END SCENE

    scene Cafeteria with fade
    MC "Hair? What kind of mutation is hair growth? This almost seems like a joke. ... Hmm, no open tables. Oh! There's a spot."
    show BBW sad at Position (xpos=0.25, xanchor=0.5) with dissolve
    show PRG sad at Position (xpos=0.75, xanchor=0.5) with dissolve
    BBW "..."
    PRG "I-Is something wrong, Nikumaru-sama? Did I use too much coriander, or..."
    show BBW neutral
    BBW "No. The dish is exemplary. It's just..."
    MC "Stewing over the test results? Is it something bad?"
    show BBW haughty
    show PRG neutral
    BBW "A Nikumaru does not 'stew.' We take action, we confront problems. Destiny does not come to us, we make things happen."
    MC "So what was it? Or is it too personal to tell?"
    show BBW angry
    BBW "(You might have thought of that before you asked.) To answer your question, yes, I am thinking about the test results. I am questioning what can be done to curtail my... expansion."
    MC "If anything can be done."
    show BBW haughty
    BBW "There is always a way, even if it might be extreme. But the lengths you are willing to go to achieve something demonstrate how much you deserve it. Right, Kodoma-san?"
    show PRG neutral
    PRG "Ah! Y-yes, Nikumaru-sama!"
    MC "So what is your 'factor?'"
    show BBW neutral
    BBW "They say, and you might have trouble believing this just as I did, that I am inclined to grow... stout."
    MC "Stout?"
    BBW "..."
    extend " Obese."
    extend " Fat."
    MC "Oh. Yeah, that's, um, hard to swallow. But maybe it won't be too bad. They can't tell how 'stout' you'll end up being, right?"
    show BBW angry
    BBW "No, they can not predict that. But any excessive weight is unbecoming, which brings me to my quandary. Do I restrict my diet even further than the modest regiment I already have, or do I allow the growth to happen and fix things later?"
    MC "You think you can lose the weight after you're done growing? Isn't this supposed to be permanent?"
    show BBW neutral
    BBW "Failure only comes when you give up. Liposuction and similar weight loss treatments have helped others, so why not me?"
    BBW "But I am interested in your thoughts. Which sounds like a better approach, tackling the growth now or dealing with it at a later date?"
    menu:
        "I don't know anything about liposuction, so I'd say try to work at it now. Eat less, eat healthier.":
            jump BBW005_c1
        "Modern medicine is pretty extraordinary. If you ended up getting really fat there's probably some surgery you can get.":
            jump BBW005_c2
        "What if you worked out? Burn those calories before they turn into fat.":
            jump BBW005_c3


label BBW005_c1:
    $setFlag("BBW005_ondiet")
    MC "I don't know anything about liposuction, so I'd say try to work at it now. Eat less, eat healthier."
    BBW "That does seem the best tactic. If I don't give my body the means to get fat..."
    MC "Just don't starve yourself or anything."
    BBW "Of course not. I know exactly what my body needs. Kodoma-san!"
    PRG "Yes, Nikumarua-sama!"
    BBW "Going forward I want my meals to have a maximum of 650 calories. Adjust my menu accordingly, but be sure to include an appetizer, entree, side dish and dessert."
    MC "So now she's your dietician?"
    BBW "All part of her job description. Did you get all that?"
    PRG "Yes, Nikumaru-sama."
    MCT "Seems a bit much to ask of anyone, even if they're as eager to please as Aida is. But what do I know about cooking?"
    jump daymenu

label BBW005_c2:
    MC "Modern medicine is pretty extraordinary. If you ended up getting really fat there's probably some surgery you can get."
    BBW "I agree, this is the idea most likely to succeed. I don't know enough right now, so how am I supposed to proceed? What if my growth is miniscule? Would I end up starving myself for nothing? Or what if it is extreme, and denying myself a proper diet is for naught?"
    PRG "N-Nikumaru-sama? The quail is ready."
    show BBW happy
    BBW "Then bring it out! And excellent choice to include the spicy mustard greens in this salad. It was exactly what it needed."
    show PRG happy
    PRG "T-thank you!" 
    MCT "Whether this will work or not, it is the path of least resistance. Maybe that's why she's eager to go along with it."
    jump daymenu

label BBW005_c3:
    $setFlag("BBW005_workout")
    MC "What if you worked out? Burn those calories before they turn into fat."
    BBW "Now that is sensible. I admit, the thought of denying myself proper meals is distressing, more so after discovering Kodoma-san's talents."
    show BBW haughty
    BBW "I mean, who else at this school is prepared to give her ability the recognition it deserves? And if I can support her while taking care of myself at the same time, so much the better."
    MC "Have your cake and eat it too, you mean?"
    show BBW neutral
    BBW "Quite. You do have a good mind, Hotsure-san, but perhaps humor is outside your reach."
    MCT "I wasn't trying to make a joke."
    jump daymenu

label BBW005A:
    scene Cafeteria with fade
    $setAffection("BBW", -2)
    MCT "Why do I always have trouble finding an open seat? I wonder how much harder this will be once some of the people start growing..."
    MC "Mind if I sit here?"
    show BBW sad at Position (xpos=0.25, xanchor=0.5) with dissolve
    show PRG neutral at Position (xpos=0.75, xanchor=0.5) with dissolve
    PRG "Oh! G-Good morning, Hotsure-san."
    BBW "... By all means."
    MC "Thanks. Say, did you two get the Lit reading done? I kind of spaced out last night."
    PRG "I did it. How far along did you get?"
    MC "About... two pages in."
    BBW "Kodoma-san."
    PRG "Yes, Nikumaru-san?"
    BBW "Can you get the other half of the grapefruit? The first half was not adequate alone."
    PRG "Certainly, ma'am. And would you like some more toast?"
    BBW "... Two slices."
    PRG "With jam or butter?"
    BBW "No. Plain."
    PRG "All right. I'll be right back."
    hide PRG with dissolve
    MCT "Someone's in a bad mood. I wonder if I should say something or not."
    MC "Light breakfast today?"
    MCT "Mouth, you're not helping."
    BBW "Light breakfast today, and every day. Light lunch every day. Light dinner every day."
    MC "Oh? ... Oh! Yeah. Your factor. I guess you're doing the diet thing, huh?"
    BBW "If I am to maintain authority over my own body and not be controlled by the whims of fate, then yes, I am doing 'the diet thing.' Every day, at every meal, I will be watching my intake, limiting the calories, sugars, and fats I take in. I will limit it all to what I need and no more."
    MC "You don't seem too happy about it."
    show BBW angry
    BBW "Is there something here I should be happy about? I have a palate more refined than people twice my age. My appreciation of the arts – culinary or otherwise – exceeds that of professional critics. And now I must cut out my tongue, surviving on simple fruits and steamed vegetables and whatever other staples a Neanderthal wandering the plains of famine would call a meal."
    MCT "That's a bit melodramatic. Better think of some positive way to look at this."
    MC "At least it will help in the long run! That'll be good, right?"
    BBW "I am already beginning to question that. I can endure an existence marked by suffering and lacking. I am strong enough to bear up in the face of abject want, unlike many others."
    BBW "But is that a life worth living? Is the path of self-denial, of self-inflicted misery, beneficial to anyone? How can one grow as a person if they have committed their life to depriving themselves of opportunity and experience? Every bowl of plain rice, every plate of salad, is another act of self-flagellation. Shall my days be marked by anguish, my life's story a tale of torment? Who would live such a life by choice? Who would be inspired by that?"
    MC "But... you just started the diet. This is your first meal."
    BBW "Is my suffering any less brutal for being so brief? Shall I remain silent until I have carried my burden for a certain number of days? No! Pain is pain. It is not to be dismissed for failing to meet some arbitrary metric. You were the one to suggest this trial of deprivation, and now you mock me for not embracing my torture?"
    show PRG neutral at Position (xpos=0.75, xanchor=0.5) with dissolve
    PRG "Miss Nikumaru? I brought you your food."
    show BBW neutral
    BBW "Thank you, Aida, but now I want you to go prepare me a real breakfast. Crepes Florentine and smoked salmon to start, along with some coffee and fresh-squeezed orange juice."
    PRG "Y-Yes, ma'am. ... I'll just leave the toast and grapefruit."
    BBW "Or does this not meet your approval, Hotsure-san?"
    MC "Whoa! I'm not judging you. I'm just..."
    show BBW angry
    BBW "You're just... what?"
    MC "I'm just saying a diet might not be easy, but in the end you might be glad you did it."
    BBW "Is my mood a concern of yours? Is it your business to tell me how I deal with my factor? I assume you have your own condition to deal with, no?"
    MC "Yeah. My hair grows really fast."
    BBW "... That is your condition? That is why you're here?"
    MC "Yep. That's it."
    BBW "I would suggest you withhold any attempts to guide others through their own crises until you have experience with actual problems yourself. Some people seem to just float through life without a care in the world, never understanding how hard and unyielding life can be."
    MC "Uh huh... Consider me properly scolded."
    MCT "I was just trying to help."
    jump daymenu
    
label BBW005B:
    $setAffection("BBW", 1)
    scene Classroom Day with fade
    "The last bell of the day rang and everyone got ready to get up and go. I had nothing in particular I wanted to do this afternoon, but like most everyone else I wanted to get out as quickly as I could."
    "I made it halfway to the door before I was stopped by a hand on my shoulder. Turning around, I saw Alice standing there with Aida hovering behind."
    show BBW neutral at Position (xpos=0.25, xanchor=0.5) with dissolve
    show PRG neutral at Position (xpos=0.75, xanchor=0.5) with dissolve
    BBW "It's time we begin our journey."
    MC "Journey?"
    BBW "Our journey towards health and well-being for myself. In order to stave off the effects of my growth factor I will be taking up an exercise routine. An intense calorie-burning regimen to keep myself fit and sleek."
    MC "Where do I come in?"
    BBW "It was your idea, after all. And I can't tackle such a daunting task myself. I remember reading that new habits undertaken with others have a better success rate, and let's be frank, some exercise wouldn't do you much harm."
    MC "I'd be insulted, but... Yeah. What about Kodoma-san, though? I thought you said she would be your personal fitness trainer."
    BBW "And she is, but she can't be both working out and coaching me. Plus, she wouldn't do as a spotter. Too frail."
    MC "I think she should be insulted, but..."
    show PRG sad
    PRG "..."
    MC "Yeah. Well, I have nothing better to do right now, so why not? Let's hit the gym."
    show BBW happy
    BBW "That's the spirit. Go change, and we'll meet you at the weight room."
    
    scene Gym with fade #weight room?
    show BBW neutral at Position (xpos=0.25, xanchor=0.5) with dissolve
    show PRG neutral at Position (xpos=0.75, xanchor=0.5) with dissolve
    BBW "OK! Where do we start?"
    MC "Um..."
    BBW "I was asking Kodoma-san. She's the official expert here."
    PRG "Uh... Maybe if we did some stretches?"
    show BBW happy
    BBW "Excellent. We'll ease into the workout."
    "We went to a set of mats set up in a corner, away from the weights and machines, and Kodoma-san led us in some light stretches and calisthenics that took me back to grade school. I can't say it did anything to burn calories, but it did loosen me up."
    "Eventually she stopped (or she ran out of exercises)."
    PRG "Now how about we... do push-ups?"
    show BBW neutral
    BBW "You're the boss. Come on, Keisuke."
    hide BBW with dissolve
    "Alice and I got down on the mat and started doing push-ups. That is, we tried. I knocked out a couple before I was struggling to keep my form, but Alice was having trouble doing just one."
    BBW "Nnnnnhg... Gggggrrrr... One!"
    BBW "Aaaaannnn... Two!"
    show PRG happy
    PRG "Come on, Nikumaru-san! Push it! Unleash the beast! Own your power!"
    "Kodoma-san tried encouraging Alice with some slogans I'm sure she got off fitness clothing commercials, and ever so slowly she managed to do a full set."
    BBW "Ggggggggnnnnnnnn... Ten!"
    PRG "You did it, ma'am! Well done!"
    show BBW happy at Position (xpos=0.25, xanchor=0.5) with dissolve
    BBW "Thank you, thank you. If you'll excuse me, I need to take a quick water break. Hydration is important, after all."
    hide BBW with dissolve
    show PRG neutral
    PRG "OK. We'll wait for you."
    "I wasn't going to say anything; after all, it's not like I'm effortlessly knocking out the push-ups one-handed or anything. And Alice was sweating by the end, so she was putting in some effort."
    "She came back five minutes later, no longer sweating and looking like she had straightened up her hair in the bathroom."
    show BBW neutral at Position (xpos=0.25, xanchor=0.5) with dissolve
    BBW "What shall we do next?"
    "Kodoma-san looked around, a little bit lost among the machines she clearly had no experience with."
    PRG "Maybe we can start here? And then work our way around?"
    "She was looking at a pulldown bar, the kind where you stay standing and pull the bar in front of your chest."
    BBW "Very well. Keisuke, you go first."
    MC "Why me- No, never mind. I'll go."
    "As I was looking at the weights in increments of ten pounds, trying to guess what my limit was, another person came over and joined us."
    show PRG neutral at Position (xpos=0.9, xanchor=0.5) with dissolve
    show FMG neutral at Position (xpos=0.75, xanchor=0.5) with dissolve
    FMG "Hey sorry to bother but how much longer are you...Oh hey guys. What brings you here?"
    MC "Hi, Akira. We're just working out, trying to help Alice lose weight."
    show BBW angry
    BBW "I don't need to lose weight. I just need to keep myself from getting fat. There is a world of difference there."
    MC "Right. Anyway, we'll try not to take too long."
    FMG "Nah it's cool, I could use the breather anyways."
    show BBW neutral
    "She stayed standing a bit to the side, watching as I decided how to adjust the weight and making me self-conscious. If it was just me and Alice I could get away with something easy, but with Akira looking over my shoulder I was afraid she would say something if I wasn't going all out."
    "In the end I decided to add 50%% more what I was originally going to lift. To my surprise it weighed more than what I expected. Before I could lift it up, Akira came and grabbed the bar."
    FMG "Sorry but I have a quick question, just how much did you put on the bar?"
    MC "About 150 pounds. Why?"
    show FMG sad
    FMG "Because it looked like it was too much for you. You gotta know your limits and take it one step at a time."
    BBW "You look like you know what you're talking about. Maybe you have some tips you can share."
    show FMG neutral
    FMG "Sure. First off, did you take a protein shake before exercising?"
    BBW "Uh, no? Is that necessary?"
    FMG "Not really but it helps. Here, I have an extra."
    MC "I don't think we need it. We're not trying to build up muscle, are we?"
    FMG "Fair enough I guess."
    "Akira puts the shake away before whispering to me."
    show FMG happy
    FMG "{i}Between you and me, I just wanted to see Alice's reaction to drinking this sludge.{/i}"
    FMG "Alright, tips. The first thing you want to do is, like I said, know your limits and pace yourself. Take short breaks when you need it. Keep consistent and follow a routine. And the most importantly, be patient, don't expect results overnight. As long as you keep it up and actively enjoy it, you won't have any problems."
    show BBW happy
    BBW "Sounds good. Let's get to it."
    show BBW neutral
    BBW "..."
    MC "..."
    BBW "You were about to begin."
    MC "Right."
    "I reset the weight to what I thought was a manageable amount. Akira was still standing by, watching, but I put her out of my mind as I did ten reps with what felt like too little weight in her eyes."
    "When I was done I stepped aside for Alice."
    BBW "My turn."
    "She left the weight where it was, but turned out to be too much for her."
    show BBW angry
    BBW "Nnnnggg! Grrrrr!"
    "She reduced the weight and tried again, then reduced it a third time."
    BBW "Gggnnnn!"
    "She probably would have reduced it again if she wasn't already at the bare minimum. I looked over at Akira as Alice struggled to get to ten reps."
    show FMG sad
    FMG "...Um, you ok Alice? Need anything?"
    BBW "Ggnnnooo, thank you. Just doing what you said and taking it slow."
    FMG "...I didn't mean to the point where you're not even pulling the damn bar. For god's sake, you have it at the lowest level!"
    BBW "Did you not just tell us to know our limits? Are you now reversing yourself and telling me to risk injury by going beyond my limitations? What is it you want me to do?"
    show FMG angry
    FMG "No I...ugh screw it, I'm getting ice cream before I really get mad!"
    hide FMG with dissolve
    "And she stormed off. For a second I thought about going after her, trying to cool things off so at least she wouldn't leave mad, but then I decided it'd be better this way."
    "Plus, turning back to Alice, I saw that if I did want to play mediator I had another opportunity."
    show BBW neutral
    BBW "Well that was uncalled for. It was certainly arrogant of her."
    MC "Arrogant?"
    BBW "Not everyone is gifted with physical prowess, and for her to carry on as if anyone should be able to do what she can... That's arrogant."
    MC "I'm not sure that was her problem, but I agree she could have been a bit more patient... How about I talk to her later, once she's cooled off? She probably could help you with this better than I or Aida could."
    show BBW happy
    BBW "That's thoughtful, but you don't need to put yourself out. This was a worthwhile experiment, but I've reached the conclusion that I'm not cut out to be a gym rat. I don't think this stress of trying to constantly outdo myself would be good for my temperament, if Mizutani-san is any indication. Still, thank you for your assistance."
    MC "You're welcome. (I guess.)"
    BBW "Now, Aida, let's go back to the dorms. I feel a hot bath and massage is the best way to unwind after a workout like this."
    PRG "Y-Yes, ma'am! I'll get the oils."
    jump daymenu

label BBW006:
    scene Hallway with fade
    MCT "Classes are done, so what now? Don't want to go back to my room, I've got enough weirdness going on without someone trying to find more lurking around every corner. Maybe I can see if any of the clubs are recruiting yet."
    "..."
    MCT "Sounds like the music club is rehearsing. Not my thing... Oh!"
    show BBW neutral with dissolve
    MC "Niku- Alice. Thinking of joining the music club?"
    show BBW haughty
    BBW "Offering my services to the ensemble is one reason I'm here, though I'm disheartened to find out freshmen are not considered for seated positions. Waiting a year just to take my rightful place on the stage..."
    BBW "I'm more sorry for the club, having to endure without my contribution."
    MC "How thoughtful. So what instrument do you play?"
    BBW "I have my own natural instrument: my voice."
    MC "You're a singer?"
    BBW "A soprano. And a gifted one, I should say. I've been coached since I was five."
    MC "I didn't know the music club did operas."
    show BBW neutral
    BBW "According to the club adviser, they do not. Put more accurately, they never have."
    show BBW haughty
    BBW "But the higher arts are not more difficult by nature. With sufficient commitment and practice I'm sure they could put on a fair performance. And with me as the star..."
    show BBW neutral
    BBW "I'd also hoped to find a talent or two I could nurture during my time here."
    MC "Nurture?"
    BBW "The Nikumarus have a long history of patronage of the arts, one I hope to continue. I would like to get a start on it by finding a budding talent to encourage. Pushing them to refine their art and attain what greatness they were born for."
    BBW "Privilege, after all, comes with the responsibility of helping others."
    MCT "You sound both selfless and selfish as you say that."
    BBW "On that note, do you play any instruments, Hotsure-san?"
    MC "Me? Uh..."
    menu:
        "No, I don't.":
            jump BBW006_c1
        "I've practiced a little, but I'm not really talented.":        #maybe these should be skill checks?
            jump BBW006_c2
        "I don't mean to brag, but I'm a pretty skilled musician.":     #maybe these should be skill checks?
            jump BBW006_c3


label BBW006_c1:
    MC "No, I don't."
    BBW "Hmm. An honest answer, but a shame."
    MC "Does anybody here catch your eye? Or ear, I should say?"
    BBW "It's too soon to say. None of them are masters, so finding the seed of potential requires a deeper look. I'll need to sit in on a few more meetings."
    MC "I take it you'll be the joining the club, even as a benchwarmer?"
    BBW "...I am unfamiliar with that term. But yes. With my gift it would only be appropriate that I join. And I cannot convince the club president of their folly in keeping me in reserve if I am not here."
    MC "You don't take 'No' for an answer, do you?"
    show BBW haughty
    BBW "I'm a Nikumaru. A 'No' to me is just another obstacle to overcome."
    jump daymenu

label BBW006_c2:
    $setAffection("BBW", -1)
    MC "I've practiced a little, but I'm not really talented."
    BBW "Oh? What instrument?"
    MCT "Immediate regret setting in. What's an impressive instrument?"
    MC "Uh... Violin. I've had a few lessons, but I'm no, you know, virtuoso."
    BBW "None of the students here are, if the music club is any indicator. But talent can blossom anywhere when given a guiding hand. Show me what you can do."
    MC "Here? Now? Are you sure it's OK to use the club's instruments?"
    BBW "Of course. The instruments belong to the school, and we're students."
    MC "All right."
    "I squeaked out a few sharp chords that sounded like someone stroking a balloon. Alice's thoughts were too easy to read as she grimaced in pain."
    show BBW angry
    BBW "Enough!"
    MC "Sorry. It's been a while since I've practiced."
    show BBW neutral
    BBW "Maybe I shouldn't have expected much. You... You might have some skill. Some day."
    "She wasn't disappointed, but as she turned away I could tell she was let down."
    jump daymenu

label BBW006_c3:
    $setAffection("BBW", -3)
    MC "I don't mean to brag, but I'm a pretty skilled musician."
    MCT "Oh dear god, why did I say that? I can't even play the triangle."
    BBW "Really? Which instruments do you favor?"
    MCT "Instruments? Plural? Oh, jeez..."
    MC "I mostly play... violin. But I also toy with the oboe."
    MCT "Sure, let's keep lying."
    BBW "The violin? It wouldn't take much to outshine the other students here, but how experienced are you? Have you had many public performances?"
    MCT "Fix this, you dolt. Now!"
    MC "I've never performed in front of an audience. I don't have the nerves for it. Just a lot of practice in private."
    BBW "All that practice must have been worth something. Show me what you can do."
    "And before I could say anything she was thrusting one of the club's violins into my hands. This was too fast for me to deal with, I couldn't think of anything to say to get out of it. So, nervously, I put the violin under my chin like I had seen people do in movies and I tried stroking the bow back and forth."
    "The disgust on Alice's face was immediate, and I couldn't blame her. If the violin was a living being I would have been arrested for animal cruelty. But I still thought I could fake it if I could, I don't know, figure out how to stroke the chords right."
    show BBW angry
    BBW "Stop! Stop!"
    MC "Sorry. It's been a while since I-"
    BBW "Learned how to tune it properly? I don't know what kind of goofing off you think constitutes 'practice,' but you should keep this musical torture private."
    hide BBW with dissolve
    "And she stormed off. Which, considering her mood, may have been preferred."
    jump daymenu

label BBW007:
    scene Cafeteria with fade
    MCT "First time I haven't had trouble finding a spot. I guess other people are spending lunch up on the roof or in their classrooms, like at a normal school. Looking around, it does seem like a lot of people are drifting into cliques or avoiding certain people."
    MCT "And I'm off by myself, which is par for the course."
    "No sooner had I thought that than someone sat down across from me."
    show BBW neutral at Position (xpos=0.25, xanchor=0.5) with dissolve
    MC "Oh, Alice. Didn't know you'd be having lunch here."
    BBW "Why wouldn't I? It is a pleasant day outside, but it seems improper to eat in some random place. Or maybe it is simply proper to eat where the food is served. Structure is an oft-overlooked virtue, in life and in business."
    MC "If you say so."
    "It took me a second to realize Alice wasn't alone. Right behind her was Aida, holding a few packages."
    show PRG sad at Position (xpos=0.75, xanchor=0.5) with dissolve
    MC "Hi, Aida. How did you get so much mail already? It's still the first week of the year."
    PRG "Oh, it's not mine. I was carrying it for Nikumaru-sama. We just came from the mail room."
    extend " ... There was nothing for me."
    MCT "She seems a bit sad. Is there something about mail that bothers her? Better change the conversation."
    BBW "Interested in what I got?"
    MC "Uh..."
    BBW "A lot of it is the usual care package stuff. Hand lotion, chewable candies, perfume, a new phone -"
    MCT "That left 'usual' territory pretty quickly."
    BBW "But I also ordered myself some things. White knee-high stockings seem to be 'in' among the other students, and I was not aware how cold winters in this part of the country can get, so I needed a new coat."
    BBW "And Aida confided in me that she only has one pair of shoes and barely any clothing besides her school uniforms. So I ordered some stuff for her."
    MC "That was considerate."
    BBW "Well, she doesn't have a credit card or bank account of her own, so ordering things online are beyond her means. But it was the least I could do to facilitate her shopping."
    MC "Facilitate... You mean she still paid for the stuff herself?"
    BBW "But of course. I'm not running a charity. And I would like to point out that with my connections I was able to buy directly from the manufacturer, saving her money."
    MC "What do you mean by connections?"
    show BBW haughty
    BBW "I know the sons and daughters of many business owners and CEOs. We always turn up at the same hotels in Monaco or ski lodges in Switzerland. You don't think the owner of a factory that makes dresses or suits has to buy off the rack, do you?"
    MC "I guess not. So if I needed to buy a new laptop could you get me one at a discount?"
    show BBW neutral
    BBW "I suppose I could. Hitomi and I – that's Hitomi Ogawa, daughter of the president of Ogawa Electronics – aren't on the closest of terms, but she could get me one for... 90,000 yen. Plus 10%% commission for myself would be 99,000."
    MC "An Ogawa laptop for under a hundred thousand yen? That's pretty steep for some old model being unloaded-"
    BBW "That's for an Ogawa D2300. 22” monitor, if I remember correctly."
    MC "... For 99,000?! Are you serious?"
    BBW "Completely."
    MCT "Unbelievable. That's a 170,000-yen machine, and she says she can get one for under 100K?"
    BBW "Don't be surprised. I'd be buying direct from the company, so there's no middle-man mark-up. Except for my commission, of course."
    MC "O-Of course."
    BBW "Or would you prefer the Essence 4K? I could probably get that for, let me see..."
    "And she checked her smartphone. Was she checking the manufacturing cost online, or did she know what the mark-up from retailers was?"
    BBW "How does 115,000 yen sound?"
    MC "I think I might faint."
    BBW "Shall I order one? You don't have to pay me now, you can take care of that when it gets here."
    MC "No, no. I don't need a new laptop. I mean, I could use one, but I don't have that kind of money."
    BBW "Well you should have said so."
    show PRG neutral
    extend " ... Idea. Aida, take a note: I am going to start a business here at school. Direct retail, goods offered at a discount."
    MC "There's already a store on campus, you know."
    BBW "I know, I've seen it. But it lacks many of the essentials of modern living, and the mark-up is scandalous. 300 yen for a soda? I can beat those prices and still make a worthwhile profit."
    PRG "What do you need me to do, Nikumaru-sama?"
    BBW "Our first step will be to get the word out. We'll need some sort of ad campaign, make the people aware of my service. Then we'll need a system of taking orders and fulfilling them. Dorm-room delivery would be an enticing service; convenient for the customer."
    BBW "But the guys' dorm... Keisuke! How would you like a job?"
    MC "Me? Doing what?"
    BBW "Haven't you been listening? I'll need runners, people to deliver packages as they come in. I can offer you 1,000 yen an hour."
    MC "I... will think about it."
    MCT "She's actually serious about this. I wouldn't have guessed she was this sort of vigorous go-getter. I guess business runs in her blood."
    jump daymenu
    
label BBW008:
    scene Hallway with fade
    "After another day of classes I found myself not in my dorm and not in my classroom. I wasn't heading anywhere special, I was just wandering around."
    "After some time I found myself at the music room."
    scene Music Classroom with fade
    MCT "Maybe I can listen in on them practicing."
    "But the club wasn't meeting right now. Instead there were two people, Aida and another student. It's not like I wanted to spy on them, but I was curious and they were talking loud enough to overhear them."
    Student "-alented or not, I have no patience for someone trying to undermine my authority."
    show PRG sad with dissolve
    PRG "Y-yes, ma'am. But I don't think she means to be-"
    Student "You seem to be the closest thing she has to a friend, so maybe she'll listen to you. Tell her she can either be happy in the chorus or she can look for another club to join."
    PRG "Y-yes, ma'am."
    "The other girl (is she the music club president?) turned away, the conversation over. Head bowed, Aida made for the door. I stepped back, but not fast enough to not get caught."
    show PRG surprised
    PRG "Oh! H-Hotsure-san."
    MC "Hey, Aida."
    MCT "Should I ask what that was about? Aida looks pretty bummed."
    MC "Is something wrong? It looked like you were being given the third degree."
    show PRG neutral
    PRG "N-no. I wasn't in trouble. It's Nikumaru-san. She doesn't like being in the chorus, but Mizawa-san won't make her lead vocalist."
    MC "Is that the club president? Is Alice butting heads with her or something?"
    PRG "Yes. They keep getting into arguments, and now Mizawa-san is threatening to kick Nikumaru-san out if she doesn't behave."
    MC "I haven't known her too long, but Alice doesn't seem like much of a team player. Guess I'm not surprised she's already getting into trouble like this."
    show PRG sad
    PRG "I-I'm supposed to t-tell her to mind herself, b-but I don't think Nikumaru will listen to me. She's kind of head strong."
    MCT "And you're kind of a pushover."
    MCT "Oh, that's mean. But it's not wrong."
    menu:
        "Well, good luck with that.":
            $setAffection("PRG", -2)
            show PRG surprised
            PRG "..."
            MCT "I could go for a soda now."
            jump daymenu
        "Maybe I could help.":
            jump BBW008_prechoice

label BBW008_prechoice:
    $setAffection("PRG", 1)
    MC "I wouldn't say Alice listens to me so much as she hears what I say. I can pass the word along for you."
    show PRG happy
    PRG "C-could you?"
    show PRG sad
    PRG "I-I don't want to trouble you, but it would be so sad if she got kicked out of the club. She's a stranger here, you know. She doesn't fit in."
    MC "We're all strangers, but I get what you mean. She kind of fits that whole 'pushy American' stereotype, doesn't she?"
    show PRG angry
    PRG "Oh, no! Nikumaru-san is just very determined."
    MCT "Determined. Sure."
    MC "Do you know where Alice is now?"
    show PRG neutral
    PRG "She should be in the cafeteria. I made some snacks for her to sample while she works on setting up her business."
    MC "Might as well deliver the news now, then."

    scene Cafeteria with fade
    "We found Alice sitting at her usual table, one hand typing on a laptop and the other picking up tea room pastries from a tray next to her."
    show BBW happy at Position (xpos=0.25, xanchor=0.5) with dissolve
    show PRG neutral at Position (xpos=0.75, xanchor=0.5) with dissolve
    BBW "Hotsure-san, good afternoon. Thank you for bringing Aida back. I've been waiting for her for...five and a half minutes now."
    MC "Actually she brought me here. There's something I need... Something you should know."
    show BBW neutral
    BBW "Oh?"
    MC "Yeah, um... How's the music club? You're still doing that, right?"
    BBW "Despite my feelings on how it is being managed, yes, I am still a member."
    MC "Right, right. So I was told- That is, Aida was told..."
    show BBW angry
    BBW "..."
    "I stammered a few words, and Alice became irritated quickly."
    MC "We were told to tell you to, you know... Maybe ease up on the prima donna thing."
    BBW "Excuse me?"
    MC "It's not that you're... You can be a little... "
    MC "You're going to get kicked out if you don't stop fighting with the president."
    BBW "Oh, really? Aida, is this true?"
    show PRG sad
    PRG "Y-yes, Nikumaru-san."
    BBW "You go back and tell her..."
    MCT "She didn't understand anything I just said, did she?"
    show PRG neutral
    menu:
        "Say nothing. Let Alice do what she wants.":
            jump BBW008_c1
        "Suggest Alice not make things worse.":
            jump BBW008_c2
        "Tell Alice she's in the wrong.":
            jump BBW008_c3

label BBW008_c1:
    $setflag("BBW008_extrascene")
    MCT "Well, if she wants to pick a fight, let her. Whatever happens is on her head."
    show BBW haughty
    BBW "Thank you for bringing this to my attention, Hotsure-san. My esteem for Mizawa-san was already low, but to use an intermediary like this is pathetic."
    MC "No problem."
    "I decided to excuse myself then. Didn't want to get caught up in this drama."
    jump daymenu

label BBW008_c2:
    $setAffection("BBW", 1)
    MCT "Oh man, this is going to get out of hand quickly if I don't do something."
    MC "Maybe you shouldn't push back right away."
    show BBW neutral
    BBW "What do you mean? Should I let this stand-?"
    MC "Some people just don't get the message right away, do they? Clearly the club president - this Mizawa girl - hasn't recognized your talent yet."
    show BBW haughty
    BBW "No, she hasn't-"
    MC "So getting her face again won't do any good. This seems like one of those times where the person needs to realize their failure on their own."
    BBW "And what do I do in the meanwhile? Resign myself to the chorus until Mizawa-san decides to admit she was wrong?"
    MC "I don't think there's much you can do at the moment."
    BBW "Are you not familiar with the phrase 'The squeaky wheel gets the grease'? If I'm supposed to wait for that tone-deaf girl to realize my talent, I will be stuck in the chorus all year."
    MC "And have you ever heard the phrase 'The upturned nail gets hammered down'? If you keep fighting her you won't even be on the chorus."
    show BBW angry
    BBW "..."
    BBW "Hmm..."
    show BBW neutral
    BBW "Is it just me, or are Japanese people excessively non-confrontational?"
    BBW "Very well. Aida, forget my last order. I'll toe the line, for now."
    BBW "But not forever, Hotsure-san. I don't intend to let my genius go ignored indefinitely."
    MC "Wait, why are you making it sound like it's my job to get you out of the chorus?"
    jump daymenu

label BBW008_c3:
    $setAffection("BBW", -1)
    MC "Can't you just admit that you're in the wrong here?"
    show BBW angry
    BBW "I beg your pardon?"
    MC "You're not the leader of the music club, are you?"
    BBW "I'm the best singer-"
    MC "That's a no, then. Well, the actual leader has made a decision, and it doesn't matter if you like it or not."
    MC "Maybe you are the best singer, but there's more to an ensemble, a group of people, than any one person getting what they want."
    MC "You're going to have a hard time getting along here if you don't understand that. We're all dealing with some pretty major stuff right now, not just you."
    BBW "How dare you..."
    "She didn't have to say anything, I knew what she was thinking. All the better, as I wasn't looking for a fight or anything."
    MC "Just something to think about."
    "And I turned and walked away. Maybe a bit quicker than I intended, but I didn't want to stay and get chewed out or anything."
    jump daymenu
