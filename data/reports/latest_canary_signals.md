# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-10T04:22:16.578867+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0076` n `12`; crypto_alt avg `-0.0027` n `228`; crypto_major avg `-0.0161` n `8`; equity avg `0.0272` n `65`; fx avg `0.0` n `5`; index avg `-0.0047` n `23`; metal avg `0.0162` n `18`; unknown avg `-0.1548` n `376`
- 1h: commodity avg `-0.1055` n `12`; crypto_alt avg `0.0156` n `228`; crypto_major avg `0.093` n `8`; equity avg `0.1461` n `65`; fx avg `0.0013` n `5`; index avg `0.0155` n `23`; metal avg `0.1086` n `18`; unknown avg `-0.4777` n `376`
- 4h: commodity avg `-0.1292` n `12`; crypto_alt avg `-0.3001` n `228`; crypto_major avg `-0.1704` n `8`; equity avg `0.29` n `65`; fx avg `0.0028` n `5`; index avg `0.0915` n `23`; metal avg `0.1755` n `18`; unknown avg `-0.6189` n `376`
- 24h: commodity avg `0.1791` n `12`; crypto_alt avg `-1.6791` n `228`; crypto_major avg `-0.8426` n `8`; equity avg `0.9552` n `65`; fx avg `-0.0074` n `5`; index avg `0.297` n `23`; metal avg `0.33` n `18`; unknown avg `-0.5523` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1165`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
