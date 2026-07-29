# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T20:22:27.796425+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0323` n `12`; crypto_alt avg `0.0313` n `230`; crypto_major avg `0.1211` n `8`; equity avg `-0.2257` n `102`; fx avg `-0.0079` n `6`; index avg `0.0163` n `25`; metal avg `-0.0322` n `20`; unknown avg `0.0025` n `778`
- 1h: commodity avg `0.0558` n `12`; crypto_alt avg `-1.0634` n `230`; crypto_major avg `-0.7589` n `8`; equity avg `-2.0412` n `102`; fx avg `0.0114` n `6`; index avg `-0.496` n `25`; metal avg `-0.379` n `20`; unknown avg `-0.3714` n `778`
- 4h: commodity avg `0.0949` n `12`; crypto_alt avg `-0.6449` n `230`; crypto_major avg `-0.5684` n `8`; equity avg `-0.749` n `102`; fx avg `0.0964` n `6`; index avg `-0.2434` n `25`; metal avg `0.2599` n `20`; unknown avg `-0.4735` n `778`
- 24h: commodity avg `1.3884` n `12`; crypto_alt avg `-2.9094` n `230`; crypto_major avg `-1.0598` n `8`; equity avg `-3.8009` n `102`; fx avg `0.0054` n `6`; index avg `-0.7018` n `25`; metal avg `0.0367` n `20`; unknown avg `-0.7221` n `760`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1645`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
