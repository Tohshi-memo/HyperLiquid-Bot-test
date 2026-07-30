# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T04:07:30.961540+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0093` n `12`; crypto_alt avg `-0.1488` n `230`; crypto_major avg `-0.158` n `8`; equity avg `-0.2593` n `102`; fx avg `-0.01` n `6`; index avg `-0.0651` n `25`; metal avg `-0.0293` n `20`; unknown avg `0.0496` n `779`
- 1h: commodity avg `0.0876` n `12`; crypto_alt avg `-0.192` n `230`; crypto_major avg `-0.2258` n `8`; equity avg `-0.3534` n `102`; fx avg `-0.0448` n `6`; index avg `-0.0459` n `25`; metal avg `-0.1035` n `20`; unknown avg `0.2172` n `779`
- 4h: commodity avg `-0.0713` n `12`; crypto_alt avg `0.3889` n `230`; crypto_major avg `-0.0736` n `8`; equity avg `-0.3636` n `102`; fx avg `-0.0249` n `6`; index avg `-0.0095` n `25`; metal avg `-0.2627` n `20`; unknown avg `0.2235` n `778`
- 24h: commodity avg `0.4401` n `12`; crypto_alt avg `0.5872` n `230`; crypto_major avg `0.5509` n `8`; equity avg `-1.2019` n `102`; fx avg `0.0172` n `6`; index avg `0.0801` n `25`; metal avg `0.2162` n `20`; unknown avg `-0.45` n `761`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1486`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
