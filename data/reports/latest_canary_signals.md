# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T07:22:28.391494+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0658` n `12`; crypto_alt avg `0.1218` n `230`; crypto_major avg `0.0914` n `8`; equity avg `-0.1189` n `114`; fx avg `0.0144` n `6`; index avg `-0.0162` n `25`; metal avg `-0.0077` n `20`; unknown avg `-0.0252` n `794`
- 1h: commodity avg `-0.1407` n `12`; crypto_alt avg `0.0324` n `230`; crypto_major avg `0.1195` n `8`; equity avg `0.0032` n `114`; fx avg `-0.0071` n `6`; index avg `0.0225` n `25`; metal avg `-0.0292` n `20`; unknown avg `0.0511` n `793`
- 4h: commodity avg `-0.0738` n `12`; crypto_alt avg `0.5748` n `230`; crypto_major avg `0.5735` n `8`; equity avg `0.1962` n `114`; fx avg `0.0242` n `6`; index avg `-0.0288` n `25`; metal avg `0.0624` n `20`; unknown avg `0.0855` n `761`
- 24h: commodity avg `0.7223` n `12`; crypto_alt avg `-1.023` n `230`; crypto_major avg `0.1707` n `8`; equity avg `-1.5724` n `114`; fx avg `-0.0174` n `6`; index avg `-0.3974` n `25`; metal avg `-0.1462` n `20`; unknown avg `0.0142` n `760`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1567`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1559`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1278`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
