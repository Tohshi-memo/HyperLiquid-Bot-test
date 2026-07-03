# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T14:52:25.722934+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0493` n `12`; crypto_alt avg `0.1478` n `229`; crypto_major avg `0.2796` n `8`; equity avg `0.04` n `88`; fx avg `-0.0062` n `6`; index avg `0.0055` n `25`; metal avg `0.04` n `20`; unknown avg `-0.1296` n `765`
- 1h: commodity avg `-0.0353` n `12`; crypto_alt avg `-0.143` n `229`; crypto_major avg `-0.0523` n `8`; equity avg `-0.0347` n `88`; fx avg `-0.0129` n `6`; index avg `-0.0537` n `25`; metal avg `0.0443` n `20`; unknown avg `0.2507` n `765`
- 4h: commodity avg `0.0312` n `12`; crypto_alt avg `0.4103` n `229`; crypto_major avg `0.2844` n `8`; equity avg `-0.2242` n `88`; fx avg `-0.0182` n `6`; index avg `-0.0054` n `25`; metal avg `-0.0713` n `20`; unknown avg `1.44` n `765`
- 24h: commodity avg `0.4433` n `12`; crypto_alt avg `2.5256` n `229`; crypto_major avg `2.2324` n `8`; equity avg `0.6652` n `88`; fx avg `-0.1152` n `6`; index avg `0.3056` n `25`; metal avg `0.5204` n `20`; unknown avg `7.6977` n `737`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0698`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0525`, n `668`, weak_sample_signal
