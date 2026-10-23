# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T06:36:23.730098+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0187` n `13`; crypto_alt avg `-0.1526` n `237`; crypto_major avg `-0.0987` n `8`; equity avg `-0.0566` n `152`; fx avg `0.0018` n `6`; index avg `-0.0226` n `26`; metal avg `-0.0351` n `20`; unknown avg `0.3375` n `1233`
- 1h: commodity avg `0.0548` n `13`; crypto_alt avg `-0.0382` n `237`; crypto_major avg `0.1102` n `8`; equity avg `0.5377` n `152`; fx avg `0.0052` n `6`; index avg `0.0652` n `26`; metal avg `-0.0597` n `20`; unknown avg `0.9306` n `1210`
- 4h: commodity avg `0.0601` n `13`; crypto_alt avg `0.1886` n `237`; crypto_major avg `0.1278` n `8`; equity avg `1.3463` n `152`; fx avg `-0.0191` n `6`; index avg `0.1421` n `26`; metal avg `0.0202` n `20`; unknown avg `1.8861` n `1202`
- 24h: commodity avg `0.2757` n `13`; crypto_alt avg `-0.412` n `237`; crypto_major avg `-0.3493` n `8`; equity avg `-1.192` n `152`; fx avg `-0.0631` n `6`; index avg `-0.0911` n `26`; metal avg `-0.4905` n `20`; unknown avg `52.3645` n `898`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1839`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1704`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1526`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1505`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1453`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1411`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1381`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1132`, n `668`, weak_sample_signal
