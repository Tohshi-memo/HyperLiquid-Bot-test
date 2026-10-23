# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T21:52:27.989755+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0814` n `13`; crypto_alt avg `-0.1193` n `237`; crypto_major avg `-0.0653` n `8`; equity avg `0.0003` n `152`; fx avg `0.003` n `6`; index avg `-0.0112` n `26`; metal avg `-0.0077` n `20`; unknown avg `0.1708` n `1228`
- 1h: commodity avg `0.1156` n `13`; crypto_alt avg `-0.2341` n `237`; crypto_major avg `-0.154` n `8`; equity avg `-0.0362` n `152`; fx avg `0.0199` n `6`; index avg `-0.0106` n `26`; metal avg `0.0127` n `20`; unknown avg `-0.2047` n `1222`
- 4h: commodity avg `0.1845` n `13`; crypto_alt avg `-1.0434` n `237`; crypto_major avg `-0.4838` n `8`; equity avg `-0.2605` n `152`; fx avg `-0.0047` n `6`; index avg `0.0043` n `26`; metal avg `-0.0202` n `20`; unknown avg `0.259` n `1141`
- 24h: commodity avg `0.5499` n `13`; crypto_alt avg `0.1316` n `237`; crypto_major avg `0.2475` n `8`; equity avg `1.4488` n `152`; fx avg `-0.0739` n `6`; index avg `0.1314` n `26`; metal avg `-0.1628` n `20`; unknown avg `-0.1525` n `1020`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1995`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1802`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1528`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1527`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1497`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1452`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1198`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
