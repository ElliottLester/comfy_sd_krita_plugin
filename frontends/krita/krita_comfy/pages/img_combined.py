from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QVBoxLayout, QToolBox, QWidget

from ..widgets import (
    QComboBoxLayout,
    QCheckBox,
)

from ..script import script
from .img_base import SDImgPageBase
from ..utils import get_workflow


class CombinedPage(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.page = SDImgPageBase("Combined")
        self.page.layout.addLayout(self.page.denoising_strength_layout)

        self.btn = QPushButton("Start workflow")
        self.get_workflow_btn = QPushButton("Get workflow")

        self.invert_mask = QCheckBox(script.cfg, "inpaint_invert_mask", "Invert mask")
        self.auto_generate_mask = QCheckBox(script.cfg, "inpaint_auto_generate_mask", "Auto generate transparency mask")
        self.fill_layout = QComboBoxLayout(
            script.cfg, "inpaint_fill_list", "inpaint_fill", label="Inpaint fill:"
        )

        self.inpaint_opts = QWidget()
        inpaint_layout = QVBoxLayout()
        inpaint_layout.addWidget(self.invert_mask)
        inpaint_layout.addWidget(self.auto_generate_mask)
        inpaint_layout.addLayout(self.fill_layout)
        self.inpaint_opts.setLayout(inpaint_layout)

        self.toolbox = QToolBox()
        self.toolbox.addItem(QWidget(), "Txt2Img Options")
        self.toolbox.addItem(QWidget(), "Img2Img Options")
        self.toolbox.addItem(self.inpaint_opts, "Inpaint Options")

        self.layout = layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.page)
        self.layout.addWidget(self.toolbox)
        self.layout.addWidget(self.btn)
        self.layout.addWidget(self.get_workflow_btn)
        self.layout.addStretch()

        self.setLayout(layout)


    def cfg_init(self):
        super().cfg_init()
        self.tips.setVisible(not script.cfg("minimize_ui", bool))

    def cfg_connect(self):
        super().cfg_connect()
