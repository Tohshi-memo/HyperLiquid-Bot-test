# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T12:22:30.243838+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0976` n `12`; crypto_alt avg `0.0473` n `230`; crypto_major avg `0.0599` n `8`; equity avg `-0.0603` n `98`; fx avg `0.0061` n `6`; index avg `-0.0101` n `25`; metal avg `-0.0075` n `20`; unknown avg `-0.0081` n `771`
- 1h: commodity avg `0.0336` n `12`; crypto_alt avg `0.2222` n `230`; crypto_major avg `0.2519` n `8`; equity avg `0.1378` n `98`; fx avg `0.0043` n `6`; index avg `0.0128` n `25`; metal avg `0.0246` n `20`; unknown avg `-0.029` n `771`
- 4h: commodity avg `0.407` n `12`; crypto_alt avg `0.0218` n `230`; crypto_major avg `-0.0302` n `8`; equity avg `-0.0242` n `98`; fx avg `-0.0288` n `6`; index avg `0.0252` n `25`; metal avg `-0.0214` n `20`; unknown avg `0.0249` n `771`
- 24h: commodity avg `0.4014` n `12`; crypto_alt avg `1.7923` n `230`; crypto_major avg `2.0995` n `8`; equity avg `1.2629` n `98`; fx avg `-0.0518` n `6`; index avg `0.191` n `25`; metal avg `0.6808` n `20`; unknown avg `0.1501` n `754`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1486`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1272`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0881`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0613`, n `666`, weak_sample_signal
