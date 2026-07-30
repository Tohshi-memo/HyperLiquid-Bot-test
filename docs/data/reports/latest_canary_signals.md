# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T06:52:31.395266+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0308` n `12`; crypto_alt avg `-0.1119` n `230`; crypto_major avg `-0.0784` n `8`; equity avg `-0.1596` n `102`; fx avg `-0.0002` n `6`; index avg `-0.0085` n `25`; metal avg `0.0374` n `20`; unknown avg `53.3488` n `779`
- 1h: commodity avg `0.0846` n `12`; crypto_alt avg `-0.0457` n `230`; crypto_major avg `-0.1291` n `8`; equity avg `-0.2362` n `102`; fx avg `-0.0318` n `6`; index avg `-0.0636` n `25`; metal avg `0.0049` n `20`; unknown avg `55.6451` n `747`
- 4h: commodity avg `0.4091` n `12`; crypto_alt avg `-0.3431` n `230`; crypto_major avg `-0.5136` n `8`; equity avg `-0.7564` n `102`; fx avg `-0.0965` n `6`; index avg `-0.1823` n `25`; metal avg `-0.2626` n `20`; unknown avg `51.4448` n `747`
- 24h: commodity avg `0.9338` n `12`; crypto_alt avg `-0.5115` n `230`; crypto_major avg `-0.9556` n `8`; equity avg `-3.0994` n `102`; fx avg `-0.0013` n `6`; index avg `-0.4576` n `25`; metal avg `-0.1598` n `20`; unknown avg `-0.6096` n `745`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1607`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1188`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0836`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
