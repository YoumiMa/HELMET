MODEL_NAME_PATH=$1

cd ~/fs/HELMET/

for TASK in recall rag rerank cite longqa summ icl; do
#for TASK in cite; do
  qsub -g tga-okazaki -N eval_${TASK} -p -3 run_eval_short_vllm.sh ${TASK} ${MODEL_NAME_PATH}
done
