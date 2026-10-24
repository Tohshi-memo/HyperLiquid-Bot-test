# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-24T14:52:32.120893+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0052` n `13`; crypto_alt avg `-0.2136` n `237`; crypto_major avg `-0.1854` n `8`; equity avg `-0.0407` n `152`; fx avg `-0.0007` n `6`; index avg `-0.0013` n `26`; metal avg `-0.0211` n `20`; unknown avg `-0.1248` n `1230`
- 1h: commodity avg `0.0243` n `13`; crypto_alt avg `-0.8889` n `237`; crypto_major avg `-0.6818` n `8`; equity avg `-0.2391` n `152`; fx avg `-0.0076` n `6`; index avg `-0.0392` n `26`; metal avg `-0.0936` n `20`; unknown avg `0.281` n `1228`
- 4h: commodity avg `0.1188` n `13`; crypto_alt avg `-1.1271` n `237`; crypto_major avg `-0.5193` n `8`; equity avg `-0.15` n `152`; fx avg `-0.0226` n `6`; index avg `-0.0349` n `26`; metal avg `-0.0714` n `20`; unknown avg `0.956` n `1192`
- 24h: commodity avg `0.3337` n `13`; crypto_alt avg `-3.9382` n `237`; crypto_major avg `-2.9255` n `8`; equity avg `-1.1743` n `152`; fx avg `-0.0521` n `6`; index avg `-0.1541` n `26`; metal avg `-0.238` n `20`; unknown avg `-0.6407` n `1043`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1914`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1913`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1897`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1582`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1506`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1408`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1356`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
