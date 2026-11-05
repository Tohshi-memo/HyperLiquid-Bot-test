# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T05:52:31.132024+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0341` n `13`; crypto_alt avg `-0.3239` n `239`; crypto_major avg `-0.3076` n `8`; equity avg `-0.3535` n `158`; fx avg `0.0006` n `6`; index avg `-0.0498` n `27`; metal avg `-0.0302` n `20`; unknown avg `3.7888` n `1263`
- 1h: commodity avg `0.1463` n `13`; crypto_alt avg `-0.6043` n `239`; crypto_major avg `-0.3756` n `8`; equity avg `-0.6531` n `158`; fx avg `0.0027` n `6`; index avg `-0.091` n `27`; metal avg `-0.2447` n `20`; unknown avg `6.3092` n `1251`
- 4h: commodity avg `0.0898` n `13`; crypto_alt avg `-0.7318` n `239`; crypto_major avg `-0.7332` n `8`; equity avg `-1.1084` n `158`; fx avg `0.0072` n `6`; index avg `-0.1932` n `27`; metal avg `-0.2153` n `20`; unknown avg `0.8839` n `1230`
- 24h: commodity avg `-1.7948` n `13`; crypto_alt avg `0.8521` n `239`; crypto_major avg `1.8282` n `8`; equity avg `-2.3277` n `158`; fx avg `0.1021` n `6`; index avg `-0.129` n `27`; metal avg `0.8747` n `20`; unknown avg `30.8284` n `1012`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2528`, n `668`, moderate_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1814`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1798`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1542`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1497`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.149`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1366`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1338`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1326`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.128`, n `668`, weak_sample_signal
