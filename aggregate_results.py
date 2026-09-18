import argparse
import os
import json

display_names = "alce_asqa:str_em,alce_asqa:citation_rec,alce_asqa:citation_prec,narrativeqa:rougeL_f1,narrativeqa:gpt-4-score,multi_lexsum:rougeL_f1,multi_lexsum:gpt-4-f1,banking77:exact_match,nlu:exact_match,hotpotqa:substring_exact_match,infbench_qa:rougeL_f1,infbench_sum:gpt-4-f1,triviaqa:substring_exact_match,ruler_niah_mv:ruler_recall,trec_fine:exact_match,infbench_choice:exact_match,msmarco_rerank_psg:NDCG@10,ruler_niah_mk_2:ruler_recall,trec_coarse:exact_match,infbench_sum:rougeL_f1,clinic150:exact_match,kilt_popqa:substring_exact_match,alce_qampari:qampari_rec_top5,alce_qampari:citation_rec,alce_qampari:citation_prec,kilt_nq:substring_exact_match,ruler_niah_mk_3:ruler_recall,json_kv:substring_exact_match"
lengths = [8192, 16384, 32768, 65536, 131072]

def aggregate_result(model_name_or_path: str, output_path: str):

    model_provider = os.path.split(model_name_or_path)[0]
    model_name = os.path.split(model_name_or_path)[-1]
    target_path = os.path.join(output_path, model_name)

    task_benchmark = display_names.split(",")
    scores = []
    names = []
    for length in lengths[::-1]:
        curr_len = f"in{length}"
        for i, task in enumerate(task_benchmark):
            task, metrics = task.split(":")
            files = [f for f in os.listdir(target_path) if task in f and curr_len in f]
            # print(files)
            score = -1
            if "gpt-4" in metrics:
                for f in files:
                    if f.endswith("gpt4eval_o.json"):
                        # print(task, metrics)
                        score_file = f
                        score_content = json.load(open(os.path.join(target_path, f)))
                        score = score_content["averaged_metrics"][metrics]
            else:
                for f in files:
                    if f.endswith(".score"):
                        score_file = f
                        score_content = json.load(open(os.path.join(target_path, f)))
                        score = score_content[metrics]
        
            scores.append(score)
            names.append(f"{curr_len}:{task}:{metrics}")
    print(",".join([f"{s}" for s in scores]))
    # print(",".join(names))
    return


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="aggregate evaluation results")
    parser.add_argument("--model_name_or_path", type=str, default="meta-llama/Llama-3.1-8B-Instruct")
    parser.add_argument("--output_path", type=str, default="./output")
    args = parser.parse_args()
    
    aggregate_result(args.model_name_or_path, args.output_path)
