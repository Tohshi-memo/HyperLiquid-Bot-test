# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T22:22:26.228199+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0043` n `12`; crypto_alt avg `0.1305` n `230`; crypto_major avg `0.1224` n `8`; equity avg `0.0033` n `92`; fx avg `0.0018` n `6`; index avg `-0.0032` n `25`; metal avg `0.0213` n `20`; unknown avg `0.032` n `766`
- 1h: commodity avg `-0.0143` n `12`; crypto_alt avg `-0.0583` n `230`; crypto_major avg `0.1675` n `8`; equity avg `0.0914` n `92`; fx avg `-0.0028` n `6`; index avg `0.0189` n `25`; metal avg `0.0359` n `20`; unknown avg `0.0176` n `766`
- 4h: commodity avg `-0.0999` n `12`; crypto_alt avg `-0.1246` n `230`; crypto_major avg `0.3537` n `8`; equity avg `0.0754` n `92`; fx avg `-0.0006` n `6`; index avg `-0.0373` n `25`; metal avg `0.1081` n `20`; unknown avg `-0.085` n `766`
- 24h: commodity avg `0.7674` n `12`; crypto_alt avg `-1.7857` n `230`; crypto_major avg `-2.1855` n `8`; equity avg `-2.9575` n `92`; fx avg `-0.0286` n `6`; index avg `-0.5771` n `25`; metal avg `-0.3128` n `20`; unknown avg `-0.3189` n `749`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1835`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1727`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0659`, n `668`, weak_sample_signal
