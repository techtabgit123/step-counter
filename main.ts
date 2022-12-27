input.onGesture(Gesture.Shake, function () {
    Steps += 1
})
let Steps = 0
basic.forever(function () {
    basic.showNumber(Steps)
})
