# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-10T10:07:14.839139+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0116` n `12`; crypto_alt avg `-0.4684` n `228`; crypto_major avg `-0.2232` n `8`; equity avg `-0.0302` n `65`; fx avg `0.0` n `5`; index avg `0.016` n `23`; metal avg `0.0063` n `18`; unknown avg `0.1985` n `376`
- 1h: commodity avg `0.0032` n `12`; crypto_alt avg `-0.531` n `228`; crypto_major avg `-0.3318` n `8`; equity avg `-0.0927` n `65`; fx avg `0.0043` n `5`; index avg `0.0085` n `23`; metal avg `0.0156` n `18`; unknown avg `0.0444` n `376`
- 4h: commodity avg `-0.1143` n `12`; crypto_alt avg `0.0423` n `228`; crypto_major avg `0.0728` n `8`; equity avg `-0.0402` n `65`; fx avg `0.0102` n `5`; index avg `-0.0077` n `23`; metal avg `-0.0883` n `18`; unknown avg `0.2103` n `376`
- 24h: commodity avg `0.0459` n `12`; crypto_alt avg `-0.1294` n `228`; crypto_major avg `-0.0511` n `8`; equity avg `0.8667` n `65`; fx avg `-0.015` n `5`; index avg `0.2885` n `23`; metal avg `0.3997` n `18`; unknown avg `0.4079` n `366`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1437`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
