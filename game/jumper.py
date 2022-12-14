class Display():

    def __init__(self):
        self.dash = '_____'
        self.parachute = [' '] * 15
    # dislay the guessed letters
    def displayLetters(self, index,letter):
        if letter != '' and index != -1:
            # append the guessed letter to sel.dash
            self.dash = self.dash[:index] + letter + self.dash[index + 1:]
            print("\t", self.dash)
            print()

        else:
            print("\t", self.dash)
            print()
    # display parachutes based on the number of chances left
    def display_parachute(self,chances):
        if chances == 0:
            print(self.parachute[1] + ' ' + '__________')
            print(self.parachute[2] + '/' + self.parachute[3] + '________' + self.parachute[4] + '\x5c')
            print(self.parachute[5] + '\x5c' + self.parachute[6] + '         /')
            print(self.parachute[7] + ' \x5c' + self.parachute[8] + '       /')
            print(self.parachute[9] + '     O')
            print(self.parachute[10] + '   /' + self.parachute[11] + '|' + self.parachute[12] + '\x5c')
            print(self.parachute[13] + '    /' + self.parachute[14] + '\x5c')
            return
        elif chances == 1:
            print(self.parachute[2] + '/' + self.parachute[3] + '________' + self.parachute[4] + '\x5c')
            print(self.parachute[5] + '\x5c' + self.parachute[6] + '         /')
            print(self.parachute[7] + ' \x5c' + self.parachute[8] + '       /')
            print(self.parachute[9] + '     O')
            print(self.parachute[10] + '   /' + self.parachute[11] + '|' + self.parachute[12] + '\x5c')
            print(self.parachute[13] + '    /' + self.parachute[14] + '\x5c')
            return
        elif chances == 2:
            print(self.parachute[5] + '\x5c' + self.parachute[6] + '         /')
            print(self.parachute[7] + ' \x5c' + self.parachute[8] + '       /')
            print(self.parachute[9] + '     O')
            print(self.parachute[10] + '   /' + self.parachute[11] + '|' + self.parachute[12] + '\x5c')
            print(self.parachute[13] + '    /' + self.parachute[14] + '\x5c')
            return
        elif chances == 3:
            print(self.parachute[7] + ' \x5c' + self.parachute[8] + '       /')
            print(self.parachute[9] + '     O')
            print(self.parachute[10] + '   /' + self.parachute[11] + '|' + self.parachute[12] + '\x5c')
            print(self.parachute[13] + '    /' + self.parachute[14] + '\x5c')
            return
        elif chances == 4:
            print(self.parachute[9] + '     O')
            print(self.parachute[10] + '   /' + self.parachute[11] + '|' + self.parachute[12] + '\x5c')
            print(self.parachute[13] + '    /' + self.parachute[14] + '\x5c')
            return
        elif chances == 5:
            print(self.parachute[9] + '     X')
            print(self.parachute[10] + '   /' + self.parachute[11] + '|' + self.parachute[12] + '\x5c')
            print(self.parachute[13] + '    /' + self.parachute[14] + '\x5c')
            return



