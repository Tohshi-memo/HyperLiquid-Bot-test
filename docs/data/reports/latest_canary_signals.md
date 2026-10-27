# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T09:52:29.993871+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.078` n `13`; crypto_alt avg `-0.2767` n `238`; crypto_major avg `-0.1287` n `8`; equity avg `0.0708` n `154`; fx avg `0.0052` n `6`; index avg `0.0069` n `27`; metal avg `0.0012` n `20`; unknown avg `0.8517` n `1238`
- 1h: commodity avg `-0.1588` n `13`; crypto_alt avg `-0.5048` n `238`; crypto_major avg `-0.2155` n `8`; equity avg `0.3185` n `154`; fx avg `-0.0284` n `6`; index avg `0.0226` n `27`; metal avg `0.0764` n `20`; unknown avg `5.5647` n `1236`
- 4h: commodity avg `0.1716` n `13`; crypto_alt avg `-0.608` n `237`; crypto_major avg `-0.4619` n `8`; equity avg `0.1926` n `154`; fx avg `-0.0166` n `6`; index avg `0.0389` n `27`; metal avg `-0.1096` n `20`; unknown avg `-0.3735` n `1174`
- 24h: commodity avg `0.0966` n `13`; crypto_alt avg `-0.9265` n `237`; crypto_major avg `-0.6072` n `8`; equity avg `0.4906` n `153`; fx avg `-0.0568` n `6`; index avg `0.26` n `27`; metal avg `-0.4006` n `20`; unknown avg `1048.701` n `1038`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2048`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1952`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1886`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1356`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1306`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1279`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1188`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
