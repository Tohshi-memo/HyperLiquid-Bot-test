# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T04:37:30.562414+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0102` n `12`; crypto_alt avg `0.0065` n `230`; crypto_major avg `0.1755` n `8`; equity avg `0.1021` n `113`; fx avg `-0.0023` n `6`; index avg `0.0222` n `25`; metal avg `0.0229` n `20`; unknown avg `0.9299` n `787`
- 1h: commodity avg `0.0792` n `12`; crypto_alt avg `0.0323` n `230`; crypto_major avg `0.1437` n `8`; equity avg `0.0484` n `113`; fx avg `-0.0021` n `6`; index avg `0.0039` n `25`; metal avg `-0.0799` n `20`; unknown avg `0.586` n `786`
- 4h: commodity avg `0.095` n `12`; crypto_alt avg `0.1131` n `230`; crypto_major avg `0.4721` n `8`; equity avg `0.3141` n `113`; fx avg `0.0358` n `6`; index avg `0.0552` n `25`; metal avg `-0.3317` n `20`; unknown avg `0.4552` n `786`
- 24h: commodity avg `-0.1566` n `12`; crypto_alt avg `-1.0162` n `230`; crypto_major avg `0.1194` n `8`; equity avg `2.4777` n `113`; fx avg `-0.0357` n `6`; index avg `0.3073` n `25`; metal avg `-0.1457` n `20`; unknown avg `0.0709` n `770`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2418`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2085`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1916`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1906`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1889`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1706`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1654`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1459`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.143`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1269`, n `668`, weak_sample_signal
