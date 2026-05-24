# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T11:04:34.898042+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0323` n `12`; crypto_alt avg `0.1526` n `228`; crypto_major avg `0.2269` n `8`; equity avg `0.1468` n `67`; fx avg `0.002` n `6`; index avg `0.0007` n `23`; metal avg `0.0117` n `18`; unknown avg `0.0898` n `396`
- 1h: commodity avg `0.0209` n `12`; crypto_alt avg `0.0163` n `228`; crypto_major avg `0.0834` n `8`; equity avg `0.2363` n `67`; fx avg `0.0025` n `6`; index avg `0.0108` n `23`; metal avg `-0.0531` n `18`; unknown avg `0.3142` n `396`
- 4h: commodity avg `0.3161` n `12`; crypto_alt avg `-0.0046` n `228`; crypto_major avg `0.4974` n `8`; equity avg `0.2769` n `67`; fx avg `0.0059` n `6`; index avg `-0.0276` n `23`; metal avg `0.0291` n `18`; unknown avg `-0.2295` n `396`
- 24h: commodity avg `-2.6815` n `12`; crypto_alt avg `3.7756` n `228`; crypto_major avg `4.7059` n `8`; equity avg `2.8218` n `67`; fx avg `0.0606` n `6`; index avg `1.4351` n `23`; metal avg `1.3595` n `18`; unknown avg `1.4951` n `386`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
