# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T07:22:26.223114+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0295` n `12`; crypto_alt avg `0.3834` n `228`; crypto_major avg `0.3312` n `8`; equity avg `0.027` n `67`; fx avg `0.0169` n `6`; index avg `-0.0287` n `23`; metal avg `0.0564` n `18`; unknown avg `0.1483` n `419`
- 1h: commodity avg `-0.0988` n `12`; crypto_alt avg `0.5152` n `228`; crypto_major avg `0.5192` n `8`; equity avg `0.1277` n `67`; fx avg `0.0482` n `6`; index avg `0.0822` n `23`; metal avg `0.424` n `18`; unknown avg `0.3276` n `419`
- 4h: commodity avg `-0.2391` n `12`; crypto_alt avg `-1.5101` n `228`; crypto_major avg `-0.5349` n `8`; equity avg `0.2249` n `67`; fx avg `-0.0123` n `6`; index avg `-0.0074` n `23`; metal avg `0.4946` n `18`; unknown avg `-0.4173` n `409`
- 24h: commodity avg `0.2088` n `12`; crypto_alt avg `-4.5459` n `228`; crypto_major avg `-3.4462` n `8`; equity avg `-1.1148` n `67`; fx avg `-0.1186` n `6`; index avg `-0.8171` n `23`; metal avg `-1.2619` n `18`; unknown avg `-1.9377` n `408`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.185`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1715`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1687`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1686`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1631`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1558`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1519`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1352`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.133`, n `668`, weak_sample_signal
