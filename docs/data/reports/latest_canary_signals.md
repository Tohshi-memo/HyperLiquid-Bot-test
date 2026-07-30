# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T07:18:05.678100+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0185` n `12`; crypto_alt avg `-0.0658` n `230`; crypto_major avg `-0.0636` n `8`; equity avg `-0.1298` n `102`; fx avg `0.001` n `6`; index avg `-0.0351` n `25`; metal avg `0.0356` n `20`; unknown avg `-0.0089` n `779`
- 1h: commodity avg `-0.1401` n `12`; crypto_alt avg `0.1021` n `230`; crypto_major avg `0.1049` n `8`; equity avg `-0.1997` n `102`; fx avg `-0.0179` n `6`; index avg `-0.0072` n `25`; metal avg `0.1433` n `20`; unknown avg `-0.1069` n `779`
- 4h: commodity avg `0.3275` n `12`; crypto_alt avg `-0.0707` n `230`; crypto_major avg `-0.2265` n `8`; equity avg `-0.0834` n `102`; fx avg `-0.0956` n `6`; index avg `-0.0594` n `25`; metal avg `-0.0198` n `20`; unknown avg `0.0295` n `747`
- 24h: commodity avg `0.8028` n `12`; crypto_alt avg `-0.3475` n `230`; crypto_major avg `-0.7267` n `8`; equity avg `-3.2722` n `102`; fx avg `-0.0058` n `6`; index avg `-0.467` n `25`; metal avg `-0.0703` n `20`; unknown avg `-0.6825` n `745`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1572`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1182`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
