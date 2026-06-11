# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T03:37:39.933184+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1045` n `12`; crypto_alt avg `0.4415` n `228`; crypto_major avg `0.4811` n `8`; equity avg `0.2954` n `74`; fx avg `0.0019` n `6`; index avg `0.108` n `23`; metal avg `0.2157` n `18`; unknown avg `0.4244` n `550`
- 1h: commodity avg `0.1822` n `12`; crypto_alt avg `0.4986` n `228`; crypto_major avg `0.5858` n `8`; equity avg `0.4247` n `74`; fx avg `-0.041` n `6`; index avg `0.1193` n `23`; metal avg `0.0111` n `18`; unknown avg `1.2647` n `550`
- 4h: commodity avg `-0.1163` n `12`; crypto_alt avg `1.6623` n `228`; crypto_major avg `1.4367` n `8`; equity avg `1.0314` n `74`; fx avg `0.0989` n `6`; index avg `0.4634` n `23`; metal avg `0.5475` n `18`; unknown avg `0.7956` n `550`
- 24h: commodity avg `1.5635` n `12`; crypto_alt avg `-0.0886` n `228`; crypto_major avg `-0.1187` n `8`; equity avg `-0.9956` n `74`; fx avg `0.0395` n `6`; index avg `-1.0307` n `23`; metal avg `-0.8102` n `18`; unknown avg `-0.0591` n `537`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1249`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
