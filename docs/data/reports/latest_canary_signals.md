# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T23:07:26.769861+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.102` n `12`; crypto_alt avg `-0.0364` n `228`; crypto_major avg `-0.0502` n `8`; equity avg `0.2758` n `74`; fx avg `0.0136` n `6`; index avg `0.1379` n `23`; metal avg `0.2288` n `18`; unknown avg `-0.0669` n `547`
- 1h: commodity avg `-0.1248` n `12`; crypto_alt avg `-0.0314` n `228`; crypto_major avg `-0.0978` n `8`; equity avg `-0.2013` n `74`; fx avg `0.0236` n `6`; index avg `-0.0441` n `23`; metal avg `-0.1425` n `18`; unknown avg `-0.0994` n `547`
- 4h: commodity avg `0.336` n `12`; crypto_alt avg `-0.4134` n `228`; crypto_major avg `-0.6156` n `8`; equity avg `-0.353` n `74`; fx avg `-0.0209` n `6`; index avg `0.3272` n `23`; metal avg `-0.4272` n `18`; unknown avg `-0.1206` n `547`
- 24h: commodity avg `-0.6414` n `12`; crypto_alt avg `-1.9512` n `228`; crypto_major avg `-3.4987` n `8`; equity avg `-2.1746` n `74`; fx avg `0.0802` n `6`; index avg `-0.8371` n `23`; metal avg `-1.6558` n `18`; unknown avg `-0.128` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0518`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0467`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0412`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0375`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0375`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0362`, n `668`, weak_sample_signal
