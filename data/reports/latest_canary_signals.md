# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T23:51:30.542929+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0417` n `12`; crypto_alt avg `-0.0051` n `229`; crypto_major avg `-0.0994` n `8`; equity avg `-0.0859` n `88`; fx avg `0.0054` n `6`; index avg `0.0442` n `25`; metal avg `-0.1085` n `20`; unknown avg `-0.0999` n `765`
- 1h: commodity avg `-0.0611` n `12`; crypto_alt avg `-0.005` n `229`; crypto_major avg `-0.1065` n `8`; equity avg `-0.1248` n `88`; fx avg `0.0035` n `6`; index avg `0.0792` n `25`; metal avg `-0.0769` n `20`; unknown avg `-0.1639` n `765`
- 4h: commodity avg `-0.2091` n `12`; crypto_alt avg `0.6055` n `229`; crypto_major avg `0.9032` n `8`; equity avg `0.0103` n `88`; fx avg `0.0855` n `6`; index avg `0.0598` n `25`; metal avg `0.0823` n `20`; unknown avg `1.0077` n `765`
- 24h: commodity avg `-0.2144` n `12`; crypto_alt avg `0.1051` n `229`; crypto_major avg `0.7274` n `8`; equity avg `0.3366` n `88`; fx avg `0.0241` n `6`; index avg `0.1265` n `25`; metal avg `0.079` n `20`; unknown avg `1.2072` n `663`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0602`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0528`, n `668`, weak_sample_signal
