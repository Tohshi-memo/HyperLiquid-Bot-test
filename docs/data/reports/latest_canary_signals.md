# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T22:37:25.294996+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0081` n `12`; crypto_alt avg `-0.0278` n `230`; crypto_major avg `-0.0448` n `8`; equity avg `0.0634` n `121`; fx avg `0.0215` n `6`; index avg `0.009` n `25`; metal avg `0.0245` n `20`; unknown avg `-0.0276` n `793`
- 1h: commodity avg `0.016` n `12`; crypto_alt avg `0.0933` n `230`; crypto_major avg `-0.4469` n `8`; equity avg `-0.0573` n `121`; fx avg `0.0101` n `6`; index avg `-0.0082` n `25`; metal avg `0.0233` n `20`; unknown avg `0.0498` n `793`
- 4h: commodity avg `-0.0631` n `12`; crypto_alt avg `0.9561` n `230`; crypto_major avg `0.4425` n `8`; equity avg `0.6813` n `121`; fx avg `-0.0248` n `6`; index avg `0.048` n `25`; metal avg `0.0767` n `20`; unknown avg `-0.2426` n `792`
- 24h: commodity avg `0.3871` n `12`; crypto_alt avg `4.4386` n `230`; crypto_major avg `4.474` n `8`; equity avg `-1.0274` n `121`; fx avg `0.2129` n `6`; index avg `-0.1351` n `25`; metal avg `0.1298` n `20`; unknown avg `2.5592` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.22`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1871`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1841`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1796`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
