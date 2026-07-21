# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T11:07:31.720210+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0221` n `12`; crypto_alt avg `-0.059` n `230`; crypto_major avg `-0.0358` n `8`; equity avg `-0.1804` n `98`; fx avg `-0.0011` n `6`; index avg `-0.0187` n `25`; metal avg `-0.0704` n `20`; unknown avg `-0.0491` n `771`
- 1h: commodity avg `0.0565` n `12`; crypto_alt avg `-0.1914` n `230`; crypto_major avg `-0.3526` n `8`; equity avg `-0.2116` n `98`; fx avg `-0.008` n `6`; index avg `-0.0013` n `25`; metal avg `-0.036` n `20`; unknown avg `0.0697` n `771`
- 4h: commodity avg `0.2` n `12`; crypto_alt avg `-0.257` n `230`; crypto_major avg `-0.0969` n `8`; equity avg `0.1061` n `98`; fx avg `-0.0131` n `6`; index avg `0.0366` n `25`; metal avg `-0.1019` n `20`; unknown avg `0.0084` n `771`
- 24h: commodity avg `0.4637` n `12`; crypto_alt avg `1.9923` n `230`; crypto_major avg `2.1888` n `8`; equity avg `1.1498` n `98`; fx avg `-0.0902` n `6`; index avg `0.1981` n `25`; metal avg `0.5153` n `20`; unknown avg `0.1147` n `754`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1474`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1255`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0854`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0705`, n `666`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0677`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
