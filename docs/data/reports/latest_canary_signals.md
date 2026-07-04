# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T23:52:31.125995+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0083` n `12`; crypto_alt avg `-0.0479` n `229`; crypto_major avg `-0.0245` n `8`; equity avg `0.0019` n `88`; fx avg `0.0039` n `6`; index avg `-0.0015` n `25`; metal avg `0.0098` n `20`; unknown avg `-0.0336` n `765`
- 1h: commodity avg `-0.0233` n `12`; crypto_alt avg `-0.1785` n `229`; crypto_major avg `-0.1894` n `8`; equity avg `-0.0459` n `88`; fx avg `0.0032` n `6`; index avg `0.0034` n `25`; metal avg `0.0138` n `20`; unknown avg `-0.4616` n `765`
- 4h: commodity avg `-0.0001` n `12`; crypto_alt avg `-0.6921` n `229`; crypto_major avg `-0.4212` n `8`; equity avg `0.0203` n `88`; fx avg `0.0318` n `6`; index avg `0.0216` n `25`; metal avg `0.0388` n `20`; unknown avg `-0.3028` n `765`
- 24h: commodity avg `0.0101` n `12`; crypto_alt avg `-0.2325` n `229`; crypto_major avg `0.2927` n `8`; equity avg `0.3017` n `88`; fx avg `-0.0087` n `6`; index avg `0.0245` n `25`; metal avg `0.0805` n `20`; unknown avg `-0.6566` n `741`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.064`, n `668`, weak_sample_signal
