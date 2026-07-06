# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T05:52:28.445933+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0301` n `12`; crypto_alt avg `-0.0676` n `229`; crypto_major avg `-0.0296` n `8`; equity avg `0.0635` n `88`; fx avg `0.0141` n `6`; index avg `0.0239` n `25`; metal avg `-0.0296` n `20`; unknown avg `1.5275` n `765`
- 1h: commodity avg `0.1218` n `12`; crypto_alt avg `-0.7269` n `229`; crypto_major avg `-0.5922` n `8`; equity avg `-0.0376` n `88`; fx avg `0.0109` n `6`; index avg `-0.0212` n `25`; metal avg `-0.0098` n `20`; unknown avg `1.5905` n `765`
- 4h: commodity avg `0.0784` n `12`; crypto_alt avg `-1.0517` n `229`; crypto_major avg `-0.9451` n `8`; equity avg `0.1172` n `88`; fx avg `0.0028` n `6`; index avg `0.0135` n `25`; metal avg `-0.3693` n `20`; unknown avg `0.5821` n `763`
- 24h: commodity avg `-0.1001` n `12`; crypto_alt avg `-0.0868` n `229`; crypto_major avg `0.9815` n `8`; equity avg `-0.702` n `88`; fx avg `0.0677` n `6`; index avg `-0.0801` n `25`; metal avg `-0.2463` n `20`; unknown avg `0.9811` n `661`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0618`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0566`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
