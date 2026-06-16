# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-16T08:07:39.016625+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1283` n `12`; crypto_alt avg `0.0216` n `228`; crypto_major avg `-0.0355` n `8`; equity avg `0.1622` n `77`; fx avg `0.0053` n `6`; index avg `0.0107` n `23`; metal avg `0.101` n `18`; unknown avg `0.0972` n `687`
- 1h: commodity avg `-0.5135` n `12`; crypto_alt avg `0.2243` n `228`; crypto_major avg `0.0738` n `8`; equity avg `0.1638` n `77`; fx avg `0.0311` n `6`; index avg `0.021` n `23`; metal avg `0.22` n `18`; unknown avg `-0.018` n `687`
- 4h: commodity avg `-0.4946` n `12`; crypto_alt avg `0.5243` n `228`; crypto_major avg `0.7663` n `8`; equity avg `0.4125` n `77`; fx avg `-0.0251` n `6`; index avg `0.0258` n `23`; metal avg `0.3035` n `18`; unknown avg `0.7621` n `647`
- 24h: commodity avg `0.169` n `12`; crypto_alt avg `0.8565` n `228`; crypto_major avg `2.8494` n `8`; equity avg `1.4516` n `76`; fx avg `-0.1129` n `6`; index avg `0.4215` n `23`; metal avg `0.073` n `18`; unknown avg `0.6212` n `623`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0595`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0576`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0539`, n `668`, weak_sample_signal
