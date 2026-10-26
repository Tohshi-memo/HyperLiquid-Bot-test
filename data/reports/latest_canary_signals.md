# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T05:37:26.411590+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0044` n `13`; crypto_alt avg `-0.0349` n `237`; crypto_major avg `-0.0477` n `8`; equity avg `-0.0563` n `152`; fx avg `-0.0047` n `6`; index avg `-0.023` n `26`; metal avg `-0.0011` n `20`; unknown avg `-0.1748` n `1240`
- 1h: commodity avg `0.0402` n `13`; crypto_alt avg `0.4112` n `237`; crypto_major avg `0.2805` n `8`; equity avg `0.2312` n `152`; fx avg `0.0083` n `6`; index avg `0.0058` n `26`; metal avg `0.0072` n `20`; unknown avg `-0.0121` n `1240`
- 4h: commodity avg `-0.0232` n `13`; crypto_alt avg `0.3825` n `237`; crypto_major avg `0.2812` n `8`; equity avg `0.1778` n `152`; fx avg `-0.0326` n `6`; index avg `0.0143` n `26`; metal avg `0.1271` n `20`; unknown avg `0.131` n `1224`
- 24h: commodity avg `-0.5596` n `13`; crypto_alt avg `-0.6977` n `237`; crypto_major avg `-0.6841` n `8`; equity avg `-0.3334` n `152`; fx avg `0.0518` n `6`; index avg `0.0388` n `26`; metal avg `0.1844` n `20`; unknown avg `-0.2536` n `983`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2547`, n `668`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.2045`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1955`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1944`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1515`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1437`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.133`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1275`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
