# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-10T08:52:19.935155+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0154` n `12`; crypto_alt avg `0.1531` n `228`; crypto_major avg `0.0366` n `8`; equity avg `0.0467` n `65`; fx avg `0.0` n `5`; index avg `-0.0284` n `23`; metal avg `0.0093` n `18`; unknown avg `0.016` n `376`
- 1h: commodity avg `0.0051` n `12`; crypto_alt avg `0.3407` n `228`; crypto_major avg `0.1865` n `8`; equity avg `0.0235` n `65`; fx avg `0.0045` n `5`; index avg `-0.0646` n `23`; metal avg `0.011` n `18`; unknown avg `0.1217` n `376`
- 4h: commodity avg `-0.0931` n `12`; crypto_alt avg `0.7158` n `228`; crypto_major avg `0.2933` n `8`; equity avg `0.0291` n `65`; fx avg `0.0064` n `5`; index avg `-0.0738` n `23`; metal avg `-0.0295` n `18`; unknown avg `-0.0193` n `366`
- 24h: commodity avg `0.0771` n `12`; crypto_alt avg `-0.5459` n `228`; crypto_major avg `-0.2398` n `8`; equity avg `0.9665` n `65`; fx avg `-0.0193` n `5`; index avg `0.2003` n `23`; metal avg `0.3494` n `18`; unknown avg `-0.1853` n `366`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1428`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
