# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T11:37:30.791619+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0175` n `12`; crypto_alt avg `0.141` n `234`; crypto_major avg `0.1941` n `8`; equity avg `0.1089` n `141`; fx avg `-0.0026` n `6`; index avg `0.0179` n `26`; metal avg `-0.0128` n `20`; unknown avg `1.7668` n `962`
- 1h: commodity avg `-0.0614` n `12`; crypto_alt avg `0.1605` n `234`; crypto_major avg `0.2289` n `8`; equity avg `0.3252` n `141`; fx avg `-0.0267` n `6`; index avg `0.0549` n `26`; metal avg `-0.0336` n `20`; unknown avg `2.2293` n `960`
- 4h: commodity avg `0.2599` n `12`; crypto_alt avg `0.2977` n `234`; crypto_major avg `0.5792` n `8`; equity avg `-0.1619` n `141`; fx avg `-0.0652` n `6`; index avg `0.0059` n `26`; metal avg `0.0663` n `20`; unknown avg `12.7552` n `942`
- 24h: commodity avg `-0.104` n `12`; crypto_alt avg `-3.6698` n `234`; crypto_major avg `-2.5179` n `8`; equity avg `-2.5431` n `141`; fx avg `0.0139` n `6`; index avg `-0.231` n `26`; metal avg `-0.9091` n `20`; unknown avg `4.5384` n `814`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1408`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
