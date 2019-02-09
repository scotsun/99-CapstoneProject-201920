import rosebot
def main():
    #test_beep_times(1)
    #test_tone(100,10)
    test_go_straight_seconds(100,10)


def test_beep_times(times):
    robot=rosebot.RoseBot()
    robot.sound_system.beep_for_n_times(times)

def test_tone(freq,duration):
    robot=rosebot.RoseBot()
    robot.sound_system.tone_freq(freq,duration)

def test_go_straight_seconds(seconds,speed):
    robot=rosebot.RoseBot()
    robot.drive_system.go_straight_for_seconds(seconds,speed)



main()