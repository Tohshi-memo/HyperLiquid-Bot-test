# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T15:37:24.188269+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.026` n `13`; crypto_alt avg `0.322` n `237`; crypto_major avg `0.2795` n `8`; equity avg `0.0329` n `152`; fx avg `0.0015` n `6`; index avg `0.0017` n `26`; metal avg `0.0032` n `20`; unknown avg `-0.2147` n `1240`
- 1h: commodity avg `-0.0314` n `13`; crypto_alt avg `0.921` n `237`; crypto_major avg `0.6134` n `8`; equity avg `0.165` n `152`; fx avg `-0.012` n `6`; index avg `0.0186` n `26`; metal avg `-0.0007` n `20`; unknown avg `0.3474` n `1231`
- 4h: commodity avg `-0.1143` n `13`; crypto_alt avg `1.1723` n `237`; crypto_major avg `0.7202` n `8`; equity avg `0.403` n `152`; fx avg `0.0046` n `6`; index avg `0.0574` n `26`; metal avg `0.0648` n `20`; unknown avg `212.9616` n `1225`
- 24h: commodity avg `-0.2124` n `13`; crypto_alt avg `1.3882` n `237`; crypto_major avg `2.2531` n `8`; equity avg `0.9213` n `152`; fx avg `-0.0006` n `6`; index avg `0.1643` n `26`; metal avg `0.1405` n `20`; unknown avg `10.5681` n `1081`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2229`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1781`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.169`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1685`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1565`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1429`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1412`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1367`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
