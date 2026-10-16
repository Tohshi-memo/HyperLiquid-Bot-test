# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T07:22:26.318145+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0062` n `13`; crypto_alt avg `0.2359` n `236`; crypto_major avg `0.1388` n `8`; equity avg `0.1321` n `151`; fx avg `0.013` n `6`; index avg `0.0212` n `26`; metal avg `0.0609` n `20`; unknown avg `0.1619` n `1136`
- 1h: commodity avg `0.1227` n `13`; crypto_alt avg `0.5827` n `236`; crypto_major avg `0.2793` n `8`; equity avg `0.2485` n `151`; fx avg `-0.006` n `6`; index avg `0.0557` n `26`; metal avg `0.1237` n `20`; unknown avg `0.9099` n `1134`
- 4h: commodity avg `0.1257` n `13`; crypto_alt avg `0.9106` n `236`; crypto_major avg `0.3974` n `8`; equity avg `0.051` n `151`; fx avg `-0.0656` n `6`; index avg `-0.004` n `26`; metal avg `0.0611` n `20`; unknown avg `0.3974` n `1102`
- 24h: commodity avg `0.1027` n `13`; crypto_alt avg `4.9512` n `236`; crypto_major avg `2.3758` n `8`; equity avg `2.6762` n `151`; fx avg `0.0054` n `6`; index avg `0.3746` n `26`; metal avg `0.4869` n `20`; unknown avg `26.61` n `904`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `-0.0989`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0941`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0926`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0909`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0765`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0668`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0597`, n `668`, weak_sample_signal
