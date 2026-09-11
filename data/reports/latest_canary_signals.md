# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T01:52:26.056024+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0691` n `12`; crypto_alt avg `0.0154` n `233`; crypto_major avg `0.1869` n `8`; equity avg `-0.0585` n `136`; fx avg `-0.0053` n `6`; index avg `-0.017` n `26`; metal avg `-0.0336` n `20`; unknown avg `0.0121` n `796`
- 1h: commodity avg `-0.1086` n `12`; crypto_alt avg `0.0163` n `233`; crypto_major avg `0.1762` n `8`; equity avg `-0.0149` n `136`; fx avg `-0.0075` n `6`; index avg `-0.0148` n `26`; metal avg `-0.064` n `20`; unknown avg `120.8563` n `794`
- 4h: commodity avg `-0.4607` n `12`; crypto_alt avg `-0.7713` n `233`; crypto_major avg `-0.5834` n `8`; equity avg `0.0123` n `136`; fx avg `-0.0078` n `6`; index avg `0.004` n `26`; metal avg `-0.0113` n `20`; unknown avg `0.1928` n `750`
- 24h: commodity avg `1.0694` n `12`; crypto_alt avg `-1.2918` n `233`; crypto_major avg `-1.6525` n `8`; equity avg `-1.5626` n `136`; fx avg `0.0971` n `6`; index avg `-0.2848` n `26`; metal avg `-1.2381` n `20`; unknown avg `-1.0854` n `683`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1397`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1349`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1168`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
