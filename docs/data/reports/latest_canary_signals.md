# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T06:52:29.073635+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0717` n `12`; crypto_alt avg `0.0302` n `230`; crypto_major avg `0.0194` n `8`; equity avg `0.0146` n `98`; fx avg `0.0103` n `6`; index avg `0.0001` n `25`; metal avg `0.0031` n `20`; unknown avg `-0.0078` n `773`
- 1h: commodity avg `0.1017` n `12`; crypto_alt avg `0.1166` n `230`; crypto_major avg `0.1516` n `8`; equity avg `0.0264` n `98`; fx avg `0.0156` n `6`; index avg `-0.0088` n `25`; metal avg `-0.0615` n `20`; unknown avg `0.0085` n `741`
- 4h: commodity avg `0.1036` n `12`; crypto_alt avg `0.0827` n `230`; crypto_major avg `-0.075` n `8`; equity avg `0.2305` n `98`; fx avg `0.0207` n `6`; index avg `0.051` n `25`; metal avg `-0.0825` n `20`; unknown avg `-0.1237` n `741`
- 24h: commodity avg `0.7186` n `12`; crypto_alt avg `0.2217` n `230`; crypto_major avg `0.2834` n `8`; equity avg `0.5604` n `98`; fx avg `-0.0803` n `6`; index avg `0.1737` n `25`; metal avg `-0.0134` n `20`; unknown avg `1.6725` n `740`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1534`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.079`, n `666`, weak_sample_signal
