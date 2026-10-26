from parag.config import get_settings


def test_settings_have_default_models() -> None:
    settings = get_settings()

    assert settings.chat_model
    assert settings.embedding_model
