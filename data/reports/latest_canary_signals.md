# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T13:22:34.959836+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1486` n `12`; crypto_alt avg `0.1335` n `230`; crypto_major avg `0.0028` n `8`; equity avg `0.1689` n `98`; fx avg `0.0048` n `6`; index avg `0.0415` n `25`; metal avg `0.0536` n `20`; unknown avg `0.1134` n `773`
- 1h: commodity avg `-0.1195` n `12`; crypto_alt avg `0.0906` n `230`; crypto_major avg `-0.0443` n `8`; equity avg `0.3287` n `98`; fx avg `0.0083` n `6`; index avg `0.0756` n `25`; metal avg `-0.0528` n `20`; unknown avg `0.3278` n `773`
- 4h: commodity avg `-0.1588` n `12`; crypto_alt avg `0.0116` n `230`; crypto_major avg `-0.2582` n `8`; equity avg `-0.419` n `98`; fx avg `0.0176` n `6`; index avg `-0.0517` n `25`; metal avg `0.0363` n `20`; unknown avg `0.7385` n `773`
- 24h: commodity avg `0.4289` n `12`; crypto_alt avg `-0.6493` n `230`; crypto_major avg `-1.6948` n `8`; equity avg `0.1745` n `98`; fx avg `0.0227` n `6`; index avg `-0.0535` n `25`; metal avg `0.5122` n `20`; unknown avg `0.7767` n `739`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1031`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.086`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0738`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0729`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0684`, n `666`, weak_sample_signal
