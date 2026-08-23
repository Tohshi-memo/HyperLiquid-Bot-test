# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T12:07:27.787008+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0001` n `12`; crypto_alt avg `-0.213` n `230`; crypto_major avg `-0.4923` n `8`; equity avg `-0.0053` n `121`; fx avg `0.0034` n `6`; index avg `0.0036` n `25`; metal avg `-0.0093` n `20`; unknown avg `0.2403` n `795`
- 1h: commodity avg `0.0026` n `12`; crypto_alt avg `0.4949` n `230`; crypto_major avg `0.283` n `8`; equity avg `0.0816` n `121`; fx avg `0.0027` n `6`; index avg `0.0072` n `25`; metal avg `0.0108` n `20`; unknown avg `1.4872` n `795`
- 4h: commodity avg `-0.0338` n `12`; crypto_alt avg `2.0338` n `230`; crypto_major avg `0.9855` n `8`; equity avg `0.2328` n `121`; fx avg `-0.0124` n `6`; index avg `0.0366` n `25`; metal avg `0.0103` n `20`; unknown avg `0.774` n `794`
- 24h: commodity avg `0.0005` n `12`; crypto_alt avg `-0.2878` n `230`; crypto_major avg `0.1566` n `8`; equity avg `0.4063` n `121`; fx avg `0.0345` n `6`; index avg `0.0384` n `25`; metal avg `0.0431` n `20`; unknown avg `3.3329` n `778`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
