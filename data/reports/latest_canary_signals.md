# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T04:37:26.645836+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0029` n `12`; crypto_alt avg `0.2` n `233`; crypto_major avg `0.1153` n `8`; equity avg `0.1662` n `134`; fx avg `0.0071` n `6`; index avg `0.0323` n `26`; metal avg `0.0245` n `20`; unknown avg `-0.203` n `792`
- 1h: commodity avg `-0.0598` n `12`; crypto_alt avg `0.7164` n `233`; crypto_major avg `0.6236` n `8`; equity avg `-0.007` n `134`; fx avg `-0.036` n `6`; index avg `-0.0106` n `26`; metal avg `-0.0158` n `20`; unknown avg `-0.2494` n `789`
- 4h: commodity avg `-0.1197` n `12`; crypto_alt avg `0.1471` n `233`; crypto_major avg `0.2354` n `8`; equity avg `0.3629` n `134`; fx avg `-0.0645` n `6`; index avg `0.0644` n `26`; metal avg `0.1149` n `20`; unknown avg `-0.1477` n `785`
- 24h: commodity avg `-0.0351` n `12`; crypto_alt avg `-0.1025` n `232`; crypto_major avg `0.9426` n `8`; equity avg `0.1969` n `134`; fx avg `-0.0622` n `6`; index avg `-0.1872` n `26`; metal avg `-0.4208` n `20`; unknown avg `-0.1883` n `681`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1458`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
