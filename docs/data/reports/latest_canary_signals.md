# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T03:37:37.993978+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0013` n `12`; crypto_alt avg `-0.5836` n `230`; crypto_major avg `-0.3885` n `8`; equity avg `-0.0383` n `121`; fx avg `-0.0051` n `6`; index avg `0.0027` n `25`; metal avg `-0.005` n `20`; unknown avg `-0.165` n `794`
- 1h: commodity avg `-0.0206` n `12`; crypto_alt avg `-1.3068` n `230`; crypto_major avg `-0.8197` n `8`; equity avg `-0.0503` n `121`; fx avg `0.0092` n `6`; index avg `0.0007` n `25`; metal avg `-0.0017` n `20`; unknown avg `-0.2221` n `794`
- 4h: commodity avg `-0.0445` n `12`; crypto_alt avg `-1.6896` n `230`; crypto_major avg `-0.1365` n `8`; equity avg `0.0957` n `121`; fx avg `0.0168` n `6`; index avg `0.0179` n `25`; metal avg `0.0213` n `20`; unknown avg `1.7579` n `794`
- 24h: commodity avg `0.0679` n `12`; crypto_alt avg `-7.4679` n `230`; crypto_major avg `-3.8418` n `8`; equity avg `-0.3388` n `121`; fx avg `0.1035` n `6`; index avg `-0.0415` n `25`; metal avg `-0.0325` n `20`; unknown avg `3.0628` n `778`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1448`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1178`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
