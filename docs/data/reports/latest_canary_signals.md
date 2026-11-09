# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T10:37:29.773154+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0187` n `13`; crypto_alt avg `-0.2366` n `239`; crypto_major avg `-0.1994` n `8`; equity avg `-0.2409` n `158`; fx avg `0.0018` n `6`; index avg `-0.0223` n `27`; metal avg `-0.0327` n `20`; unknown avg `0.1161` n `1263`
- 1h: commodity avg `0.0071` n `13`; crypto_alt avg `-0.3278` n `239`; crypto_major avg `-0.6865` n `8`; equity avg `0.2511` n `158`; fx avg `-0.0009` n `6`; index avg `0.041` n `27`; metal avg `-0.0041` n `20`; unknown avg `-0.0769` n `1257`
- 4h: commodity avg `0.0656` n `13`; crypto_alt avg `0.5473` n `239`; crypto_major avg `-0.4744` n `8`; equity avg `0.3475` n `158`; fx avg `0.0816` n `6`; index avg `0.0335` n `27`; metal avg `-0.0438` n `20`; unknown avg `170.6505` n `1129`
- 24h: commodity avg `-0.1558` n `13`; crypto_alt avg `-1.6876` n `239`; crypto_major avg `-3.6301` n `8`; equity avg `-0.3053` n `158`; fx avg `-0.0933` n `6`; index avg `-0.027` n `27`; metal avg `0.2723` n `20`; unknown avg `0.2616` n `1028`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1779`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1636`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1477`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1306`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1189`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
