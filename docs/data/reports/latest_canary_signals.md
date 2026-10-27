# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T00:07:27.054069+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.02` n `13`; crypto_alt avg `0.17` n `237`; crypto_major avg `0.2328` n `8`; equity avg `0.3547` n `154`; fx avg `-0.0043` n `6`; index avg `0.0693` n `27`; metal avg `0.0491` n `20`; unknown avg `-0.0036` n `1230`
- 1h: commodity avg `0.0078` n `13`; crypto_alt avg `0.9407` n `237`; crypto_major avg `0.8624` n `8`; equity avg `0.761` n `154`; fx avg `0.0064` n `6`; index avg `0.1735` n `27`; metal avg `0.0521` n `20`; unknown avg `0.2293` n `1230`
- 4h: commodity avg `-0.1022` n `13`; crypto_alt avg `0.6308` n `237`; crypto_major avg `0.4757` n `8`; equity avg `0.8691` n `154`; fx avg `-0.0182` n `6`; index avg `0.1729` n `27`; metal avg `0.0406` n `20`; unknown avg `8.8096` n `1136`
- 24h: commodity avg `-0.0475` n `13`; crypto_alt avg `0.3954` n `237`; crypto_major avg `0.7236` n `8`; equity avg `1.5285` n `153`; fx avg `-0.0196` n `6`; index avg `0.1109` n `27`; metal avg `0.0554` n `20`; unknown avg `759.5713` n `972`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2232`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1884`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1798`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1367`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1206`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
