# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T14:37:30.491155+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2697` n `13`; crypto_alt avg `-0.0125` n `239`; crypto_major avg `0.0078` n `8`; equity avg `0.7411` n `158`; fx avg `0.0042` n `6`; index avg `0.1121` n `27`; metal avg `-0.0742` n `20`; unknown avg `0.2231` n `1263`
- 1h: commodity avg `0.1633` n `13`; crypto_alt avg `0.0055` n `239`; crypto_major avg `0.2245` n `8`; equity avg `0.9239` n `158`; fx avg `0.0274` n `6`; index avg `0.122` n `27`; metal avg `0.0074` n `20`; unknown avg `3.4487` n `1257`
- 4h: commodity avg `-0.2019` n `13`; crypto_alt avg `1.5554` n `239`; crypto_major avg `0.9538` n `8`; equity avg `1.5731` n `158`; fx avg `-0.0217` n `6`; index avg `0.2123` n `27`; metal avg `0.0946` n `20`; unknown avg `35.8102` n `1251`
- 24h: commodity avg `-0.2849` n `13`; crypto_alt avg `0.0833` n `239`; crypto_major avg `-3.0274` n `8`; equity avg `1.1515` n `158`; fx avg `-0.107` n `6`; index avg `0.1969` n `27`; metal avg `0.3733` n `20`; unknown avg `4.3471` n `1028`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1741`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.154`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1331`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1309`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1246`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
