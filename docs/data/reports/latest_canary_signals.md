# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T18:37:27.972416+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1109` n `12`; crypto_alt avg `-0.0803` n `230`; crypto_major avg `-0.085` n `8`; equity avg `-0.1355` n `102`; fx avg `0.0026` n `6`; index avg `-0.0045` n `25`; metal avg `0.0047` n `20`; unknown avg `0.1254` n `774`
- 1h: commodity avg `0.0194` n `12`; crypto_alt avg `-0.4022` n `230`; crypto_major avg `-0.5585` n `8`; equity avg `-0.0986` n `102`; fx avg `0.0258` n `6`; index avg `0.0232` n `25`; metal avg `-0.0276` n `20`; unknown avg `-0.1132` n `774`
- 4h: commodity avg `-0.1787` n `12`; crypto_alt avg `0.1422` n `230`; crypto_major avg `0.1736` n `8`; equity avg `0.391` n `102`; fx avg `-0.058` n `6`; index avg `-0.0332` n `25`; metal avg `0.0794` n `20`; unknown avg `-0.3404` n `774`
- 24h: commodity avg `-0.782` n `12`; crypto_alt avg `-1.2545` n `230`; crypto_major avg `-0.6298` n `8`; equity avg `-1.9778` n `102`; fx avg `0.0034` n `6`; index avg `-0.4922` n `25`; metal avg `0.1368` n `20`; unknown avg `-0.4101` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1863`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1302`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1279`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
