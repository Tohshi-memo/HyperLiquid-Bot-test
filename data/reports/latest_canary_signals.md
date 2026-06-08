# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T08:37:29.088848+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1665` n `12`; crypto_alt avg `0.1647` n `228`; crypto_major avg `0.1901` n `8`; equity avg `0.0343` n `74`; fx avg `-0.0021` n `6`; index avg `0.0207` n `23`; metal avg `-0.0451` n `18`; unknown avg `0.0872` n `517`
- 1h: commodity avg `-0.1107` n `12`; crypto_alt avg `-0.197` n `228`; crypto_major avg `-0.483` n `8`; equity avg `0.2659` n `74`; fx avg `-0.0428` n `6`; index avg `0.1008` n `23`; metal avg `-0.2971` n `18`; unknown avg `-0.0809` n `517`
- 4h: commodity avg `-0.2651` n `12`; crypto_alt avg `0.7963` n `228`; crypto_major avg `0.4398` n `8`; equity avg `0.2764` n `74`; fx avg `-0.2351` n `6`; index avg `0.1107` n `23`; metal avg `-0.3709` n `18`; unknown avg `-0.1141` n `507`
- 24h: commodity avg `0.7966` n `12`; crypto_alt avg `0.0806` n `228`; crypto_major avg `0.9998` n `8`; equity avg `0.9903` n `74`; fx avg `-0.3321` n `6`; index avg `0.1701` n `23`; metal avg `-0.8821` n `18`; unknown avg `-4.8967` n `506`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1301`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1271`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1264`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
