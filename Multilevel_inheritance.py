class MoveCharacter:
    def move_fwd(self):
        print("Move FWD")

    def move_bwd(self):
        print("Move FWD")


class JumpCharacter(MoveCharacter):
    def jump_1level(self):
        print("Jump character 1 level")

    def jump_2level(self):
        print("Jump character 2 level")

class Pokemon(JumpCharacter):
    # pass
    def move_fwd(self):
        print("Pokemaon moving")


p = Pokemon()
p.move_fwd()
p.move_bwd()
p.jump_1level()
p.jump_2level()
