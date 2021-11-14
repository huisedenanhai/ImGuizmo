import os


for fname in os.listdir('.'):
    if fname.endswith(('.h', '.cpp')):
        with open(fname) as f:
            lines = f.readlines()
        t = {
            '#include "imgui.h"': '#include <imgui/imgui.h>\n',
            '#include "imgui_internal.h"': '#include <imgui/imgui_internal.h>\n',
        }
        lines = [t[l.strip()] if l.strip() in t else l for l in lines]
        with open(fname, 'w') as f:
            f.writelines(lines)
