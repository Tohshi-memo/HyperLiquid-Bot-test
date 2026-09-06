# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T15:37:25.150314+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0027` n `12`; crypto_alt avg `0.0859` n `232`; crypto_major avg `-0.0364` n `8`; equity avg `0.047` n `134`; fx avg `-0.0063` n `6`; index avg `0.0096` n `26`; metal avg `-0.0074` n `20`; unknown avg `144.8359` n `792`
- 1h: commodity avg `-0.0351` n `12`; crypto_alt avg `0.2658` n `232`; crypto_major avg `0.0459` n `8`; equity avg `0.0016` n `134`; fx avg `-0.0075` n `6`; index avg `0.0079` n `26`; metal avg `0.0121` n `20`; unknown avg `1.1869` n `790`
- 4h: commodity avg `0.008` n `12`; crypto_alt avg `-0.9526` n `232`; crypto_major avg `-0.5735` n `8`; equity avg `-0.24` n `134`; fx avg `-0.0148` n `6`; index avg `-0.0344` n `26`; metal avg `-0.0159` n `20`; unknown avg `226.9441` n `720`
- 24h: commodity avg `0.0869` n `12`; crypto_alt avg `1.3325` n `232`; crypto_major avg `0.7075` n `8`; equity avg `0.2213` n `134`; fx avg `-0.0378` n `6`; index avg `0.0441` n `26`; metal avg `-0.0168` n `20`; unknown avg `1.881` n `664`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1392`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1276`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
