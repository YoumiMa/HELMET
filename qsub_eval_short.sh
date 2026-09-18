MODEL_NAME_PATH=$1

cd ~/fs/HELMET/

for TASK in recall rag rerank cite longqa summ icl; do
#for TASK in cite; do
  qsub -g tga-okazaki  -N eval_${TASK} run_eval_short.sh ${TASK} ${MODEL_NAME_PATH}
done
