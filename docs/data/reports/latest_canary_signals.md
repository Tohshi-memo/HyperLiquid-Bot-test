# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T19:52:31.325823+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0075` n `12`; crypto_alt avg `0.0617` n `230`; crypto_major avg `0.0899` n `8`; equity avg `0.1226` n `114`; fx avg `0.0052` n `6`; index avg `0.0053` n `25`; metal avg `-0.0005` n `20`; unknown avg `0.0188` n `791`
- 1h: commodity avg `-0.0557` n `12`; crypto_alt avg `0.0171` n `230`; crypto_major avg `0.0891` n `8`; equity avg `0.1159` n `114`; fx avg `0.0059` n `6`; index avg `0.0045` n `25`; metal avg `0.0306` n `20`; unknown avg `-0.166` n `791`
- 4h: commodity avg `-0.0146` n `12`; crypto_alt avg `0.212` n `230`; crypto_major avg `-0.2184` n `8`; equity avg `0.2861` n `114`; fx avg `0.0036` n `6`; index avg `0.0457` n `25`; metal avg `-0.0319` n `20`; unknown avg `18.3374` n `791`
- 24h: commodity avg `0.1838` n `12`; crypto_alt avg `0.2925` n `230`; crypto_major avg `-0.9711` n `8`; equity avg `-0.2845` n `114`; fx avg `0.0841` n `6`; index avg `-0.0569` n `25`; metal avg `0.2648` n `20`; unknown avg `-0.0151` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2148`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1836`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1806`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1549`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1531`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.147`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.146`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1446`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1403`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1355`, n `668`, weak_sample_signal
