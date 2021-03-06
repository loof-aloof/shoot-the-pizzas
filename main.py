@namespace
class SpriteKind:
    crate = SpriteKind.create()

def on_on_overlap(sprite, otherSprite):
    global Ammo
    otherSprite.destroy()
    Ammo += 5
    music.power_up.play()
sprites.on_overlap(SpriteKind.player, SpriteKind.crate, on_on_overlap)

def on_a_pressed():
    global projectile, Ammo
    if not (Ammo <= 0):
        if Appearance == 2:
            projectile = sprites.create_projectile_from_sprite(img("""
                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . 5 5 1 1 1 . . . . . 
                                    . . . . . 4 4 5 5 5 1 . . . . . 
                                    . . . . . . 4 4 4 5 5 . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . .
                """),
                Dude,
                -150,
                0)
            music.pew_pew.play()
            Ammo += -1
        else:
            projectile = sprites.create_projectile_from_sprite(img("""
                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . 5 5 1 1 1 . . . . . . . 
                                    . . . . 4 5 5 5 1 1 . . . . . . 
                                    . . . . 4 4 4 5 5 . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . .
                """),
                Dude,
                150,
                0)
            music.pew_pew.play()
            Ammo += -1
    else:
        game.splash("OUT OF AMMO! HOLD OUT", "FOR THE NEXT CRATE!")
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_left_pressed():
    global Appearance
    Dude.set_image(img("""
        .........................................
                .........................................
                .........................................
                .........................................
                .........................................
                .........................................
                .........................................
                .........................................
                .........................................
                .........................................
                ................555555555................
                ...............55555555555...............
                ..............5555555555555..............
                .............555555552222255.............
                ............22222222222222222............
                ............ffffffffffffff22f............
                ............f5ffffff5ffffff2f............
                ....f.......55fff1f555fff1f25............
                ...ffffffff.55ff1ff555ff1ff22............
                .ffffffffff.555fff55555fff552............
                ...ffffffff.55555555555555552............
                .......fff..55555555555555555............
                .......fff..555555fffff555555............
                .......fff...5555f55555f5555.............
                .......fff....555555555f555..............
                ........f......55555555555...............
                ................555555555................
                .........................................
                .........................................
                .........................................
                .........................................
                .........................................
                .........................................
                .........................................
                .........................................
                .........................................
                .........................................
                .........................................
                .........................................
                .........................................
                .........................................
    """))
    Appearance = 2
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_on_overlap2(sprite, otherSprite):
    sprite.destroy(effects.spray, 200)
    music.ba_ding.play()
    info.change_score_by(10)
sprites.on_overlap(SpriteKind.enemy, SpriteKind.projectile, on_on_overlap2)

def on_right_pressed():
    global Appearance
    Dude.set_image(img("""
        .........................................
                .........................................
                .........................................
                .........................................
                .........................................
                .........................................
                .........................................
                .........................................
                .........................................
                .........................................
                ................555555555................
                ...............55555555555...............
                ..............5555555555555..............
                .............555555552222255.............
                ............22222222222222222............
                ............ffffffffffffff22f............
                ............f5ffffff5ffffff2f............
                ............55fff1f555fff1f25.......f....
                ............55ff1ff555ff1ff22.ffffffff...
                ............555fff55555fff552.ffffffffff.
                ............55555555555555552.ffffffff...
                ............55555555555555555..fff.......
                ............555555fffff555555..fff.......
                .............5555f55555f5555...fff.......
                ..............555555555f555....fff.......
                ...............55555555555......f........
                ................555555555................
                .........................................
                .........................................
                .........................................
                .........................................
                .........................................
                .........................................
                .........................................
                .........................................
                .........................................
                .........................................
                .........................................
                .........................................
                .........................................
                .........................................
    """))
    Appearance = 1
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_on_overlap3(sprite, otherSprite):
    mySprite.destroy()
    info.change_life_by(1)
    music.power_up.play()
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap3)

def on_on_overlap4(sprite, otherSprite):
    otherSprite.destroy()
    music.power_down.play()
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap4)

ammo_box: Sprite = None
Pizza: Sprite = None
Spawn_location = 0
mySprite: Sprite = None
projectile: Sprite = None
Appearance = 0
Dude: Sprite = None
Ammo = 0
scene.set_background_color(11)
info.set_life(3)
Ammo = 10
Dude = sprites.create(img("""
        .........................................
            .........................................
            .........................................
            .........................................
            .........................................
            .........................................
            .........................................
            .........................................
            .........................................
            .........................................
            ................555555555................
            ...............55555555555...............
            ..............5555555555555..............
            .............555555552222255.............
            ............22222222222222222............
            ............ffffffffffffff22f............
            ............f5ffffff5ffffff2f............
            ............55fff1f555fff1f25.......f....
            ............55ff1ff555ff1ff22.ffffffff...
            ............555fff55555fff552.ffffffffff.
            ............55555555555555552.ffffffff...
            ............55555555555555555..fff.......
            ............555555fffff555555..fff.......
            .............5555f55555f5555...fff.......
            ..............555555555f555....fff.......
            ...............55555555555......f........
            ................555555555................
            .........................................
            .........................................
            .........................................
            .........................................
            .........................................
            .........................................
            .........................................
            .........................................
            .........................................
            .........................................
            .........................................
            .........................................
            .........................................
            .........................................
    """),
    SpriteKind.player)
Dude.set_position(6, 80)
Dude.set_flag(SpriteFlag.STAY_IN_SCREEN, False)
controller.move_sprite(Dude, 100, 100)
info.set_score(0)

def on_update_interval():
    global Spawn_location, Pizza, mySprite, ammo_box
    if not (info.score() >= 5000):
        Spawn_location = randint(1, 4)
        if Spawn_location == 1:
            Pizza = sprites.create(img("""
                    .........................................
                                    .........................................
                                    .........................................
                                    .........................................
                                    .........................................
                                    .........................................
                                    .........................................
                                    .........................................
                                    .........................................
                                    .........................................
                                    ..............eeeeeeeee..................
                                    .............eeeeeeeeeee.................
                                    ............eeeeeeeeeeee.................
                                    ............e25555555555.................
                                    ............e2555ff555ff.................
                                    ............e255f1f55f1f.................
                                    ............e225ff555ff5.................
                                    .............e2555555555.................
                                    .............e25555fff55.................
                                    ..............e255ffff55.................
                                    ..............e2552fff55.................
                                    ...............e2525555..................
                                    ...............e2522555..................
                                    ................e252555..................
                                    ................fe2555f..................
                                    ................ffe255f..................
                                    ................ff.eeff..................
                                    ................ff...ff..................
                                    ................ff...ff..................
                                    ................ff...ff..................
                                    ................ff...ff..................
                                    ..............ffff...ffff................
                                    .........................................
                                    .........................................
                                    .........................................
                                    .........................................
                                    .........................................
                                    .........................................
                                    .........................................
                                    .........................................
                                    .........................................
                """),
                SpriteKind.enemy)
            Pizza.set_position(7, 7)
            Pizza.follow(Dude, 16)
        if Spawn_location == 2:
            Pizza = sprites.create(img("""
                    .........................................
                                    .........................................
                                    .........................................
                                    .........................................
                                    .........................................
                                    .........................................
                                    .........................................
                                    .........................................
                                    .........................................
                                    .........................................
                                    ..............eeeeeeeee..................
                                    .............eeeeeeeeeee.................
                                    ............eeeeeeeeeeee.................
                                    ............e25555555555.................
                                    ............e2555ff555ff.................
                                    ............e255f1f55f1f.................
                                    ............e225ff555ff5.................
                                    .............e2555555555.................
                                    .............e25555fff55.................
                                    ..............e255ffff55.................
                                    ..............e2552fff55.................
                                    ...............e2525555..................
                                    ...............e2522555..................
                                    ................e252555..................
                                    ................fe2555f..................
                                    ................ffe255f..................
                                    ................ff.eeff..................
                                    ................ff...ff..................
                                    ................ff...ff..................
                                    ................ff...ff..................
                                    ................ff...ff..................
                                    ..............ffff...ffff................
                                    .........................................
                                    .........................................
                                    .........................................
                                    .........................................
                                    .........................................
                                    .........................................
                                    .........................................
                                    .........................................
                                    .........................................
                """),
                SpriteKind.enemy)
            Pizza.set_position(145, 7)
            Pizza.follow(Dude, 16)
            if info.life() < 4:
                mySprite = sprites.create(img("""
                        .....................
                                            .....................
                                            .....................
                                            .....................
                                            ...eeeeeeeeeeeeeee...
                                            ...e1111111111111e...
                                            ...e1111111111111e...
                                            ...e1111155511111e...
                                            ...eeeeee555eeeeee...
                                            ...e1111155511111e...
                                            ...e1111111111111e...
                                            ...e1111112111111e...
                                            ...e1111122211111e...
                                            ...e1111112111111e...
                                            ...e1111111111111e...
                                            ...eeeeeeeeeeeeeee...
                                            .....................
                                            .....................
                                            .....................
                                            .....................
                                            .....................
                    """),
                    SpriteKind.food)
        if Spawn_location == 3:
            Pizza = sprites.create(img("""
                    .........................................
                                    .........................................
                                    .........................................
                                    .........................................
                                    .........................................
                                    .........................................
                                    .........................................
                                    .........................................
                                    .........................................
                                    .........................................
                                    ..............eeeeeeeee..................
                                    .............eeeeeeeeeee.................
                                    ............eeeeeeeeeeee.................
                                    ............e25555555555.................
                                    ............e2555ff555ff.................
                                    ............e255f1f55f1f.................
                                    ............e225ff555ff5.................
                                    .............e2555555555.................
                                    .............e25555fff55.................
                                    ..............e255ffff55.................
                                    ..............e2552fff55.................
                                    ...............e2525555..................
                                    ...............e2522555..................
                                    ................e252555..................
                                    ................fe2555f..................
                                    ................ffe255f..................
                                    ................ff.eeff..................
                                    ................ff...ff..................
                                    ................ff...ff..................
                                    ................ff...ff..................
                                    ................ff...ff..................
                                    ..............ffff...ffff................
                                    .........................................
                                    .........................................
                                    .........................................
                                    .........................................
                                    .........................................
                                    .........................................
                                    .........................................
                                    .........................................
                                    .........................................
                """),
                SpriteKind.enemy)
            Pizza.set_position(6, 107)
            if Ammo < 4:
                ammo_box = sprites.create(img("""
                        .....................
                                            .....................
                                            .....................
                                            .....................
                                            ...eeeeeeeeeeeeeee...
                                            ...e7777777777777e...
                                            ...e7777777777777e...
                                            ...e7777755577777e...
                                            ...eeeeee555eeeeee...
                                            ...e7777755577777e...
                                            ...e7777777777777e...
                                            ...e7777dddd77777e...
                                            ...e777777df77777e...
                                            ...e7777777f77777e...
                                            ...e7777777777777e...
                                            ...eeeeeeeeeeeeeee...
                                            .....................
                                            .....................
                                            .....................
                                            .....................
                                            .....................
                    """),
                    SpriteKind.crate)
            Pizza.follow(Dude, 16)
        if Spawn_location == 4:
            Pizza = sprites.create(img("""
                    .........................................
                                    .........................................
                                    .........................................
                                    .........................................
                                    .........................................
                                    .........................................
                                    .........................................
                                    .........................................
                                    .........................................
                                    .........................................
                                    ..............eeeeeeeee..................
                                    .............eeeeeeeeeee.................
                                    ............eeeeeeeeeeee.................
                                    ............e25555555555.................
                                    ............e2555ff555ff.................
                                    ............e255f1f55f1f.................
                                    ............e225ff555ff5.................
                                    .............e2555555555.................
                                    .............e25555fff55.................
                                    ..............e255ffff55.................
                                    ..............e2552fff55.................
                                    ...............e2525555..................
                                    ...............e2522555..................
                                    ................e252555..................
                                    ................fe2555f..................
                                    ................ffe255f..................
                                    ................ff.eeff..................
                                    ................ff...ff..................
                                    ................ff...ff..................
                                    ................ff...ff..................
                                    ................ff...ff..................
                                    ..............ffff...ffff................
                                    .........................................
                                    .........................................
                                    .........................................
                                    .........................................
                                    .........................................
                                    .........................................
                                    .........................................
                                    .........................................
                                    .........................................
                """),
                SpriteKind.enemy)
            Pizza.set_position(147, 106)
            Pizza.follow(Dude, 16)
    else:
        game.over(True, effects.melt)
game.on_update_interval(2000, on_update_interval)
