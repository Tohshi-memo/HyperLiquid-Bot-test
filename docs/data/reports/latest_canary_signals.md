# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T02:52:24.771793+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0105` n `12`; crypto_alt avg `-0.0059` n `230`; crypto_major avg `0.0132` n `8`; equity avg `-0.0691` n `98`; fx avg `-0.0037` n `6`; index avg `-0.0026` n `25`; metal avg `-0.042` n `20`; unknown avg `-0.1211` n `771`
- 1h: commodity avg `-0.0965` n `12`; crypto_alt avg `-0.1102` n `230`; crypto_major avg `-0.243` n `8`; equity avg `-0.4149` n `98`; fx avg `0.005` n `6`; index avg `-0.0623` n `25`; metal avg `-0.0659` n `20`; unknown avg `0.0122` n `771`
- 4h: commodity avg `0.083` n `12`; crypto_alt avg `0.1776` n `230`; crypto_major avg `0.1743` n `8`; equity avg `-0.2135` n `98`; fx avg `0.0141` n `6`; index avg `0.0159` n `25`; metal avg `0.3918` n `20`; unknown avg `-0.1943` n `771`
- 24h: commodity avg `0.5932` n `12`; crypto_alt avg `0.7425` n `230`; crypto_major avg `0.4751` n `8`; equity avg `3.5372` n `98`; fx avg `0.0325` n `6`; index avg `0.4824` n `25`; metal avg `0.8971` n `20`; unknown avg `0.3701` n `755`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0971`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0614`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0599`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0578`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0515`, n `668`, weak_sample_signal
