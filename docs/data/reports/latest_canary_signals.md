# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T02:52:28.757727+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0005` n `13`; crypto_alt avg `-0.0121` n `237`; crypto_major avg `-0.0116` n `8`; equity avg `-0.0152` n `152`; fx avg `0.0111` n `6`; index avg `-0.0044` n `26`; metal avg `-0.0051` n `20`; unknown avg `-0.0968` n `1229`
- 1h: commodity avg `0.0148` n `13`; crypto_alt avg `-0.1159` n `237`; crypto_major avg `0.1013` n `8`; equity avg `-0.0401` n `152`; fx avg `0.0028` n `6`; index avg `-0.0001` n `26`; metal avg `-0.0019` n `20`; unknown avg `0.2223` n `1227`
- 4h: commodity avg `-0.0342` n `13`; crypto_alt avg `-0.0168` n `237`; crypto_major avg `0.6782` n `8`; equity avg `0.1176` n `152`; fx avg `0.0062` n `6`; index avg `0.0116` n `26`; metal avg `0.0168` n `20`; unknown avg `0.159` n `1213`
- 24h: commodity avg `-0.0266` n `13`; crypto_alt avg `-1.251` n `237`; crypto_major avg `-0.1021` n `8`; equity avg `-0.0778` n `152`; fx avg `-0.0322` n `6`; index avg `-0.0103` n `26`; metal avg `-0.0863` n `20`; unknown avg `4.0477` n `1066`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1951`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1711`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1639`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1593`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.153`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1508`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1364`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1277`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1192`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
