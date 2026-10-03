# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T12:07:27.298888+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0151` n `13`; crypto_alt avg `-0.041` n `235`; crypto_major avg `0.0618` n `8`; equity avg `0.0034` n `143`; fx avg `-0.0004` n `6`; index avg `0.0017` n `26`; metal avg `-0.011` n `20`; unknown avg `-0.0086` n `974`
- 1h: commodity avg `-0.0408` n `13`; crypto_alt avg `0.0978` n `235`; crypto_major avg `0.1086` n `8`; equity avg `-0.0065` n `143`; fx avg `-0.0047` n `6`; index avg `-0.0174` n `26`; metal avg `-0.0051` n `20`; unknown avg `0.0056` n `972`
- 4h: commodity avg `-0.0186` n `13`; crypto_alt avg `0.739` n `235`; crypto_major avg `0.1727` n `8`; equity avg `0.0106` n `143`; fx avg `-0.0182` n `6`; index avg `-0.0098` n `26`; metal avg `-0.0137` n `20`; unknown avg `1.1916` n `972`
- 24h: commodity avg `0.5868` n `13`; crypto_alt avg `-1.7552` n `235`; crypto_major avg `-2.2103` n `8`; equity avg `0.387` n `142`; fx avg `0.0338` n `6`; index avg `0.1494` n `26`; metal avg `-0.2338` n `20`; unknown avg `-0.3216` n `874`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1966`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1863`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1552`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1542`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
