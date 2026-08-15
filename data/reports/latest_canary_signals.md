# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T19:11:03.178047+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0124` n `12`; crypto_alt avg `0.0147` n `230`; crypto_major avg `0.037` n `8`; equity avg `-0.0002` n `114`; fx avg `0.0015` n `6`; index avg `0.0025` n `25`; metal avg `-0.0015` n `20`; unknown avg `0.0073` n `791`
- 1h: commodity avg `0.0358` n `12`; crypto_alt avg `-0.0482` n `230`; crypto_major avg `-0.0845` n `8`; equity avg `0.0145` n `114`; fx avg `0.0018` n `6`; index avg `0.0018` n `25`; metal avg `-0.0002` n `20`; unknown avg `0.498` n `791`
- 4h: commodity avg `0.0684` n `12`; crypto_alt avg `0.0613` n `230`; crypto_major avg `0.124` n `8`; equity avg `0.0462` n `114`; fx avg `-0.0003` n `6`; index avg `0.0065` n `25`; metal avg `0.0017` n `20`; unknown avg `5.7167` n `791`
- 24h: commodity avg `-0.0216` n `12`; crypto_alt avg `1.1393` n `230`; crypto_major avg `0.7454` n `8`; equity avg `0.4756` n `114`; fx avg `0.0299` n `6`; index avg `0.0353` n `25`; metal avg `0.0609` n `20`; unknown avg `0.09` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2183`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.2036`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1822`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1787`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1581`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1506`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1487`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1484`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1434`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1385`, n `668`, weak_sample_signal
