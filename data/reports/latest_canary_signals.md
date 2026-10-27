# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T10:07:28.326280+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0197` n `13`; crypto_alt avg `-0.1243` n `238`; crypto_major avg `-0.0843` n `8`; equity avg `-0.0881` n `154`; fx avg `0.0232` n `6`; index avg `-0.0212` n `27`; metal avg `0.0225` n `20`; unknown avg `0.2106` n `1234`
- 1h: commodity avg `-0.0242` n `13`; crypto_alt avg `-0.6994` n `238`; crypto_major avg `-0.4345` n `8`; equity avg `-0.0116` n `154`; fx avg `0.0124` n `6`; index avg `-0.0102` n `27`; metal avg `0.0115` n `20`; unknown avg `5.7504` n `1234`
- 4h: commodity avg `0.1318` n `13`; crypto_alt avg `-0.6531` n `237`; crypto_major avg `-0.4525` n `8`; equity avg `0.1183` n `154`; fx avg `-0.0002` n `6`; index avg `0.0042` n `27`; metal avg `-0.069` n `20`; unknown avg `-0.251` n `1188`
- 24h: commodity avg `0.0587` n `13`; crypto_alt avg `-0.9391` n `237`; crypto_major avg `-0.5967` n `8`; equity avg `0.5354` n `153`; fx avg `-0.0333` n `6`; index avg `0.262` n `27`; metal avg `-0.3419` n `20`; unknown avg `1045.9696` n `1040`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2045`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.193`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.187`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.135`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1308`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1282`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
