"""
Demo flower using cython
=========================

Defines the Kivy garden :class:`CythonFlowerLabel` class which is
the widget provided by the demo cython flower.
"""

from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.widget import Widget
from ._version import __version__

__all__ = ('VispyWidget', )


class VispyWidget(RelativeLayout):

    vispy_canvas = None

    vispy_canvas_backend = None

    _clock_trigger_next_frame = None

    _clock_trigger_draw = None

    def link_vispy_canvas(self, canvas):
        if self.vispy_canvas is not None or \
                self.vispy_canvas_backend is not None:
            raise TypeError('Widget has already been linked to a vispy canvas')
        self.vispy_canvas = canvas
        self.vispy_canvas_backend = canvas._backend
        self.vispy_canvas_backend.link_kivy_widget(self)
        self.vispy_canvas_backend.reinit_from_widget()

        def reinit_canvas(*largs):
            if self.parent is None:
                pass
            else:
                self.vispy_canvas_backend.reinit_from_widget()
        self.fbind('parent', reinit_canvas)

        def resize(*largs):
            self.vispy_canvas.events.resize(size=self.size)
        self.fbind('size', resize)

