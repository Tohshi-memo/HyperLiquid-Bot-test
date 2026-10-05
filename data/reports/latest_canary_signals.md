# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T02:52:36.663436+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.84` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0215` n `13`; crypto_alt avg `0.0083` n `235`; crypto_major avg `-0.1225` n `8`; equity avg `-0.0513` n `144`; fx avg `-0.0066` n `6`; index avg `-0.0158` n `26`; metal avg `-0.0708` n `20`; unknown avg `0.1102` n `1078`
- 1h: commodity avg `0.0013` n `13`; crypto_alt avg `0.3324` n `235`; crypto_major avg `0.1184` n `8`; equity avg `-0.1883` n `144`; fx avg `-0.011` n `6`; index avg `-0.0481` n `26`; metal avg `-0.1316` n `20`; unknown avg `0.0312` n `1076`
- 4h: commodity avg `-0.1029` n `13`; crypto_alt avg `0.6489` n `235`; crypto_major avg `0.1548` n `8`; equity avg `0.1761` n `144`; fx avg `-0.0806` n `6`; index avg `-0.0088` n `26`; metal avg `0.0257` n `20`; unknown avg `4.4579` n `1038`
- 24h: commodity avg `-0.3351` n `13`; crypto_alt avg `1.6477` n `235`; crypto_major avg `1.7493` n `8`; equity avg `0.4989` n `144`; fx avg `-0.0587` n `6`; index avg `0.0087` n `26`; metal avg `0.1065` n `20`; unknown avg `0.8221` n `950`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1967`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.178`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1648`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1447`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1317`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
