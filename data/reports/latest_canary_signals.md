# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T04:52:28.733794+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0345` n `12`; crypto_alt avg `-0.033` n `230`; crypto_major avg `0.001` n `8`; equity avg `-0.2434` n `102`; fx avg `0.0159` n `6`; index avg `-0.0439` n `25`; metal avg `-0.025` n `20`; unknown avg `-0.0904` n `779`
- 1h: commodity avg `0.0415` n `12`; crypto_alt avg `-0.3034` n `230`; crypto_major avg `-0.2697` n `8`; equity avg `-0.5513` n `102`; fx avg `-0.0319` n `6`; index avg `-0.0896` n `25`; metal avg `-0.0997` n `20`; unknown avg `-0.0419` n `779`
- 4h: commodity avg `-0.1103` n `12`; crypto_alt avg `0.4905` n `230`; crypto_major avg `0.2065` n `8`; equity avg `-0.6385` n `102`; fx avg `-0.0248` n `6`; index avg `-0.0156` n `25`; metal avg `-0.1944` n `20`; unknown avg `0.3192` n `778`
- 24h: commodity avg `0.6052` n `12`; crypto_alt avg `-0.0506` n `230`; crypto_major avg `-0.0001` n `8`; equity avg `-1.7969` n `102`; fx avg `0.0901` n `6`; index avg `0.0278` n `25`; metal avg `0.0845` n `20`; unknown avg `-0.4914` n `761`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1506`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
