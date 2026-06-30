# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T17:07:30.743126+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.17` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0724` n `12`; crypto_alt avg `0.2448` n `228`; crypto_major avg `0.3428` n `8`; equity avg `0.0564` n `88`; fx avg `-0.0034` n `6`; index avg `0.0075` n `23`; metal avg `-0.1192` n `20`; unknown avg `0.23` n `765`
- 1h: commodity avg `-0.0648` n `12`; crypto_alt avg `0.0558` n `228`; crypto_major avg `0.24` n `8`; equity avg `0.2331` n `88`; fx avg `-0.0117` n `6`; index avg `0.0466` n `23`; metal avg `-0.0804` n `20`; unknown avg `0.2052` n `765`
- 4h: commodity avg `-0.2599` n `12`; crypto_alt avg `1.0352` n `228`; crypto_major avg `0.8849` n `8`; equity avg `1.3604` n `88`; fx avg `0.0677` n `6`; index avg `0.2748` n `23`; metal avg `-0.0014` n `20`; unknown avg `0.0773` n `765`
- 24h: commodity avg `0.1357` n `12`; crypto_alt avg `-1.8128` n `228`; crypto_major avg `-1.3379` n `8`; equity avg `1.5498` n `88`; fx avg `0.1271` n `6`; index avg `0.3639` n `23`; metal avg `0.3198` n `20`; unknown avg `8.7961` n `735`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1231`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0533`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0516`, n `668`, weak_sample_signal
