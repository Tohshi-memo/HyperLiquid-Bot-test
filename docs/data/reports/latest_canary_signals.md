# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T11:43:00.261667+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1759` n `12`; crypto_alt avg `0.2821` n `228`; crypto_major avg `0.1862` n `8`; equity avg `0.1575` n `74`; fx avg `-0.002` n `6`; index avg `-0.01` n `23`; metal avg `-0.0138` n `18`; unknown avg `0.0889` n `547`
- 1h: commodity avg `0.1766` n `12`; crypto_alt avg `0.2462` n `228`; crypto_major avg `-0.0193` n `8`; equity avg `0.2711` n `74`; fx avg `0.0363` n `6`; index avg `0.1042` n `23`; metal avg `0.0548` n `18`; unknown avg `-0.1391` n `547`
- 4h: commodity avg `0.005` n `12`; crypto_alt avg `-0.3142` n `228`; crypto_major avg `-0.5674` n `8`; equity avg `0.3258` n `74`; fx avg `0.1982` n `6`; index avg `0.3555` n `23`; metal avg `0.4931` n `18`; unknown avg `-0.23` n `547`
- 24h: commodity avg `-0.2308` n `12`; crypto_alt avg `-1.5754` n `228`; crypto_major avg `-1.0121` n `8`; equity avg `1.3993` n `74`; fx avg `0.1006` n `6`; index avg `0.7304` n `23`; metal avg `0.364` n `18`; unknown avg `-3.1387` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1154`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0591`, n `668`, weak_sample_signal
