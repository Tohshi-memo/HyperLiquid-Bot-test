# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T09:37:34.813804+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0359` n `13`; crypto_alt avg `0.046` n `239`; crypto_major avg `0.066` n `8`; equity avg `0.2687` n `158`; fx avg `-0.0187` n `6`; index avg `0.0501` n `27`; metal avg `0.0133` n `20`; unknown avg `0.2516` n `1249`
- 1h: commodity avg `0.1146` n `13`; crypto_alt avg `-0.1657` n `239`; crypto_major avg `-0.2919` n `8`; equity avg `-0.0442` n `158`; fx avg `-0.0138` n `6`; index avg `-0.0433` n `27`; metal avg `0.0257` n `20`; unknown avg `1.0328` n `1189`
- 4h: commodity avg `0.2938` n `13`; crypto_alt avg `0.3103` n `239`; crypto_major avg `0.1324` n `8`; equity avg `0.431` n `158`; fx avg `-0.0508` n `6`; index avg `0.0655` n `27`; metal avg `0.102` n `20`; unknown avg `0.2014` n `1149`
- 24h: commodity avg `-1.6228` n `13`; crypto_alt avg `0.9381` n `239`; crypto_major avg `1.7743` n `8`; equity avg `-2.7538` n `158`; fx avg `-0.064` n `6`; index avg `-0.2448` n `27`; metal avg `0.6125` n `20`; unknown avg `0.51` n `1078`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2452`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1904`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1868`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1548`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1414`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1309`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1286`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
