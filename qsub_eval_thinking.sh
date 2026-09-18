MODEL_NAME_PATH=$1

cd ~/fs_act-x/HELMET/

for TASK in recall rag rerank cite longqa summ icl; do
#for TASK in recall; do
	qsub -g tga-okazaki -ar 8513 -N eval_${TASK} run_eval_thinking.sh ${TASK} ${MODEL_NAME_PATH}
done
