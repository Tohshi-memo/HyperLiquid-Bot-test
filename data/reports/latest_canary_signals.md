# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T18:52:30.328254+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1323` n `12`; crypto_alt avg `-0.6339` n `229`; crypto_major avg `-0.6854` n `8`; equity avg `-0.3808` n `91`; fx avg `0.0045` n `6`; index avg `-0.068` n `25`; metal avg `-0.1756` n `20`; unknown avg `0.2884` n `763`
- 1h: commodity avg `0.0951` n `12`; crypto_alt avg `-0.8143` n `229`; crypto_major avg `-0.9779` n `8`; equity avg `-0.7115` n `91`; fx avg `-0.0123` n `6`; index avg `-0.1029` n `25`; metal avg `-0.2035` n `20`; unknown avg `0.4703` n `763`
- 4h: commodity avg `0.173` n `12`; crypto_alt avg `-0.2961` n `229`; crypto_major avg `-0.171` n `8`; equity avg `0.2807` n `91`; fx avg `-0.0613` n `6`; index avg `0.091` n `25`; metal avg `-0.2108` n `20`; unknown avg `-0.111` n `755`
- 24h: commodity avg `0.6143` n `12`; crypto_alt avg `-1.7752` n `229`; crypto_major avg `-1.1336` n `8`; equity avg `-3.1104` n `91`; fx avg `-0.2539` n `6`; index avg `-0.5734` n `25`; metal avg `-0.4095` n `20`; unknown avg `-0.4453` n `731`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0571`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0563`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0558`, n `668`, weak_sample_signal
