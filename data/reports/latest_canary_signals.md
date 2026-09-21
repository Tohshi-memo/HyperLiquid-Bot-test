# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T23:07:29.187017+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0046` n `12`; crypto_alt avg `0.6248` n `234`; crypto_major avg `0.6879` n `8`; equity avg `0.1338` n `140`; fx avg `0.0011` n `6`; index avg `0.0052` n `26`; metal avg `0.0267` n `20`; unknown avg `-0.0437` n `942`
- 1h: commodity avg `0.0615` n `12`; crypto_alt avg `0.7643` n `234`; crypto_major avg `0.4724` n `8`; equity avg `0.1888` n `140`; fx avg `-0.0018` n `6`; index avg `0.024` n `26`; metal avg `0.0804` n `20`; unknown avg `0.1844` n `942`
- 4h: commodity avg `-0.0596` n `12`; crypto_alt avg `1.3411` n `234`; crypto_major avg `1.5562` n `8`; equity avg `0.1501` n `140`; fx avg `-0.0196` n `6`; index avg `0.0097` n `26`; metal avg `0.1161` n `20`; unknown avg `-0.3424` n `852`
- 24h: commodity avg `-0.7038` n `12`; crypto_alt avg `4.6164` n `234`; crypto_major avg `6.6027` n `8`; equity avg `2.7305` n `140`; fx avg `-0.1428` n `6`; index avg `0.5551` n `26`; metal avg `0.103` n `20`; unknown avg `7.6468` n `771`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1754`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1557`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.133`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1296`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
