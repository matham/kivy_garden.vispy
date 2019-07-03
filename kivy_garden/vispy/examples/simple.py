"""
"""
import os
#os.environ['KIVY_GL_DEBUG'] = '1'
from kivy.app import App
from kivy_garden.vispy import VispyWidget
import vispy.plot as vp


class MyApp(App):

    def build(self):
        return VispyWidget()

    def on_start(self):
        widget = self.root
        fig = vp.Fig(app='kivy_glir')
        widget.link_vispy_canvas(fig)

        plotwidget = fig[0, 0]
        # fig.title = "bollu"
        plotwidget.plot([(x, x**2) for x in range(0, 100)], title="y = x^2")
        plotwidget.colorbar(position="top", cmap="autumn")
        fig.show()
        widget.vispy_canvas_backend.kivy_draw_trigger()


if __name__ == '__main__':
    MyApp().run()
