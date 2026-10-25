# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T11:52:32.156508+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0027` n `13`; crypto_alt avg `0.6606` n `237`; crypto_major avg `0.4561` n `8`; equity avg `0.0987` n `152`; fx avg `0.0042` n `6`; index avg `0.0132` n `26`; metal avg `0.0243` n `20`; unknown avg `0.1077` n `1231`
- 1h: commodity avg `-0.012` n `13`; crypto_alt avg `0.7693` n `237`; crypto_major avg `0.6214` n `8`; equity avg `0.1283` n `152`; fx avg `0.0039` n `6`; index avg `0.0271` n `26`; metal avg `0.0316` n `20`; unknown avg `1.7342` n `1231`
- 4h: commodity avg `0.0026` n `13`; crypto_alt avg `-0.1995` n `237`; crypto_major avg `-0.1317` n `8`; equity avg `-0.0353` n `152`; fx avg `0.013` n `6`; index avg `0.0063` n `26`; metal avg `0.0175` n `20`; unknown avg `17.8035` n `1181`
- 24h: commodity avg `-0.0661` n `13`; crypto_alt avg `-1.1412` n `237`; crypto_major avg `0.2921` n `8`; equity avg `0.098` n `152`; fx avg `-0.0011` n `6`; index avg `0.0495` n `26`; metal avg `-0.0096` n `20`; unknown avg `18.3304` n `1048`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2103`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1687`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1662`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1578`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1536`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1501`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1323`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1313`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1287`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
