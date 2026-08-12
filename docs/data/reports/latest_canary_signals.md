# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T09:37:26.268272+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1076` n `12`; crypto_alt avg `0.2069` n `230`; crypto_major avg `0.3448` n `8`; equity avg `0.1028` n `113`; fx avg `-0.0218` n `6`; index avg `0.0231` n `25`; metal avg `-0.0052` n `20`; unknown avg `0.0161` n `786`
- 1h: commodity avg `-0.1545` n `12`; crypto_alt avg `0.2504` n `230`; crypto_major avg `0.4812` n `8`; equity avg `0.2205` n `113`; fx avg `-0.0365` n `6`; index avg `0.0727` n `25`; metal avg `0.1258` n `20`; unknown avg `-0.0753` n `786`
- 4h: commodity avg `-0.1446` n `12`; crypto_alt avg `-0.2748` n `230`; crypto_major avg `0.3332` n `8`; equity avg `0.6618` n `113`; fx avg `-0.0156` n `6`; index avg `0.1207` n `25`; metal avg `0.2816` n `20`; unknown avg `-0.1364` n `770`
- 24h: commodity avg `-0.2335` n `12`; crypto_alt avg `-1.0405` n `230`; crypto_major avg `0.9592` n `8`; equity avg `2.7526` n `113`; fx avg `-0.0298` n `6`; index avg `0.2851` n `25`; metal avg `0.2577` n `20`; unknown avg `-0.2342` n `769`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2336`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.229`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2176`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1969`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1678`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1569`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1495`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.122`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1191`, n `668`, weak_sample_signal
