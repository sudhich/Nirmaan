# Few-Shot Prompting

Few-shot prompting gives the model examples before the new task.

## Sentiment classification

```text
You are a sentiment classifier.

Examples:
Text: "I love this product."
Label: Positive

Text: "The service was terrible."
Label: Negative

Text: "The package arrived today."
Label: Neutral

Now classify:
Text: "The support team solved my problem quickly."
Label:
```

## Support classification

```text
Examples:
Message: "I forgot my password."
Category: Account

Message: "My card was charged twice."
Category: Billing

Message: "The application shows an error."
Category: Technical

Now classify:
Message: "The dashboard is not loading."
Category:
```
