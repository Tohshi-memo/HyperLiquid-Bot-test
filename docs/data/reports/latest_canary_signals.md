# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T10:07:31.681525+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0105` n `12`; crypto_alt avg `-0.004` n `230`; crypto_major avg `-0.0022` n `8`; equity avg `-0.1982` n `120`; fx avg `0.0176` n `6`; index avg `-0.0352` n `25`; metal avg `0.0198` n `20`; unknown avg `0.0031` n `791`
- 1h: commodity avg `-0.0112` n `12`; crypto_alt avg `-0.2244` n `230`; crypto_major avg `-0.1602` n `8`; equity avg `-0.728` n `120`; fx avg `-0.0365` n `6`; index avg `-0.1065` n `25`; metal avg `0.0272` n `20`; unknown avg `0.0784` n `791`
- 4h: commodity avg `0.0259` n `12`; crypto_alt avg `0.2233` n `230`; crypto_major avg `0.3082` n `8`; equity avg `0.8397` n `120`; fx avg `-0.0363` n `6`; index avg `0.1771` n `25`; metal avg `0.1703` n `20`; unknown avg `0.0471` n `789`
- 24h: commodity avg `0.4527` n `12`; crypto_alt avg `0.1323` n `230`; crypto_major avg `0.2985` n `8`; equity avg `-1.8309` n `120`; fx avg `-0.203` n `6`; index avg `-0.236` n `25`; metal avg `-0.4593` n `20`; unknown avg `-0.2357` n `757`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1383`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1264`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.125`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1189`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
