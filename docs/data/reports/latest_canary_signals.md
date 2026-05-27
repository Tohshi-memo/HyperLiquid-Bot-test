# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T19:52:20.594045+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0422` n `12`; crypto_alt avg `-0.2278` n `228`; crypto_major avg `-0.1152` n `8`; equity avg `-0.0009` n `67`; fx avg `-0.004` n `6`; index avg `-0.002` n `23`; metal avg `-0.0151` n `18`; unknown avg `-0.0963` n `419`
- 1h: commodity avg `0.1604` n `12`; crypto_alt avg `0.1605` n `228`; crypto_major avg `0.2214` n `8`; equity avg `0.0102` n `67`; fx avg `0.0034` n `6`; index avg `-0.0334` n `23`; metal avg `0.0201` n `18`; unknown avg `-0.0546` n `419`
- 4h: commodity avg `-0.4112` n `12`; crypto_alt avg `-0.7025` n `228`; crypto_major avg `-0.4945` n `8`; equity avg `0.538` n `67`; fx avg `0.0177` n `6`; index avg `0.3965` n `23`; metal avg `0.2912` n `18`; unknown avg `-0.6616` n `418`
- 24h: commodity avg `-1.1567` n `12`; crypto_alt avg `-0.4406` n `228`; crypto_major avg `-0.5139` n `8`; equity avg `-0.0653` n `67`; fx avg `-0.0725` n `6`; index avg `-0.5749` n `23`; metal avg `-1.2743` n `18`; unknown avg `-0.2793` n `400`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.169`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1684`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1571`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1567`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1546`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1441`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1421`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1413`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1301`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1294`, n `668`, weak_sample_signal
