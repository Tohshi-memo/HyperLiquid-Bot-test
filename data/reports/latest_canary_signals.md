# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T17:22:29.137623+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0057` n `12`; crypto_alt avg `0.0107` n `230`; crypto_major avg `-0.0724` n `8`; equity avg `-0.0079` n `114`; fx avg `-0.0036` n `6`; index avg `-0.0021` n `25`; metal avg `-0.0024` n `20`; unknown avg `0.0181` n `791`
- 1h: commodity avg `0.0141` n `12`; crypto_alt avg `0.0579` n `230`; crypto_major avg `0.0026` n `8`; equity avg `-0.0328` n `114`; fx avg `-0.0052` n `6`; index avg `-0.0011` n `25`; metal avg `-0.0048` n `20`; unknown avg `1.2313` n `791`
- 4h: commodity avg `-0.0016` n `12`; crypto_alt avg `0.4644` n `230`; crypto_major avg `0.1701` n `8`; equity avg `0.0048` n `114`; fx avg `-0.0077` n `6`; index avg `0.0001` n `25`; metal avg `-0.006` n `20`; unknown avg `-0.0227` n `791`
- 24h: commodity avg `-0.139` n `12`; crypto_alt avg `0.8086` n `230`; crypto_major avg `0.2212` n `8`; equity avg `0.1181` n `114`; fx avg `0.0302` n `6`; index avg `0.0295` n `25`; metal avg `-0.0134` n `20`; unknown avg `-0.0585` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2162`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.2119`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.183`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1785`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1582`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1559`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1479`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1465`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1456`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.142`, n `668`, weak_sample_signal
