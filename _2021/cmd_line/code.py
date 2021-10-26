from manimlib import *
class cmd_str(Scene):
    def construct(self):
        circle = Circle()
        command = Text("$ cmd [OPTIONS]... [ARGUMENTS]...", 
                font_size=30,
                font="Consolas",
                t2c={"$": GREEN, 
                    "[OPTIONS]...": BLUE, 
                    "[ARGUMENTS]...": RED})

        ls_cmd = Text("$ ls -a ~/Documents", 
                font_size=30,
                font="Consolas",
                t2c={"$": GREEN, 
                    "-a": BLUE, 
                    "~/Documents": RED})

        self.play(Write(command))
        self.wait()
        self.play(FadeTransform(command, ls_cmd))
        self.wait()
