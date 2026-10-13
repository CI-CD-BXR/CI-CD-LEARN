import pytest


def test_basic():
    """最基本的测试，确保环境能跑"""
    assert 1 + 1 == 3


def test_string():
    """测个字符串操作"""
    text = "CI/CD"
    assert "CI" in text
    assert len(text) == 5
