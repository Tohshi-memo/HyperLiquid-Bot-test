# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T22:07:26.133810+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0197` n `12`; crypto_alt avg `-0.393` n `232`; crypto_major avg `-0.3426` n `8`; equity avg `-0.0328` n `134`; fx avg `-0.003` n `6`; index avg `0.0006` n `26`; metal avg `-0.0573` n `20`; unknown avg `1.4581` n `791`
- 1h: commodity avg `0.0225` n `12`; crypto_alt avg `-0.0139` n `232`; crypto_major avg `-0.2765` n `8`; equity avg `-0.0248` n `134`; fx avg `-0.0016` n `6`; index avg `0.0023` n `26`; metal avg `-0.0781` n `20`; unknown avg `6.395` n `791`
- 4h: commodity avg `-0.0217` n `12`; crypto_alt avg `0.3021` n `232`; crypto_major avg `0.048` n `8`; equity avg `0.0781` n `134`; fx avg `0.0256` n `6`; index avg `0.0184` n `26`; metal avg `-0.0761` n `20`; unknown avg `0.1664` n `755`
- 24h: commodity avg `-0.0076` n `12`; crypto_alt avg `0.9166` n `232`; crypto_major avg `0.0651` n `8`; equity avg `0.3167` n `134`; fx avg `0.0192` n `6`; index avg `0.0308` n `26`; metal avg `-0.1078` n `20`; unknown avg `150.7728` n `678`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1804`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1233`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
