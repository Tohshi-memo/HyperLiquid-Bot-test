# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-24T22:22:30.217936+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0237` n `13`; crypto_alt avg `-0.0445` n `237`; crypto_major avg `-0.0145` n `8`; equity avg `0.0054` n `152`; fx avg `0.0007` n `6`; index avg `-0.0049` n `26`; metal avg `0.0113` n `20`; unknown avg `0.0363` n `1231`
- 1h: commodity avg `0.0205` n `13`; crypto_alt avg `0.2086` n `237`; crypto_major avg `0.0647` n `8`; equity avg `0.0655` n `152`; fx avg `-0.0012` n `6`; index avg `0.0117` n `26`; metal avg `0.0078` n `20`; unknown avg `-0.1552` n `1161`
- 4h: commodity avg `-0.082` n `13`; crypto_alt avg `0.6869` n `237`; crypto_major avg `0.5926` n `8`; equity avg `0.2861` n `152`; fx avg `-0.0033` n `6`; index avg `0.0482` n `26`; metal avg `0.0194` n `20`; unknown avg `0.8102` n `1137`
- 24h: commodity avg `0.0097` n `13`; crypto_alt avg `-2.072` n `237`; crypto_major avg `-1.55` n `8`; equity avg `-0.257` n `152`; fx avg `-0.0751` n `6`; index avg `-0.043` n `26`; metal avg `-0.1503` n `20`; unknown avg `0.197` n `1064`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1916`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1884`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1792`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1581`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1503`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1374`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1368`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1211`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
