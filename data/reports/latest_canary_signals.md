# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T19:22:28.633189+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.022` n `12`; crypto_alt avg `0.1409` n `230`; crypto_major avg `0.1723` n `8`; equity avg `0.0463` n `113`; fx avg `0.0079` n `6`; index avg `-0.001` n `25`; metal avg `0.026` n `20`; unknown avg `-0.013` n `785`
- 1h: commodity avg `-0.1474` n `12`; crypto_alt avg `-0.0566` n `230`; crypto_major avg `0.1604` n `8`; equity avg `0.1426` n `113`; fx avg `0.0095` n `6`; index avg `0.0272` n `25`; metal avg `0.2165` n `20`; unknown avg `-0.0312` n `785`
- 4h: commodity avg `0.1496` n `12`; crypto_alt avg `0.1495` n `230`; crypto_major avg `0.2529` n `8`; equity avg `0.0288` n `113`; fx avg `0.014` n `6`; index avg `0.0028` n `25`; metal avg `0.2934` n `20`; unknown avg `-0.1043` n `784`
- 24h: commodity avg `1.1316` n `12`; crypto_alt avg `-0.831` n `230`; crypto_major avg `-1.0723` n `8`; equity avg `-1.3159` n `113`; fx avg `0.258` n `6`; index avg `-0.0693` n `25`; metal avg `0.197` n `20`; unknown avg `103.5854` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.172`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1652`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.152`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1513`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1509`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1492`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
