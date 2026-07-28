# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T21:02:28.533354+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.06` n `12`; crypto_alt avg `0.0564` n `230`; crypto_major avg `0.0587` n `8`; equity avg `0.1428` n `102`; fx avg `0.0082` n `6`; index avg `0.01` n `25`; metal avg `0.0054` n `20`; unknown avg `0.0965` n `776`
- 1h: commodity avg `0.0183` n `12`; crypto_alt avg `0.0829` n `230`; crypto_major avg `0.0716` n `8`; equity avg `0.6518` n `102`; fx avg `-0.006` n `6`; index avg `0.0554` n `25`; metal avg `0.0153` n `20`; unknown avg `0.0933` n `776`
- 4h: commodity avg `0.1205` n `12`; crypto_alt avg `-0.2193` n `230`; crypto_major avg `-0.1466` n `8`; equity avg `0.4909` n `102`; fx avg `-0.0331` n `6`; index avg `-0.0905` n `25`; metal avg `-0.1205` n `20`; unknown avg `0.7925` n `774`
- 24h: commodity avg `-0.8605` n `12`; crypto_alt avg `-2.1058` n `230`; crypto_major avg `-1.6764` n `8`; equity avg `-2.6871` n `102`; fx avg `-0.0918` n `6`; index avg `-0.3864` n `25`; metal avg `-0.4346` n `20`; unknown avg `1.0998` n `758`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
