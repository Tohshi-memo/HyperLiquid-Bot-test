# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T10:14:30.671394+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0101` n `12`; crypto_alt avg `-0.0804` n `230`; crypto_major avg `-0.1724` n `8`; equity avg `-0.0857` n `108`; fx avg `0.0058` n `6`; index avg `-0.0153` n `25`; metal avg `-0.0546` n `20`; unknown avg `-0.016` n `781`
- 1h: commodity avg `0.0964` n `12`; crypto_alt avg `-0.0474` n `230`; crypto_major avg `-0.2213` n `8`; equity avg `-0.0452` n `108`; fx avg `0.01` n `6`; index avg `-0.0093` n `25`; metal avg `-0.1041` n `20`; unknown avg `0.6575` n `781`
- 4h: commodity avg `0.2808` n `12`; crypto_alt avg `-0.1701` n `230`; crypto_major avg `-0.1748` n `8`; equity avg `-1.0025` n `108`; fx avg `0.0548` n `6`; index avg `-0.1553` n `25`; metal avg `-0.1444` n `20`; unknown avg `0.729` n `781`
- 24h: commodity avg `-1.2048` n `12`; crypto_alt avg `0.6414` n `230`; crypto_major avg `0.8658` n `8`; equity avg `2.6462` n `108`; fx avg `-0.011` n `6`; index avg `0.6214` n `25`; metal avg `1.066` n `20`; unknown avg `0.1351` n `748`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1486`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1265`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1198`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
