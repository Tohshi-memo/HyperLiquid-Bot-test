# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T10:22:25.504745+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0622` n `12`; crypto_alt avg `-0.2975` n `228`; crypto_major avg `-0.2633` n `8`; equity avg `-0.249` n `74`; fx avg `0.0191` n `6`; index avg `-0.0542` n `23`; metal avg `-0.1246` n `18`; unknown avg `-0.2006` n `517`
- 1h: commodity avg `0.0342` n `12`; crypto_alt avg `-0.0816` n `228`; crypto_major avg `-0.0901` n `8`; equity avg `-0.1089` n `74`; fx avg `0.0342` n `6`; index avg `0.0022` n `23`; metal avg `-0.0962` n `18`; unknown avg `-0.1954` n `517`
- 4h: commodity avg `-0.1055` n `12`; crypto_alt avg `0.38` n `228`; crypto_major avg `0.0054` n `8`; equity avg `0.7987` n `74`; fx avg `-0.0672` n `6`; index avg `0.3413` n `23`; metal avg `-0.2374` n `18`; unknown avg `-0.4713` n `517`
- 24h: commodity avg `0.8497` n `12`; crypto_alt avg `0.3652` n `228`; crypto_major avg `1.4475` n `8`; equity avg `1.1243` n `74`; fx avg `-0.2902` n `6`; index avg `0.6025` n `23`; metal avg `-0.8486` n `18`; unknown avg `-2.5753` n `506`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.129`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.127`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1263`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
