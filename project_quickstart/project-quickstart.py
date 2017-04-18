
_ROOT = os.path.abspath(os.path.dirname(__file__))

sys.path.append(_ROOT)

import project_quickstart

print(dir(project_quickstart))

print(project_quickstart.__loader__)
project_quickstart.__loader__

print(project_quickstart.load_entry_point)
project_quickstart.load_entry_point

print('Hello, this works')

project_quickstart.doSuperTest()

project_quickstart.main()

