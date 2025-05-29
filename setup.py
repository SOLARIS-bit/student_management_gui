from setuptools import setup, find_packages

setup(
    name="student_management_gui",
    version="1.0.0",
    author="SOLARIS-bit",
    description="A colorful, scrollable Tkinter-based GUI to manage students, subjects, and grades.",
    packages=find_packages(),
    install_requires=[
        # tkinter is usually built-in; no need to specify unless using a special environment
    ],
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "student-management=main:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
