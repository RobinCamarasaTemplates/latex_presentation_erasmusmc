"""
**Author** : Robin Camarasa

**Institution** : Erasmus Medical Center

**Position** : PhD student

**Contact** : r.camarasa@erasmusmc.nl

**Date** : 2020-08-06

**Project** : Slide latex template ErasmusMC

**Test project generation of Erasmus MC Slides**

"""
import sys
from datetime import datetime
import pytest
import shutil
from pathlib import Path
from cookiecutter import main


ROOT = Path(__file__).parents[1]
TESTS_ROOT = ROOT / 'test_output'
EXTRA_CONTEXT = {
    "repo_name": "Latex",
    "author_names": 'John Doe',
    "author_institutions": 'Inst1, Inst2',

    "author_mail": "john.doe@gmail.com",
    "author_github": "https://johndoe.github.io",
    "author_scholar": "https://google.scholar.com",
    "author_website": "https://127.0.0.1:8080"
}


def test_generate_project() -> None:
    """
    Test project generation

    :return: None
    """
    # Clean
    if TESTS_ROOT.exists():
        shutil.rmtree(TESTS_ROOT)
    TESTS_ROOT.mkdir()

    # Get path
    output_dir = TESTS_ROOT.resolve()

    # Launch project generation
    main.cookiecutter(
        str(ROOT),
        no_input=True,
        extra_context=EXTRA_CONTEXT,
        output_dir=output_dir
    )

    # Test project generation
    project_name = '{} - Latex'.format(
        datetime.now().strftime('%Y-%m-%d')
    )
    assert (TESTS_ROOT / project_name).exists()

    # Test file generation
    files = [
        'commands.sty',
        'presentation.tex',
        'theme.sty'
    ]
    for file_ in files:
        assert (TESTS_ROOT / project_name / file_).exists()
    assert (
        TESTS_ROOT / project_name / 'images' / 'logo.png'
    ).exists()



