# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T21:22:12.777931+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0117` n `12`; crypto_alt avg `0.0276` n `228`; crypto_major avg `-0.0018` n `8`; equity avg `0.0262` n `65`; fx avg `-0.0289` n `5`; index avg `0.0122` n `23`; metal avg `0.0016` n `18`; unknown avg `0.0851` n `376`
- 1h: commodity avg `-0.0011` n `12`; crypto_alt avg `0.0599` n `228`; crypto_major avg `0.0437` n `8`; equity avg `0.1168` n `65`; fx avg `-0.0127` n `5`; index avg `0.0263` n `23`; metal avg `0.0176` n `18`; unknown avg `0.0482` n `376`
- 4h: commodity avg `-0.0071` n `12`; crypto_alt avg `0.1518` n `228`; crypto_major avg `0.1158` n `8`; equity avg `0.3304` n `65`; fx avg `-0.0117` n `5`; index avg `0.0482` n `23`; metal avg `0.1364` n `18`; unknown avg `-0.0706` n `376`
- 24h: commodity avg `0.2795` n `12`; crypto_alt avg `0.5337` n `228`; crypto_major avg `0.4792` n `8`; equity avg `0.8753` n `65`; fx avg `-0.0352` n `5`; index avg `0.4378` n `23`; metal avg `0.0426` n `18`; unknown avg `0.249` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1313`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
