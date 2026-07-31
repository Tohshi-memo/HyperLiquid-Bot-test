# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T07:32:54.354758+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0233` n `12`; crypto_alt avg `0.2083` n `230`; crypto_major avg `0.0785` n `8`; equity avg `0.127` n `102`; fx avg `0.0306` n `6`; index avg `0.0501` n `25`; metal avg `-0.006` n `20`; unknown avg `-0.0068` n `779`
- 1h: commodity avg `0.1248` n `12`; crypto_alt avg `-0.157` n `230`; crypto_major avg `-0.4777` n `8`; equity avg `0.0824` n `102`; fx avg `0.0772` n `6`; index avg `0.0658` n `25`; metal avg `-0.0578` n `20`; unknown avg `-0.0748` n `779`
- 4h: commodity avg `0.0564` n `12`; crypto_alt avg `-0.0201` n `230`; crypto_major avg `-0.2452` n `8`; equity avg `0.2341` n `102`; fx avg `-0.0485` n `6`; index avg `0.1168` n `25`; metal avg `-0.0471` n `20`; unknown avg `-0.0646` n `747`
- 24h: commodity avg `-0.4738` n `12`; crypto_alt avg `0.0554` n `230`; crypto_major avg `0.5909` n `8`; equity avg `8.7988` n `102`; fx avg `-0.1173` n `6`; index avg `1.4389` n `25`; metal avg `0.5815` n `20`; unknown avg `0.0198` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.13`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
