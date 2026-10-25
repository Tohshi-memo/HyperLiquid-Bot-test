# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T10:52:27.219129+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0217` n `13`; crypto_alt avg `-0.1669` n `237`; crypto_major avg `-0.0472` n `8`; equity avg `-0.0003` n `152`; fx avg `0.0068` n `6`; index avg `-0.0031` n `26`; metal avg `0.0017` n `20`; unknown avg `0.0712` n `1231`
- 1h: commodity avg `0.0302` n `13`; crypto_alt avg `-0.3673` n `237`; crypto_major avg `-0.1069` n `8`; equity avg `0.0212` n `152`; fx avg `0.0161` n `6`; index avg `-0.0064` n `26`; metal avg `0.0076` n `20`; unknown avg `8.1356` n `1227`
- 4h: commodity avg `-0.028` n `13`; crypto_alt avg `-0.7245` n `237`; crypto_major avg `-0.3761` n `8`; equity avg `-0.044` n `152`; fx avg `0.0141` n `6`; index avg `-0.0011` n `26`; metal avg `0.0223` n `20`; unknown avg `20.0921` n `1181`
- 24h: commodity avg `0.0281` n `13`; crypto_alt avg `-1.9633` n `237`; crypto_major avg `-0.3009` n `8`; equity avg `-0.015` n `152`; fx avg `-0.0194` n `6`; index avg `0.0143` n `26`; metal avg `-0.0411` n `20`; unknown avg `20.7796` n `1048`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1973`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1618`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1607`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1554`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1425`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.142`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1179`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
