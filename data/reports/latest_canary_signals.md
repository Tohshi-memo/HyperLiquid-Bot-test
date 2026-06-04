# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T04:07:24.415745+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0328` n `12`; crypto_alt avg `0.0818` n `228`; crypto_major avg `0.127` n `8`; equity avg `0.1534` n `73`; fx avg `0.0029` n `6`; index avg `-0.015` n `23`; metal avg `0.1096` n `18`; unknown avg `1.76` n `420`
- 1h: commodity avg `0.1069` n `12`; crypto_alt avg `0.6327` n `228`; crypto_major avg `0.8156` n `8`; equity avg `0.1989` n `73`; fx avg `0.0139` n `6`; index avg `0.0429` n `23`; metal avg `-0.2017` n `18`; unknown avg `4.9298` n `420`
- 4h: commodity avg `-0.2694` n `12`; crypto_alt avg `-2.3345` n `228`; crypto_major avg `-0.2612` n `8`; equity avg `0.5137` n `73`; fx avg `-0.0088` n `6`; index avg `0.0969` n `23`; metal avg `0.1971` n `18`; unknown avg `2.595` n `419`
- 24h: commodity avg `0.0139` n `12`; crypto_alt avg `-0.501` n `228`; crypto_major avg `-0.8795` n `8`; equity avg `-3.3701` n `73`; fx avg `-0.0071` n `6`; index avg `-1.1823` n `23`; metal avg `-1.8043` n `18`; unknown avg `0.9132` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1932`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1757`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1613`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1559`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
