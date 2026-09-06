# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T14:37:32.826344+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0295` n `12`; crypto_alt avg `-0.2498` n `232`; crypto_major avg `-0.0306` n `8`; equity avg `0.0029` n `134`; fx avg `0.0046` n `6`; index avg `0.0062` n `26`; metal avg `-0.0083` n `20`; unknown avg `1.2307` n `792`
- 1h: commodity avg `0.0454` n `12`; crypto_alt avg `-0.821` n `232`; crypto_major avg `-0.4288` n `8`; equity avg `-0.1341` n `134`; fx avg `-0.0052` n `6`; index avg `-0.0223` n `26`; metal avg `-0.0263` n `20`; unknown avg `147.0673` n `790`
- 4h: commodity avg `0.0313` n `12`; crypto_alt avg `-0.8343` n `232`; crypto_major avg `-0.5234` n `8`; equity avg `-0.2194` n `134`; fx avg `-0.0236` n `6`; index avg `-0.0349` n `26`; metal avg `-0.0255` n `20`; unknown avg `68.386` n `720`
- 24h: commodity avg `0.152` n `12`; crypto_alt avg `0.8301` n `232`; crypto_major avg `0.6319` n `8`; equity avg `0.2605` n `134`; fx avg `-0.034` n `6`; index avg `0.0463` n `26`; metal avg `-0.016` n `20`; unknown avg `1.4114` n `664`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1323`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
