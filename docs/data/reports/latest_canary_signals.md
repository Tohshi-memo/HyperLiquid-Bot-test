# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T01:37:30.832392+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0185` n `12`; crypto_alt avg `-0.16` n `228`; crypto_major avg `-0.1923` n `8`; equity avg `-0.0151` n `74`; fx avg `-0.0248` n `6`; index avg `-0.0029` n `23`; metal avg `-0.0025` n `18`; unknown avg `11.4685` n `645`
- 1h: commodity avg `0.0299` n `12`; crypto_alt avg `-0.0523` n `228`; crypto_major avg `0.0234` n `8`; equity avg `0.0231` n `74`; fx avg `-0.015` n `6`; index avg `0.0646` n `23`; metal avg `0.1995` n `18`; unknown avg `18.0399` n `645`
- 4h: commodity avg `-0.3793` n `12`; crypto_alt avg `0.0706` n `228`; crypto_major avg `0.3761` n `8`; equity avg `0.1104` n `74`; fx avg `-0.0524` n `6`; index avg `-0.1282` n `23`; metal avg `-0.6807` n `18`; unknown avg `9.8276` n `644`
- 24h: commodity avg `-0.7701` n `12`; crypto_alt avg `1.3014` n `228`; crypto_major avg `1.3623` n `8`; equity avg `0.4965` n `74`; fx avg `-0.0181` n `6`; index avg `0.446` n `23`; metal avg `0.2637` n `18`; unknown avg `0.5865` n `611`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0636`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0594`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0575`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0569`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0549`, n `668`, weak_sample_signal
