# Structured Output

Structured output is useful when an LLM response will be consumed by software.

## JSON Example

```text
Analyze the following customer review.

Return ONLY valid JSON using this structure:

{
  "sentiment": "Positive | Negative | Neutral",
  "confidence": 0.0,
  "reason": "short explanation"
}

Review:
"The product is excellent and delivery was very fast."
```

Expected shape:

```json
{
  "sentiment": "Positive",
  "confidence": 0.98,
  "reason": "The customer expresses satisfaction with the product and delivery."
}
```
