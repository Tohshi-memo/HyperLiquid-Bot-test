# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T16:22:28.611444+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `2.094` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0194` n `12`; crypto_alt avg `0.26` n `228`; crypto_major avg `0.1601` n `8`; equity avg `0.2205` n `74`; fx avg `0.0002` n `6`; index avg `0.0565` n `23`; metal avg `-0.0818` n `18`; unknown avg `0.0079` n `517`
- 1h: commodity avg `-0.0291` n `12`; crypto_alt avg `0.0369` n `228`; crypto_major avg `-0.1064` n `8`; equity avg `-0.0355` n `74`; fx avg `-0.0196` n `6`; index avg `-0.0746` n `23`; metal avg `-0.1437` n `18`; unknown avg `0.0342` n `517`
- 4h: commodity avg `0.0925` n `12`; crypto_alt avg `1.3105` n `228`; crypto_major avg `1.882` n `8`; equity avg `1.0358` n `74`; fx avg `0.0039` n `6`; index avg `0.3376` n `23`; metal avg `-0.212` n `18`; unknown avg `0.5828` n `517`
- 24h: commodity avg `-0.575` n `12`; crypto_alt avg `2.6406` n `228`; crypto_major avg `3.7829` n `8`; equity avg `2.5712` n `74`; fx avg `-0.2723` n `6`; index avg `1.2192` n `23`; metal avg `0.083` n `18`; unknown avg `-3.0058` n `506`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
