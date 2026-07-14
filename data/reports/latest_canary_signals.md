# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T06:07:28.468631+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0846` n `12`; crypto_alt avg `0.0119` n `230`; crypto_major avg `-0.1134` n `8`; equity avg `0.1686` n `92`; fx avg `-0.0143` n `6`; index avg `0.0156` n `25`; metal avg `-0.0225` n `20`; unknown avg `-0.0023` n `750`
- 1h: commodity avg `-0.0664` n `12`; crypto_alt avg `0.1134` n `230`; crypto_major avg `-0.0889` n `8`; equity avg `0.3571` n `92`; fx avg `0.0253` n `6`; index avg `0.0468` n `25`; metal avg `0.0775` n `20`; unknown avg `0.0422` n `750`
- 4h: commodity avg `0.0541` n `12`; crypto_alt avg `0.2013` n `230`; crypto_major avg `0.1217` n `8`; equity avg `0.6661` n `92`; fx avg `-0.0203` n `6`; index avg `0.1706` n `25`; metal avg `0.2806` n `20`; unknown avg `-0.0102` n `750`
- 24h: commodity avg `0.8664` n `12`; crypto_alt avg `-0.4694` n `230`; crypto_major avg `-0.6212` n `8`; equity avg `-0.3958` n `92`; fx avg `-0.2154` n `6`; index avg `0.0074` n `25`; metal avg `0.2401` n `20`; unknown avg `-0.0624` n `750`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1778`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1616`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
