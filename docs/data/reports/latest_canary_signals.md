# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T14:07:41.082933+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0203` n `12`; crypto_alt avg `0.1445` n `230`; crypto_major avg `0.3248` n `8`; equity avg `0.4256` n `113`; fx avg `0.0026` n `6`; index avg `0.0667` n `25`; metal avg `0.0446` n `20`; unknown avg `0.0584` n `784`
- 1h: commodity avg `0.2974` n `12`; crypto_alt avg `-0.1235` n `230`; crypto_major avg `-0.129` n `8`; equity avg `0.1316` n `113`; fx avg `0.0257` n `6`; index avg `0.0625` n `25`; metal avg `-0.0553` n `20`; unknown avg `0.0972` n `784`
- 4h: commodity avg `0.4925` n `12`; crypto_alt avg `0.0579` n `230`; crypto_major avg `-0.2385` n `8`; equity avg `-0.5316` n `113`; fx avg `0.0237` n `6`; index avg `-0.032` n `25`; metal avg `-0.0932` n `20`; unknown avg `0.0083` n `784`
- 24h: commodity avg `1.0032` n `12`; crypto_alt avg `0.4146` n `230`; crypto_major avg `-0.6386` n `8`; equity avg `-0.7434` n `113`; fx avg `0.258` n `6`; index avg `0.0197` n `25`; metal avg `-0.256` n `20`; unknown avg `59.0265` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1724`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1611`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1566`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1444`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1416`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1376`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1293`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
