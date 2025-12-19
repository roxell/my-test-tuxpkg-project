import my_test_tuxpkg_project


def test_version():
    assert my_test_tuxpkg_project.__version__ == "0.0.0"


def test_main(capsys, monkeypatch):
    monkeypatch.setattr("sys.argv", ["my-test-tuxpkg-project"])
    my_test_tuxpkg_project.main()
    captured = capsys.readouterr()
    assert "0.0.0" in captured.out
