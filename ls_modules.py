import os
import stat
from color_settings import *
from rich.text import Text

def get_permissions(filepath):
    #=========================
    # Get the mode of the file
    #=========================

    file_stat = os.stat(filepath)
    permissions = stat.filemode(file_stat.st_mode)
    colorPerm = Text()
    
    mode_colors = {
            'r': 'green',
            'w': 'red',
            'x': 'blue',
            '-': 'grey'
            }

    for mode in permissions:
        colorPerm.append(mode, style=mode_colors.get(mode, 'white'))
    return colorPerm

def file_icon(filename):
    
    icon_map = {
            '.txt': '📄',
            '.py': '🐍',
            }

    file_extension = os.path.splitext(filename)[1]
    return icon_map.get(file_extension, '📁')
