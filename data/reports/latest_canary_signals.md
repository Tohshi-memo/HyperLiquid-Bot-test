# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T09:56:39.528249+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.13` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0471` n `12`; crypto_alt avg `0.1277` n `228`; crypto_major avg `0.1077` n `8`; equity avg `-0.025` n `88`; fx avg `0.0232` n `6`; index avg `-0.0048` n `23`; metal avg `-0.1761` n `20`; unknown avg `-0.231` n `764`
- 1h: commodity avg `0.1401` n `12`; crypto_alt avg `0.1505` n `228`; crypto_major avg `0.0429` n `8`; equity avg `-0.069` n `88`; fx avg `0.0257` n `6`; index avg `-0.0257` n `23`; metal avg `-0.3039` n `20`; unknown avg `-0.4051` n `764`
- 4h: commodity avg `0.1227` n `12`; crypto_alt avg `0.3865` n `228`; crypto_major avg `0.259` n `8`; equity avg `0.3032` n `88`; fx avg `0.0734` n `6`; index avg `0.0108` n `23`; metal avg `-0.323` n `20`; unknown avg `0.1152` n `732`
- 24h: commodity avg `-0.306` n `12`; crypto_alt avg `0.2413` n `228`; crypto_major avg `-0.162` n `8`; equity avg `0.3586` n `88`; fx avg `0.0692` n `6`; index avg `0.0622` n `23`; metal avg `-0.5606` n `20`; unknown avg `0.2006` n `732`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.156`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
