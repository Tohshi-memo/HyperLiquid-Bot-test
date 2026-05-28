# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T08:37:19.239950+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0195` n `12`; crypto_alt avg `-0.047` n `228`; crypto_major avg `-0.1063` n `8`; equity avg `-0.0652` n `67`; fx avg `-0.0052` n `6`; index avg `-0.0339` n `23`; metal avg `-0.1007` n `18`; unknown avg `-0.0561` n `419`
- 1h: commodity avg `-0.1149` n `12`; crypto_alt avg `-0.4843` n `228`; crypto_major avg `-0.518` n `8`; equity avg `0.0519` n `67`; fx avg `-0.0224` n `6`; index avg `0.0398` n `23`; metal avg `-0.0216` n `18`; unknown avg `-0.2061` n `419`
- 4h: commodity avg `-0.5495` n `12`; crypto_alt avg `-0.2858` n `228`; crypto_major avg `-0.0172` n `8`; equity avg `1.2335` n `67`; fx avg `0.0311` n `6`; index avg `0.5257` n `23`; metal avg `0.8634` n `18`; unknown avg `-0.1004` n `409`
- 24h: commodity avg `0.6686` n `12`; crypto_alt avg `-5.2771` n `228`; crypto_major avg `-4.0017` n `8`; equity avg `-1.4675` n `67`; fx avg `-0.12` n `6`; index avg `-0.9872` n `23`; metal avg `-1.5328` n `18`; unknown avg `-1.6638` n `408`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.183`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1776`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1712`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1618`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1606`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1516`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1447`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1331`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1323`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1292`, n `668`, weak_sample_signal
