# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T03:52:27.447814+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0684` n `12`; crypto_alt avg `0.1731` n `228`; crypto_major avg `0.069` n `8`; equity avg `-0.0428` n `74`; fx avg `-0.0163` n `6`; index avg `0.0067` n `23`; metal avg `-0.0322` n `18`; unknown avg `0.3648` n `643`
- 1h: commodity avg `0.003` n `12`; crypto_alt avg `0.0516` n `228`; crypto_major avg `-0.1838` n `8`; equity avg `-0.2112` n `74`; fx avg `-0.0275` n `6`; index avg `0.0039` n `23`; metal avg `-0.0514` n `18`; unknown avg `0.1153` n `643`
- 4h: commodity avg `0.0265` n `12`; crypto_alt avg `0.7956` n `228`; crypto_major avg `-0.1194` n `8`; equity avg `-0.1332` n `74`; fx avg `-0.0086` n `6`; index avg `0.2192` n `23`; metal avg `-0.0195` n `18`; unknown avg `-0.306` n `643`
- 24h: commodity avg `-0.784` n `12`; crypto_alt avg `0.1575` n `228`; crypto_major avg `-0.3223` n `8`; equity avg `-0.8195` n `74`; fx avg `-0.0244` n `6`; index avg `0.6896` n `23`; metal avg `0.2524` n `18`; unknown avg `40.0658` n `515`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0556`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0547`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0545`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0535`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0511`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0497`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0485`, n `668`, weak_sample_signal
