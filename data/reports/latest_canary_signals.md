# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T15:37:31.747399+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0606` n `13`; crypto_alt avg `-0.4461` n `234`; crypto_major avg `-0.4828` n `8`; equity avg `-0.1586` n `142`; fx avg `-0.0381` n `6`; index avg `-0.0401` n `26`; metal avg `-0.0411` n `20`; unknown avg `0.2876` n `975`
- 1h: commodity avg `0.1251` n `13`; crypto_alt avg `-0.549` n `234`; crypto_major avg `-0.6514` n `8`; equity avg `-0.2891` n `142`; fx avg `-0.0741` n `6`; index avg `-0.0707` n `26`; metal avg `-0.1675` n `20`; unknown avg `0.2964` n `937`
- 4h: commodity avg `0.1736` n `13`; crypto_alt avg `-1.018` n `234`; crypto_major avg `-0.7567` n `8`; equity avg `-0.7739` n `142`; fx avg `-0.1619` n `6`; index avg `-0.2241` n `26`; metal avg `-0.156` n `20`; unknown avg `0.97` n `909`
- 24h: commodity avg `-0.1095` n `13`; crypto_alt avg `-1.5808` n `234`; crypto_major avg `-0.4356` n `8`; equity avg `-0.3458` n `142`; fx avg `-0.1252` n `6`; index avg `-0.1745` n `26`; metal avg `-0.1498` n `20`; unknown avg `3.04` n `840`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1739`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1548`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
