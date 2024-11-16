# AI Paperboy

## 📋 Project Abstract

### Purpose

* 사용자가 질문으로 요청하면 답변이 있는 뉴스 기사를 스크랩 해주는 서비스

### Functions
* 기사를 읽고 다시 보고 싶은 기사 스크랩 기능
* 실시간 질문에 대한 답변 기사 AI 스크랩 기능
* 일정 시간마다 기사 목록 업데이트 후 질문에 대한 답변 기사 AI 스크랩 기능



### Collaboration tool
<img src="https://img.shields.io/badge/Google Drive-4285F4?style=flat-square&logo=Google Drive&logoColor=white"/> <img src="https://img.shields.io/badge/MS ToDo-6264A7?style=flat-square&logo=Microsoft&logoColor=white"/> <img src="https://img.shields.io/badge/Notion-5E5E5E?style=flat-square&logo=Notion&logoColor=white"/> 

## 💾 Installation
### 1. Set up the python environment:
- Recommended python version 3.8.5

```
$ conda create -n venv python=3.8.5 pip
$ conda activate venv
```
### 2. Install other required packages

```
$ cd $ROOT/final-project-level3-nlp-19/code
$ poetry install
$ poetry shell
```

## 🖥 Usage
### 1. Project Structure
```
code
├──routers/
├──schema/
├──services/
├──templates/
├──AIPaperboy.py
└──model train file (.py)
```
**4 folder for serving**
- **routers**: Controller
- **schema**: Model
- **sevices**: Project's functions
- **templates**: HTML & CSS file

### 2. Train
```
$ cd $ROOT/final-project-level3-nlp-19/code
$ python train_copy.py --output_dir ./outputs  --run_extraction True --run_generation False --do_train --do_eval \
--evaluation_strategy 'steps' --eval_steps 60 --logging_steps 60 --per_device_eval_batch_size 16 \
 --per_device_train_batch_size 16 --save_strategy "no" --fp16 True --fp16_full_eval True --num_train_epochs 9 --report_to "wandb" \
 --overwrite_output_dir
```

### 3. Inference
```
$ python inference_copy.py --output_dir ./outputs/test_dataset/ --dataset_name ../data/test_dataset/ --model_name_or_path ./models/train_dataset/ --do_predict  --overwrite_cache --overwrite_output_dir
```

### 4. Execute
```
$ cd $ROOT/final-project-level3-nlp-19/code
$ python AIPaperboy.py --output_dir ./outputs/test_dataset/ --model_name_or_path ./models/train_dataset/ --dataset_name ../data/test_dataset/ --do_predict
```

## 📽 Demo
* [AI Paperboy Demo Video](https://www.youtube.com/watch?v=n7oPu7vrQ8s)
* [AI Paperboy Presentation](https://docs.google.com/presentation/d/1rpgp9knamiiqs4lITZMEiixSA8sfWyvv/edit?usp=sharing&ouid=110643334622897859461&rtpof=true&sd=true)
