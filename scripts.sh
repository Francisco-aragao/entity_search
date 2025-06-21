## 2.1  Converter o JSONL para o formato Anserini (um por linha)
mkdir -p corp_anserini
python ./tools/jsonl_to_anserini.py \
       --input ./data/ir-20251-rc/corpus.jsonl \
       --output ./corp_anserini/corpus.jsonl


## criação do indice no formato correto
# necessário usar o java para dar certo
export _JAVA_OPTIONS="-Xms4g -Xmx24g"

# as threads podem ser ajustadas
python -m pyserini.index.lucene \
  -collection JsonCollection \
  -generator DefaultLuceneDocumentGenerator \
  -input ./corp_anserini \
  -index index_entities \
  -threads 16 \ 
  -storePositions -storeDocvectors -storeRaw