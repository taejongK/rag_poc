# rag_poc

## 실행
### API 실행
```
cd src/app
python3 main.py
```

### Client 실행
```
cd src/app
streamlit run client.py  
```


## 구성
### 데이터 
- BA_사용메뉴얼_분석가.pdf(회사)
- 데이터는 기밀사항이라 숨김 처리

### PDF2Markdown
- pdf_reading_test.ipynb에서 pdf를 읽어와서 markdown으로 변환하는 코드를 작성하였습니다.
- 몇 가지 모델을 실행해 봤을 때, pdf를 markdown으로 변환했을 때, 이미지를 활용하기가 가장 좋았습니다.
- 물론 멀티모달 모델을 사용한다면 더 좋은 결과를 얻을 수 있을 것입니다. 하지만 비용과 시간이 많이 들 것으로 예상됩니다.

### Embedding
- llm_test.ipynb에서 huggingface의 모델을 사용하여 pdf를 embedding하는 코드를 작성하였습니다.
- 무료 모델임에도 불구하고 embedding 결과가 꽤 괜찮았습니다.

### Answer model
- 마찬가지로 llm_test.ipynb에서 google의 무료 모델(gemini-pro)를 사용하여 답변을 출력했습니다. 
- 답변의 경우는 결과가 좋지는 않았습니다. 
- 검색된 정보에는 충분한 정보가 있었지만 일치하는 결과가 없다고 하거나 하는 문제가 발견되었습니다.

### Image
- 이미지를 따로 저장하고 markdown으로 변환된 텍스트에서 이미지 경로를 metadata로 추가하는 코드를 작성하였습니다.
- 관련 내용일 검색되어 answer model에 들어가면 이미지를 같이 보여주는 형태로 구현했습니다. 

### SQLite
- 대화내용을 sqlite에 저장하는 코드를 작성하였습니다.
- 아직 구조를 본격적으로 셜계한 것은 아니고 그냥 이렇게 가능하다는 느낌으로만 코드를 작성했습니다.
- 추후 프로토타입을 만들면서 본격적으로 구현할 계획입니다.