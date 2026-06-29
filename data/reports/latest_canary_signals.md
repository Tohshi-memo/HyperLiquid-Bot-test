# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T22:22:29.901206+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.11` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0038` n `12`; crypto_alt avg `-0.1115` n `228`; crypto_major avg `-0.0812` n `8`; equity avg `0.0447` n `88`; fx avg `-0.0126` n `6`; index avg `0.002` n `23`; metal avg `0.0034` n `20`; unknown avg `-0.0947` n `763`
- 1h: commodity avg `-0.0225` n `12`; crypto_alt avg `0.0313` n `228`; crypto_major avg `0.1084` n `8`; equity avg `0.0542` n `88`; fx avg `0.0061` n `6`; index avg `-0.0327` n `23`; metal avg `0.0192` n `20`; unknown avg `-0.1218` n `763`
- 4h: commodity avg `-0.0317` n `12`; crypto_alt avg `-0.573` n `228`; crypto_major avg `-0.1013` n `8`; equity avg `0.4071` n `88`; fx avg `0.0217` n `6`; index avg `0.0263` n `23`; metal avg `-0.037` n `20`; unknown avg `0.1153` n `763`
- 24h: commodity avg `-0.2819` n `12`; crypto_alt avg `1.9519` n `228`; crypto_major avg `3.421` n `8`; equity avg `1.717` n `88`; fx avg `0.2141` n `6`; index avg `0.0906` n `23`; metal avg `-0.2653` n `20`; unknown avg `1.7245` n `730`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1549`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
