# mock-aiservice

## Installation

```bash
git clone https://github.com/chuangk-p/mock-aiservice.git
pip install -e .
```

How To Use

```bash
from mockaiservice import setting
from mockaiservice.nlp import tokenizer, sentiment, similarity
from mockaiservice.nlp.translation import translate

setting.set_api_key('YOUR_API_KEY')
tokenizer.tokenize('สวัสดี AI')
tokenizer.tokenize('สวัสดี AI', return_json=True)
sentiment.analyze('อาหารร้านนี้อร่อยมาก')
sentiment.analyze('บุกจับปรับอะไรครับเนี่ย', engine='emonews')
translate('สวัสดี', 'th', 'zh')
```