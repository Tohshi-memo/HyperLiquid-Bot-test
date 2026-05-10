# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-10T06:52:12.521841+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.015` n `12`; crypto_alt avg `0.0401` n `228`; crypto_major avg `0.0831` n `8`; equity avg `0.0462` n `65`; fx avg `0.0006` n `5`; index avg `0.0092` n `23`; metal avg `-0.0475` n `18`; unknown avg `0.1507` n `376`
- 1h: commodity avg `-0.0075` n `12`; crypto_alt avg `-0.1885` n `228`; crypto_major avg `0.0456` n `8`; equity avg `0.035` n `65`; fx avg `0.0006` n `5`; index avg `-0.02` n `23`; metal avg `-0.3315` n `18`; unknown avg `-0.0158` n `366`
- 4h: commodity avg `-0.1228` n `12`; crypto_alt avg `0.1055` n `228`; crypto_major avg `0.1699` n `8`; equity avg `0.2882` n `65`; fx avg `0.0043` n `5`; index avg `0.0149` n `23`; metal avg `0.1802` n `18`; unknown avg `-0.0058` n `366`
- 24h: commodity avg `0.1431` n `12`; crypto_alt avg `-1.2494` n `228`; crypto_major avg `-0.542` n `8`; equity avg `0.979` n `65`; fx avg `-0.0238` n `5`; index avg `0.2987` n `23`; metal avg `0.3642` n `18`; unknown avg `-0.3597` n `366`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1384`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
