# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T07:52:25.713241+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0` n `12`; crypto_alt avg `-0.2422` n `232`; crypto_major avg `-0.3007` n `8`; equity avg `-0.0095` n `133`; fx avg `0.0161` n `6`; index avg `-0.0014` n `26`; metal avg `0.009` n `20`; unknown avg `1.1483` n `792`
- 1h: commodity avg `0.0318` n `12`; crypto_alt avg `-0.047` n `232`; crypto_major avg `-0.1836` n `8`; equity avg `0.1144` n `133`; fx avg `0.0413` n `6`; index avg `-0.0056` n `26`; metal avg `0.0526` n `20`; unknown avg `0.1406` n `790`
- 4h: commodity avg `-0.144` n `12`; crypto_alt avg `0.4414` n `232`; crypto_major avg `-0.0193` n `8`; equity avg `-0.3185` n `133`; fx avg `-0.0383` n `6`; index avg `-0.12` n `26`; metal avg `0.0058` n `20`; unknown avg `-0.0589` n `754`
- 24h: commodity avg `0.1292` n `12`; crypto_alt avg `0.5331` n `232`; crypto_major avg `0.41` n `8`; equity avg `1.2166` n `133`; fx avg `-0.3294` n `6`; index avg `0.0953` n `26`; metal avg `0.7591` n `20`; unknown avg `-0.4967` n `735`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0535`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0516`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0448`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0387`, n `668`, weak_sample_signal
