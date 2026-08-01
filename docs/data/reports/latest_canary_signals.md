# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T20:07:31.736532+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.049` n `12`; crypto_alt avg `0.0258` n `230`; crypto_major avg `0.0299` n `8`; equity avg `-0.016` n `102`; fx avg `0.0039` n `6`; index avg `-0.0005` n `25`; metal avg `-0.01` n `20`; unknown avg `-0.0182` n `782`
- 1h: commodity avg `0.1115` n `12`; crypto_alt avg `0.0792` n `230`; crypto_major avg `-0.0015` n `8`; equity avg `-0.0091` n `102`; fx avg `0.0051` n `6`; index avg `-0.0052` n `25`; metal avg `0.0056` n `20`; unknown avg `0.0844` n `782`
- 4h: commodity avg `0.1742` n `12`; crypto_alt avg `-0.9206` n `230`; crypto_major avg `-1.0564` n `8`; equity avg `-0.3039` n `102`; fx avg `0.0063` n `6`; index avg `-0.063` n `25`; metal avg `0.0089` n `20`; unknown avg `2.8265` n `782`
- 24h: commodity avg `0.6418` n `12`; crypto_alt avg `-0.6517` n `230`; crypto_major avg `-1.155` n `8`; equity avg `-0.7845` n `102`; fx avg `-0.1273` n `6`; index avg `-0.1017` n `25`; metal avg `-0.0165` n `20`; unknown avg `4.3459` n `764`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
