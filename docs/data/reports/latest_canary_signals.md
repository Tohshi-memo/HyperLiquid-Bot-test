# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-24T10:37:31.680518+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0355` n `13`; crypto_alt avg `0.3797` n `237`; crypto_major avg `0.2445` n `8`; equity avg `0.0741` n `152`; fx avg `0.0012` n `6`; index avg `0.0041` n `26`; metal avg `-0.0035` n `20`; unknown avg `0.4699` n `1230`
- 1h: commodity avg `-0.0228` n `13`; crypto_alt avg `0.4571` n `237`; crypto_major avg `0.3793` n `8`; equity avg `0.1216` n `152`; fx avg `0.0058` n `6`; index avg `-0.0015` n `26`; metal avg `0.0109` n `20`; unknown avg `116.9523` n `1228`
- 4h: commodity avg `0.0147` n `13`; crypto_alt avg `-0.356` n `237`; crypto_major avg `-0.5992` n `8`; equity avg `-0.1658` n `152`; fx avg `0.0043` n `6`; index avg `-0.0298` n `26`; metal avg `-0.0326` n `20`; unknown avg `119.4391` n `1194`
- 24h: commodity avg `0.1496` n `13`; crypto_alt avg `-2.3129` n `237`; crypto_major avg `-2.0341` n `8`; equity avg `-0.6933` n `152`; fx avg `0.0031` n `6`; index avg `-0.0175` n `26`; metal avg `-0.1464` n `20`; unknown avg `194.0725` n `1053`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1965`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1949`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1948`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1629`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1516`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1444`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1436`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1289`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
