# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T19:22:27.016678+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0209` n `13`; crypto_alt avg `0.023` n `237`; crypto_major avg `0.1026` n `8`; equity avg `0.0293` n `152`; fx avg `0.0169` n `6`; index avg `0.0087` n `26`; metal avg `-0.0` n `20`; unknown avg `2.4503` n `1240`
- 1h: commodity avg `-0.0059` n `13`; crypto_alt avg `-0.1482` n `237`; crypto_major avg `-0.0365` n `8`; equity avg `0.0279` n `152`; fx avg `0.0025` n `6`; index avg `0.0134` n `26`; metal avg `0.0033` n `20`; unknown avg `9.8025` n `1240`
- 4h: commodity avg `-0.068` n `13`; crypto_alt avg `0.5137` n `237`; crypto_major avg `0.3386` n `8`; equity avg `0.334` n `152`; fx avg `0.0106` n `6`; index avg `0.0511` n `26`; metal avg `0.0503` n `20`; unknown avg `4.4468` n `1194`
- 24h: commodity avg `-0.2471` n `13`; crypto_alt avg `0.3454` n `237`; crypto_major avg `0.7759` n `8`; equity avg `0.7071` n `152`; fx avg `0.0443` n `6`; index avg `0.1409` n `26`; metal avg `0.1483` n `20`; unknown avg `10.0586` n `1043`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2254`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1788`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1683`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1671`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1545`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1471`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1346`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1338`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
