# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T16:22:33.155452+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.171` n `13`; crypto_alt avg `-0.1342` n `237`; crypto_major avg `-0.1851` n `8`; equity avg `-0.2223` n `152`; fx avg `0.0062` n `6`; index avg `-0.0342` n `26`; metal avg `-0.0054` n `20`; unknown avg `-0.1427` n `1233`
- 1h: commodity avg `0.2621` n `13`; crypto_alt avg `0.3037` n `237`; crypto_major avg `0.0314` n `8`; equity avg `0.0889` n `152`; fx avg `0.0164` n `6`; index avg `0.0173` n `26`; metal avg `0.0056` n `20`; unknown avg `-0.5501` n `1225`
- 4h: commodity avg `0.1371` n `13`; crypto_alt avg `0.0071` n `237`; crypto_major avg `0.0033` n `8`; equity avg `0.3264` n `152`; fx avg `0.0451` n `6`; index avg `0.1076` n `26`; metal avg `0.0601` n `20`; unknown avg `-0.613` n `1161`
- 24h: commodity avg `0.5501` n `13`; crypto_alt avg `0.9658` n `237`; crypto_major avg `0.3217` n `8`; equity avg `0.4746` n `152`; fx avg `-0.0866` n `6`; index avg `-0.0373` n `26`; metal avg `-0.1687` n `20`; unknown avg `-0.8781` n `1036`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1925`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1573`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.144`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1398`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1362`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.118`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
