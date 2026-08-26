# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T04:55:05.414611+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0359` n `12`; crypto_alt avg `-0.3471` n `231`; crypto_major avg `-0.2464` n `8`; equity avg `-0.0693` n `122`; fx avg `0.0029` n `6`; index avg `-0.014` n `25`; metal avg `-0.0213` n `20`; unknown avg `-0.079` n `797`
- 1h: commodity avg `0.065` n `12`; crypto_alt avg `-0.1003` n `231`; crypto_major avg `-0.0369` n `8`; equity avg `-0.0524` n `122`; fx avg `-0.0103` n `6`; index avg `-0.0264` n `25`; metal avg `-0.0419` n `20`; unknown avg `0.2236` n `797`
- 4h: commodity avg `-0.0127` n `12`; crypto_alt avg `0.3974` n `231`; crypto_major avg `0.3488` n `8`; equity avg `0.6505` n `122`; fx avg `-0.0225` n `6`; index avg `0.1699` n `25`; metal avg `0.109` n `20`; unknown avg `0.9865` n `796`
- 24h: commodity avg `-0.7507` n `12`; crypto_alt avg `-2.7671` n `231`; crypto_major avg `-2.5591` n `8`; equity avg `1.3384` n `122`; fx avg `0.0317` n `6`; index avg `0.1913` n `25`; metal avg `0.305` n `20`; unknown avg `0.3463` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1857`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1422`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1372`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1233`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
