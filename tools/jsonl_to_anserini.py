#!/usr/bin/env python
"""
Converte corpus.jsonl para formato Anserini:
{id: ..., contents: "<title> <keywords...> <text>"}
"""
import json, argparse, tqdm, pathlib

ap = argparse.ArgumentParser()
ap.add_argument("--input",  required=True)
ap.add_argument("--output", required=True)
args = ap.parse_args()

path_in  = pathlib.Path(args.input)
path_out = pathlib.Path(args.output)

with path_in.open(encoding="utf-8") as fin, \
     path_out.open("w", encoding="utf-8") as fout:
    for line in tqdm.tqdm(fin, desc="convert"):
        obj = json.loads(line)
        contents = " ".join([
            obj.get("title",""),
            " ".join(obj.get("keywords", [])),
            obj.get("text","")
        ])
        fout.write(json.dumps({"id": obj["id"], "contents": contents}) + "\n")
