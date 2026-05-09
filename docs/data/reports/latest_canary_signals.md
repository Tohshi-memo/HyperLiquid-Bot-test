# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T13:37:17.038253+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0077` n `12`; crypto_alt avg `0.0806` n `228`; crypto_major avg `0.0366` n `8`; equity avg `0.0142` n `65`; fx avg `-0.0187` n `5`; index avg `0.0185` n `23`; metal avg `-0.0142` n `18`; unknown avg `0.0104` n `376`
- 1h: commodity avg `0.0784` n `12`; crypto_alt avg `-0.4374` n `228`; crypto_major avg `-0.1115` n `8`; equity avg `-0.0043` n `65`; fx avg `-0.0127` n `5`; index avg `0.0512` n `23`; metal avg `-0.0289` n `18`; unknown avg `0.0558` n `376`
- 4h: commodity avg `0.0358` n `12`; crypto_alt avg `-0.427` n `228`; crypto_major avg `-0.2756` n `8`; equity avg `0.117` n `65`; fx avg `-0.0163` n `5`; index avg `0.0133` n `23`; metal avg `-0.0445` n `18`; unknown avg `-0.1757` n `376`
- 24h: commodity avg `0.0116` n `12`; crypto_alt avg `2.8564` n `228`; crypto_major avg `2.1027` n `8`; equity avg `2.2714` n `65`; fx avg `0.0072` n `5`; index avg `0.9615` n `23`; metal avg `-0.4155` n `18`; unknown avg `0.3159` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1168`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0643`, n `668`, weak_sample_signal
