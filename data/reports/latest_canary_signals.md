# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T00:22:28.837286+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0269` n `12`; crypto_alt avg `-0.0585` n `234`; crypto_major avg `-0.0408` n `8`; equity avg `-0.114` n `142`; fx avg `-0.0077` n `6`; index avg `-0.0272` n `26`; metal avg `-0.0796` n `20`; unknown avg `0.1495` n `965`
- 1h: commodity avg `0.0782` n `12`; crypto_alt avg `-0.164` n `234`; crypto_major avg `-0.2455` n `8`; equity avg `-0.0471` n `142`; fx avg `0.0344` n `6`; index avg `-0.0136` n `26`; metal avg `-0.1033` n `20`; unknown avg `0.8007` n `951`
- 4h: commodity avg `-0.0415` n `12`; crypto_alt avg `0.0388` n `234`; crypto_major avg `0.0133` n `8`; equity avg `-0.0094` n `142`; fx avg `0.0491` n `6`; index avg `0.0302` n `26`; metal avg `-0.1066` n `20`; unknown avg `0.2365` n `909`
- 24h: commodity avg `0.2496` n `12`; crypto_alt avg `1.3198` n `234`; crypto_major avg `1.1091` n `8`; equity avg `-0.3808` n `142`; fx avg `0.1227` n `6`; index avg `-0.0426` n `26`; metal avg `-0.3538` n `20`; unknown avg `777.8255` n `797`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1359`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.133`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1319`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
