# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T20:52:27.203016+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.88` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0441` n `12`; crypto_alt avg `-0.2389` n `233`; crypto_major avg `-0.2565` n `8`; equity avg `-0.0077` n `136`; fx avg `-0.0103` n `6`; index avg `0.0003` n `26`; metal avg `-0.0052` n `20`; unknown avg `0.2585` n `824`
- 1h: commodity avg `-0.1003` n `12`; crypto_alt avg `0.0195` n `233`; crypto_major avg `-0.0494` n `8`; equity avg `-0.0048` n `136`; fx avg `-0.0252` n `6`; index avg `-0.0171` n `26`; metal avg `0.0221` n `20`; unknown avg `0.0009` n `790`
- 4h: commodity avg `-0.0189` n `12`; crypto_alt avg `-1.2404` n `233`; crypto_major avg `-0.9818` n `8`; equity avg `-0.2209` n `136`; fx avg `-0.0106` n `6`; index avg `-0.0271` n `26`; metal avg `-0.0437` n `20`; unknown avg `-0.0167` n `726`
- 24h: commodity avg `-0.7426` n `12`; crypto_alt avg `0.1627` n `233`; crypto_major avg `0.8935` n `8`; equity avg `0.6467` n `136`; fx avg `-0.1626` n `6`; index avg `0.2972` n `26`; metal avg `0.2726` n `20`; unknown avg `1.2459` n `670`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1233`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0603`, n `668`, weak_sample_signal
