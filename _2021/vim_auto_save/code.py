from manimlib import *
class DrawFile(Scene):
    def construct(self):
        file = Square(4)
        self.play(ShowCreation(file))

class vim_intro(Scene):
    def construct(self):
        vim_def = Text("The best text editor (after Emacs of course)",
                font_size=30)
        vim_def.to_edge(DOWN * 3)
        self.play(Write(vim_def))
        self.wait()
class cmd_explanation(Scene):
    command = "autocmd BufWritePost <Path to the file> !<Commands>" 
    command_exp = "autocmd BufWritePost ~/dox/myfile !cp ~/dox/myfile ~"
    mono_font = "monaco"
    include_pi = True
    def construct(self):
        cmd = Text(self.command,
                font_size=25,
                font= self.mono_font,
                t2c={"autocmd": RED,
                "BufWritePost": YELLOW_D,
                })
        underline = Underline(cmd, buff=0.5)
        underline.insert_n_curves(30)
        underline.set_stroke(BLUE, width=[0, 3, 3, 3, 0])
        underline.scale(1.5)
                
        cmd_exp = Text(self.command_exp,
                font_size=25,
                font= self.mono_font,
                t2c={"autocmd": RED,
                "BufWritePost": YELLOW_D,
                })

        self.play(Write(cmd), run_time=2)
        self.wait()
        self.play(FadeTransform(cmd, cmd_exp))
        self.wait()
        self.play(cmd_exp.animate.scale(0.75).to_corner(UL),run_time=2)
