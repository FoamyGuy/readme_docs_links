import os
import time

DOCS_MESSAGE = """Documentation
=============

API documentation for this library can be found on `Read the Docs <{}>`_.

Contributing"""

def find_readthedocs_link(lines):
    for i in range(10):
        cur_line = readme_lines[i]
        if "https://circuitpython.readthedocs.io" in cur_line:
            return cur_line.split(":target: ")[1]



# checkout main branch
os.system("git checkout main")

f = open("README.rst", 'r')
readme_str = f.read()
f.close()

readme_lines = readme_str.split("\n")

link = find_readthedocs_link(readme_lines)
print(link)

readme_str = readme_str.replace("Contributing", DOCS_MESSAGE.format(link))

#os.system("git pull origin main")


# modify file
f = open("README.rst", 'w')
f.write(readme_str)
f.close()


# add readme change
os.system("git add README.rst")

# make new commit
os.system('git commit -m "add docs link to readme"')


# push origin main
os.system("git push origin main")

time.sleep(3)
