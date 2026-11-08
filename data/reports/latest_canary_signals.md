# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T18:52:27.119616+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0384` n `13`; crypto_alt avg `0.0617` n `239`; crypto_major avg `0.0093` n `8`; equity avg `-0.0175` n `158`; fx avg `-0.0066` n `6`; index avg `0.0097` n `27`; metal avg `0.0045` n `20`; unknown avg `1.4419` n `1260`
- 1h: commodity avg `-0.1484` n `13`; crypto_alt avg `0.7133` n `239`; crypto_major avg `0.3821` n `8`; equity avg `0.3941` n `158`; fx avg `-0.0217` n `6`; index avg `0.0335` n `27`; metal avg `0.0102` n `20`; unknown avg `3.514` n `1208`
- 4h: commodity avg `-0.1421` n `13`; crypto_alt avg `-0.0094` n `239`; crypto_major avg `-0.1822` n `8`; equity avg `0.2578` n `158`; fx avg `0.0146` n `6`; index avg `0.0252` n `27`; metal avg `-0.0073` n `20`; unknown avg `1.5491` n `1194`
- 24h: commodity avg `-0.0618` n `13`; crypto_alt avg `-1.5654` n `239`; crypto_major avg `-0.1927` n `8`; equity avg `0.3772` n `158`; fx avg `0.0477` n `6`; index avg `0.0064` n `27`; metal avg `-0.0335` n `20`; unknown avg `0.5168` n `1046`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.207`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1587`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.148`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
