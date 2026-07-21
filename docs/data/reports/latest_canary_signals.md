# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T15:57:52.031601+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.034` n `12`; crypto_alt avg `0.0447` n `230`; crypto_major avg `0.2115` n `8`; equity avg `0.0242` n `98`; fx avg `0.0018` n `6`; index avg `-0.0146` n `25`; metal avg `-0.0564` n `20`; unknown avg `0.0752` n `771`
- 1h: commodity avg `0.0998` n `12`; crypto_alt avg `0.0589` n `230`; crypto_major avg `-0.0131` n `8`; equity avg `0.3486` n `98`; fx avg `-0.0102` n `6`; index avg `0.0641` n `25`; metal avg `0.043` n `20`; unknown avg `0.0413` n `771`
- 4h: commodity avg `0.1212` n `12`; crypto_alt avg `0.002` n `230`; crypto_major avg `-0.0396` n `8`; equity avg `1.2835` n `98`; fx avg `-0.0049` n `6`; index avg `0.2016` n `25`; metal avg `0.085` n `20`; unknown avg `0.1129` n `771`
- 24h: commodity avg `0.6836` n `12`; crypto_alt avg `1.036` n `230`; crypto_major avg `1.0437` n `8`; equity avg `2.7637` n `98`; fx avg `0.0119` n `6`; index avg `0.3939` n `25`; metal avg `0.6141` n `20`; unknown avg `0.2116` n `754`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0865`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0596`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0559`, n `666`, weak_sample_signal
