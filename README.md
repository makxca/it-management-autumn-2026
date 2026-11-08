# Транскрипты и конспекты лекций по ИТ-менеджменту

- **Семестр**: осень 2026
- **Лектор**: Владислав Горбунов
- [Полные записи лекций](https://drive.google.com/drive/folders/1BevGJhmHxy7Y0jzOWBUVkk8HZ7oA6uBr?usp=sharing)

## Транскрибация

В каталоге проекта (macOS/Linux):

```bash
python3 -m venv .venv           # один раз
source .venv/bin/activate      # в каждом новом терминале
python -m pip install faster-whisper  # один раз
python transcribe.py "путь/к/записи.mp3"
deactivate                    # выйти из venv после работы
```

При первом запуске скачивается модель `large-v3` — нужен интернет. Скрипт распознаёт русскую речь на CPU и сохраняет текст с таймкодами в минутах в `transcript.txt` текущего каталога, перезаписывая предыдущий результат.
