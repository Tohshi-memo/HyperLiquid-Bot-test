# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-24T23:25:23.524456+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0151` n `13`; crypto_alt avg `0.1271` n `237`; crypto_major avg `0.0195` n `8`; equity avg `0.0318` n `152`; fx avg `0.0034` n `6`; index avg `-0.0043` n `26`; metal avg `-0.0008` n `20`; unknown avg `-0.0593` n `1231`
- 1h: commodity avg `-0.0663` n `13`; crypto_alt avg `0.236` n `237`; crypto_major avg `0.1911` n `8`; equity avg `0.0889` n `152`; fx avg `-0.0036` n `6`; index avg `0.0061` n `26`; metal avg `0.0126` n `20`; unknown avg `156.1399` n `1231`
- 4h: commodity avg `-0.0646` n `13`; crypto_alt avg `0.603` n `237`; crypto_major avg `0.3715` n `8`; equity avg `0.1316` n `152`; fx avg `0.0065` n `6`; index avg `0.0158` n `26`; metal avg `0.0146` n `20`; unknown avg `0.0321` n `1137`
- 24h: commodity avg `-0.0651` n `13`; crypto_alt avg `-0.6527` n `237`; crypto_major avg `-0.6275` n `8`; equity avg `0.0725` n `152`; fx avg `-0.0431` n `6`; index avg `0.0055` n `26`; metal avg `-0.0963` n `20`; unknown avg `0.4617` n `1064`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1922`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1793`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1769`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1587`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1506`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1397`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1363`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1225`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1198`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
