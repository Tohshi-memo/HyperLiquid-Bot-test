# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T14:37:30.725081+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0341` n `12`; crypto_alt avg `-0.0428` n `229`; crypto_major avg `0.0392` n `8`; equity avg `-0.3149` n `88`; fx avg `-0.0034` n `6`; index avg `-0.0551` n `25`; metal avg `0.017` n `20`; unknown avg `-0.009` n `763`
- 1h: commodity avg `-0.1056` n `12`; crypto_alt avg `-0.7363` n `229`; crypto_major avg `-0.6006` n `8`; equity avg `-0.6806` n `88`; fx avg `-0.0045` n `6`; index avg `-0.1386` n `25`; metal avg `-0.1252` n `20`; unknown avg `0.1235` n `763`
- 4h: commodity avg `-0.0529` n `12`; crypto_alt avg `0.3344` n `229`; crypto_major avg `1.2394` n `8`; equity avg `0.3596` n `88`; fx avg `0.0118` n `6`; index avg `0.0492` n `25`; metal avg `0.5691` n `20`; unknown avg `-0.4354` n `763`
- 24h: commodity avg `-0.4005` n `12`; crypto_alt avg `2.1086` n `228`; crypto_major avg `3.6416` n `8`; equity avg `-1.0821` n `88`; fx avg `-0.0342` n `6`; index avg `-0.3266` n `25`; metal avg `0.304` n `20`; unknown avg `1.4147` n `739`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
