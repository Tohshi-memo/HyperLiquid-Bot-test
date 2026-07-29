# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T23:52:30.515331+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.025` n `12`; crypto_alt avg `0.0636` n `230`; crypto_major avg `0.028` n `8`; equity avg `0.0566` n `102`; fx avg `-0.0107` n `6`; index avg `-0.0062` n `25`; metal avg `-0.0215` n `20`; unknown avg `-0.0344` n `778`
- 1h: commodity avg `-0.0379` n `12`; crypto_alt avg `0.1908` n `230`; crypto_major avg `0.1148` n `8`; equity avg `0.2` n `102`; fx avg `-0.0201` n `6`; index avg `0.0277` n `25`; metal avg `0.0516` n `20`; unknown avg `0.052` n `778`
- 4h: commodity avg `-0.1172` n `12`; crypto_alt avg `0.5151` n `230`; crypto_major avg `0.6641` n `8`; equity avg `-0.209` n `102`; fx avg `0.0221` n `6`; index avg `0.031` n `25`; metal avg `0.1603` n `20`; unknown avg `0.8161` n `778`
- 24h: commodity avg `0.5926` n `12`; crypto_alt avg `-2.1768` n `230`; crypto_major avg `-0.3649` n `8`; equity avg `-3.7313` n `102`; fx avg `0.03` n `6`; index avg `-0.6769` n `25`; metal avg `0.384` n `20`; unknown avg `-0.7287` n `761`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.155`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1254`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
