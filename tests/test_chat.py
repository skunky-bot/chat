from html.parser import HTMLParser
from pathlib import Path


class Parser(HTMLParser):
    pass


def test_preview_accessibility_and_no_remote_tokens():
    html = (Path(__file__).resolve().parents[1] / "index.html").read_text(encoding="utf-8")
    Parser().feed(html)
    assert 'aria-live="polite"' in html
    assert 'id="form"' in html
    assert "No generative AI is connected" in html
    assert "localStorage" not in html
    assert "fetch(" not in html
