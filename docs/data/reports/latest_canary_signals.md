# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T02:37:28.513843+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.005` n `12`; crypto_alt avg `-0.1099` n `230`; crypto_major avg `-0.028` n `8`; equity avg `0.1033` n `113`; fx avg `-0.0065` n `6`; index avg `0.0186` n `25`; metal avg `-0.0826` n `20`; unknown avg `0.0611` n `785`
- 1h: commodity avg `-0.0017` n `12`; crypto_alt avg `-0.0366` n `230`; crypto_major avg `0.0183` n `8`; equity avg `0.0773` n `113`; fx avg `0.0227` n `6`; index avg `0.0241` n `25`; metal avg `-0.0559` n `20`; unknown avg `-0.1013` n `785`
- 4h: commodity avg `0.0128` n `12`; crypto_alt avg `0.2772` n `230`; crypto_major avg `0.182` n `8`; equity avg `0.3996` n `113`; fx avg `-0.0281` n `6`; index avg `0.1173` n `25`; metal avg `0.1219` n `20`; unknown avg `-0.3127` n `785`
- 24h: commodity avg `0.8233` n `12`; crypto_alt avg `-0.3271` n `230`; crypto_major avg `-0.4906` n `8`; equity avg `-0.9531` n `113`; fx avg `0.1203` n `6`; index avg `0.0465` n `25`; metal avg `0.5535` n `20`; unknown avg `103.7776` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1709`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1648`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1575`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1544`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1542`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1424`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
