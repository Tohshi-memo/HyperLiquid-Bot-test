# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T18:52:26.018018+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0023` n `12`; crypto_alt avg `0.074` n `230`; crypto_major avg `0.1282` n `8`; equity avg `0.1869` n `113`; fx avg `-0.0003` n `6`; index avg `0.0153` n `25`; metal avg `0.0288` n `20`; unknown avg `0.102` n `785`
- 1h: commodity avg `-0.0466` n `12`; crypto_alt avg `-0.0196` n `230`; crypto_major avg `-0.0809` n `8`; equity avg `-0.0411` n `113`; fx avg `0.0085` n `6`; index avg `-0.038` n `25`; metal avg `-0.0275` n `20`; unknown avg `0.0903` n `785`
- 4h: commodity avg `0.1647` n `12`; crypto_alt avg `-0.6785` n `230`; crypto_major avg `0.0185` n `8`; equity avg `-0.5359` n `113`; fx avg `0.0124` n `6`; index avg `-0.1615` n `25`; metal avg `-0.1605` n `20`; unknown avg `-0.1123` n `785`
- 24h: commodity avg `0.1163` n `12`; crypto_alt avg `-1.9229` n `230`; crypto_major avg `-0.0649` n `8`; equity avg `0.0955` n `113`; fx avg `-0.0676` n `6`; index avg `0.0248` n `25`; metal avg `-0.1447` n `20`; unknown avg `-0.2392` n `753`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2075`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2008`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1996`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.193`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1804`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1494`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1319`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
