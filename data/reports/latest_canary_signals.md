# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T14:07:31.437975+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.45` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.055` n `12`; crypto_alt avg `-0.3286` n `228`; crypto_major avg `-0.3688` n `8`; equity avg `-1.2377` n `88`; fx avg `0.0128` n `6`; index avg `-0.1866` n `23`; metal avg `-0.1541` n `20`; unknown avg `-0.2439` n `764`
- 1h: commodity avg `0.0424` n `12`; crypto_alt avg `-0.9349` n `228`; crypto_major avg `-1.0519` n `8`; equity avg `-1.5019` n `88`; fx avg `0.0331` n `6`; index avg `-0.2095` n `23`; metal avg `-0.3306` n `20`; unknown avg `0.1405` n `764`
- 4h: commodity avg `-0.1963` n `12`; crypto_alt avg `-0.6719` n `228`; crypto_major avg `-0.4511` n `8`; equity avg `-1.3731` n `88`; fx avg `0.0566` n `6`; index avg `-0.216` n `23`; metal avg `-0.1356` n `20`; unknown avg `0.1362` n `764`
- 24h: commodity avg `-0.623` n `12`; crypto_alt avg `-0.2104` n `228`; crypto_major avg `-0.3133` n `8`; equity avg `-0.9163` n `88`; fx avg `0.1286` n `6`; index avg `-0.1352` n `23`; metal avg `-0.6496` n `20`; unknown avg `1.0093` n `732`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1543`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1267`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
