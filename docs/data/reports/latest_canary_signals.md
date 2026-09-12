# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T05:07:24.847763+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.85` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0088` n `12`; crypto_alt avg `-0.1066` n `233`; crypto_major avg `-0.1074` n `8`; equity avg `0.0337` n `136`; fx avg `-0.0028` n `6`; index avg `0.0001` n `26`; metal avg `0.0077` n `20`; unknown avg `-0.1098` n `836`
- 1h: commodity avg `-0.0234` n `12`; crypto_alt avg `-0.0899` n `233`; crypto_major avg `-0.1356` n `8`; equity avg `0.0237` n `136`; fx avg `-0.0032` n `6`; index avg `-0.0038` n `26`; metal avg `0.0146` n `20`; unknown avg `0.7212` n `828`
- 4h: commodity avg `-0.1033` n `12`; crypto_alt avg `0.1079` n `233`; crypto_major avg `-0.0647` n `8`; equity avg `-0.0278` n `136`; fx avg `0.0011` n `6`; index avg `-0.0124` n `26`; metal avg `-0.0261` n `20`; unknown avg `0.0116` n `814`
- 24h: commodity avg `-0.5662` n `12`; crypto_alt avg `0.7083` n `233`; crypto_major avg `0.7864` n `8`; equity avg `0.8807` n `136`; fx avg `-0.1256` n `6`; index avg `0.2556` n `26`; metal avg `0.1339` n `20`; unknown avg `1.514` n `690`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0637`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0628`, n `668`, weak_sample_signal
