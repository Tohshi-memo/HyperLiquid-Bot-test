# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-10T12:37:15.906248+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0531` n `12`; crypto_alt avg `-0.0272` n `228`; crypto_major avg `-0.0056` n `8`; equity avg `-0.0133` n `65`; fx avg `0.0002` n `5`; index avg `-0.0321` n `23`; metal avg `-0.0009` n `18`; unknown avg `-0.0361` n `376`
- 1h: commodity avg `-0.0737` n `12`; crypto_alt avg `-0.1548` n `228`; crypto_major avg `-0.022` n `8`; equity avg `0.0386` n `65`; fx avg `-0.0006` n `5`; index avg `-0.0135` n `23`; metal avg `0.0578` n `18`; unknown avg `0.0113` n `376`
- 4h: commodity avg `0.0335` n `12`; crypto_alt avg `-0.2589` n `228`; crypto_major avg `-0.3345` n `8`; equity avg `0.0255` n `65`; fx avg `-0.0055` n `5`; index avg `0.0004` n `23`; metal avg `0.1233` n `18`; unknown avg `0.2072` n `376`
- 24h: commodity avg `0.1521` n `12`; crypto_alt avg `-0.3883` n `228`; crypto_major avg `-0.3361` n `8`; equity avg `0.865` n `65`; fx avg `-0.0212` n `5`; index avg `0.2913` n `23`; metal avg `0.4802` n `18`; unknown avg `0.5263` n `366`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1469`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1249`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
