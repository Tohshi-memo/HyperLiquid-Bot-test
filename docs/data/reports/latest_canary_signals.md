# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T08:52:29.125390+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.005` n `12`; crypto_alt avg `-0.14` n `228`; crypto_major avg `0.0347` n `8`; equity avg `-0.1032` n `86`; fx avg `0.0153` n `6`; index avg `-0.0159` n `23`; metal avg `-0.0328` n `20`; unknown avg `0.0956` n `765`
- 1h: commodity avg `-0.1323` n `12`; crypto_alt avg `-0.1766` n `228`; crypto_major avg `-0.2401` n `8`; equity avg `-0.1078` n `86`; fx avg `0.0414` n `6`; index avg `-0.0131` n `23`; metal avg `0.1348` n `20`; unknown avg `0.0963` n `765`
- 4h: commodity avg `0.0666` n `12`; crypto_alt avg `0.6875` n `228`; crypto_major avg `0.7701` n `8`; equity avg `0.1908` n `86`; fx avg `-0.0212` n `6`; index avg `0.016` n `23`; metal avg `0.0491` n `20`; unknown avg `0.2696` n `733`
- 24h: commodity avg `-0.3145` n `12`; crypto_alt avg `-1.1791` n `228`; crypto_major avg `-0.9224` n `8`; equity avg `-0.0415` n `86`; fx avg `-0.0088` n `6`; index avg `0.4854` n `23`; metal avg `-1.3597` n `20`; unknown avg `-0.5724` n `700`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0618`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0553`, n `668`, weak_sample_signal
