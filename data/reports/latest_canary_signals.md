# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T07:37:25.529107+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0311` n `12`; crypto_alt avg `0.1491` n `230`; crypto_major avg `-0.0784` n `8`; equity avg `0.1223` n `102`; fx avg `0.0207` n `6`; index avg `0.0409` n `25`; metal avg `-0.0087` n `20`; unknown avg `-0.0252` n `779`
- 1h: commodity avg `0.1326` n `12`; crypto_alt avg `-0.216` n `230`; crypto_major avg `-0.6339` n `8`; equity avg `0.0775` n `102`; fx avg `0.0672` n `6`; index avg `0.0566` n `25`; metal avg `-0.0605` n `20`; unknown avg `-0.0779` n `779`
- 4h: commodity avg `0.0642` n `12`; crypto_alt avg `-0.0793` n `230`; crypto_major avg `-0.4024` n `8`; equity avg `0.2295` n `102`; fx avg `-0.0585` n `6`; index avg `0.1075` n `25`; metal avg `-0.0498` n `20`; unknown avg `-0.0746` n `747`
- 24h: commodity avg `-0.466` n `12`; crypto_alt avg `-0.0041` n `230`; crypto_major avg `0.4307` n `8`; equity avg `8.7951` n `102`; fx avg `-0.1272` n `6`; index avg `1.4282` n `25`; metal avg `0.5789` n `20`; unknown avg `0.0094` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.13`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
