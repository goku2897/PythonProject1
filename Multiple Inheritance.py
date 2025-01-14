class MoveCharacter:
    def move_fwd(self):
        print("Move FWD")

    def move_bwd(self):
        print("Move FWD")


class JumpCharacter:
    def jump_1level(self):
        print("Jump character 1 level")

    def jump_2level(self):
        print("Jump character 2 level")

class Pokemon(MoveCharacter, JumpCharacter):
    # pass
    def move_fwd(self):
        print("Pokemaon moving")

p = Pokemon()

p.move_bwd()
p.move_fwd()
p.jump_1level()
p.jump_2level()