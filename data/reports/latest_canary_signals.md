# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T13:37:32.261266+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0745` n `13`; crypto_alt avg `-0.0435` n `237`; crypto_major avg `-0.0408` n `8`; equity avg `-0.0286` n `152`; fx avg `0.0002` n `6`; index avg `0.0007` n `26`; metal avg `0.004` n `20`; unknown avg `1.4445` n `1231`
- 1h: commodity avg `-0.0774` n `13`; crypto_alt avg `-0.0166` n `237`; crypto_major avg `-0.0333` n `8`; equity avg `0.1268` n `152`; fx avg `-0.0072` n `6`; index avg `0.0242` n `26`; metal avg `0.0127` n `20`; unknown avg `2.4122` n `1231`
- 4h: commodity avg `-0.1012` n `13`; crypto_alt avg `0.5097` n `237`; crypto_major avg `0.3877` n `8`; equity avg `0.4038` n `152`; fx avg `0.0284` n `6`; index avg `0.0288` n `26`; metal avg `0.062` n `20`; unknown avg `8.2817` n `1199`
- 24h: commodity avg `-0.1954` n `13`; crypto_alt avg `-1.0074` n `237`; crypto_major avg `-0.0279` n `8`; equity avg `0.2243` n `152`; fx avg `0.006` n `6`; index avg `0.0601` n `26`; metal avg `-0.0159` n `20`; unknown avg `18.2593` n `1080`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2238`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1797`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1728`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1701`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1608`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1482`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1433`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1419`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1235`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1198`, n `668`, weak_sample_signal
