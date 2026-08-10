# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T20:22:25.814170+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.005` n `12`; crypto_alt avg `0.1104` n `230`; crypto_major avg `-0.0608` n `8`; equity avg `0.0493` n `113`; fx avg `-0.001` n `6`; index avg `-0.0107` n `25`; metal avg `-0.01` n `20`; unknown avg `2.9787` n `785`
- 1h: commodity avg `0.0223` n `12`; crypto_alt avg `0.0289` n `230`; crypto_major avg `0.1458` n `8`; equity avg `-0.4042` n `113`; fx avg `0.0118` n `6`; index avg `-0.0424` n `25`; metal avg `-0.0347` n `20`; unknown avg `2.6738` n `785`
- 4h: commodity avg `0.1443` n `12`; crypto_alt avg `0.1465` n `230`; crypto_major avg `0.5319` n `8`; equity avg `-0.5019` n `113`; fx avg `0.0287` n `6`; index avg `-0.0605` n `25`; metal avg `0.1127` n `20`; unknown avg `0.9393` n `785`
- 24h: commodity avg `1.1723` n `12`; crypto_alt avg `-0.9359` n `230`; crypto_major avg `-0.8885` n `8`; equity avg `-1.7259` n `113`; fx avg `0.2617` n `6`; index avg `-0.1009` n `25`; metal avg `0.1461` n `20`; unknown avg `103.5609` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1728`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1678`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1536`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1535`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1524`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1462`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
