# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T13:37:20.751099+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2874` n `12`; crypto_alt avg `-0.1455` n `228`; crypto_major avg `-0.1297` n `8`; equity avg `-0.1704` n `67`; fx avg `0.0084` n `6`; index avg `-0.024` n `23`; metal avg `-0.4124` n `18`; unknown avg `0.8804` n `419`
- 1h: commodity avg `0.4833` n `12`; crypto_alt avg `-0.0894` n `228`; crypto_major avg `-0.1673` n `8`; equity avg `-0.1173` n `67`; fx avg `0.041` n `6`; index avg `-0.0162` n `23`; metal avg `-0.0861` n `18`; unknown avg `0.8806` n `419`
- 4h: commodity avg `0.5995` n `12`; crypto_alt avg `-0.6547` n `228`; crypto_major avg `-0.4979` n `8`; equity avg `0.0628` n `67`; fx avg `0.0945` n `6`; index avg `0.0832` n `23`; metal avg `-0.1798` n `18`; unknown avg `0.5999` n `419`
- 24h: commodity avg `0.9339` n `12`; crypto_alt avg `-4.8901` n `228`; crypto_major avg `-3.2841` n `8`; equity avg `-0.6613` n `67`; fx avg `0.0121` n `6`; index avg `-0.4792` n `23`; metal avg `-0.9332` n `18`; unknown avg `-1.8969` n `408`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1915`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1841`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1787`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1744`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1555`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1542`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1494`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1413`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1402`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
