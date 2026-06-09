# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T10:52:29.434103+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0679` n `12`; crypto_alt avg `0.2379` n `228`; crypto_major avg `0.1889` n `8`; equity avg `0.0405` n `74`; fx avg `0.0131` n `6`; index avg `0.0093` n `23`; metal avg `-0.0617` n `18`; unknown avg `-0.176` n `547`
- 1h: commodity avg `0.1099` n `12`; crypto_alt avg `0.1812` n `228`; crypto_major avg `0.0696` n `8`; equity avg `-0.1078` n `74`; fx avg `0.0608` n `6`; index avg `-0.037` n `23`; metal avg `0.0838` n `18`; unknown avg `-0.0669` n `547`
- 4h: commodity avg `-0.131` n `12`; crypto_alt avg `-0.4022` n `228`; crypto_major avg `-0.5509` n `8`; equity avg `-0.009` n `74`; fx avg `0.1846` n `6`; index avg `0.2307` n `23`; metal avg `0.2071` n `18`; unknown avg `0.0208` n `547`
- 24h: commodity avg `-1.1482` n `12`; crypto_alt avg `-0.468` n `228`; crypto_major avg `0.3719` n `8`; equity avg `2.1529` n `74`; fx avg `0.0912` n `6`; index avg `1.0834` n `23`; metal avg `1.0238` n `18`; unknown avg `-2.8758` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.054`, n `668`, weak_sample_signal
