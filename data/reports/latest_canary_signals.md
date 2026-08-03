# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T09:07:35.095867+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0909` n `12`; crypto_alt avg `0.0349` n `230`; crypto_major avg `0.11` n `8`; equity avg `-0.0013` n `102`; fx avg `0.0067` n `6`; index avg `-0.0137` n `25`; metal avg `-0.0025` n `20`; unknown avg `0.0269` n `784`
- 1h: commodity avg `0.0687` n `12`; crypto_alt avg `0.0505` n `230`; crypto_major avg `0.0372` n `8`; equity avg `-0.0462` n `102`; fx avg `0.0395` n `6`; index avg `-0.0114` n `25`; metal avg `-0.0048` n `20`; unknown avg `-0.031` n `784`
- 4h: commodity avg `0.1737` n `12`; crypto_alt avg `-0.1451` n `230`; crypto_major avg `-0.2758` n `8`; equity avg `-0.5549` n `102`; fx avg `0.0376` n `6`; index avg `-0.0539` n `25`; metal avg `-0.0321` n `20`; unknown avg `-0.0454` n `768`
- 24h: commodity avg `-0.0331` n `12`; crypto_alt avg `-1.0098` n `230`; crypto_major avg `-0.5136` n `8`; equity avg `0.1507` n `102`; fx avg `-0.1406` n `6`; index avg `-0.0845` n `25`; metal avg `-0.0771` n `20`; unknown avg `1.0088` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0657`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0638`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0607`, n `668`, weak_sample_signal
