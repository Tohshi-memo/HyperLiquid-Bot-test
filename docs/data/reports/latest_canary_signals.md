# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T10:37:42.339565+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0002` n `13`; crypto_alt avg `0.1084` n `237`; crypto_major avg `0.121` n `8`; equity avg `0.0257` n `152`; fx avg `0.0056` n `6`; index avg `-0.0058` n `26`; metal avg `-0.0357` n `20`; unknown avg `2.5709` n `1240`
- 1h: commodity avg `-0.0203` n `13`; crypto_alt avg `-0.1697` n `237`; crypto_major avg `-0.0065` n `8`; equity avg `-0.1166` n `152`; fx avg `0.0026` n `6`; index avg `-0.0417` n `26`; metal avg `-0.0545` n `20`; unknown avg `27.7123` n `1240`
- 4h: commodity avg `0.0877` n `13`; crypto_alt avg `0.6798` n `237`; crypto_major avg `0.5283` n `8`; equity avg `0.2531` n `152`; fx avg `0.0126` n `6`; index avg `0.0753` n `26`; metal avg `0.0765` n `20`; unknown avg `20.1987` n `1142`
- 24h: commodity avg `-0.4612` n `13`; crypto_alt avg `0.6632` n `237`; crypto_major avg `0.569` n `8`; equity avg `-0.1368` n `152`; fx avg `0.0581` n `6`; index avg `0.0306` n `26`; metal avg `0.1778` n `20`; unknown avg `-0.1408` n `977`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2649`, n `668`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.2317`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2308`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.2064`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1598`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1543`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.151`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1508`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
