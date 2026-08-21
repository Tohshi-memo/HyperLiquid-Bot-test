# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T13:37:25.984247+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0483` n `12`; crypto_alt avg `-0.0826` n `230`; crypto_major avg `0.12` n `8`; equity avg `-0.2205` n `121`; fx avg `-0.0164` n `6`; index avg `-0.08` n `25`; metal avg `-0.0361` n `20`; unknown avg `0.0107` n `793`
- 1h: commodity avg `0.0954` n `12`; crypto_alt avg `-0.2868` n `230`; crypto_major avg `0.3759` n `8`; equity avg `-0.3726` n `121`; fx avg `-0.0349` n `6`; index avg `-0.1316` n `25`; metal avg `0.0783` n `20`; unknown avg `1.1937` n `793`
- 4h: commodity avg `0.1336` n `12`; crypto_alt avg `1.1827` n `230`; crypto_major avg `-0.3223` n `8`; equity avg `-0.3396` n `121`; fx avg `-0.0104` n `6`; index avg `-0.0864` n `25`; metal avg `-0.0179` n `20`; unknown avg `1.4785` n `793`
- 24h: commodity avg `0.1834` n `12`; crypto_alt avg `8.1236` n `230`; crypto_major avg `6.93` n `8`; equity avg `0.9356` n `121`; fx avg `-0.0853` n `6`; index avg `-0.0259` n `25`; metal avg `0.8377` n `20`; unknown avg `3.4905` n `776`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2344`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1978`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1968`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1927`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
