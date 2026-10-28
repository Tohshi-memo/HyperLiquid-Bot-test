# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T17:37:40.991941+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.6` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0573` n `13`; crypto_alt avg `0.0579` n `238`; crypto_major avg `0.0855` n `8`; equity avg `-0.0102` n `155`; fx avg `-0.0057` n `6`; index avg `0.0043` n `27`; metal avg `-0.0045` n `20`; unknown avg `0.3161` n `1238`
- 1h: commodity avg `-0.1854` n `13`; crypto_alt avg `-0.1979` n `238`; crypto_major avg `0.079` n `8`; equity avg `-0.0189` n `155`; fx avg `-0.0146` n `6`; index avg `0.0093` n `27`; metal avg `-0.0139` n `20`; unknown avg `2.613` n `1232`
- 4h: commodity avg `0.0223` n `13`; crypto_alt avg `-0.5242` n `238`; crypto_major avg `-0.3359` n `8`; equity avg `0.1711` n `155`; fx avg `0.0773` n `6`; index avg `0.0106` n `27`; metal avg `-0.1126` n `20`; unknown avg `3.6227` n `1150`
- 24h: commodity avg `0.583` n `13`; crypto_alt avg `-0.4092` n `238`; crypto_major avg `-0.1807` n `8`; equity avg `0.9623` n `154`; fx avg `0.2504` n `6`; index avg `0.2453` n `27`; metal avg `-0.2163` n `20`; unknown avg `4.0825` n `1100`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1679`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1606`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1458`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1453`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
