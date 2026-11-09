# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T02:52:31.289806+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0641` n `13`; crypto_alt avg `-0.1464` n `239`; crypto_major avg `-0.1736` n `8`; equity avg `-0.056` n `158`; fx avg `-0.0064` n `6`; index avg `-0.0067` n `27`; metal avg `-0.0197` n `20`; unknown avg `-0.0804` n `1260`
- 1h: commodity avg `0.2043` n `13`; crypto_alt avg `0.0404` n `239`; crypto_major avg `-0.0531` n `8`; equity avg `0.469` n `158`; fx avg `-0.0543` n `6`; index avg `0.0252` n `27`; metal avg `0.0039` n `20`; unknown avg `-0.1473` n `1254`
- 4h: commodity avg `-0.0007` n `13`; crypto_alt avg `1.6451` n `239`; crypto_major avg `0.8621` n `8`; equity avg `1.6284` n `158`; fx avg `-0.0894` n `6`; index avg `0.2433` n `27`; metal avg `0.608` n `20`; unknown avg `1.7908` n `1228`
- 24h: commodity avg `0.0639` n `13`; crypto_alt avg `-1.19` n `239`; crypto_major avg `-1.7222` n `8`; equity avg `0.891` n `158`; fx avg `-0.0858` n `6`; index avg `0.0881` n `27`; metal avg `0.5092` n `20`; unknown avg `1.2658` n `992`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1674`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1547`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1539`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1511`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1413`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1197`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
