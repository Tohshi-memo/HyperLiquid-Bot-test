# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T14:52:27.909766+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0595` n `12`; crypto_alt avg `0.4108` n `232`; crypto_major avg `0.4306` n `8`; equity avg `-0.103` n `128`; fx avg `0.0168` n `6`; index avg `-0.0124` n `26`; metal avg `-0.0053` n `20`; unknown avg `0.3151` n `794`
- 1h: commodity avg `-0.1108` n `12`; crypto_alt avg `0.7923` n `232`; crypto_major avg `0.8567` n `8`; equity avg `-0.0691` n `128`; fx avg `0.0174` n `6`; index avg `-0.018` n `26`; metal avg `0.0247` n `20`; unknown avg `0.4293` n `790`
- 4h: commodity avg `-0.0771` n `12`; crypto_alt avg `-0.2726` n `232`; crypto_major avg `-0.1903` n `8`; equity avg `-0.1835` n `128`; fx avg `0.0485` n `6`; index avg `-0.0807` n `26`; metal avg `-0.2672` n `20`; unknown avg `0.342` n `790`
- 24h: commodity avg `0.5297` n `12`; crypto_alt avg `-1.0605` n `231`; crypto_major avg `-1.5715` n `8`; equity avg `-0.5823` n `128`; fx avg `-0.0802` n `6`; index avg `-0.1777` n `26`; metal avg `-0.5009` n `20`; unknown avg `0.9238` n `759`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0612`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0606`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.056`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0553`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0495`, n `668`, weak_sample_signal
