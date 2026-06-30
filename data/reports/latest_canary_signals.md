# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T03:07:34.550174+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0147` n `12`; crypto_alt avg `0.0369` n `228`; crypto_major avg `-0.0251` n `8`; equity avg `-0.0147` n `88`; fx avg `-0.0072` n `6`; index avg `0.0087` n `23`; metal avg `0.0064` n `20`; unknown avg `0.024` n `765`
- 1h: commodity avg `0.0375` n `12`; crypto_alt avg `0.266` n `228`; crypto_major avg `0.1485` n `8`; equity avg `0.2224` n `88`; fx avg `-0.0248` n `6`; index avg `0.062` n `23`; metal avg `0.0119` n `20`; unknown avg `-0.3106` n `765`
- 4h: commodity avg `0.0924` n `12`; crypto_alt avg `-0.4344` n `228`; crypto_major avg `-0.8694` n `8`; equity avg `-0.004` n `88`; fx avg `0.0175` n `6`; index avg `0.0128` n `23`; metal avg `-0.4814` n `20`; unknown avg `-0.0065` n `763`
- 24h: commodity avg `-0.1809` n `12`; crypto_alt avg `-0.074` n `228`; crypto_major avg `0.9153` n `8`; equity avg `1.9942` n `88`; fx avg `0.1359` n `6`; index avg `0.296` n `23`; metal avg `-0.7975` n `20`; unknown avg `1.5218` n `728`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.127`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1086`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0825`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
