# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T23:52:26.563048+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.011` n `12`; crypto_alt avg `0.4649` n `230`; crypto_major avg `0.4829` n `8`; equity avg `0.0102` n `121`; fx avg `-0.0063` n `6`; index avg `-0.0031` n `25`; metal avg `0.0009` n `20`; unknown avg `0.1608` n `794`
- 1h: commodity avg `-0.0183` n `12`; crypto_alt avg `0.1446` n `230`; crypto_major avg `0.3236` n `8`; equity avg `0.0704` n `121`; fx avg `0.013` n `6`; index avg `0.0128` n `25`; metal avg `0.0057` n `20`; unknown avg `0.1719` n `794`
- 4h: commodity avg `0.0891` n `12`; crypto_alt avg `-1.0396` n `230`; crypto_major avg `-0.732` n `8`; equity avg `0.0887` n `121`; fx avg `0.0401` n `6`; index avg `0.0082` n `25`; metal avg `-0.0024` n `20`; unknown avg `0.3121` n `794`
- 24h: commodity avg `0.0832` n `12`; crypto_alt avg `-1.8376` n `230`; crypto_major avg `0.371` n `8`; equity avg `-0.371` n `121`; fx avg `0.1067` n `6`; index avg `-0.0556` n `25`; metal avg `-0.0741` n `20`; unknown avg `3.0262` n `777`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1491`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1276`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1271`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.119`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
