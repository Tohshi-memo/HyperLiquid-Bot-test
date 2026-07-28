# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T21:52:27.115239+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0855` n `12`; crypto_alt avg `0.0533` n `230`; crypto_major avg `0.119` n `8`; equity avg `0.0061` n `102`; fx avg `0.002` n `6`; index avg `0.0089` n `25`; metal avg `0.0125` n `20`; unknown avg `0.0286` n `776`
- 1h: commodity avg `0.2895` n `12`; crypto_alt avg `0.1915` n `230`; crypto_major avg `0.2775` n `8`; equity avg `0.1748` n `102`; fx avg `0.0279` n `6`; index avg `0.0563` n `25`; metal avg `0.0324` n `20`; unknown avg `-0.0215` n `776`
- 4h: commodity avg `0.1602` n `12`; crypto_alt avg `0.5537` n `230`; crypto_major avg `0.8595` n `8`; equity avg `1.0881` n `102`; fx avg `0.0161` n `6`; index avg `0.0542` n `25`; metal avg `0.0116` n `20`; unknown avg `0.4214` n `774`
- 24h: commodity avg `-0.6892` n `12`; crypto_alt avg `-1.7394` n `230`; crypto_major avg `-1.1405` n `8`; equity avg `-2.6763` n `102`; fx avg `-0.0732` n `6`; index avg `-0.3527` n `25`; metal avg `-0.4106` n `20`; unknown avg `0.2616` n `758`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0705`, n `668`, weak_sample_signal
