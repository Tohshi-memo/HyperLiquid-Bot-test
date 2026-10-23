# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T11:37:28.148473+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0009` n `13`; crypto_alt avg `0.1024` n `237`; crypto_major avg `0.1122` n `8`; equity avg `-0.1192` n `152`; fx avg `-0.0108` n `6`; index avg `-0.0149` n `26`; metal avg `-0.0421` n `20`; unknown avg `0.1548` n `1233`
- 1h: commodity avg `-0.097` n `13`; crypto_alt avg `-0.0351` n `237`; crypto_major avg `-0.1149` n `8`; equity avg `-0.3822` n `152`; fx avg `-0.0075` n `6`; index avg `-0.0366` n `26`; metal avg `0.0455` n `20`; unknown avg `1.8347` n `1231`
- 4h: commodity avg `0.0117` n `13`; crypto_alt avg `-0.3438` n `237`; crypto_major avg `-0.3131` n `8`; equity avg `-0.7312` n `152`; fx avg `-0.0452` n `6`; index avg `-0.1015` n `26`; metal avg `0.0032` n `20`; unknown avg `1.3655` n `1151`
- 24h: commodity avg `0.2787` n `13`; crypto_alt avg `-0.1885` n `237`; crypto_major avg `-0.0167` n `8`; equity avg `-1.7808` n `152`; fx avg `-0.0464` n `6`; index avg `-0.2269` n `26`; metal avg `-0.3074` n `20`; unknown avg `49.668` n `950`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2123`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.175`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1744`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1609`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1531`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1361`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1346`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1329`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1217`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
