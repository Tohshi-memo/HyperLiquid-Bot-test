# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T05:07:32.570331+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0035` n `12`; crypto_alt avg `-0.1184` n `230`; crypto_major avg `-0.1689` n `8`; equity avg `-0.2413` n `98`; fx avg `-0.0012` n `6`; index avg `-0.0523` n `25`; metal avg `0.0341` n `20`; unknown avg `-0.2035` n `771`
- 1h: commodity avg `0.0179` n `12`; crypto_alt avg `-0.0588` n `230`; crypto_major avg `-0.1221` n `8`; equity avg `-0.3777` n `98`; fx avg `0.0008` n `6`; index avg `-0.1104` n `25`; metal avg `-0.0458` n `20`; unknown avg `-0.3779` n `771`
- 4h: commodity avg `-0.0198` n `12`; crypto_alt avg `-0.3869` n `230`; crypto_major avg `-0.474` n `8`; equity avg `-0.8818` n `98`; fx avg `0.0335` n `6`; index avg `-0.1399` n `25`; metal avg `0.0532` n `20`; unknown avg `-0.4757` n `771`
- 24h: commodity avg `0.6236` n `12`; crypto_alt avg `-0.117` n `230`; crypto_major avg `-0.1809` n `8`; equity avg `1.9206` n `98`; fx avg `0.0855` n `6`; index avg `0.2103` n `25`; metal avg `0.778` n `20`; unknown avg `0.2635` n `755`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.097`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0624`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0538`, n `666`, weak_sample_signal
