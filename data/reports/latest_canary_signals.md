# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T05:22:31.784635+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0091` n `12`; crypto_alt avg `0.0097` n `230`; crypto_major avg `0.0265` n `8`; equity avg `0.0851` n `98`; fx avg `-0.0115` n `6`; index avg `0.0156` n `25`; metal avg `-0.0237` n `20`; unknown avg `-0.0282` n `773`
- 1h: commodity avg `0.0075` n `12`; crypto_alt avg `0.0002` n `230`; crypto_major avg `-0.0805` n `8`; equity avg `0.0336` n `98`; fx avg `0.0074` n `6`; index avg `0.017` n `25`; metal avg `-0.0958` n `20`; unknown avg `-0.2472` n `773`
- 4h: commodity avg `0.0237` n `12`; crypto_alt avg `-0.279` n `230`; crypto_major avg `-0.3246` n `8`; equity avg `-0.4127` n `98`; fx avg `-0.0113` n `6`; index avg `-0.0503` n `25`; metal avg `-0.0919` n `20`; unknown avg `-0.162` n `773`
- 24h: commodity avg `0.7421` n `12`; crypto_alt avg `-0.2426` n `230`; crypto_major avg `-0.194` n `8`; equity avg `0.1746` n `98`; fx avg `-0.1302` n `6`; index avg `0.0929` n `25`; metal avg `-0.077` n `20`; unknown avg `1.5488` n `739`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1583`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0771`, n `666`, weak_sample_signal
