# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-16T06:07:36.436485+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0952` n `12`; crypto_alt avg `0.0457` n `228`; crypto_major avg `0.0333` n `8`; equity avg `0.0604` n `77`; fx avg `-0.0098` n `6`; index avg `-0.0032` n `23`; metal avg `-0.024` n `18`; unknown avg `0.0314` n `647`
- 1h: commodity avg `0.0367` n `12`; crypto_alt avg `0.2689` n `228`; crypto_major avg `0.249` n `8`; equity avg `0.0162` n `77`; fx avg `-0.0192` n `6`; index avg `-0.2354` n `23`; metal avg `-0.2687` n `18`; unknown avg `0.2569` n `647`
- 4h: commodity avg `-0.2264` n `12`; crypto_alt avg `0.2678` n `228`; crypto_major avg `0.4915` n `8`; equity avg `0.345` n `77`; fx avg `-0.0467` n `6`; index avg `0.0491` n `23`; metal avg `0.2848` n `18`; unknown avg `0.5037` n `639`
- 24h: commodity avg `0.1544` n `12`; crypto_alt avg `0.2134` n `228`; crypto_major avg `2.2751` n `8`; equity avg `1.2032` n `76`; fx avg `-0.1079` n `6`; index avg `0.38` n `23`; metal avg `-0.1243` n `18`; unknown avg `0.7469` n `623`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0564`, n `668`, weak_sample_signal
