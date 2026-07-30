# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T07:22:32.915848+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0308` n `12`; crypto_alt avg `0.0313` n `230`; crypto_major avg `0.0514` n `8`; equity avg `-0.2149` n `102`; fx avg `0.0029` n `6`; index avg `-0.0689` n `25`; metal avg `-0.0059` n `20`; unknown avg `8.4739` n `779`
- 1h: commodity avg `-0.1278` n `12`; crypto_alt avg `0.1996` n `230`; crypto_major avg `0.2201` n `8`; equity avg `-0.2846` n `102`; fx avg `-0.016` n `6`; index avg `-0.0411` n `25`; metal avg `0.1016` n `20`; unknown avg `2.0229` n `779`
- 4h: commodity avg `0.3399` n `12`; crypto_alt avg `0.0268` n `230`; crypto_major avg `-0.1118` n `8`; equity avg `-0.1688` n `102`; fx avg `-0.0937` n `6`; index avg `-0.0931` n `25`; metal avg `-0.0612` n `20`; unknown avg `2.2485` n `747`
- 24h: commodity avg `0.8155` n `12`; crypto_alt avg `-0.251` n `230`; crypto_major avg `-0.6125` n `8`; equity avg `-3.3545` n `102`; fx avg `-0.0039` n `6`; index avg `-0.5` n `25`; metal avg `-0.1116` n `20`; unknown avg `-0.6722` n `745`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1573`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1186`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
