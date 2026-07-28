# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T20:52:40.100342+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0329` n `12`; crypto_alt avg `0.081` n `230`; crypto_major avg `0.0682` n `8`; equity avg `0.0265` n `102`; fx avg `-0.0124` n `6`; index avg `-0.0064` n `25`; metal avg `-0.0022` n `20`; unknown avg `-0.0225` n `776`
- 1h: commodity avg `-0.0158` n `12`; crypto_alt avg `0.0252` n `230`; crypto_major avg `0.0559` n `8`; equity avg `0.5031` n `102`; fx avg `-0.0292` n `6`; index avg `0.007` n `25`; metal avg `-0.0287` n `20`; unknown avg `0.9482` n `776`
- 4h: commodity avg `0.0732` n `12`; crypto_alt avg `-0.4282` n `230`; crypto_major avg `-0.3902` n `8`; equity avg `0.1748` n `102`; fx avg `-0.0474` n `6`; index avg `-0.1302` n `25`; metal avg `-0.1111` n `20`; unknown avg `0.8181` n `774`
- 24h: commodity avg `-0.888` n `12`; crypto_alt avg `-2.0813` n `230`; crypto_major avg `-1.6264` n `8`; equity avg `-2.79` n `102`; fx avg `-0.1134` n `6`; index avg `-0.4032` n `25`; metal avg `-0.436` n `20`; unknown avg `1.1101` n `758`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
