# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T06:22:29.021133+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.019` n `12`; crypto_alt avg `-0.0089` n `230`; crypto_major avg `-0.0261` n `8`; equity avg `-0.1929` n `108`; fx avg `0.0094` n `6`; index avg `-0.0332` n `25`; metal avg `0.04` n `20`; unknown avg `0.0724` n `781`
- 1h: commodity avg `0.0045` n `12`; crypto_alt avg `-0.0075` n `230`; crypto_major avg `-0.0969` n `8`; equity avg `-0.1657` n `108`; fx avg `-0.0123` n `6`; index avg `-0.0108` n `25`; metal avg `0.2421` n `20`; unknown avg `0.051` n `749`
- 4h: commodity avg `0.0495` n `12`; crypto_alt avg `0.2938` n `230`; crypto_major avg `0.0735` n `8`; equity avg `0.5247` n `108`; fx avg `0.0345` n `6`; index avg `0.0446` n `25`; metal avg `0.4911` n `20`; unknown avg `0.0673` n `749`
- 24h: commodity avg `-1.4187` n `12`; crypto_alt avg `0.4575` n `230`; crypto_major avg `0.7614` n `8`; equity avg `3.5593` n `108`; fx avg `-0.0052` n `6`; index avg `0.7181` n `25`; metal avg `1.2544` n `20`; unknown avg `0.4765` n `748`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.148`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1411`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1262`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1246`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
