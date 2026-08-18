# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T19:22:28.423710+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0269` n `12`; crypto_alt avg `-0.025` n `230`; crypto_major avg `0.01` n `8`; equity avg `0.0049` n `120`; fx avg `-0.0055` n `6`; index avg `-0.0013` n `25`; metal avg `0.0023` n `20`; unknown avg `0.0001` n `789`
- 1h: commodity avg `0.0106` n `12`; crypto_alt avg `-0.0281` n `230`; crypto_major avg `0.0272` n `8`; equity avg `-0.0539` n `120`; fx avg `-0.0026` n `6`; index avg `-0.0087` n `25`; metal avg `0.0166` n `20`; unknown avg `0.161` n `789`
- 4h: commodity avg `0.0557` n `12`; crypto_alt avg `-0.1019` n `230`; crypto_major avg `-0.0864` n `8`; equity avg `-0.237` n `120`; fx avg `-0.0022` n `6`; index avg `-0.01` n `25`; metal avg `0.0042` n `20`; unknown avg `3.9997` n `789`
- 24h: commodity avg `0.2954` n `12`; crypto_alt avg `-0.5401` n `230`; crypto_major avg `0.355` n `8`; equity avg `-4.3741` n `120`; fx avg `-0.0407` n `6`; index avg `-0.6681` n `25`; metal avg `-0.6738` n `20`; unknown avg `-0.1603` n `754`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0706`, n `668`, weak_sample_signal
