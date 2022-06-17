#настройки
define config.hard_rollback_limit = 0
define config.rollback_enabled = False
define config.has_autosave = False
#персонажи
define narrator = Character(kind=nvl, color="#fff", what_xalign=0.5, what_textalign=0.0)
define narrator1 = Character(kind=nvl, color="#fff", what_xalign=0.5, what_yalign=0.5, what_textalign=0.5, what_layout='subtitle')
define gg = Character(color="#fff")
define au = Character(color="#fff",what_outlines=[(1, "#6e8491")], what_xalign=0.5, what_textalign=0.0)
#переходы
define flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')
define teleport = ImageDissolve("imagedissolve teleport.png", 1.0, 0)
define tp = ImageDissolve("imagedissolve teleport.png", 0.2, 0)
define bl = Fade(0.8, 1.8, 0.8, color="#000")