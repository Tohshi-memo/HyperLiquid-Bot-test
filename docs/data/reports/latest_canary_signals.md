# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T10:07:25.812266+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0331` n `12`; crypto_alt avg `-0.0826` n `230`; crypto_major avg `-0.2518` n `8`; equity avg `-0.0651` n `102`; fx avg `-0.016` n `6`; index avg `-0.0229` n `25`; metal avg `-0.0625` n `20`; unknown avg `0.0038` n `774`
- 1h: commodity avg `0.0206` n `12`; crypto_alt avg `0.101` n `230`; crypto_major avg `-0.1158` n `8`; equity avg `-0.2797` n `102`; fx avg `-0.0575` n `6`; index avg `-0.0563` n `25`; metal avg `-0.2232` n `20`; unknown avg `-0.0155` n `774`
- 4h: commodity avg `-0.3426` n `12`; crypto_alt avg `0.0903` n `230`; crypto_major avg `0.0435` n `8`; equity avg `0.1128` n `102`; fx avg `-0.0308` n `6`; index avg `0.0236` n `25`; metal avg `-0.1626` n `20`; unknown avg `0.0807` n `774`
- 24h: commodity avg `-0.4618` n `12`; crypto_alt avg `-3.5991` n `230`; crypto_major avg `-3.7209` n `8`; equity avg `-4.3915` n `102`; fx avg `-0.1938` n `6`; index avg `-0.913` n `25`; metal avg `-0.6767` n `20`; unknown avg `998.0782` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1547`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
