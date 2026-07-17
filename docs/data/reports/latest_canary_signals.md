# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T16:37:29.214520+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0459` n `12`; crypto_alt avg `0.1063` n `230`; crypto_major avg `0.187` n `8`; equity avg `0.0773` n `96`; fx avg `0.0075` n `6`; index avg `0.0094` n `25`; metal avg `-0.0277` n `20`; unknown avg `-0.0466` n `769`
- 1h: commodity avg `0.1833` n `12`; crypto_alt avg `0.3355` n `230`; crypto_major avg `0.2959` n `8`; equity avg `0.8297` n `96`; fx avg `0.0133` n `6`; index avg `0.0488` n `25`; metal avg `0.0252` n `20`; unknown avg `-0.0261` n `769`
- 4h: commodity avg `0.2901` n `12`; crypto_alt avg `0.4743` n `230`; crypto_major avg `0.4125` n `8`; equity avg `1.8778` n `96`; fx avg `0.0999` n `6`; index avg `0.2315` n `25`; metal avg `0.3273` n `20`; unknown avg `-0.0781` n `769`
- 24h: commodity avg `0.6628` n `12`; crypto_alt avg `-1.6524` n `230`; crypto_major avg `-2.3368` n `8`; equity avg `-1.3259` n `94`; fx avg `0.0992` n `6`; index avg `-0.2891` n `25`; metal avg `-0.2235` n `20`; unknown avg `-0.3047` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1277`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
