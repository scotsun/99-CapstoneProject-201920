import rosebot
def main():
    test_beep_times(1)
    test_tone(100,10)


def test_beep_times(times):
    robot=rosebot.RoseBot()
    robot.sound_system.beep_for_n_times(times)

def test_tone(freq,duration):
    robot=rosebot.RoseBot()
    robot.sound_system.tone_freq(freq,duration)


main()