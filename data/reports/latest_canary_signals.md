# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T14:07:30.616950+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0012` n `12`; crypto_alt avg `0.2342` n `229`; crypto_major avg `0.3103` n `8`; equity avg `0.0401` n `88`; fx avg `-0.0009` n `6`; index avg `-0.0059` n `25`; metal avg `-0.0007` n `20`; unknown avg `-0.0092` n `765`
- 1h: commodity avg `-0.0257` n `12`; crypto_alt avg `0.1998` n `229`; crypto_major avg `0.2718` n `8`; equity avg `0.0125` n `88`; fx avg `-0.009` n `6`; index avg `-0.0068` n `25`; metal avg `-0.0035` n `20`; unknown avg `-0.0262` n `765`
- 4h: commodity avg `-0.0228` n `12`; crypto_alt avg `0.8129` n `229`; crypto_major avg `0.3532` n `8`; equity avg `-0.0548` n `88`; fx avg `-0.0051` n `6`; index avg `-0.0018` n `25`; metal avg `0.0091` n `20`; unknown avg `-0.0896` n `759`
- 24h: commodity avg `-0.1078` n `12`; crypto_alt avg `0.8539` n `229`; crypto_major avg `1.3785` n `8`; equity avg `0.309` n `88`; fx avg `-0.0525` n `6`; index avg `-0.0274` n `25`; metal avg `0.0584` n `20`; unknown avg `2.4028` n `741`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0698`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0617`, n `668`, weak_sample_signal
