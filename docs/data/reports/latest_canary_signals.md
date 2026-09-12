# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T03:53:09.108987+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.93` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0028` n `12`; crypto_alt avg `-0.015` n `233`; crypto_major avg `-0.0368` n `8`; equity avg `-0.0218` n `136`; fx avg `0.0069` n `6`; index avg `0.0003` n `26`; metal avg `-0.0049` n `20`; unknown avg `-0.0473` n `826`
- 1h: commodity avg `0.0023` n `12`; crypto_alt avg `-0.0091` n `233`; crypto_major avg `0.0191` n `8`; equity avg `-0.0548` n `136`; fx avg `0.0001` n `6`; index avg `0.0056` n `26`; metal avg `-0.0106` n `20`; unknown avg `-0.2836` n `824`
- 4h: commodity avg `-0.0612` n `12`; crypto_alt avg `0.7493` n `233`; crypto_major avg `0.0012` n `8`; equity avg `0.0374` n `136`; fx avg `0.0114` n `6`; index avg `0.0227` n `26`; metal avg `-0.0312` n `20`; unknown avg `0.1447` n `814`
- 24h: commodity avg `-0.758` n `12`; crypto_alt avg `1.5163` n `233`; crypto_major avg `1.4659` n `8`; equity avg `1.2047` n `136`; fx avg `-0.1253` n `6`; index avg `0.3447` n `26`; metal avg `0.3383` n `20`; unknown avg `11.5306` n `690`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0588`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.058`, n `668`, weak_sample_signal
