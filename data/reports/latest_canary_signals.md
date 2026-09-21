# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T18:22:32.206100+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0199` n `12`; crypto_alt avg `0.0415` n `234`; crypto_major avg `0.2114` n `8`; equity avg `0.1284` n `140`; fx avg `0.0058` n `6`; index avg `0.0202` n `26`; metal avg `0.0222` n `20`; unknown avg `-0.0485` n `942`
- 1h: commodity avg `0.1431` n `12`; crypto_alt avg `0.026` n `234`; crypto_major avg `0.4289` n `8`; equity avg `0.326` n `140`; fx avg `0.0082` n `6`; index avg `0.0442` n `26`; metal avg `0.0604` n `20`; unknown avg `0.0177` n `940`
- 4h: commodity avg `0.0596` n `12`; crypto_alt avg `-0.2255` n `234`; crypto_major avg `0.9567` n `8`; equity avg `0.8377` n `140`; fx avg `0.0077` n `6`; index avg `0.1981` n `26`; metal avg `-0.0343` n `20`; unknown avg `0.5739` n `892`
- 24h: commodity avg `-0.9224` n `12`; crypto_alt avg `3.5742` n `234`; crypto_major avg `5.2585` n `8`; equity avg `2.9444` n `140`; fx avg `-0.0915` n `6`; index avg `0.6255` n `26`; metal avg `0.0483` n `20`; unknown avg `6.645` n `739`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1838`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1636`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.136`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1331`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
