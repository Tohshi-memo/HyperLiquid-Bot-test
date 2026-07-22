# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T13:37:32.267090+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0232` n `12`; crypto_alt avg `0.1859` n `230`; crypto_major avg `0.2878` n `8`; equity avg `0.6452` n `98`; fx avg `0.0102` n `6`; index avg `0.0658` n `25`; metal avg `0.0379` n `20`; unknown avg `10.0647` n `773`
- 1h: commodity avg `-0.0499` n `12`; crypto_alt avg `0.3137` n `230`; crypto_major avg `0.2294` n `8`; equity avg `0.7539` n `98`; fx avg `0.0156` n `6`; index avg `0.0847` n `25`; metal avg `0.0033` n `20`; unknown avg `10.3007` n `773`
- 4h: commodity avg `-0.1102` n `12`; crypto_alt avg `0.3224` n `230`; crypto_major avg `0.2187` n `8`; equity avg `0.3825` n `98`; fx avg `0.008` n `6`; index avg `0.0399` n `25`; metal avg `0.0602` n `20`; unknown avg `10.7816` n `773`
- 24h: commodity avg `0.4208` n `12`; crypto_alt avg `-0.3554` n `230`; crypto_major avg `-1.3033` n `8`; equity avg `0.6178` n `98`; fx avg `0.0354` n `6`; index avg `-0.0197` n `25`; metal avg `0.5771` n `20`; unknown avg `0.8256` n `739`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1022`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0812`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0685`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0685`, n `666`, weak_sample_signal
