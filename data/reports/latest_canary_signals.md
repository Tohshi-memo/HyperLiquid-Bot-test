# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T11:37:17.907246+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1376` n `12`; crypto_alt avg `-0.0117` n `228`; crypto_major avg `-0.0296` n `8`; equity avg `0.0595` n `67`; fx avg `0.0222` n `6`; index avg `0.0124` n `23`; metal avg `-0.0754` n `18`; unknown avg `-0.2526` n `419`
- 1h: commodity avg `0.4844` n `12`; crypto_alt avg `-0.4964` n `228`; crypto_major avg `-0.2841` n `8`; equity avg `-0.0523` n `67`; fx avg `0.0161` n `6`; index avg `-0.0285` n `23`; metal avg `-0.1612` n `18`; unknown avg `-0.3684` n `419`
- 4h: commodity avg `0.3067` n `12`; crypto_alt avg `-1.0021` n `228`; crypto_major avg `-0.589` n `8`; equity avg `-0.2023` n `67`; fx avg `-0.0233` n `6`; index avg `-0.1226` n `23`; metal avg `-0.341` n `18`; unknown avg `-0.4631` n `419`
- 24h: commodity avg `0.7104` n `12`; crypto_alt avg `-5.4955` n `228`; crypto_major avg `-4.0209` n `8`; equity avg `-1.9195` n `67`; fx avg `-0.0836` n `6`; index avg `-1.2543` n `23`; metal avg `-1.2533` n `18`; unknown avg `-1.8097` n `408`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.188`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1777`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1743`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1728`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1666`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1561`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1463`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1429`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.138`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1365`, n `668`, weak_sample_signal
