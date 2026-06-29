# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T17:22:34.257189+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.87` - Polymarket crypto volume is unusually high.
- 1h_crypto_metal_divergence: score `1.9516` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_metal_divergence: score `1.6785` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0971` n `12`; crypto_alt avg `0.5407` n `228`; crypto_major avg `0.9016` n `8`; equity avg `0.1014` n `88`; fx avg `-0.0056` n `6`; index avg `-0.0197` n `23`; metal avg `-0.0276` n `20`; unknown avg `-0.0791` n `765`
- 1h: commodity avg `0.0798` n `12`; crypto_alt avg `1.1047` n `228`; crypto_major avg `1.9046` n `8`; equity avg `0.542` n `88`; fx avg `-0.0102` n `6`; index avg `0.0226` n `23`; metal avg `-0.047` n `20`; unknown avg `1.3434` n `765`
- 4h: commodity avg `0.2139` n `12`; crypto_alt avg `0.7842` n `228`; crypto_major avg `1.3414` n `8`; equity avg `0.6585` n `88`; fx avg `0.0275` n `6`; index avg `0.0479` n `23`; metal avg `-0.3371` n `20`; unknown avg `0.331` n `764`
- 24h: commodity avg `-0.5084` n `12`; crypto_alt avg `1.8122` n `228`; crypto_major avg `2.6391` n `8`; equity avg `1.2535` n `88`; fx avg `0.138` n `6`; index avg `0.1176` n `23`; metal avg `-0.6562` n `20`; unknown avg `3.802` n `732`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1518`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
