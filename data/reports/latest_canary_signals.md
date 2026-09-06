# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T22:18:48.032814+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0029` n `12`; crypto_alt avg `-0.3987` n `232`; crypto_major avg `-0.3594` n `8`; equity avg `-0.0548` n `134`; fx avg `0.0157` n `6`; index avg `-0.0087` n `26`; metal avg `0.0172` n `20`; unknown avg `1.1122` n `793`
- 1h: commodity avg `0.0269` n `12`; crypto_alt avg `-0.6627` n `232`; crypto_major avg `-0.7647` n `8`; equity avg `-0.0662` n `134`; fx avg `0.0168` n `6`; index avg `-0.0104` n `26`; metal avg `-0.0761` n `20`; unknown avg `-0.0429` n `791`
- 4h: commodity avg `-0.0136` n `12`; crypto_alt avg `-0.0817` n `232`; crypto_major avg `-0.3513` n `8`; equity avg `0.0051` n `134`; fx avg `0.0343` n `6`; index avg `0.0042` n `26`; metal avg `-0.0571` n `20`; unknown avg `0.5023` n `761`
- 24h: commodity avg `-0.0054` n `12`; crypto_alt avg `0.5537` n `232`; crypto_major avg `-0.1475` n `8`; equity avg `0.2631` n `134`; fx avg `0.0351` n `6`; index avg `-0.006` n `26`; metal avg `-0.0893` n `20`; unknown avg `153.4464` n `678`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1806`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
