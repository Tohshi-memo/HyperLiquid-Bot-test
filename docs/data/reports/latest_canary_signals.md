# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T08:52:29.830917+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0777` n `12`; crypto_alt avg `0.1551` n `230`; crypto_major avg `0.1415` n `8`; equity avg `0.2058` n `102`; fx avg `0.006` n `6`; index avg `0.0073` n `25`; metal avg `-0.0025` n `20`; unknown avg `0.0381` n `784`
- 1h: commodity avg `0.2846` n `12`; crypto_alt avg `0.0456` n `230`; crypto_major avg `-0.067` n `8`; equity avg `-0.2071` n `102`; fx avg `0.0224` n `6`; index avg `-0.0467` n `25`; metal avg `-0.0405` n `20`; unknown avg `-0.0711` n `784`
- 4h: commodity avg `0.26` n `12`; crypto_alt avg `-0.2093` n `230`; crypto_major avg `-0.4794` n `8`; equity avg `-0.654` n `102`; fx avg `0.0214` n `6`; index avg `-0.0726` n `25`; metal avg `-0.0812` n `20`; unknown avg `-0.0748` n `768`
- 24h: commodity avg `0.0659` n `12`; crypto_alt avg `-1.0866` n `230`; crypto_major avg `-0.7331` n `8`; equity avg `0.0619` n `102`; fx avg `-0.0863` n `6`; index avg `-0.0921` n `25`; metal avg `-0.081` n `20`; unknown avg `0.9917` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0606`, n `668`, weak_sample_signal
