# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-10T12:43:57.033303+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0556` n `12`; crypto_alt avg `0.0307` n `228`; crypto_major avg `0.0308` n `8`; equity avg `-0.0173` n `65`; fx avg `0.0002` n `5`; index avg `-0.0401` n `23`; metal avg `-0.0057` n `18`; unknown avg `-0.05` n `376`
- 1h: commodity avg `-0.0762` n `12`; crypto_alt avg `-0.0971` n `228`; crypto_major avg `0.0144` n `8`; equity avg `0.0339` n `65`; fx avg `-0.0006` n `5`; index avg `-0.0216` n `23`; metal avg `0.053` n `18`; unknown avg `-0.0025` n `376`
- 4h: commodity avg `0.031` n `12`; crypto_alt avg `-0.2025` n `228`; crypto_major avg `-0.2983` n `8`; equity avg `0.0206` n `65`; fx avg `-0.0055` n `5`; index avg `-0.0077` n `23`; metal avg `0.1185` n `18`; unknown avg `0.195` n `376`
- 24h: commodity avg `0.1496` n `12`; crypto_alt avg `-0.3318` n `228`; crypto_major avg `-0.2999` n `8`; equity avg `0.8613` n `65`; fx avg `-0.0212` n `5`; index avg `0.2832` n `23`; metal avg `0.4754` n `18`; unknown avg `0.5464` n `366`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1469`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1249`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
