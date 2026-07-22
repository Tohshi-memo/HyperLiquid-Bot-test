# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T08:52:29.897349+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0755` n `12`; crypto_alt avg `-0.038` n `230`; crypto_major avg `-0.0165` n `8`; equity avg `-0.0522` n `98`; fx avg `-0.0104` n `6`; index avg `-0.0043` n `25`; metal avg `-0.0754` n `20`; unknown avg `-0.0207` n `773`
- 1h: commodity avg `-0.0781` n `12`; crypto_alt avg `0.2684` n `230`; crypto_major avg `0.3322` n `8`; equity avg `0.1025` n `98`; fx avg `0.0012` n `6`; index avg `0.0377` n `25`; metal avg `0.0063` n `20`; unknown avg `0.1092` n `773`
- 4h: commodity avg `0.3316` n `12`; crypto_alt avg `-0.5891` n `230`; crypto_major avg `-0.93` n `8`; equity avg `-0.9717` n `98`; fx avg `-0.0643` n `6`; index avg `-0.2097` n `25`; metal avg `-0.1647` n `20`; unknown avg `-0.1304` n `739`
- 24h: commodity avg `0.8484` n `12`; crypto_alt avg `-0.9936` n `230`; crypto_major avg `-1.5826` n `8`; equity avg `0.3012` n `98`; fx avg `-0.0217` n `6`; index avg `-0.0088` n `25`; metal avg `0.2379` n `20`; unknown avg `0.0927` n `739`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1064`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0811`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0702`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.07`, n `666`, weak_sample_signal
