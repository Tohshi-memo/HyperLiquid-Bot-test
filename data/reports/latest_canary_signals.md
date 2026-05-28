# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T12:02:01.893452+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0785` n `12`; crypto_alt avg `-0.0047` n `228`; crypto_major avg `-0.0189` n `8`; equity avg `-0.0188` n `67`; fx avg `0.0162` n `6`; index avg `-0.0117` n `23`; metal avg `0.189` n `18`; unknown avg `-0.102` n `419`
- 1h: commodity avg `0.2456` n `12`; crypto_alt avg `0.0437` n `228`; crypto_major avg `0.0401` n `8`; equity avg `0.2116` n `67`; fx avg `0.0505` n `6`; index avg `0.0533` n `23`; metal avg `-0.1354` n `18`; unknown avg `-0.5039` n `419`
- 4h: commodity avg `0.3798` n `12`; crypto_alt avg `-0.8487` n `228`; crypto_major avg `-0.4508` n `8`; equity avg `-0.2596` n `67`; fx avg `0.0125` n `6`; index avg `-0.1913` n `23`; metal avg `-0.4922` n `18`; unknown avg `-0.447` n `419`
- 24h: commodity avg `0.5626` n `12`; crypto_alt avg `-4.9417` n `228`; crypto_major avg `-3.5767` n `8`; equity avg `-1.7931` n `67`; fx avg `-0.0568` n `6`; index avg `-1.1795` n `23`; metal avg `-1.1458` n `18`; unknown avg `-1.8388` n `408`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.187`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1771`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1761`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1651`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1622`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1559`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1458`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1405`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1366`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
