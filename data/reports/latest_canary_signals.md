# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T15:22:26.750970+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.012` n `12`; crypto_alt avg `-0.3621` n `229`; crypto_major avg `-0.3755` n `8`; equity avg `-0.0276` n `88`; fx avg `-0.0165` n `6`; index avg `-0.0014` n `25`; metal avg `0.0057` n `20`; unknown avg `-0.0211` n `765`
- 1h: commodity avg `-0.0165` n `12`; crypto_alt avg `0.0812` n `229`; crypto_major avg `0.1512` n `8`; equity avg `0.069` n `88`; fx avg `-0.0294` n `6`; index avg `0.0262` n `25`; metal avg `0.0081` n `20`; unknown avg `0.0477` n `765`
- 4h: commodity avg `-0.0214` n `12`; crypto_alt avg `0.4874` n `229`; crypto_major avg `0.8236` n `8`; equity avg `0.0275` n `88`; fx avg `-0.0929` n `6`; index avg `0.0524` n `25`; metal avg `0.0239` n `20`; unknown avg `0.1878` n `765`
- 24h: commodity avg `-0.0155` n `12`; crypto_alt avg `-1.4676` n `229`; crypto_major avg `-0.862` n `8`; equity avg `0.2456` n `88`; fx avg `-0.1032` n `6`; index avg `0.077` n `25`; metal avg `0.081` n `20`; unknown avg `-1.0479` n `731`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
