# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T22:38:04.013973+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0108` n `12`; crypto_alt avg `-0.5005` n `232`; crypto_major avg `-0.3698` n `8`; equity avg `-0.0055` n `133`; fx avg `0.008` n `6`; index avg `-0.0131` n `26`; metal avg `-0.0137` n `20`; unknown avg `12.4123` n `792`
- 1h: commodity avg `0.0124` n `12`; crypto_alt avg `-0.8501` n `232`; crypto_major avg `-0.7584` n `8`; equity avg `-0.0926` n `133`; fx avg `0.0159` n `6`; index avg `-0.0105` n `26`; metal avg `-0.003` n `20`; unknown avg `10.5977` n `784`
- 4h: commodity avg `0.0818` n `12`; crypto_alt avg `-0.558` n `232`; crypto_major avg `-0.1138` n `8`; equity avg `-0.1621` n `133`; fx avg `0.0152` n `6`; index avg `-0.0444` n `26`; metal avg `-0.0456` n `20`; unknown avg `14.4307` n `766`
- 24h: commodity avg `-0.1158` n `12`; crypto_alt avg `3.9701` n `232`; crypto_major avg `5.0147` n `8`; equity avg `1.219` n `133`; fx avg `-0.2121` n `6`; index avg `0.1483` n `26`; metal avg `0.7851` n `20`; unknown avg `3.2197` n `736`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0698`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
