# aeffect

<p align="center">
  <img src="aeffect.jpg">
  This is what you get when you search "aeffect" on Google Images.
</p>

I can never remember when to use affect/effect, so I built this to tell me which to use. It is basically a very small amount of code using HuggingFace's [fill-mask](https://huggingface.co/tasks/fill-mask) pipelines, with a `"bert-base-cased"` model to predict the `[MASK]` token. The code is wrapped in an installable package and script, so can be called from anywhere.

## Usage

Install with:

- `git clone https://github.com/bentrevett/aeffect.git`
- `cd aeffect`
- `pip install -e .`

Use aeffect with:

- `aeffect "These tricks have no [MASK] on me."`
  - Your query needs to be enclosed in quotation marks.
  - The `[MASK]` is where the affect/effect should be.
  - There should only be a single `[MASK]` token in the query.

This will print:

```bash
(92.28%): These tricks have no effect on me.
(01.00%): These tricks have no affect on me.
```

In other words, the model thinks that there's a 92.28% the `[MASK]` token should be "effect", and 1% it should be "affect". These percentages will not add up to 100%, because there are other words the model thinks might be appropriate!
