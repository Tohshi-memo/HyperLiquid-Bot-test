# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T15:52:29.144059+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0228` n `12`; crypto_alt avg `-0.0072` n `230`; crypto_major avg `0.0088` n `8`; equity avg `-0.0165` n `102`; fx avg `-0.0176` n `6`; index avg `0.0016` n `25`; metal avg `-0.0021` n `20`; unknown avg `-0.0533` n `782`
- 1h: commodity avg `0.0412` n `12`; crypto_alt avg `-0.1254` n `230`; crypto_major avg `-0.0782` n `8`; equity avg `-0.0676` n `102`; fx avg `-0.0156` n `6`; index avg `0.0031` n `25`; metal avg `0.0235` n `20`; unknown avg `-0.0627` n `782`
- 4h: commodity avg `0.0323` n `12`; crypto_alt avg `-0.0049` n `230`; crypto_major avg `0.0968` n `8`; equity avg `-0.2175` n `102`; fx avg `0.0137` n `6`; index avg `0.0117` n `25`; metal avg `0.0157` n `20`; unknown avg `-0.1554` n `781`
- 24h: commodity avg `0.7644` n `12`; crypto_alt avg `0.3906` n `230`; crypto_major avg `-0.3134` n `8`; equity avg `-0.1944` n `102`; fx avg `-0.0779` n `6`; index avg `0.0299` n `25`; metal avg `0.0217` n `20`; unknown avg `4.1138` n `764`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
