# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-10T11:37:14.274893+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0144` n `12`; crypto_alt avg `0.1214` n `228`; crypto_major avg `0.0069` n `8`; equity avg `0.0043` n `65`; fx avg `-0.0059` n `5`; index avg `-0.0189` n `23`; metal avg `-0.0` n `18`; unknown avg `-0.0938` n `376`
- 1h: commodity avg `0.0497` n `12`; crypto_alt avg `-0.0332` n `228`; crypto_major avg `-0.1665` n `8`; equity avg `-0.0051` n `65`; fx avg `-0.0085` n `5`; index avg `-0.0034` n `23`; metal avg `0.0177` n `18`; unknown avg `0.1545` n `376`
- 4h: commodity avg `0.0017` n `12`; crypto_alt avg `0.0749` n `228`; crypto_major avg `-0.1996` n `8`; equity avg `-0.0319` n `65`; fx avg `0.0002` n `5`; index avg `0.0051` n `23`; metal avg `0.0673` n `18`; unknown avg `0.4053` n `376`
- 24h: commodity avg `0.2635` n `12`; crypto_alt avg `-0.4966` n `228`; crypto_major avg `-0.4023` n `8`; equity avg `0.9003` n `65`; fx avg `-0.0333` n `5`; index avg `0.3101` n `23`; metal avg `0.4333` n `18`; unknown avg `0.2888` n `366`

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
