# Hair-Fusion 동작

### 환경 어떻게 맞추었는지..
뭔가 이슈가 많았다. 그 중 가장 큰 이슈는 CUDA 드라이버와 PyTorch 빌드 버전의 불일치였다
"The detected CUDA version (12.6) mismatches PyTorch (11.7)” 경고/오류가 끊임없이 나왔다.
그러니까 호스트 드라이버는 12.6인데 설치한 Torch는 cu117로 빌드됨

### 입력 이미지(source/ref)
<p align="center">
  <img src="images/source.png" width="300"/>
  <img src="images/ref1.png" width="300"/>
</p>

### Hair-Agnostic
<p align="center">
  <img src="images/source_agnostic_mask.png" width="300"/>
  <img src="images/source.png" width="300"/>
  <img src="images/source_agnostic.png" width="300"/>
</p>

### Result
<img src="images/result1.png" />
<img src="images/result1_full.png" />

### 입력 이미지(source/ref)
<p align="center">
  <img src="images/ref1.png" width="300"/>ㅎ
  <img src="images/source.png" width="300"/>
</p>


### Hair-Agnostic
<p align="center">
  <img src="images/source2_agnostic_mask.png" width="300"/>
  <img src="images/ref1.png" width="300"/>
  <img src="images/source2_agnostic.png" width="300"/>
</p>

### Preprocess
<p align="center">
  <img src="images/ref1.png" width="300" />
</p>

<p align="center">
  <img src="images/source2_agnoistic_crop.png" width="300"/>
  <img src="images/source2_agnoistic_mask_crop.png" width="300"/>
  <img src="images/source2_face_agnostic.png" width="300"/>
</p>

### Pose Encoder
<p align="center">
  <img src="images/source2_encoder.jpg" width="300"/>
  <img src="images/ref2_encoder.jpg" width="300"/>
</p>

### Result
<img src="images/result2.png" />
<img src="images/result2_full.png" />








