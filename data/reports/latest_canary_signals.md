# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-10T09:37:18.615647+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0186` n `12`; crypto_alt avg `-0.0819` n `228`; crypto_major avg `-0.0876` n `8`; equity avg `-0.0454` n `65`; fx avg `0.0` n `5`; index avg `0.0118` n `23`; metal avg `-0.0003` n `18`; unknown avg `0.1118` n `376`
- 1h: commodity avg `-0.0257` n `12`; crypto_alt avg `0.0114` n `228`; crypto_major avg `0.014` n `8`; equity avg `-0.0324` n `65`; fx avg `0.0043` n `5`; index avg `0.0293` n `23`; metal avg `0.0355` n `18`; unknown avg `0.094` n `376`
- 4h: commodity avg `-0.138` n `12`; crypto_alt avg `0.317` n `228`; crypto_major avg `0.2382` n `8`; equity avg `0.0039` n `65`; fx avg `0.0115` n `5`; index avg `-0.007` n `23`; metal avg `-0.1264` n `18`; unknown avg `0.18` n `366`
- 24h: commodity avg `0.052` n `12`; crypto_alt avg `-0.101` n `228`; crypto_major avg `-0.1513` n `8`; equity avg `0.9378` n `65`; fx avg `-0.015` n `5`; index avg `0.2821` n `23`; metal avg `0.3755` n `18`; unknown avg `0.1055` n `366`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1433`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
