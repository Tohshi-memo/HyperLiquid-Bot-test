# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T23:32:55.035355+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0406` n `12`; crypto_alt avg `0.0353` n `228`; crypto_major avg `0.0168` n `8`; equity avg `0.054` n `74`; fx avg `-0.0012` n `6`; index avg `0.0225` n `23`; metal avg `0.0321` n `18`; unknown avg `0.0145` n `515`
- 1h: commodity avg `0.0434` n `12`; crypto_alt avg `0.1766` n `228`; crypto_major avg `0.2391` n `8`; equity avg `0.2164` n `74`; fx avg `-0.0113` n `6`; index avg `0.0588` n `23`; metal avg `0.0146` n `18`; unknown avg `0.1592` n `515`
- 4h: commodity avg `0.3429` n `12`; crypto_alt avg `0.4048` n `228`; crypto_major avg `0.2441` n `8`; equity avg `0.2793` n `74`; fx avg `-0.0521` n `6`; index avg `0.1471` n `23`; metal avg `0.0072` n `18`; unknown avg `1.9674` n `515`
- 24h: commodity avg `0.4416` n `12`; crypto_alt avg `-0.6415` n `228`; crypto_major avg `-0.8213` n `8`; equity avg `-0.2277` n `74`; fx avg `0.0127` n `6`; index avg `0.157` n `23`; metal avg `-0.3913` n `18`; unknown avg `-0.1202` n `401`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0583`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0582`, n `668`, weak_sample_signal
