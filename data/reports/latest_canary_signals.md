# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T03:22:24.648836+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0002` n `12`; crypto_alt avg `-0.085` n `230`; crypto_major avg `-0.0935` n `8`; equity avg `-0.0665` n `121`; fx avg `-0.0055` n `6`; index avg `-0.0009` n `25`; metal avg `-0.0164` n `20`; unknown avg `-0.0526` n `792`
- 1h: commodity avg `-0.0124` n `12`; crypto_alt avg `-0.4236` n `230`; crypto_major avg `-0.6947` n `8`; equity avg `-0.0018` n `121`; fx avg `0.0159` n `6`; index avg `0.0147` n `25`; metal avg `0.0365` n `20`; unknown avg `0.1127` n `792`
- 4h: commodity avg `0.018` n `12`; crypto_alt avg `0.0114` n `230`; crypto_major avg `-0.5323` n `8`; equity avg `0.0032` n `121`; fx avg `0.1029` n `6`; index avg `0.0751` n `25`; metal avg `-0.1563` n `20`; unknown avg `-0.0176` n `792`
- 24h: commodity avg `-0.0962` n `12`; crypto_alt avg `4.8966` n `230`; crypto_major avg `9.0654` n `8`; equity avg `0.9492` n `120`; fx avg `0.0645` n `6`; index avg `0.2963` n `25`; metal avg `1.0379` n `20`; unknown avg `1.5977` n `757`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1907`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1578`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1443`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1265`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
