# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T20:07:29.027997+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.72` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `1.8533` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0093` n `12`; crypto_alt avg `-0.0295` n `228`; crypto_major avg `-0.1574` n `8`; equity avg `0.0762` n `88`; fx avg `0.0031` n `6`; index avg `0.0062` n `23`; metal avg `0.0033` n `20`; unknown avg `1.1147` n `765`
- 1h: commodity avg `0.0173` n `12`; crypto_alt avg `0.0383` n `228`; crypto_major avg `0.5242` n `8`; equity avg `0.2239` n `88`; fx avg `0.0034` n `6`; index avg `0.0259` n `23`; metal avg `0.0102` n `20`; unknown avg `0.8531` n `765`
- 4h: commodity avg `-0.0835` n `12`; crypto_alt avg `0.6937` n `228`; crypto_major avg `1.8245` n `8`; equity avg `1.0242` n `88`; fx avg `-0.0194` n `6`; index avg `0.1365` n `23`; metal avg `-0.0288` n `20`; unknown avg `2.4023` n `765`
- 24h: commodity avg `-0.6407` n `12`; crypto_alt avg `1.9933` n `228`; crypto_major avg `3.2982` n `8`; equity avg `1.7462` n `88`; fx avg `0.1316` n `6`; index avg `0.2176` n `23`; metal avg `-0.4846` n `20`; unknown avg `0.5671` n `732`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1545`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
