# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T12:07:33.443698+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0511` n `12`; crypto_alt avg `0.0658` n `230`; crypto_major avg `0.1565` n `8`; equity avg `-0.0051` n `113`; fx avg `-0.0271` n `6`; index avg `-0.0008` n `25`; metal avg `0.0313` n `20`; unknown avg `0.0134` n `784`
- 1h: commodity avg `0.0028` n `12`; crypto_alt avg `0.3071` n `230`; crypto_major avg `0.3699` n `8`; equity avg `0.1066` n `113`; fx avg `-0.0285` n `6`; index avg `-0.0035` n `25`; metal avg `0.0668` n `20`; unknown avg `-0.0425` n `784`
- 4h: commodity avg `0.253` n `12`; crypto_alt avg `0.0937` n `230`; crypto_major avg `0.0483` n `8`; equity avg `-0.4884` n `113`; fx avg `-0.0153` n `6`; index avg `-0.0938` n `25`; metal avg `-0.0914` n `20`; unknown avg `-0.1339` n `784`
- 24h: commodity avg `0.615` n `12`; crypto_alt avg `1.1253` n `230`; crypto_major avg `0.4361` n `8`; equity avg `-0.3458` n `113`; fx avg `0.186` n `6`; index avg `0.0195` n `25`; metal avg `-0.1122` n `20`; unknown avg `57.0493` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1774`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1492`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1483`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1457`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1311`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1271`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1179`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
