# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T23:52:28.037837+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0119` n `12`; crypto_alt avg `-0.3791` n `230`; crypto_major avg `-0.3593` n `8`; equity avg `0.1555` n `102`; fx avg `-0.0015` n `6`; index avg `0.0337` n `25`; metal avg `0.019` n `20`; unknown avg `0.4319` n `779`
- 1h: commodity avg `0.0151` n `12`; crypto_alt avg `-0.1482` n `230`; crypto_major avg `-0.1997` n `8`; equity avg `0.2729` n `102`; fx avg `0.0173` n `6`; index avg `0.0202` n `25`; metal avg `-0.0131` n `20`; unknown avg `-0.0858` n `779`
- 4h: commodity avg `0.054` n `12`; crypto_alt avg `-0.1681` n `230`; crypto_major avg `-0.0901` n `8`; equity avg `1.3035` n `102`; fx avg `0.0403` n `6`; index avg `0.1444` n `25`; metal avg `0.0021` n `20`; unknown avg `-0.3171` n `779`
- 24h: commodity avg `-0.0061` n `12`; crypto_alt avg `0.6758` n `230`; crypto_major avg `1.5061` n `8`; equity avg `7.7438` n `102`; fx avg `-0.3634` n `6`; index avg `0.9139` n `25`; metal avg `0.4753` n `20`; unknown avg `0.0726` n `738`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1451`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1409`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0825`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0606`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
