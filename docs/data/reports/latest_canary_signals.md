# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T18:50:59.008020+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0242` n `12`; crypto_alt avg `0.1405` n `230`; crypto_major avg `0.2752` n `8`; equity avg `0.0396` n `98`; fx avg `0.0018` n `6`; index avg `0.0039` n `25`; metal avg `0.0294` n `20`; unknown avg `0.1071` n `773`
- 1h: commodity avg `0.0524` n `12`; crypto_alt avg `-0.3031` n `230`; crypto_major avg `-0.2823` n `8`; equity avg `-0.2723` n `98`; fx avg `0.0058` n `6`; index avg `-0.0365` n `25`; metal avg `-0.0326` n `20`; unknown avg `0.199` n `773`
- 4h: commodity avg `0.1086` n `12`; crypto_alt avg `-0.0284` n `230`; crypto_major avg `0.233` n `8`; equity avg `-0.2868` n `98`; fx avg `0.0161` n `6`; index avg `0.0424` n `25`; metal avg `-0.0997` n `20`; unknown avg `-0.1395` n `773`
- 24h: commodity avg `0.6093` n `12`; crypto_alt avg `-0.4208` n `230`; crypto_major avg `-0.5605` n `8`; equity avg `-0.4289` n `98`; fx avg `-0.039` n `6`; index avg `-0.1217` n `25`; metal avg `0.2701` n `20`; unknown avg `1.4377` n `739`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1703`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0863`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0721`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
