**Table of Contents**

- [Promt Engineering](#promt-engineering)
- [Types of prompting](#types-of-prompting)
  - [Zero-Shot Prompting](#zero-shot-prompting)
  - [One-Shot Prompting](#one-shot-prompting)
  - [Few-Shot Prompting](#few-shot-prompting)
  - [Chain-of-Thought Prompting](#chain-of-thought-prompting)
  - [Self-Criticism](#self-criticism)
  - [Iterative](#iterative)
- [To do Items](#to-do-items)

## Promt Engineering

It is process of discovering prompts which reliably yield useful or desired results

### Types of prompting

- ##### Zero-Shot Prompting
  The zero-shot strategy involves the LLM generating an answer without any examples or context. This strategy can be useful when the user wants a quick answer without providing additional detail, or when the topic is so general that examples would artificially limit the response. For example:

```
Generate 10 possible names for my new dog.
```

- ##### One-Shot Prompting

  The one-shot strategy involves the LLM generating an answer based on a single example or piece of context provided by the user. This strategy can guide LLM's response and ensure it aligns with the user’s intent. The idea here would be that one example would provide more guidance to the model than none. For example:

      ```
      Generate 10 possible names for my new dog.
      A dog name that I like is Banana.
      ```

  Tips: Do not give 2 similar example as they are constraining the creative space

- ##### Few-Shot Prompting

  The few-shot strategy involves the LLM generating an answer based on a few examples or pieces of context provided by the user. This strategy can guide LLM's response and ensure it aligns with the user’s intent. The idea here would be that several examples would provide more guidance to the model than one. For example:

  ```
  Generate 10 possible names for my new dog.
  Dog names that I like include:
  – Banana
  – Kiwi
  – Pineapple
  – Coconut
  ```

  As we can guess, the more examples the prompt included, the closer the generated output conforms to what is desired. With zero-shot, there may be no fruit names suggested; with one-shot, there may be several; and with few-shot, the suggestions may consist entirely of fruit-themed names.

- ##### Chain-of-Thought Prompting
- ##### Self-Criticism
- ##### Iterative

Read Following link for above prompting types
https://machinelearningmastery.com/prompt-engineering-for-effective-interaction-with-chatgpt/

##### Chaining AIs

Combining multiple AI responses or multiple AI models, in order to complete more sophisticated task.

- Break a task into multiple subtask
- output of first task will be input to another task
-

## Notes

#### Image Models

- DALL E
- Tencent ARC
- Midjourney

# To do Items

- Read aboout stable diffusion
-
