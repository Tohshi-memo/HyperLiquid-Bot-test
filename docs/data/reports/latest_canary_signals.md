# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T08:22:26.266853+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0081` n `12`; crypto_alt avg `0.0227` n `230`; crypto_major avg `0.0759` n `8`; equity avg `-0.0042` n `121`; fx avg `-0.0139` n `6`; index avg `-0.0005` n `25`; metal avg `0.0022` n `20`; unknown avg `0.4705` n `794`
- 1h: commodity avg `0.0224` n `12`; crypto_alt avg `0.6115` n `230`; crypto_major avg `0.3719` n `8`; equity avg `0.1017` n `121`; fx avg `-0.2051` n `6`; index avg `0.0149` n `25`; metal avg `0.006` n `20`; unknown avg `0.5871` n `794`
- 4h: commodity avg `0.0127` n `12`; crypto_alt avg `1.154` n `230`; crypto_major avg `0.0546` n `8`; equity avg `-0.0394` n `121`; fx avg `-0.0443` n `6`; index avg `-0.0209` n `25`; metal avg `0.001` n `20`; unknown avg `0.9978` n `778`
- 24h: commodity avg `-0.0099` n `12`; crypto_alt avg `-3.0957` n `230`; crypto_major avg `-1.4695` n `8`; equity avg `0.1056` n `121`; fx avg `0.0611` n `6`; index avg `0.0036` n `25`; metal avg `0.0609` n `20`; unknown avg `2.7237` n `778`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1478`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1253`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
