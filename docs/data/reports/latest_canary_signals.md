# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T06:07:24.125381+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0083` n `12`; crypto_alt avg `-0.0755` n `230`; crypto_major avg `-0.0359` n `8`; equity avg `-0.1488` n `113`; fx avg `0.0104` n `6`; index avg `-0.0315` n `25`; metal avg `-0.0689` n `20`; unknown avg `-0.0384` n `755`
- 1h: commodity avg `0.0097` n `12`; crypto_alt avg `0.0388` n `230`; crypto_major avg `0.1344` n `8`; equity avg `-0.2063` n `113`; fx avg `0.0129` n `6`; index avg `-0.048` n `25`; metal avg `-0.1213` n `20`; unknown avg `-0.0318` n `755`
- 4h: commodity avg `0.1776` n `12`; crypto_alt avg `0.4673` n `230`; crypto_major avg `0.8142` n `8`; equity avg `-0.1284` n `113`; fx avg `0.0078` n `6`; index avg `-0.0362` n `25`; metal avg `-0.2033` n `20`; unknown avg `0.6322` n `754`
- 24h: commodity avg `-0.1274` n `12`; crypto_alt avg `-0.8755` n `230`; crypto_major avg `0.3923` n `8`; equity avg `2.3615` n `113`; fx avg `-0.0385` n `6`; index avg `0.2591` n `25`; metal avg `-0.1954` n `20`; unknown avg `0.1263` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2453`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2135`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.193`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.19`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1863`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1684`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1638`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.145`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1446`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
