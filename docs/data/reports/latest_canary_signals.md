# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T20:52:26.734063+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0011` n `12`; crypto_alt avg `-0.0317` n `229`; crypto_major avg `-0.081` n `8`; equity avg `-0.0326` n `91`; fx avg `-0.0077` n `6`; index avg `-0.0155` n `25`; metal avg `-0.0073` n `20`; unknown avg `-0.1017` n `763`
- 1h: commodity avg `-0.0191` n `12`; crypto_alt avg `-0.0712` n `229`; crypto_major avg `-0.1583` n `8`; equity avg `-0.0421` n `91`; fx avg `-0.0047` n `6`; index avg `-0.0229` n `25`; metal avg `-0.0511` n `20`; unknown avg `-0.164` n `763`
- 4h: commodity avg `0.1492` n `12`; crypto_alt avg `-0.1846` n `229`; crypto_major avg `-0.1442` n `8`; equity avg `-0.4983` n `91`; fx avg `-0.0149` n `6`; index avg `-0.0634` n `25`; metal avg `0.0994` n `20`; unknown avg `-0.3822` n `763`
- 24h: commodity avg `0.0816` n `12`; crypto_alt avg `0.8261` n `229`; crypto_major avg `0.596` n `8`; equity avg `-0.6713` n `90`; fx avg `0.2161` n `6`; index avg `0.0097` n `25`; metal avg `-0.2134` n `20`; unknown avg `0.2979` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0612`, n `668`, weak_sample_signal
