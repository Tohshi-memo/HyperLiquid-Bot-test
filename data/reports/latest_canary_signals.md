# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T03:52:25.403881+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0125` n `12`; crypto_alt avg `0.1339` n `228`; crypto_major avg `-0.0552` n `8`; equity avg `-0.1007` n `74`; fx avg `0.0152` n `6`; index avg `-0.0046` n `23`; metal avg `0.111` n `18`; unknown avg `14.0618` n `517`
- 1h: commodity avg `-0.0237` n `12`; crypto_alt avg `0.0288` n `228`; crypto_major avg `-0.1848` n `8`; equity avg `-0.2245` n `74`; fx avg `0.0074` n `6`; index avg `0.0609` n `23`; metal avg `-0.065` n `18`; unknown avg `4.1205` n `517`
- 4h: commodity avg `0.2704` n `12`; crypto_alt avg `-0.0106` n `228`; crypto_major avg `0.2587` n `8`; equity avg `0.8741` n `74`; fx avg `-0.028` n `6`; index avg `0.3757` n `23`; metal avg `-0.4661` n `18`; unknown avg `-0.2826` n `517`
- 24h: commodity avg `0.3517` n `12`; crypto_alt avg `1.343` n `228`; crypto_major avg `3.4811` n `8`; equity avg `1.6297` n `74`; fx avg `-0.0896` n `6`; index avg `0.2752` n `23`; metal avg `-0.2309` n `18`; unknown avg `-5.3896` n `506`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0666`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
