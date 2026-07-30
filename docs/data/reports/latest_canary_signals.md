# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T07:07:36.065271+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1076` n `12`; crypto_alt avg `0.1954` n `230`; crypto_major avg `0.2135` n `8`; equity avg `0.1386` n `102`; fx avg `-0.0025` n `6`; index avg `0.0374` n `25`; metal avg `0.0724` n `20`; unknown avg `-0.1047` n `779`
- 1h: commodity avg `-0.0554` n `12`; crypto_alt avg `0.1188` n `230`; crypto_major avg `-0.0024` n `8`; equity avg `-0.2374` n `102`; fx avg `-0.0228` n `6`; index avg `-0.0279` n `25`; metal avg `0.089` n `20`; unknown avg `-0.0906` n `779`
- 4h: commodity avg `0.3231` n `12`; crypto_alt avg `-0.1164` n `230`; crypto_major avg `-0.2308` n `8`; equity avg `-0.3962` n `102`; fx avg `-0.1164` n `6`; index avg `-0.1051` n `25`; metal avg `-0.1548` n `20`; unknown avg `-0.0027` n `747`
- 24h: commodity avg `0.8223` n `12`; crypto_alt avg `-0.3084` n `230`; crypto_major avg `-0.7412` n `8`; equity avg `-2.9828` n `102`; fx avg `-0.0122` n `6`; index avg `-0.4449` n `25`; metal avg `-0.1002` n `20`; unknown avg `-0.5829` n `745`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1594`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1187`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
