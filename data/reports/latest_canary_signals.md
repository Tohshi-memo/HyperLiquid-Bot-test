# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T02:37:25.230019+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1101` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0399` n `12`; crypto_alt avg `-0.3657` n `228`; crypto_major avg `-0.3239` n `8`; equity avg `-0.2311` n `74`; fx avg `-0.0009` n `6`; index avg `-0.053` n `23`; metal avg `-0.1253` n `18`; unknown avg `-0.0562` n `547`
- 1h: commodity avg `-0.0183` n `12`; crypto_alt avg `-0.6174` n `228`; crypto_major avg `-0.7362` n `8`; equity avg `-0.6405` n `74`; fx avg `0.0214` n `6`; index avg `-0.1406` n `23`; metal avg `-0.5492` n `18`; unknown avg `-0.3318` n `547`
- 4h: commodity avg `-0.1778` n `12`; crypto_alt avg `-0.7705` n `228`; crypto_major avg `-1.2133` n `8`; equity avg `-0.4173` n `74`; fx avg `-0.0354` n `6`; index avg `-0.1032` n `23`; metal avg `-1.3279` n `18`; unknown avg `-0.5686` n `547`
- 24h: commodity avg `-0.6348` n `12`; crypto_alt avg `0.0924` n `228`; crypto_major avg `-2.5101` n `8`; equity avg `-2.5487` n `74`; fx avg `0.1214` n `6`; index avg `-0.9864` n `23`; metal avg `-2.7112` n `18`; unknown avg `-0.4946` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0544`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.048`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.044`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0412`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0398`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0376`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0352`, n `668`, weak_sample_signal
