# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T18:52:37.919109+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.088` n `12`; crypto_alt avg `-0.0492` n `230`; crypto_major avg `-0.1052` n `8`; equity avg `0.1072` n `102`; fx avg `0.0286` n `6`; index avg `0.0107` n `25`; metal avg `-0.0019` n `20`; unknown avg `0.0144` n `775`
- 1h: commodity avg `-0.1118` n `12`; crypto_alt avg `0.1116` n `230`; crypto_major avg `0.1856` n `8`; equity avg `0.0905` n `102`; fx avg `0.0264` n `6`; index avg `-0.0022` n `25`; metal avg `-0.0169` n `20`; unknown avg `-0.0396` n `774`
- 4h: commodity avg `-0.5342` n `12`; crypto_alt avg `0.1224` n `230`; crypto_major avg `0.343` n `8`; equity avg `0.4835` n `102`; fx avg `0.0184` n `6`; index avg `0.0287` n `25`; metal avg `0.032` n `20`; unknown avg `-0.3525` n `774`
- 24h: commodity avg `-0.9867` n `12`; crypto_alt avg `-1.8241` n `230`; crypto_major avg `-1.6356` n `8`; equity avg `-2.8333` n `102`; fx avg `-0.0874` n `6`; index avg `-0.2903` n `25`; metal avg `-0.3764` n `20`; unknown avg `-0.4504` n `758`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0638`, n `668`, weak_sample_signal
