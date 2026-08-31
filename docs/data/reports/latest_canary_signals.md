# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T20:07:33.898402+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0092` n `12`; crypto_alt avg `0.0424` n `232`; crypto_major avg `0.054` n `8`; equity avg `-0.0418` n `129`; fx avg `-0.0032` n `6`; index avg `-0.0109` n `26`; metal avg `-0.0176` n `20`; unknown avg `0.5421` n `783`
- 1h: commodity avg `0.05` n `12`; crypto_alt avg `-0.3074` n `232`; crypto_major avg `-0.24` n `8`; equity avg `0.4122` n `129`; fx avg `-0.0036` n `6`; index avg `0.091` n `26`; metal avg `0.1225` n `20`; unknown avg `1.6557` n `783`
- 4h: commodity avg `0.0723` n `12`; crypto_alt avg `0.6262` n `232`; crypto_major avg `0.7417` n `8`; equity avg `0.6281` n `129`; fx avg `0.0013` n `6`; index avg `0.0887` n `26`; metal avg `0.1083` n `20`; unknown avg `-0.3576` n `783`
- 24h: commodity avg `0.2448` n `12`; crypto_alt avg `-0.9859` n `231`; crypto_major avg `-0.8328` n `8`; equity avg `-0.0597` n `129`; fx avg `-0.0909` n `6`; index avg `-0.1655` n `26`; metal avg `-0.4288` n `20`; unknown avg `-0.053` n `750`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0578`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0571`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0553`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0518`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0505`, n `668`, weak_sample_signal
