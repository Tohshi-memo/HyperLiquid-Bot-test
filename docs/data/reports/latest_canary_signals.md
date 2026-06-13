# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T13:11:50.723394+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0875` n `12`; crypto_alt avg `-0.0691` n `228`; crypto_major avg `0.0662` n `8`; equity avg `0.0238` n `74`; fx avg `0.0` n `6`; index avg `0.04` n `23`; metal avg `-0.1407` n `18`; unknown avg `1.0966` n `644`
- 1h: commodity avg `-0.1313` n `12`; crypto_alt avg `0.0907` n `228`; crypto_major avg `0.4657` n `8`; equity avg `0.1491` n `74`; fx avg `-0.0014` n `6`; index avg `0.1288` n `23`; metal avg `-0.0866` n `18`; unknown avg `1.277` n `644`
- 4h: commodity avg `-0.5764` n `12`; crypto_alt avg `0.5193` n `228`; crypto_major avg `0.6948` n `8`; equity avg `0.0664` n `74`; fx avg `0.1216` n `6`; index avg `0.1647` n `23`; metal avg `0.1166` n `18`; unknown avg `1.8001` n `635`
- 24h: commodity avg `-0.7606` n `12`; crypto_alt avg `1.1853` n `228`; crypto_major avg `0.6551` n `8`; equity avg `0.099` n `74`; fx avg `0.0312` n `6`; index avg `1.035` n `23`; metal avg `0.8876` n `18`; unknown avg `27.2043` n `611`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0606`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0596`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0576`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0561`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0521`, n `668`, weak_sample_signal
