label p1:
    play music "audio/panst_02.ogg"
    scene room
    with fade

    gg "{cps=20}{i}был очень тяжелый день. я даже не могу описать насколько сильно я устал... {/i}{p=0.5}{/cps}"
    gg "{cps=20}{i}радует, что все трудности этого дня позади и я наконец-то могу лечь в свою любимую кроватку, укрыться любимым мягеньким одеялком и хорошо поспать.{/i}{p=0.5}{/cps}"
    gg "{cps=20}{i}мне интересно, что ждет меня завтра, но, если честно, я даже не могу об этом, как обычно, подумать..{/i}{p=0.5}{/cps}"
    gg "{cps=20}{i}..я очень сильно хочу спать..{/i}{p=0.5}{/cps}{nw}"

    menu:
        gg "{i}..я очень сильно хочу спать..{/i}"
        "{cps=20}все таки подумать о том, что будет завтра{/cps}":
            jump ch1_1
        "{cps=20}утро вечера мудренее{/cps}":
            jump ch1_2

    label ch1_1:

        gg "{cps=20}{i}...думаю я все же слишком устал для этого...{/i}{/cps}"
        jump ch1

    label ch1_2:

        gg "{cps=20}{i}..наконец-то.. я могу поспать...{/i}{/cps}"
        jump ch1

    label ch1:
        scene w
        with bl
        gg "{cps=20}{i}как же рано я проснулся..{/i}{p=0.5}{/cps}"
        gg "{cps=20}{i}хотя, \"проснулся\" - это громко сказано.{p=0.5}как бы сильно мне не хотелось продолжить спать,{w=0.2} нужно вставать.{/i} {/cps}"

    menu:
        gg "{i}может, меня немного порадует кофе?{/i}"
        "сделать кофе":
            jump ch2
        "обойтись чаем":
            jump ch3

    label ch3:
        scene kit
        with fade
        gg "{cps=20}{i}пока греется чайник, можно и написать список продуктов.{/i}{/cps}"
        au "{cps=20}наш дорогой друг составляет список продуктов. давно не было у него настроения что-то готовить.{p=0.2}наконец-то будет нормальная еда в доме. сегодня он будет готовить овощное рагу с мясом.{w=0.3} превосходно!{p}{/cps}"
        gg "{cps=20}{i}так, теперь чай.{/i}{/cps}"
        scene kit2
        with fade
        gg "{cps=20}{i}утро... что-то в нем, все таки, есть..{p=0.2}правда, сейчас как-то это не особо заметно.{/i}{p}{/cps}"
        gg "{cps=20}{i}единственное, что меня сейчас немного радует, так это горячий чай. так согревает....{/i}{nw}{/cps}"
        stop music
        jump flash
        
    label ch2:
        scene kit
        with fade
        gg "{cps=20}{i}пока греется чайник, можно и написать список продуктов.{/i}{/cps}"
        au "{cps=20}наш дорогой друг составляет список продуктов. давно не было у него настроения что-то готовить.{p=0.2} наконец-то будет нормальная еда в доме.{p}{/cps}"
        au "{cps=20}сегодня он будет готовить овощное рагу с мясом.{w=0.3} превосходно!{p}{/cps}"
        gg "{cps=20}{i}так, теперь можно сделать кофе!{/i}{/cps}"
        scene kit2
        with fade
        gg "{cps=20}{i}утро... что-то в нем, все таки, есть..{p=0.2}правда, если оно начинается с кофе.{/i}{p}{/cps}"
        gg "{cps=20}{i}а что? я слишком сильно люблю кофе! стоит сделать всего глоток, как ранний подъем становится не такой уж и трагедией, да и вообще...{/i}{nw}{/cps}"
        stop music
        jump flash

    label flash:
        play music "audio/kap_01.ogg"
        play sound "audio/voices1.ogg"
        scene black
        with flashbulb
        window hide
        scene 1
        pause .2
        scene 2
        pause .2
        scene 3
        pause .2
        scene 4
        pause .2
        scene 5
        pause .2
        scene 6
        pause .2
        scene 7
        pause .2
        scene 8
        pause .2
        scene 9
        pause .2
        scene 10
        pause .2
        scene 11
        pause .2
        scene 12
        pause .2
        scene 13
        pause .2
        scene 14
        pause .2
        scene 15
        pause .2
        scene 16
        pause .2
        scene 17
        pause .2
        scene 18
        pause .2
        scene 19
        pause .2
        scene 20
        pause .2
        scene 21
        pause .2
        scene 22
        pause .2
        scene 23
        pause .2
        scene 24
        pause .2
        scene 25
        pause .2
        scene 26
        pause .2
        scene 27
        pause .2
        scene 28
        pause .02
        scene 29
        pause .002
        scene 30
        pause .002
        scene 31
        pause .002
        scene black
        with teleport
        $ renpy.pause (2)
        stop sound
        scene kit2
        with flashbulb
        window show
        gg "{cps=20}{i}...какого черта это сейчас было?....{/i}{p}{/cps}"
        $ renpy.notify(_("Странные голоса в голове?..."))
        gg "{cps=20}{i}..и кружка любимая разбилась...{p=0.2}...прекрасно началось утро. {p=0.2}просто {w=0.1} прекрасно.{/i}{/cps}"
        scene kit
        with fade
        gg "{cps=20}{i}все таки очень странное явление меня посетило..{p=0.1}надеюсь, этого больше не будет.{/i}{p}{/cps}"
        stop music fadeout 2
        gg "{cps=20}{i}ладно, нужно идти в магазин.{/i}{p}{/cps}"
        scene mr
        with fade
        play music "audio/panst_02.ogg" fadeout 5
        au "{cps=20}как же давно он не выходил из дома.. {w=0.2}даже очень.{p=0.2}наконец-то он сходил в магазин. ему давно пора прогуляться!{/cps}"
        scene st
        with fade
        gg "{cps=20}{i}на улице так хорошо. ни холодно, ни жарко, легкий ветер.. люблю такую погоду!{/i}{p}{/cps}"
    menu:
        gg "{i}может, немного посидеть в парке?..{/i}"
        "зайти в парк":
            jump ch4
        "пойти домой":
            jump ch5


    label ch4:
        scene park
        with fade
        gg "{cps=20}{i}люблю этот парк. тут очень много белок и здесь всегда выгуливают много собак.{/i}{p}{/cps}"
        gg "{cps=20}{i}если повезет, можно погладить какую нибудь собачку. {p=0.1}если крупно повезет, можно погладить и белку..{/i}{p}{/cps}"
        window hide
        $ renpy.pause(5)
        window show
        gg "{cps=20}{i}что ж.. пора домой. нужно готовить!{/i}{p}{/cps}"
        jump ch5

    label ch5:
        scene kit
        with fade
        au "{cps=20}он прекрасно готовит. вообще, ему стоило быть поваром, как он изначально и хотел!{p=0.2}но пошел на дизайнера. не то что бы он великий дизайнер...{p=0.2}он просто довольно хорош в этом и смог пройти на бюджет.{/cps}"
        au "{cps=20}он подумал, что это принесет больше счастья... {w=0.2}но это принесло ему только печаль и творческий кризис. так и рушатся мечты.{/cps}"
        gg "{cps=20}{i}и..... с готовкой покончено! только вот я совсем не голоден. но мне все равно срочно нужно заняться работой!{/i}{p}{/cps}"
        stop music
        play music "audio/kap_01.ogg"
        play sound "audio/voices2.ogg"
        scene aa
        with flashbulb
        window hide
        scene a1
        pause .2
        scene a2
        pause .2
        scene a3
        pause .2
        scene a4
        pause .2
        scene a5
        pause .2
        scene a6
        pause .2
        scene a7
        pause .2
        scene a8
        pause .2
        scene a9
        pause .2
        scene a10
        pause .2
        scene a11
        pause .2
        scene a12
        with flashbulb
        pause .2
        scene a13
        with teleport
        pause .2
        scene a14
        with teleport
        pause .2
        scene a15
        with flashbulb
        pause .2
        scene a16
        with teleport
        pause .2
        scene a17
        with teleport
        pause .2
        scene a18
        with flashbulb
        pause .0001
        scene a19
        with tp
        pause .0001
        scene a20
        with tp
        pause .0001
        scene a21
        with tp
        pause .0001
        scene a22
        with tp
        pause .0001
        scene a23
        with flashbulb
        pause .0001
        scene a24
        with tp
        pause .0001
        scene a25
        with tp
        pause .0001
        scene a26
        with tp
        pause .0001
        scene a27
        with tp
        pause .0001
        scene a28
        with tp
        pause .001
        $ renpy.pause (0.02)
        stop music fadeout 2
        scene bed
        with flashbulb
        window show
        play sound "audio/end_01.ogg"
        gg "{cps=20}{i}иногда мне кажется, что у меня потребность страдать..{/i}{p}{/cps}"
        gg "{cps=20}{i}когда-то у меня все было замечательно..{/i}{p}{/cps}"
        gg "{cps=20}{i}вокруг меня было много людей,{w=0.2} а сейчас я совершенно один{/i}{p}{/cps}"
        gg "{cps=20}{i}сам с собой и своими мыслями{/i}{p}{/cps}"
        gg "{cps=20}{i}как же хочется снова оказаться в том прекрасном времени, где я не был одинок...{/i}{p}{/cps}"
        gg "{cps=20}{i}почему все так получилось?..{/i}{p}{/cps}"
        gg "{cps=20}{i}...{/i}{p}{/cps}"
        gg "{cps=20}{i}как же хочется покоя.{/i}{p}{/cps}"

        jump demo




