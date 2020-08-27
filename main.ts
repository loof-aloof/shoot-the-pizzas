controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    if (!(Ammo <= 0)) {
        projectile = sprites.createProjectileFromSprite(img`
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
            `, Dude, 150, 0)
        music.pewPew.play()
        Ammo += -1
    } else {
        music.playMelody("- C - C - C - C ", 120)
    }
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (!(Ammo <= 0)) {
        projectile = sprites.createProjectileFromSprite(img`
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
            `, Dude, -150, 0)
        Ammo += -1
    } else {
        music.playMelody("- C - C - C - C ", 120)
    }
})
let projectile: Sprite = null
let Dude: Sprite = null
let Ammo = 0
scene.setBackgroundColor(11)
Ammo = 15
Dude = sprites.create(img`
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 5 5 5 5 5 5 5 5 5 . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . 5 5 5 5 5 5 5 5 5 5 5 . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . 5 5 5 5 5 5 5 5 5 5 5 5 5 . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . 5 5 5 5 5 5 5 5 2 2 2 2 2 5 5 . . . . . . . . . . . . . 
    . . . . . . . . . . . . 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 . . . . . . . . . . . . 
    . . . . . . . . . . . . f f f f f f f f f f f f f f 2 2 f . . . . . . . . . . . . 
    . . . . . . . . . . . . f 5 f f f f f f 5 f f f f f f 2 f . . . . . . . . . . . . 
    . . . . f . . . . . . . 5 5 f f f 1 f 5 5 5 f f f 1 f 2 5 . . . . . . . f . . . . 
    . . . f f f f f f f f . 5 5 f f 1 f f 5 5 5 f f 1 f f 2 2 . f f f f f f f f . . . 
    . f f f f f f f f f f . 5 5 5 f f f 5 5 5 5 5 f f f 5 5 2 . f f f f f f f f f f . 
    . . . f f f f f f f f . 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 2 . f f f f f f f f . . . 
    . . . . . . . f f f . . 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 . . f f f . . . . . . . 
    . . . . . . . f f f . . 5 5 5 5 5 5 f f f f f 5 5 5 5 5 5 . . f f f . . . . . . . 
    . . . . . . . f f f . . . 5 5 5 5 f 5 5 5 5 5 f 5 5 5 5 . . . f f f . . . . . . . 
    . . . . . . . f f f . . . . 5 5 5 5 5 5 5 5 5 f 5 5 5 . . . . f f f . . . . . . . 
    . . . . . . . . f . . . . . . 5 5 5 5 5 5 5 5 5 5 5 . . . . . . f . . . . . . . . 
    . . . . . . . . . . . . . . . . 5 5 5 5 5 5 5 5 5 . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
    `, SpriteKind.Player)
Dude.setPosition(6, 80)
Dude.setFlag(SpriteFlag.StayInScreen, true)
controller.moveSprite(Dude, 100, 100)
info.setScore(0)
let Pizza = sprites.create(img`
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . e e e e e e e e e . . . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . e e e e e e e e e e e . . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . e e e e e e e e e e e e . . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . e 2 5 5 5 5 5 5 5 5 5 5 . . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . e 2 5 5 5 f f 5 5 5 f f . . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . e 2 5 5 f 1 f 5 5 f 1 f . . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . e 2 2 5 f f 5 5 5 f f 5 . . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . e 2 5 5 5 5 5 5 5 5 5 . . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . e 2 5 5 5 5 f f f 5 5 . . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . e 2 5 5 f f f f 5 5 . . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . e 2 5 5 2 f f f 5 5 . . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . e 2 5 2 5 5 5 5 . . . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . e 2 5 2 2 5 5 5 . . . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . e 2 5 2 5 5 5 . . . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . f e 2 5 5 5 f . . . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . f f e 2 5 5 f . . . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . f f . e e f f . . . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . f f . . . f f . . . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . f f . . . f f . . . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . f f . . . f f . . . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . f f . . . f f . . . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . f f f f . . . f f f f . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
    `, SpriteKind.Enemy)
Pizza.follow(Dude, 16)
game.onUpdateInterval(500, function () {
    if (!(info.score() >= 5000)) {
    	
    } else {
    	
    }
})
