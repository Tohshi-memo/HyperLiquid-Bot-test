# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T02:22:27.669605+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0396` n `13`; crypto_alt avg `-0.1688` n `239`; crypto_major avg `-0.141` n `8`; equity avg `-0.0089` n `168`; fx avg `-0.0013` n `6`; index avg `-0.0051` n `27`; metal avg `0.013` n `20`; unknown avg `0.1278` n `1265`
- 1h: commodity avg `0.0427` n `13`; crypto_alt avg `-0.2632` n `239`; crypto_major avg `-0.0489` n `8`; equity avg `0.0575` n `168`; fx avg `-0.0081` n `6`; index avg `0.0014` n `27`; metal avg `0.0116` n `20`; unknown avg `1.1524` n `1257`
- 4h: commodity avg `-0.0734` n `13`; crypto_alt avg `0.2547` n `239`; crypto_major avg `0.7864` n `8`; equity avg `0.3418` n `168`; fx avg `-0.0081` n `6`; index avg `0.0343` n `27`; metal avg `0.016` n `20`; unknown avg `0.5694` n `1239`
- 24h: commodity avg `-0.7115` n `13`; crypto_alt avg `-0.7357` n `239`; crypto_major avg `-0.5975` n `8`; equity avg `1.8628` n `168`; fx avg `-0.1482` n `6`; index avg `0.1779` n `27`; metal avg `0.3154` n `20`; unknown avg `285.1794` n `989`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1409`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1356`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0617`, n `668`, weak_sample_signal
