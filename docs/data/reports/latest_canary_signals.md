# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T10:37:25.148600+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2416` n `12`; crypto_alt avg `0.4308` n `228`; crypto_major avg `0.1162` n `8`; equity avg `0.1908` n `74`; fx avg `0.024` n `6`; index avg `0.0985` n `23`; metal avg `0.2843` n `18`; unknown avg `0.0431` n `517`
- 1h: commodity avg `-0.1576` n `12`; crypto_alt avg `0.4338` n `228`; crypto_major avg `0.0743` n `8`; equity avg `0.1361` n `74`; fx avg `0.0604` n `6`; index avg `0.162` n `23`; metal avg `0.122` n `18`; unknown avg `-0.177` n `517`
- 4h: commodity avg `-0.4495` n `12`; crypto_alt avg `0.696` n `228`; crypto_major avg `0.2098` n `8`; equity avg `0.917` n `74`; fx avg `-0.0164` n `6`; index avg `0.4873` n `23`; metal avg `0.329` n `18`; unknown avg `-0.2191` n `517`
- 24h: commodity avg `0.5854` n `12`; crypto_alt avg `0.971` n `228`; crypto_major avg `1.7892` n `8`; equity avg `1.2875` n `74`; fx avg `-0.2995` n `6`; index avg `0.6458` n `23`; metal avg `-0.5635` n `18`; unknown avg `-2.4977` n `506`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1252`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1249`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1242`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
