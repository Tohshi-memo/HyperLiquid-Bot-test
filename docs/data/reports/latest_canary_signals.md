# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T22:07:31.184200+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.21` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.002` n `12`; crypto_alt avg `-0.1619` n `233`; crypto_major avg `-0.2063` n `8`; equity avg `-0.0215` n `136`; fx avg `-0.0083` n `6`; index avg `0.0028` n `26`; metal avg `-0.0265` n `20`; unknown avg `0.4735` n `828`
- 1h: commodity avg `-0.0218` n `12`; crypto_alt avg `-0.7343` n `233`; crypto_major avg `-0.5394` n `8`; equity avg `-0.0605` n `136`; fx avg `-0.0129` n `6`; index avg `0.0181` n `26`; metal avg `-0.0143` n `20`; unknown avg `0.3839` n `820`
- 4h: commodity avg `-0.0009` n `12`; crypto_alt avg `-0.6366` n `233`; crypto_major avg `-0.2451` n `8`; equity avg `-0.3185` n `136`; fx avg `-0.0141` n `6`; index avg `-0.0475` n `26`; metal avg `-0.0336` n `20`; unknown avg `0.1007` n `770`
- 24h: commodity avg `-0.8165` n `12`; crypto_alt avg `-0.2816` n `233`; crypto_major avg `0.6523` n `8`; equity avg `0.7024` n `136`; fx avg `-0.2025` n `6`; index avg `0.3171` n `26`; metal avg `0.2707` n `20`; unknown avg `0.9725` n `670`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1286`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0631`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0591`, n `668`, weak_sample_signal
