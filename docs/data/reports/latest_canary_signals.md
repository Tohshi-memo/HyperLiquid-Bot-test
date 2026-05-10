# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-10T12:52:22.801568+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0193` n `12`; crypto_alt avg `0.09` n `228`; crypto_major avg `0.0152` n `8`; equity avg `-0.0083` n `65`; fx avg `0.0` n `5`; index avg `0.0037` n `23`; metal avg `0.0378` n `18`; unknown avg `0.003` n `376`
- 1h: commodity avg `-0.0943` n `12`; crypto_alt avg `0.0585` n `228`; crypto_major avg `-0.0171` n `8`; equity avg `-0.0067` n `65`; fx avg `-0.0006` n `5`; index avg `-0.0588` n `23`; metal avg `0.0662` n `18`; unknown avg `0.2959` n `376`
- 4h: commodity avg `-0.0036` n `12`; crypto_alt avg `-0.2659` n `228`; crypto_major avg `-0.3196` n `8`; equity avg `-0.0329` n `65`; fx avg `-0.0055` n `5`; index avg `0.0248` n `23`; metal avg `0.147` n `18`; unknown avg `0.1851` n `376`
- 24h: commodity avg `0.071` n `12`; crypto_alt avg `-0.2273` n `228`; crypto_major avg `-0.3277` n `8`; equity avg `0.8755` n `65`; fx avg `-0.0212` n `5`; index avg `0.2834` n `23`; metal avg `0.5152` n `18`; unknown avg `0.5317` n `366`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1472`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
