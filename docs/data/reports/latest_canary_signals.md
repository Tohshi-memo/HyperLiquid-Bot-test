# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-24T16:22:31.951148+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.5296` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0027` n `13`; crypto_alt avg `-0.1886` n `237`; crypto_major avg `-0.1806` n `8`; equity avg `-0.0075` n `152`; fx avg `-0.0043` n `6`; index avg `-0.0018` n `26`; metal avg `-0.0022` n `20`; unknown avg `-0.1657` n `1231`
- 1h: commodity avg `0.0271` n `13`; crypto_alt avg `-0.0096` n `237`; crypto_major avg `0.1486` n `8`; equity avg `-0.1487` n `152`; fx avg `-0.0118` n `6`; index avg `-0.0231` n `26`; metal avg `-0.0166` n `20`; unknown avg `-0.4257` n `1224`
- 4h: commodity avg `0.0079` n `13`; crypto_alt avg `-2.2249` n `237`; crypto_major avg `-1.622` n `8`; equity avg `-0.6809` n `152`; fx avg `-0.028` n `6`; index avg `-0.0924` n `26`; metal avg `-0.1347` n `20`; unknown avg `0.8541` n `1192`
- 24h: commodity avg `0.1284` n `13`; crypto_alt avg `-4.7731` n `237`; crypto_major avg `-3.5725` n `8`; equity avg `-1.2292` n `152`; fx avg `-0.0511` n `6`; index avg `-0.1641` n `26`; metal avg `-0.3273` n `20`; unknown avg `-0.755` n `1043`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1915`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1903`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1871`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.16`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1516`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1452`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1391`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1302`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1204`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1187`, n `668`, weak_sample_signal
