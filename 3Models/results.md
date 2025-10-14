## 입력 이미지(VividHairStyler dataset)
<p align="center">
  <img src="images/00090.jpg" width="300"/>
  <img src="images/vivid_hair6.jpg" width="300"/>
</p>
Stable-Hair 입력 이미지 size : 512*512(jpg 파일) - png 파일 시 오류
VividHairStyler 입력 이미지 size : 1024*1024(png 파일)- 다른 사이즈일 시 오류

### Stable-Hair 결과 이미지(Bald/Transfer)
<p align="center">
  <img src="images/bald_result_stable_hair.png" width="300"/>
  <img src="images/transfer_result_stable_hair.png" width="300"/>
</p>

- Bald 변환
    - 실행 시간 : 17:20
- Hair Transfer
    - 실행 시간 : 48:44



### Stable-Hair 결과 이미지(Bald/Transfer)
<p align="center">
  <img src="images/bald_result_stable_hair.png" width="300" />
  <img src="images/transfer_result_stable_hair.png" width="300"/>
</p>




### VividHairStyler 결과 이미지(Bald / Transfer)
<p align="center">
  <img src="images/vividHairStyler_bald.png" width="300"/>
  <img src="images/VividHairStyler_transfer.png" width="300"/>
</p>

실행 시간 5분 내외


### HairFusion 결과 이미지(Bald / Transfer)
<p align="center">
  <img src="images/00090_01.png" width="300"/>
  <img src="images/0000.png" width="300"/>
</p>

### STABLE_HAIR
<img src="images/CWHF4.jpg"/>

### HAIR_FUSION
<img src="images/CHHF4_fusion.png"/>

### STABLE_HAIR
<img src="images/CWHF5.jpg"/>

### HAIR_FUSION
<img src="images/CHWHF5_fusion.png"/>

### STABLE_HAIR
<img src="images/CWHF6.jpg"/>

###  HAIR_FUSION
<img src="images/CWHF6_fusion.png"/>


우선 Stable-Hair 모음ZIP
<img src="images/CWHF4.jpg"/>
<img src="images/CWHF5.jpg"/>
<img src="images/CWHF6.jpg"/>

### 문제 현상 요약(STABLE_HAIR)
1. 색상 전이(color transfer)는 매우 정확함(염색, 하이라이트, 톤 변화 모두 반영됨)
2. 그러나 머리길이와 모양은 거의 변하지 않고 원본 두상에 맞추어 짧은 머리로 제한 되는 경향이 있음

과연 원본 두상이 영향을 주는 것일까?
원본 이미지에 긴 머리의 여성을 입력해보자

<img src="images/CWHF2.jpg"/>
<img src="images/CWHF3.jpg"/>

살짝 애매. 더 돌려보자

<img src="images/CWHF7.jpg"/>

영향은 조금 있는 듯? 
(1) Bald Converter 기반의 기준화된 두상 문제.
논문에서는 1단계로 모든 입력 이미지를 완전히 대머리 상태로 변환해 표준화.
이는 identity consistency(얼굴 동일성)유지에는 유리하지만, 머리 길이 정보가 손실
모델 입장에서는 얼마나 긴 머리를 어디까지 생성할 지에 대한 기하학적 기준이 사라짐.
=> 주어진 얼굴 윤곽에 너무 강하게 맞추어 머리가 짧아질 수도?

얼굴 크기가 작은 걸 입력으로 넣는다면?

<img src="images/CWHF8.jpg"/>


??? 뒤에 나온 저것들은.... 멀까
H

(1) Latent ControlNet의 근본적 trade-off
논문에 따르면, Stable-Hair는 ControlNet의 pixel-space 대신 latent-space mapping을 사용하여 색상 일관성을 확보

color 안정성은 없었지만 geometry control capability 떨어짐. latent 공간은 high-frequency spatial cue를 충분히 보존하지 못함.

(2) 자동생성 데이터셋의 한계

STABLE_HAIR 학습 데이터는 다음과 같이 만들어짐.

STABLE_HAIR는 real-world dataset이 아니라 자동 생성 triplet dataset을 사용

We propose an automated data generation pipeline …
The pipeline uses ChatGPT to generate text prompts, the Stable Diffusion Inpainting model to generate reference images,
and our pre-trained Bald Converter to convert the original image or one of the frames sampled from videos into the bald proxy image.”

[1] 입력단계
 - 원본 이미지에서 머리 부분을 segment 하여 hair mask 생성
 - 얼굴 및 배경은 inpainting으로 덮어쓸 예정임

[2] 텍스트 조건 생성 단계
 - ChatGPT가 이미지의 "설명 문장"을 자동으로 만듬
 - 이 문장은 inpainting 모델이 새 identity와 배경을 만들 때 사용

[3] Inpainting 단계
 - Stable Diffusion Inpainting 모델은
       - ChatGPT 문장을 prompt로 받고.
       - 머리카락 영역은 보호,
       - 나머지 영역은 새로 그림
    - 결과적으로 머리만 유지된 상태에서 다른 사람 처럼 보이는 reference 이미지 생성

{x_original, x_bald, x_reference } triplet
==> HairExtractor 와 Latent Identity IdentityNet 학습의 감독 데이터

이렇게 생성된 synthetic triplet dataset을 사용
최종적으로 150,000장의 triplet(by Stable Diffusion Inpainting 방식)
원본 소스 -> FFHQ + CelebV-HQ

FFHQ 논문에 따르면, FFHQ-CelebV-HQ는 본질적으로 머리 길이/형태 다양성이 적은 얼굴 중심 데이터셋임.
머리 전체가 아니라 face-centored crop!!! -> shoulder-length 이하 중심

따라서 Stable-Hair에서 학습 분포는 short ~ medium hair 중심으로 제한될 수 밖에 없음

Inpainting 기반 
Inpainting 기반은 기존 mask 범위 안에서만 채우는 local 연산 머리의 길이를 늘리는 형태이 판차는 적음

논문에 따르면 ...
Due to the limitation of training data, our method may inadvertently transfer certain hair accessories to the source image (as shown in Fig. 8),
which may not be desirable in some scenarios.”

=> 데이터 편향으로 인한 전이 한계를 의미. 길이 역시 제한을 받지 않을까???

그래서 이런 결과가 나온거면 ㅇㅈ

<img src="images/CWHF8.jpg"  />
<img src="images/CWHF8_fusion.png" />
<img src="images/CWHF9_fusion.png" />



(2) Latent Control Net 구조의 한계
이 구조는 색상 일관성을 유지하기 위하여 latent 공간에서만 수항
덕분에, 색상 전이는 그 어떤 모델보다 우수함
하지만, latent space는 고주파 geometry 정보를 약화시킬 수 있음
따라서 ControlNet이 형상 정보를 충분히 반영하지 못하고, 조금 이상한 머리 모양이 비슷한 결과가 나옴

(3) Hair Extractor의 표현
Hair extractor는 referene 이미지를 U-Net self-attention에 cross-attention으로 삽입해 머리 속성을 주입한다. 덕분에 색상.덱스터에는 강함

### HAIR_FUSION 모음ZIP

<img src="images/CHHF4_fusion.png"/>
<img src="images/CHWHF5_fusion.png"/>
<img src="images/CWHF6_fusion.png" />

문제 사항 요약
1. 머리 끊김 현상

논문 중...
HairFusion highly depends on the performance of external parsing models;
a single strand of bangs may not be captured due to mask failure (Fig.10).

마스크 경계가 조금이라도 어긋나면 -> feature map 경계가 물리적으로 단절

2. 색상 전이는 Stable-Hair가 훨씬 나음. 중간중간 색이 다른 것도 있고. 색이 조금 연해지는 현상 발생. 이것이 latent 공간 + Hair Extractor의 역할..(시간 좀 오래걸리긴 하심)

3. hair mask가 DensePose + Parsing으로 나타남. 

<p align="center">
  <img src="images/densepose.jpg" width="300" />
  <img src="images/a_01_densepose.jpg" width="300" />
  <img src="images/b_01_densepose.jpg" width="300" />
</p>



이게 무슨 영향이 있을까... 더 찾아보기