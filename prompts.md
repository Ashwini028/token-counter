“Loved the camera quality, photos look amazing.”
“Battery died in two hours, very disappointed.”
“It works as described.”
“Delivery was late but the product is excellent.”
“Packaging was good, but the screen has a scratch.”


No.	Technique	Prompt (short)	Output (short)	Better or worse	Why
1 Zero-shot	Classify sentiment as Positive, Negative or Neutral: “Loved the camera quality...”	Positive + one line explanation	Correct, but extra text	I did not ask for only the label, so the model added an explanation
2 Zero-shot with format | Classify sentiment. Reply with only one word: Positive, Negative or Neutral. “Battery died in two hours...” | Negative | Better | Clear format instruction gave only the label, no extra text | 
3 Few-shot (3 examples) | Classify sentiment. 3 labelled examples, then “Delivery was late but the product is excellent.” | Mixed (Neutral) | Okay, not perfect | Followed the pattern and said Neutral, but added “Mixed”, which is not one of the allowed labels |
4 | Few-shot (4 examples) + only one word | Same as 3, plus “Reply with only one of these three words” and a mixed example (Neutral). Review: “Packaging was good, but the screen has a scratch.” | Negative | Better format, label debatable | Only one word came back, but the mixed example said Neutral and the model still chose Negative |
5 | Role + clear format | “You are a review analyst for an online store.” + classify + reply with only one word. Review: “Delivery was late but the product is excellent.” | Neutral | Good | Role and format gave a clean one-word label, and the mixed review got a reasonable label |


## Summary

- Zero-shot gave the correct label, but added an extra explanation until I asked for "only one word".
- Clear format instructions (and a role) gave clean one-word outputs. The role + format prompt worked best.
- Few-shot followed the pattern, but on a mixed review it added a label ("Mixed") that was not allowed. Adding "reply with only one of these three words" fixed that.
- Mixed reviews are hard to label: the model did not always follow my example, so prompts should be tested on different inputs.