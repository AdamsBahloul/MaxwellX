import numpy as np
from vispy import scene
from vispy.scene import visuals


class FieldCanvas(scene.SceneCanvas):
    def __init__(self):
        super().__init__(keys="interactive", bgcolor="#121212", size=(800, 600))
        self.unfreeze()

        self.view = self.central_widget.add_view()
        self.view.camera = scene.cameras.PanZoomCamera(aspect=1)
        self.view.camera.set_range(x=(-5, 5), y=(-5, 5))

        self._draw_grid()
        self._draw_dummy_field()

        self.freeze()

    def _draw_grid(self):
        grid = visuals.GridLines(color=(0.3, 0.3, 0.3, 1))
        self.view.add(grid)

    def _draw_dummy_field(self):
        # Dummy vector field (placeholder for real physics)
        x, y = np.meshgrid(np.linspace(-4, 4, 16), np.linspace(-4, 4, 16))
        u = -y
        v = x

        arrows = visuals.Arrow(
            pos=np.c_[x.flatten(), y.flatten()],
            arrows=np.c_[u.flatten(), v.flatten()],
            color="cyan",
            arrow_size=6
        )

        self.view.add(arrows)
