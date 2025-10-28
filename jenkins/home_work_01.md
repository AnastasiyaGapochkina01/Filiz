1) Написать пайплайн с параметром `HOST` (тип string), состоящий из трех этапов (stage):
- build: выводит строку `run build ${BUILD_NUMBER}`
- test: выводит строку `run tests on ${HOST} by ${BUILD_NUMBER} job`
- deploy: `run deploy on ${HOST}`
2) Написать пайплайн для сборки и тестирования модуля python из репозитория https://github.com/AnastasiyaGapochkina01/calculate-py-module;

**Параметры пайплайна**:
- RUN_TESTS 
  
**Переменные пайплайна:**
- BASE_DIR
- PRJ_NAME
- GIT_URL

**Этапы пайплайна:**
- `Clone repo` - реализацию взять из урока
- `Setup Environment` - инициализация рабочего окружения; для этого этапа использовать shell команды
```bash
cd ${env.BASE_DIR}/${env.PRJ_NAME}
python3 -m venv venv
. venv/bin/activate
pip install --upgrade pip
pip install -e .
pip install -r requirements.txt
```
- `Security Scan` - сканирование на уязвимости; для этого этапа использовать shell команды
```bash
cd ${env.BASE_DIR}/${env.PRJ_NAME}
. venv/bin/activate
bandit -r app/ -f json -o bandit_results.json || true
```
- `Run Unit Tests` - запуск тестов, если отмечен чекбокс RUN_TESTS; для этого этапа использовать shell команды
```bash
cd ${env.BASE_DIR}/${env.PRJ_NAME}
. venv/bin/activate
PYTHONPATH=src pytest -v tests/ --junitxml=test-results.xml
```
- `Package Application` - сборка модуля; для этого этапа использовать shell команды
```bash
cd ${env.BASE_DIR}/${env.PRJ_NAME}
. venv/bin/activate
python setup.py sdist bdist_wheel
ls -la dist/ || echo "Папка dist не существует"
```
