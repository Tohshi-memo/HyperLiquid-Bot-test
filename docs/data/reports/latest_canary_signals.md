# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T08:52:25.511764+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1187` n `12`; crypto_alt avg `0.0321` n `230`; crypto_major avg `0.018` n `8`; equity avg `-0.1405` n `102`; fx avg `0.0112` n `6`; index avg `-0.0259` n `25`; metal avg `-0.0709` n `20`; unknown avg `-0.0066` n `779`
- 1h: commodity avg `-0.0117` n `12`; crypto_alt avg `0.2455` n `230`; crypto_major avg `0.3813` n `8`; equity avg `0.4194` n `102`; fx avg `0.0284` n `6`; index avg `0.0807` n `25`; metal avg `0.192` n `20`; unknown avg `-0.0725` n `779`
- 4h: commodity avg `0.1861` n `12`; crypto_alt avg `0.2858` n `230`; crypto_major avg `0.3639` n `8`; equity avg `0.441` n `102`; fx avg `0.0081` n `6`; index avg `-0.0301` n `25`; metal avg `0.1774` n `20`; unknown avg `-0.0596` n `747`
- 24h: commodity avg `0.8611` n `12`; crypto_alt avg `-0.2023` n `230`; crypto_major avg `-0.3051` n `8`; equity avg `-2.9582` n `102`; fx avg `-0.0015` n `6`; index avg `-0.4501` n `25`; metal avg `0.1547` n `20`; unknown avg `-0.4573` n `745`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1506`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
