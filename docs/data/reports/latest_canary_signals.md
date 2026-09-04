# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T08:52:29.761443+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0096` n `12`; crypto_alt avg `0.2443` n `232`; crypto_major avg `0.1399` n `8`; equity avg `-0.0295` n `133`; fx avg `0.0215` n `6`; index avg `0.0065` n `26`; metal avg `-0.0278` n `20`; unknown avg `-0.1031` n `793`
- 1h: commodity avg `0.0342` n `12`; crypto_alt avg `0.4631` n `232`; crypto_major avg `0.3684` n `8`; equity avg `0.1422` n `133`; fx avg `-0.0103` n `6`; index avg `0.0052` n `26`; metal avg `-0.0061` n `20`; unknown avg `-0.0891` n `785`
- 4h: commodity avg `-0.1428` n `12`; crypto_alt avg `0.2761` n `232`; crypto_major avg `-0.0142` n `8`; equity avg `0.1664` n `133`; fx avg `-0.0305` n `6`; index avg `0.0224` n `26`; metal avg `0.0748` n `20`; unknown avg `0.4507` n `749`
- 24h: commodity avg `-0.2731` n `12`; crypto_alt avg `2.3087` n `232`; crypto_major avg `4.006` n `8`; equity avg `1.9445` n `133`; fx avg `-0.0136` n `6`; index avg `0.3456` n `26`; metal avg `0.4915` n `20`; unknown avg `1.608` n `730`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1179`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
