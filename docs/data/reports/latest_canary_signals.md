# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T04:22:27.131875+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0295` n `13`; crypto_alt avg `-0.113` n `237`; crypto_major avg `-0.0947` n `8`; equity avg `-0.2399` n `151`; fx avg `-0.0088` n `6`; index avg `-0.0345` n `26`; metal avg `-0.0395` n `20`; unknown avg `0.141` n `1233`
- 1h: commodity avg `-0.0771` n `13`; crypto_alt avg `0.1138` n `237`; crypto_major avg `0.0044` n `8`; equity avg `0.207` n `151`; fx avg `-0.0175` n `6`; index avg `0.0518` n `26`; metal avg `-0.077` n `20`; unknown avg `0.0242` n `1225`
- 4h: commodity avg `0.082` n `13`; crypto_alt avg `1.1306` n `237`; crypto_major avg `0.6884` n `8`; equity avg `1.171` n `151`; fx avg `0.0253` n `6`; index avg `0.1234` n `26`; metal avg `-0.0845` n `20`; unknown avg `0.4691` n `1223`
- 24h: commodity avg `0.331` n `13`; crypto_alt avg `-1.8286` n `237`; crypto_major avg `-1.1613` n `8`; equity avg `-2.6258` n `151`; fx avg `-0.1344` n `6`; index avg `-0.2675` n `26`; metal avg `-0.6073` n `20`; unknown avg `53.1732` n `903`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1819`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1694`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1627`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1588`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1488`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1343`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1296`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
