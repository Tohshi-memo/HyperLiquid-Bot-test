# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T09:22:18.659351+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1894` n `12`; crypto_alt avg `0.0577` n `228`; crypto_major avg `0.0886` n `8`; equity avg `-0.0397` n `67`; fx avg `-0.0028` n `6`; index avg `-0.0074` n `23`; metal avg `0.0972` n `18`; unknown avg `0.0448` n `419`
- 1h: commodity avg `-0.0472` n `12`; crypto_alt avg `-0.1451` n `228`; crypto_major avg `-0.0295` n `8`; equity avg `-0.0469` n `67`; fx avg `-0.0048` n `6`; index avg `-0.0462` n `23`; metal avg `0.0143` n `18`; unknown avg `-0.0093` n `419`
- 4h: commodity avg `-0.5055` n `12`; crypto_alt avg `0.5153` n `228`; crypto_major avg `0.48` n `8`; equity avg `0.9953` n `67`; fx avg `0.0324` n `6`; index avg `0.3898` n `23`; metal avg `1.0091` n `18`; unknown avg `0.2504` n `409`
- 24h: commodity avg `0.8235` n `12`; crypto_alt avg `-4.7777` n `228`; crypto_major avg `-3.7437` n `8`; equity avg `-1.3833` n `67`; fx avg `-0.0884` n `6`; index avg `-0.9479` n `23`; metal avg `-1.6086` n `18`; unknown avg `-1.6933` n `408`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1845`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1722`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.172`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1671`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1642`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1481`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1466`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1343`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1303`, n `668`, weak_sample_signal
