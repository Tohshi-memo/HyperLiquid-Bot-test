# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T02:52:26.479062+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0599` n `13`; crypto_alt avg `0.0549` n `234`; crypto_major avg `-0.0284` n `8`; equity avg `0.0124` n `142`; fx avg `-0.0038` n `6`; index avg `0.0088` n `26`; metal avg `0.0065` n `20`; unknown avg `0.0299` n `974`
- 1h: commodity avg `0.1558` n `13`; crypto_alt avg `0.2523` n `234`; crypto_major avg `-0.118` n `8`; equity avg `0.2269` n `142`; fx avg `-0.0303` n `6`; index avg `0.0701` n `26`; metal avg `-0.0344` n `20`; unknown avg `-0.1255` n `972`
- 4h: commodity avg `-0.0905` n `13`; crypto_alt avg `0.0206` n `234`; crypto_major avg `-0.4133` n `8`; equity avg `0.3323` n `142`; fx avg `0.1003` n `6`; index avg `0.1224` n `26`; metal avg `0.0095` n `20`; unknown avg `1.0779` n `942`
- 24h: commodity avg `0.0111` n `13`; crypto_alt avg `0.4714` n `234`; crypto_major avg `0.3778` n `8`; equity avg `0.2382` n `142`; fx avg `0.2267` n `6`; index avg `0.1464` n `26`; metal avg `-0.2004` n `20`; unknown avg `777.088` n `796`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.151`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1304`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
