# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-10T09:52:17.630530+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0147` n `12`; crypto_alt avg `0.12` n `228`; crypto_major avg `0.0395` n `8`; equity avg `-0.0066` n `65`; fx avg `0.0` n `5`; index avg `-0.0142` n `23`; metal avg `-0.0048` n `18`; unknown avg `0.0495` n `376`
- 1h: commodity avg `-0.0264` n `12`; crypto_alt avg `-0.0213` n `228`; crypto_major avg `0.0168` n `8`; equity avg `-0.0848` n `65`; fx avg `0.0043` n `5`; index avg `0.0437` n `23`; metal avg `0.0214` n `18`; unknown avg `0.1218` n `376`
- 4h: commodity avg `-0.106` n `12`; crypto_alt avg `0.443` n `228`; crypto_major avg `0.3218` n `8`; equity avg `-0.0051` n `65`; fx avg `0.0102` n `5`; index avg `-0.0243` n `23`; metal avg `-0.3281` n `18`; unknown avg `0.1831` n `366`
- 24h: commodity avg `0.0618` n `12`; crypto_alt avg `0.2633` n `228`; crypto_major avg `0.108` n `8`; equity avg `0.9539` n `65`; fx avg `-0.015` n `5`; index avg `0.2706` n `23`; metal avg `0.372` n `18`; unknown avg `0.1915` n `366`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1434`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
