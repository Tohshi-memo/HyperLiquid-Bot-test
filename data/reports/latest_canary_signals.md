# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T11:22:31.191837+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0274` n `12`; crypto_alt avg `0.1434` n `230`; crypto_major avg `0.0841` n `8`; equity avg `-0.0505` n `113`; fx avg `0.0094` n `6`; index avg `-0.0055` n `25`; metal avg `0.0436` n `20`; unknown avg `-0.0055` n `787`
- 1h: commodity avg `-0.0533` n `12`; crypto_alt avg `0.0476` n `230`; crypto_major avg `-0.0401` n `8`; equity avg `0.1235` n `113`; fx avg `0.0119` n `6`; index avg `0.0152` n `25`; metal avg `-0.0007` n `20`; unknown avg `2.2767` n `787`
- 4h: commodity avg `-0.2377` n `12`; crypto_alt avg `-0.1531` n `230`; crypto_major avg `-0.2271` n `8`; equity avg `0.617` n `113`; fx avg `-0.0261` n `6`; index avg `0.0867` n `25`; metal avg `0.1492` n `20`; unknown avg `1.4983` n `787`
- 24h: commodity avg `-0.0936` n `12`; crypto_alt avg `-0.7015` n `230`; crypto_major avg `-0.5817` n `8`; equity avg `1.9721` n `113`; fx avg `-0.0355` n `6`; index avg `0.3667` n `25`; metal avg `-0.1826` n `20`; unknown avg `0.8765` n `755`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1908`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1862`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1751`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1655`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1614`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1607`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1572`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1555`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.149`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1453`, n `668`, weak_sample_signal
