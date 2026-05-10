# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-10T11:38:39.645450+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0139` n `12`; crypto_alt avg `0.1054` n `228`; crypto_major avg `0.0061` n `8`; equity avg `0.0045` n `65`; fx avg `-0.0066` n `5`; index avg `-0.0304` n `23`; metal avg `0.0021` n `18`; unknown avg `-0.113` n `376`
- 1h: commodity avg `0.0492` n `12`; crypto_alt avg `-0.0494` n `228`; crypto_major avg `-0.1672` n `8`; equity avg `-0.005` n `65`; fx avg `-0.0091` n `5`; index avg `-0.0149` n `23`; metal avg `0.0198` n `18`; unknown avg `0.1353` n `376`
- 4h: commodity avg `0.0012` n `12`; crypto_alt avg `0.0586` n `228`; crypto_major avg `-0.2004` n `8`; equity avg `-0.032` n `65`; fx avg `-0.0004` n `5`; index avg `-0.0064` n `23`; metal avg `0.0693` n `18`; unknown avg `0.3857` n `376`
- 24h: commodity avg `0.263` n `12`; crypto_alt avg `-0.5121` n `228`; crypto_major avg `-0.4031` n `8`; equity avg `0.8998` n `65`; fx avg `-0.0339` n `5`; index avg `0.2985` n `23`; metal avg `0.4354` n `18`; unknown avg `0.2713` n `366`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1467`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
