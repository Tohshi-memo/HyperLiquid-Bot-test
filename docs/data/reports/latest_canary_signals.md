# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T19:28:14.728994+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0589` n `12`; crypto_alt avg `-0.133` n `228`; crypto_major avg `-0.1544` n `8`; equity avg `-0.0484` n `66`; fx avg `0.0009` n `6`; index avg `0.0214` n `23`; metal avg `-0.0747` n `18`; unknown avg `-0.0625` n `383`
- 1h: commodity avg `0.3202` n `12`; crypto_alt avg `-0.2237` n `228`; crypto_major avg `-0.1361` n `8`; equity avg `-0.4348` n `66`; fx avg `-0.0022` n `6`; index avg `-0.3217` n `23`; metal avg `-0.0901` n `18`; unknown avg `0.0464` n `383`
- 4h: commodity avg `0.5969` n `12`; crypto_alt avg `0.4919` n `228`; crypto_major avg `0.1972` n `8`; equity avg `1.146` n `66`; fx avg `-0.0151` n `6`; index avg `0.718` n `23`; metal avg `-0.1088` n `18`; unknown avg `1.4767` n `383`
- 24h: commodity avg `1.3287` n `12`; crypto_alt avg `0.5241` n `228`; crypto_major avg `0.5579` n `8`; equity avg `0.8513` n `66`; fx avg `0.0504` n `6`; index avg `0.0138` n `23`; metal avg `-2.2876` n `18`; unknown avg `1.3544` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1807`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
