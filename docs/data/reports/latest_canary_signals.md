# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T22:52:28.150087+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0136` n `12`; crypto_alt avg `-0.1223` n `228`; crypto_major avg `-0.0387` n `8`; equity avg `0.1584` n `74`; fx avg `-0.0271` n `6`; index avg `0.0169` n `23`; metal avg `0.275` n `18`; unknown avg `-0.1434` n `556`
- 1h: commodity avg `-0.1553` n `12`; crypto_alt avg `-0.3321` n `228`; crypto_major avg `-0.0523` n `8`; equity avg `0.409` n `74`; fx avg `0.006` n `6`; index avg `0.2757` n `23`; metal avg `0.4021` n `18`; unknown avg `0.7983` n `556`
- 4h: commodity avg `-1.1754` n `12`; crypto_alt avg `0.0854` n `228`; crypto_major avg `0.032` n `8`; equity avg `1.3679` n `74`; fx avg `0.0494` n `6`; index avg `0.7497` n `23`; metal avg `1.0857` n `18`; unknown avg `0.8538` n `556`
- 24h: commodity avg `-2.9547` n `12`; crypto_alt avg `4.6603` n `228`; crypto_major avg `4.5092` n `8`; equity avg `5.1115` n `74`; fx avg `0.1191` n `6`; index avg `2.8138` n `23`; metal avg `4.0989` n `18`; unknown avg `2.1228` n `530`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1616`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1152`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
