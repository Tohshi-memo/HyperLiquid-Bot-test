# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T03:07:27.232684+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0137` n `12`; crypto_alt avg `0.1098` n `228`; crypto_major avg `0.1811` n `8`; equity avg `0.1163` n `74`; fx avg `-0.021` n `6`; index avg `0.0989` n `23`; metal avg `0.2442` n `18`; unknown avg `-0.1493` n `550`
- 1h: commodity avg `0.0482` n `12`; crypto_alt avg `-0.3582` n `228`; crypto_major avg `-0.2024` n `8`; equity avg `-0.2934` n `74`; fx avg `-0.0406` n `6`; index avg `-0.036` n `23`; metal avg `-0.5385` n `18`; unknown avg `-0.1956` n `550`
- 4h: commodity avg `-0.4318` n `12`; crypto_alt avg `1.7813` n `228`; crypto_major avg `1.5585` n `8`; equity avg `1.1161` n `74`; fx avg `0.1453` n `6`; index avg `0.5593` n `23`; metal avg `0.7614` n `18`; unknown avg `0.6629` n `550`
- 24h: commodity avg `1.413` n `12`; crypto_alt avg `-0.426` n `228`; crypto_major avg `-0.2031` n `8`; equity avg `-1.2124` n `74`; fx avg `0.0437` n `6`; index avg `-1.0635` n `23`; metal avg `-0.7143` n `18`; unknown avg `-0.0048` n `537`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1571`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
