MODEL_NAME_PATH=$1

cd ~/fs_act-x/HELMET/

for TASK in recall rag rerank cite longqa summ icl; do
#for TASK in longqa summ; do
  qsub -g tga-okazaki  -N eval_${TASK} -ar 8736 run_eval_short_thinking.sh ${TASK} ${MODEL_NAME_PATH}
done
