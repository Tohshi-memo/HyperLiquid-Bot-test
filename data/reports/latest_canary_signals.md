# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T08:37:39.405231+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1353` n `12`; crypto_alt avg `-0.0088` n `230`; crypto_major avg `-0.0349` n `8`; equity avg `-0.2288` n `107`; fx avg `-0.0045` n `6`; index avg `-0.0411` n `25`; metal avg `-0.0261` n `20`; unknown avg `-0.0088` n `781`
- 1h: commodity avg `0.1263` n `12`; crypto_alt avg `0.0217` n `230`; crypto_major avg `-0.1217` n `8`; equity avg `0.1288` n `107`; fx avg `0.0162` n `6`; index avg `-0.0046` n `25`; metal avg `-0.0077` n `20`; unknown avg `0.1017` n `781`
- 4h: commodity avg `0.0717` n `12`; crypto_alt avg `-0.2222` n `230`; crypto_major avg `-0.2703` n `8`; equity avg `0.9968` n `107`; fx avg `0.0565` n `6`; index avg `0.141` n `25`; metal avg `0.0772` n `20`; unknown avg `0.8663` n `765`
- 24h: commodity avg `0.2385` n `12`; crypto_alt avg `1.3958` n `230`; crypto_major avg `1.605` n `8`; equity avg `3.4826` n `107`; fx avg `0.0798` n `6`; index avg `0.3211` n `25`; metal avg `0.1532` n `20`; unknown avg `1.1448` n `763`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1431`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
