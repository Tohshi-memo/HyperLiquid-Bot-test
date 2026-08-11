# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T02:07:39.121737+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0327` n `12`; crypto_alt avg `0.042` n `230`; crypto_major avg `-0.0168` n `8`; equity avg `-0.1263` n `113`; fx avg `0.0084` n `6`; index avg `-0.0287` n `25`; metal avg `-0.0915` n `20`; unknown avg `-0.0331` n `785`
- 1h: commodity avg `0.0022` n `12`; crypto_alt avg `0.2297` n `230`; crypto_major avg `0.2824` n `8`; equity avg `0.2273` n `113`; fx avg `0.0441` n `6`; index avg `0.0962` n `25`; metal avg `0.077` n `20`; unknown avg `-0.0963` n `785`
- 4h: commodity avg `0.0007` n `12`; crypto_alt avg `0.5534` n `230`; crypto_major avg `0.2245` n `8`; equity avg `0.212` n `113`; fx avg `-0.0315` n `6`; index avg `0.0768` n `25`; metal avg `0.1864` n `20`; unknown avg `-0.2531` n `785`
- 24h: commodity avg `0.8033` n `12`; crypto_alt avg `-0.4016` n `230`; crypto_major avg `-0.625` n `8`; equity avg `-1.1783` n `113`; fx avg `0.1052` n `6`; index avg `-0.0026` n `25`; metal avg `0.642` n `20`; unknown avg `103.8009` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1784`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1704`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1586`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1551`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1546`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1432`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
