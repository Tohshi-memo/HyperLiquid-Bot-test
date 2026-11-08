# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T11:37:26.364075+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0049` n `13`; crypto_alt avg `-0.1959` n `239`; crypto_major avg `-0.1172` n `8`; equity avg `0.0025` n `158`; fx avg `0.0026` n `6`; index avg `0.0015` n `27`; metal avg `0.0002` n `20`; unknown avg `0.2582` n `1262`
- 1h: commodity avg `-0.0198` n `13`; crypto_alt avg `0.3056` n `239`; crypto_major avg `0.3193` n `8`; equity avg `0.1053` n `158`; fx avg `0.006` n `6`; index avg `0.0092` n `27`; metal avg `0.0025` n `20`; unknown avg `-0.124` n `1256`
- 4h: commodity avg `0.0002` n `13`; crypto_alt avg `-0.0999` n `239`; crypto_major avg `0.1336` n `8`; equity avg `0.232` n `158`; fx avg `-0.0008` n `6`; index avg `0.0052` n `27`; metal avg `0.0049` n `20`; unknown avg `220.7988` n `1160`
- 24h: commodity avg `0.0824` n `13`; crypto_alt avg `-1.1311` n `239`; crypto_major avg `-0.37` n `8`; equity avg `0.1999` n `158`; fx avg `0.0574` n `6`; index avg `0.0371` n `27`; metal avg `-0.0301` n `20`; unknown avg `5.5572` n `1097`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1609`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1546`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
