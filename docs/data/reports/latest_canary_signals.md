# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T23:52:21.562626+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0862` n `12`; crypto_alt avg `0.1779` n `228`; crypto_major avg `0.1265` n `8`; equity avg `0.1448` n `74`; fx avg `0.0025` n `6`; index avg `-0.034` n `23`; metal avg `0.0368` n `18`; unknown avg `0.0423` n `515`
- 1h: commodity avg `0.0389` n `12`; crypto_alt avg `0.3777` n `228`; crypto_major avg `0.2794` n `8`; equity avg `0.3751` n `74`; fx avg `-0.0049` n `6`; index avg `0.0081` n `23`; metal avg `0.0355` n `18`; unknown avg `0.0603` n `515`
- 4h: commodity avg `0.0624` n `12`; crypto_alt avg `0.7627` n `228`; crypto_major avg `0.6566` n `8`; equity avg `0.426` n `74`; fx avg `-0.0402` n `6`; index avg `0.104` n `23`; metal avg `0.0417` n `18`; unknown avg `0.0228` n `515`
- 24h: commodity avg `0.5532` n `12`; crypto_alt avg `-0.9092` n `228`; crypto_major avg `-0.9885` n `8`; equity avg `-0.0528` n `74`; fx avg `0.0137` n `6`; index avg `0.0959` n `23`; metal avg `-0.3163` n `18`; unknown avg `-0.1206` n `401`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0585`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.058`, n `668`, weak_sample_signal
