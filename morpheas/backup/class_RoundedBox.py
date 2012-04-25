from . class_Morph import Morph
from . basics_morpheas import Point

class RoundedBox(Morph):

#    def __init__(self, edge=4, border=2, bordercolor=pygame.Color(0,0,0)):
    def __init__(self, edge=4, border=20, color = (1,1,1,1),  bordercolor=(0,0,0,1)):
        super(RoundedBox, self).__init__()
        self.bounds = Point(0,0).corner( Point(100,100))
        self.edge = edge
        self.border = border
        self.color = color
        self.bordercolor = bordercolor        
        print("****RoundedBox created with color and backgroundcelor",self.color, self.bordercolor)
        
    def draw_new(self, event):
        self.fill_rounded(self.edge, self.bordercolor, 0)
        self.fill_rounded(max(self.edge - (self.border // 2),0),
                          self.bordercolor, self.border)
#PKHG.means no inset black color if not changed at creation-time

    def fill_rounded(self, edge, color, inset):        
        "private"
        if inset == 0:
            Morph.draw_rounded_morph(self, 0.5, color, rectangle = False)
        else:
            rect = self.bounds.inset_by(inset)
            Morph.draw_rounded_morph(rect,  0.1,  color, rectangle = True )

    #RoundedBox menu:
    def developers_menu(self):
        menu = super(RoundedBox, self).developers_menu()
        menu.add_line()
        menu.add_item("border color...", 'choose_border_color')
        menu.add_item("border size...", 'choose_border')
        menu.add_item("corner size...", 'choose_edge')
        return menu

    def choose_border(self):
        result = self.prompt("border:",
                            str(self.border),
                            50)
        if result != None:
            self.changed()
            self.border = min(max(int(result),0),self.width()//3)
            self.draw_new()
            self.changed()

    def choose_edge(self):
        result = self.prompt("corner:",
                            str(self.edge),
                            50)
        if result != None:
            self.changed()
            self.edge = min(max(int(result),0),self.width()//3)
            self.draw_new()
            self.changed()

    def choose_border_color(self):
        result = self.pick_color(self.__class__.__name__ + "\nborder color:",
                            self.bordercolor)
        if result != None:
            self.bordercolor = result
            self.draw_new()
            self.changed()
