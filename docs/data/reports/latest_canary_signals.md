# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T01:37:28.456794+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0083` n `12`; crypto_alt avg `-0.1376` n `230`; crypto_major avg `-0.03` n `8`; equity avg `0.0025` n `114`; fx avg `-0.0035` n `6`; index avg `-0.0036` n `25`; metal avg `-0.0005` n `20`; unknown avg `0.0064` n `791`
- 1h: commodity avg `0.0351` n `12`; crypto_alt avg `-0.2617` n `230`; crypto_major avg `0.0084` n `8`; equity avg `-0.0268` n `114`; fx avg `-0.0006` n `6`; index avg `-0.0029` n `25`; metal avg `0.0071` n `20`; unknown avg `-0.0097` n `791`
- 4h: commodity avg `0.03` n `12`; crypto_alt avg `-0.6292` n `230`; crypto_major avg `-0.2869` n `8`; equity avg `-0.0244` n `114`; fx avg `-0.0047` n `6`; index avg `0.0137` n `25`; metal avg `0.0041` n `20`; unknown avg `0.0234` n `791`
- 24h: commodity avg `0.0099` n `12`; crypto_alt avg `0.0025` n `230`; crypto_major avg `-0.0081` n `8`; equity avg `0.1509` n `114`; fx avg `0.0412` n `6`; index avg `0.0078` n `25`; metal avg `-0.0259` n `20`; unknown avg `0.0978` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2238`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1845`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1771`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1738`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1708`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1548`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1503`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1486`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.148`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1427`, n `668`, weak_sample_signal
