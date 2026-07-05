# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T15:07:30.906174+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0047` n `12`; crypto_alt avg `0.3787` n `229`; crypto_major avg `0.4549` n `8`; equity avg `0.0866` n `88`; fx avg `-0.0066` n `6`; index avg `0.0052` n `25`; metal avg `0.005` n `20`; unknown avg `0.0262` n `765`
- 1h: commodity avg `-0.0038` n `12`; crypto_alt avg `0.4575` n `229`; crypto_major avg `0.5456` n `8`; equity avg `0.0559` n `88`; fx avg `-0.0384` n `6`; index avg `0.0444` n `25`; metal avg `0.0063` n `20`; unknown avg `0.0992` n `765`
- 4h: commodity avg `-0.0242` n `12`; crypto_alt avg `0.8309` n `229`; crypto_major avg `1.193` n `8`; equity avg `0.0296` n `88`; fx avg `-0.0751` n `6`; index avg `0.0538` n `25`; metal avg `0.0084` n `20`; unknown avg `0.2341` n `765`
- 24h: commodity avg `-0.0493` n `12`; crypto_alt avg `-0.7984` n `229`; crypto_major avg `-0.1927` n `8`; equity avg `0.325` n `88`; fx avg `-0.096` n `6`; index avg `0.0788` n `25`; metal avg `0.0746` n `20`; unknown avg `-0.9518` n `731`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
