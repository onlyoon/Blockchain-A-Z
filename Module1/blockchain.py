# -*- coding: utf-8 -*-
# Module 1 - Create a Blockchain

# Importing the Libraries

import datetime # 블록이 생성되고 채굴된 타임스탬프
import hashlib # 블록 해시할때 사용
import json # 블록 해시 이전 블록 인코딩을 위해 dumps함수 사용
# 웹 어플리케이션이 되는 Flask 객체 생성하기 위해
# Jsonify는 POSTMAN에서 블록체인과 상호작용시 메세지를 보내기 위해 사용하는 함수
from flask import Flask, jsonify 


# Part 1 - Building a Blockchain
# 블록체인 아키텍처 설계

# 클래스로 설계하는 이유는 클래스는 
# property, function, tools, method 이 모든 것이 상호작용하는 것이
# 가능하기 때문이다.
class Blockchain:
    
    # 클래스로 작성시 init 메서드로 시작 (생성자?)
    def __init__(self):
        # 다른 블록을 포함하는 리스트
        self.chain = []
        # proof인자 블록체인은 자체 증명을 가지고 임의의 값을 선택 가능
        # 첫번째 블록이니, prev_hash 값은 0
        self.create_block(proof = 1, previous_hash = '0')
        
    # create_block함수와 mine_block의 차이점은
    # create_block은 블록 채굴 직후에 함수 적용
    # mine_block은 해결해야할 POW를 얻게 된다.
    # 이 POW를 해결하고 찾아내야 블록체인에 새 블록이 추가가 된다.
    
    # create_block의 인수는 3가지
    # self: 객체의 변수를 사용하기 때문
    # proof: 블록 채굴 직후에 사용하는 create_block 함수는
    # 증명을 인수로 가져야 한다.
    # prev_hash: 이전 블록과 연결해야 하기 때문에
    def create_block(self, proof, previous_hash):
        # block은 딕셔너리이다. 각 블록을 4개의 필수 키로 정의
        block = {
            # block 번호
            'index': len(self.chain) + 1,
            # 블록 채굴된 시간 json이어서 str 타입 변환
            'timestamp': str(datetime.datetime.now()),
            # 작업 증명을 해결해서 채굴시 얻는 증명
            'proof': proof,
            # 이전 해시
            'previous_hash': previous_hash
            # 추가적으로 다른 블록들을 넣을 수 있음
            'data': 
            } 
        # 리스트에 append 함수를 이용해 방금 생성한 블록 추가
        self.chain.append(block)
        # 블록체인 반환
        return block
    
    # 마지막 블록 불러오기, 인덱스 [-1] 
    def get_previous_block(self):
        return self.chain[-1]
    
    # 채굴은 어려워야 하지만 검증은 쉬워야 한다.
    # 작업 증명 함수
    # 문제를 정의할 뿐만 아니라 해결까지 한다.
    # prev_proof: 이전 증명은 새로운 증명을 찾기위해 고려되는 한 요소
    def proof_of_work(self, previous_proof):
        new_proof = 1
        # check_proof로 알맞은 proof를 찾을 때까지 while반복, 
        # 맞으면 True값
        check_proof = False
        while check_proof is False:
            # 비대칭적으로 작성을 해야함 그렇지 않을경우 동일한 증명이 나온다.
            # encode 함수를 통해 콘솔을 확인하고 문자열 이전에 'b'를 추가 시킨다.
            # hexdigest 함수를 통해 16진수의 64자로 변환된다.
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof*2).encode()).hexdigest()
            # 조건 입력 선행제로 4개
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof
    
  
    # 해당 블록의 암호화 해시를 도출하는 해시 함수
    # 인수
    # self: 현재 구축하려는 블록체인 클래스의 메서드, 마이닝에 사용될 메서드가 되기 
    # block: 모든 블록들을 가져온다.
    def hash(self,  block):
        # 블록과 블록 딕셔너리를 키별로 정리, dumps함수로 문자열로 바꾸며, 인코딩되게 만들어준다.
        encoded_block = json.dumps(block, sort_keys = True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
    
    # 각 블록의 해시가 이전 블록의 해시와 같은지의 함수
    # 작업 증명 문제에 따라 각 블록의 증명이 유효한지 확인하는 함수
    def is_chain_vaild(self, chain):
        # while문을 돌리기 전에 초기화를 해서 제네시스 블록 인덱스를 0으로 설정
        previous_block = chain[0]
        block_index  = 1
        
        while block_index < len(chain):
            block = chain[block_index]
            # 현재 블록의 해시가 이전 블록의 해시와 같지 않다면
            if block['previous_hash'] != self.hash(previous_block):
                return False
            # 이전 블록의 증명 불러오기
            previous_proof = previous_block['proof']
            # 현재 블록의 증명 불러오기
            proof = block['proof']
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof*2).encode()).hexdigest()
            # 이 해시 연산이 4 선행 제로를 가지는 것이 맞는지
            if hash_operation[:4] != '0000':
                return False
            previous_block = block
            block_index += 1        
        return True
    
# Part 2 - Make two Function 
# 1. Express Blockchain Statement
# 2. Mining Function
# Postman에서 get요청을 만들어 블록체인과 상호작용할 Flask 기반 웹앱 생성
# Creating A Web App (Flask)








