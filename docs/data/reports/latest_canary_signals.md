# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T15:07:33.361712+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0614` n `12`; crypto_alt avg `-0.0412` n `230`; crypto_major avg `-0.1471` n `8`; equity avg `0.2298` n `98`; fx avg `-0.0086` n `6`; index avg `0.0284` n `25`; metal avg `-0.0341` n `20`; unknown avg `0.0555` n `771`
- 1h: commodity avg `0.0298` n `12`; crypto_alt avg `-0.2077` n `230`; crypto_major avg `-0.2935` n `8`; equity avg `0.6459` n `98`; fx avg `-0.0048` n `6`; index avg `0.1507` n `25`; metal avg `0.0954` n `20`; unknown avg `0.0061` n `771`
- 4h: commodity avg `0.1307` n `12`; crypto_alt avg `-0.0307` n `230`; crypto_major avg `0.0322` n `8`; equity avg `1.2529` n `98`; fx avg `-0.0013` n `6`; index avg `0.1562` n `25`; metal avg `0.0189` n `20`; unknown avg `0.1037` n `771`
- 24h: commodity avg `0.6143` n `12`; crypto_alt avg `1.6999` n `230`; crypto_major avg `1.897` n `8`; equity avg `3.0988` n `98`; fx avg `0.0005` n `6`; index avg `0.4442` n `25`; metal avg `0.6141` n `20`; unknown avg `0.3714` n `754`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.084`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0544`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0534`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0518`, n `668`, weak_sample_signal
