import sys
import main
import io


def test_main(capsys):
    # Test on a short snippet first
    sys.stdin = io.StringIO("abcdef")
    sys.argv = ["main.py", "f"]

    main.index
