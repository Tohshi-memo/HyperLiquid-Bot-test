# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T15:37:42.027611+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.73` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `1.907` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0947` n `12`; crypto_alt avg `0.137` n `230`; crypto_major avg `0.0084` n `8`; equity avg `-0.0081` n `102`; fx avg `-0.0068` n `6`; index avg `0.0038` n `25`; metal avg `0.0079` n `20`; unknown avg `0.0586` n `778`
- 1h: commodity avg `-0.0327` n `12`; crypto_alt avg `-0.0051` n `230`; crypto_major avg `0.0232` n `8`; equity avg `-0.2935` n `102`; fx avg `-0.043` n `6`; index avg `-0.065` n `25`; metal avg `0.019` n `20`; unknown avg `0.0296` n `778`
- 4h: commodity avg `0.5074` n `12`; crypto_alt avg `-0.4656` n `230`; crypto_major avg `-0.391` n `8`; equity avg `-2.298` n `102`; fx avg `-0.0253` n `6`; index avg `-0.3273` n `25`; metal avg `-0.1636` n `20`; unknown avg `1.1558` n `777`
- 24h: commodity avg `1.2908` n `12`; crypto_alt avg `-2.5177` n `230`; crypto_major avg `-0.5556` n `8`; equity avg `-2.0763` n `102`; fx avg `-0.0726` n `6`; index avg `-0.4831` n `25`; metal avg `-0.2806` n `20`; unknown avg `0.1684` n `758`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1937`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1567`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
