1. 
conda activate hairfusion

변환하고 싶은 이미지. \data\taek_preprocessed\images

CUDA_VISIBLE_DEVICES=0 python preprocess.py   --img_path ./data/taek_preprocessed/images/vivid_hair6.png   --save_dir_name taek_preprocessed 

실행

2. DenPose Extraction

docker start hairfusion-117
docker exec -it hairfusion-cu117 bash

cd HairFusion2/detectron2/projects/DensePose

for img in ../../../data/taek_preprocessed/images/*.{jpg,jpeg,png}; do [ -e "$img" ] || continue; base=$(basename "${img%.*}"); outdir=../../../data/taek_preprocessed/images-densepose; mkdir -p "$outdir"; out="$outdir/$base.jpg"; tmp="${out%.jpg}.0001.jpg"; CUDA_VISIBLE_DEVICES=0 python apply_net.py show configs/densepose_rcnn_R_50_FPN_s1x.yaml https://dl.fbaipublicfiles.com/densepose/densepose_rcnn_R_50_FPN_s1x/165712039/model_final_162be9.pkl "$img" dp_contour --output "$out" -v; [ -f "$tmp" ] && mv "$tmp" "$out"; done



3. Make Agnostic Images
run:
export dir_name=taek_preprocessed
CUDA_VISIBLE_DEVICES=0 python make_agnostic.py --dir_name ${dir_name}

4. Make Test Pairs
cd data/{dir_name}/test_pairs.txt
nano test_pairs.txt -> 이걸로 ref/source img 지정 + config.yaml 가면 저장된 이미지 이름도 지정할 수 있음(default 0000)

5. Inference 
bash ./scripts/test.sh
