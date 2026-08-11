# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T21:07:26.077619+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0405` n `12`; crypto_alt avg `0.0459` n `230`; crypto_major avg `0.1322` n `8`; equity avg `0.1166` n `113`; fx avg `0.0041` n `6`; index avg `0.0094` n `25`; metal avg `0.0152` n `20`; unknown avg `0.0455` n `785`
- 1h: commodity avg `-0.0866` n `12`; crypto_alt avg `-0.1384` n `230`; crypto_major avg `-0.0008` n `8`; equity avg `0.4507` n `113`; fx avg `-0.0098` n `6`; index avg `0.0293` n `25`; metal avg `0.0061` n `20`; unknown avg `0.0118` n `785`
- 4h: commodity avg `-0.0418` n `12`; crypto_alt avg `0.3976` n `230`; crypto_major avg `0.9151` n `8`; equity avg `0.7643` n `113`; fx avg `0.0073` n `6`; index avg `0.0508` n `25`; metal avg `-0.0443` n `20`; unknown avg `0.6864` n `785`
- 24h: commodity avg `0.0363` n `12`; crypto_alt avg `-1.5066` n `230`; crypto_major avg `0.2399` n `8`; equity avg `1.177` n `113`; fx avg `-0.0664` n `6`; index avg `0.1195` n `25`; metal avg `-0.2285` n `20`; unknown avg `-0.2561` n `753`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2174`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2103`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2088`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2072`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1947`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1539`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1358`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1302`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1155`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
