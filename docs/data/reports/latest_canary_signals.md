# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T10:22:29.656151+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0295` n `12`; crypto_alt avg `-0.1917` n `230`; crypto_major avg `-0.1904` n `8`; equity avg `-0.043` n `100`; fx avg `-0.0032` n `6`; index avg `0.0094` n `25`; metal avg `-0.0055` n `20`; unknown avg `-0.0219` n `773`
- 1h: commodity avg `0.1117` n `12`; crypto_alt avg `-0.0893` n `230`; crypto_major avg `-0.0375` n `8`; equity avg `0.1716` n `100`; fx avg `-0.007` n `6`; index avg `0.0303` n `25`; metal avg `0.0498` n `20`; unknown avg `0.1576` n `773`
- 4h: commodity avg `-0.2787` n `12`; crypto_alt avg `-0.3867` n `230`; crypto_major avg `-0.2419` n `8`; equity avg `0.5571` n `100`; fx avg `-0.0564` n `6`; index avg `0.1343` n `25`; metal avg `0.2766` n `20`; unknown avg `0.2381` n `772`
- 24h: commodity avg `-0.2414` n `12`; crypto_alt avg `-1.2627` n `230`; crypto_major avg `-1.7137` n `8`; equity avg `-1.5886` n `99`; fx avg `-0.1465` n `6`; index avg `-0.4091` n `25`; metal avg `-0.2743` n `20`; unknown avg `0.2191` n `756`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1481`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1357`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0967`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0824`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0807`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
