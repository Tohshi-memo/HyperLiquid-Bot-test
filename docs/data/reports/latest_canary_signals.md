# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T02:56:13.589790+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0203` n `12`; crypto_alt avg `-0.0476` n `230`; crypto_major avg `0.0344` n `8`; equity avg `0.0488` n `113`; fx avg `-0.0088` n `6`; index avg `0.0098` n `25`; metal avg `-0.0603` n `20`; unknown avg `-0.052` n `785`
- 1h: commodity avg `-0.0174` n `12`; crypto_alt avg `-0.175` n `230`; crypto_major avg `-0.04` n `8`; equity avg `0.026` n `113`; fx avg `-0.0007` n `6`; index avg `-0.0066` n `25`; metal avg `-0.21` n `20`; unknown avg `-0.1058` n `785`
- 4h: commodity avg `0.0442` n `12`; crypto_alt avg `0.2138` n `230`; crypto_major avg `0.1366` n `8`; equity avg `0.4501` n `113`; fx avg `-0.0399` n `6`; index avg `0.1196` n `25`; metal avg `0.0314` n `20`; unknown avg `-0.2718` n `785`
- 24h: commodity avg `0.8414` n `12`; crypto_alt avg `-0.6166` n `230`; crypto_major avg `-0.7057` n `8`; equity avg `-1.0368` n `113`; fx avg `0.1048` n `6`; index avg `0.0135` n `25`; metal avg `0.53` n `20`; unknown avg `103.8401` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1701`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1643`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1611`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1568`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1543`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1417`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1251`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
