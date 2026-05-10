# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-10T07:52:21.050003+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0948` n `12`; crypto_alt avg `-0.0265` n `228`; crypto_major avg `-0.037` n `8`; equity avg `0.0033` n `65`; fx avg `0.0` n `5`; index avg `0.0154` n `23`; metal avg `0.0021` n `18`; unknown avg `0.0736` n `376`
- 1h: commodity avg `-0.0771` n `12`; crypto_alt avg `0.3149` n `228`; crypto_major avg `0.0725` n `8`; equity avg `0.0196` n `65`; fx avg `0.0008` n `5`; index avg `0.0169` n `23`; metal avg `-0.0301` n `18`; unknown avg `-0.0687` n `376`
- 4h: commodity avg `-0.1485` n `12`; crypto_alt avg `0.409` n `228`; crypto_major avg `0.1058` n `8`; equity avg `0.1265` n `65`; fx avg `0.0026` n `5`; index avg `0.035` n `23`; metal avg `0.0724` n `18`; unknown avg `0.0055` n `366`
- 24h: commodity avg `0.0401` n `12`; crypto_alt avg `-0.6184` n `228`; crypto_major avg `-0.3496` n `8`; equity avg `1.103` n `65`; fx avg `-0.0246` n `5`; index avg `0.2872` n `23`; metal avg `0.3192` n `18`; unknown avg `-0.2453` n `366`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
