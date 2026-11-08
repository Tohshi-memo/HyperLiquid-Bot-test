# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T13:07:26.869279+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0046` n `13`; crypto_alt avg `0.0731` n `239`; crypto_major avg `0.1085` n `8`; equity avg `0.0812` n `158`; fx avg `0.0176` n `6`; index avg `-0.0017` n `27`; metal avg `0.0003` n `20`; unknown avg `-0.0387` n `1258`
- 1h: commodity avg `0.0153` n `13`; crypto_alt avg `-0.3066` n `239`; crypto_major avg `0.0451` n `8`; equity avg `0.0719` n `158`; fx avg `0.0143` n `6`; index avg `-0.0081` n `27`; metal avg `-0.0056` n `20`; unknown avg `0.3336` n `1256`
- 4h: commodity avg `0.0265` n `13`; crypto_alt avg `-0.1497` n `239`; crypto_major avg `0.2367` n `8`; equity avg `0.2226` n `158`; fx avg `0.0169` n `6`; index avg `-0.0062` n `27`; metal avg `-0.006` n `20`; unknown avg `218.9079` n `1170`
- 24h: commodity avg `0.1409` n `13`; crypto_alt avg `-1.3249` n `239`; crypto_major avg `0.1033` n `8`; equity avg `0.1482` n `158`; fx avg `0.0173` n `6`; index avg `0.013` n `27`; metal avg `-0.0336` n `20`; unknown avg `5.6263` n `1097`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1614`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1505`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
