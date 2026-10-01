# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T08:07:46.990092+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0502` n `13`; crypto_alt avg `-0.1369` n `234`; crypto_major avg `-0.0922` n `8`; equity avg `-0.065` n `142`; fx avg `0.0227` n `6`; index avg `-0.0018` n `26`; metal avg `-0.0047` n `20`; unknown avg `5.5509` n `957`
- 1h: commodity avg `0.197` n `13`; crypto_alt avg `-1.2592` n `234`; crypto_major avg `-1.062` n `8`; equity avg `-0.5639` n `142`; fx avg `0.0032` n `6`; index avg `-0.1485` n `26`; metal avg `-0.1906` n `20`; unknown avg `5.5404` n `957`
- 4h: commodity avg `0.7565` n `13`; crypto_alt avg `-1.01` n `234`; crypto_major avg `-0.5981` n `8`; equity avg `-0.283` n `142`; fx avg `-0.0016` n `6`; index avg `-0.1153` n `26`; metal avg `-0.1919` n `20`; unknown avg `2.9908` n `930`
- 24h: commodity avg `0.2758` n `13`; crypto_alt avg `0.4422` n `234`; crypto_major avg `0.5358` n `8`; equity avg `0.1681` n `142`; fx avg `0.1779` n `6`; index avg `0.0278` n `26`; metal avg `-0.3767` n `20`; unknown avg `773.4586` n `794`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1612`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.139`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1362`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1272`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
