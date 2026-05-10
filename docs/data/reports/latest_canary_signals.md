# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-10T09:07:13.790202+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0413` n `12`; crypto_alt avg `0.0419` n `228`; crypto_major avg `0.1261` n `8`; equity avg `-0.021` n `65`; fx avg `0.0` n `5`; index avg `0.0511` n `23`; metal avg `0.0121` n `18`; unknown avg `0.282` n `376`
- 1h: commodity avg `-0.04` n `12`; crypto_alt avg `0.4213` n `228`; crypto_major avg `0.3271` n `8`; equity avg `0.0207` n `65`; fx avg `0.003` n `5`; index avg `-0.0019` n `23`; metal avg `0.0361` n `18`; unknown avg `0.4955` n `376`
- 4h: commodity avg `-0.1355` n `12`; crypto_alt avg `0.8132` n `228`; crypto_major avg `0.4908` n `8`; equity avg `0.0407` n `65`; fx avg `0.0064` n `5`; index avg `-0.0087` n `23`; metal avg `0.002` n `18`; unknown avg `0.2016` n `366`
- 24h: commodity avg `0.032` n `12`; crypto_alt avg `-0.3919` n `228`; crypto_major avg `-0.1355` n `8`; equity avg `0.9623` n `65`; fx avg `-0.0193` n `5`; index avg `0.2231` n `23`; metal avg `0.3505` n `18`; unknown avg `0.0086` n `366`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1428`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
