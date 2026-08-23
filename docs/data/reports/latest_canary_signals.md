# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T03:52:25.267419+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0073` n `12`; crypto_alt avg `0.0351` n `230`; crypto_major avg `0.06` n `8`; equity avg `0.0107` n `121`; fx avg `-0.0003` n `6`; index avg `-0.0006` n `25`; metal avg `0.0005` n `20`; unknown avg `0.0357` n `794`
- 1h: commodity avg `-0.0378` n `12`; crypto_alt avg `-1.395` n `230`; crypto_major avg `-0.7813` n `8`; equity avg `-0.0511` n `121`; fx avg `-0.0023` n `6`; index avg `0.001` n `25`; metal avg `-0.0038` n `20`; unknown avg `-0.09` n `794`
- 4h: commodity avg `-0.0408` n `12`; crypto_alt avg `-2.1062` n `230`; crypto_major avg `-0.5547` n `8`; equity avg `0.0964` n `121`; fx avg `0.0228` n `6`; index avg `0.0204` n `25`; metal avg `0.021` n `20`; unknown avg `1.6641` n `794`
- 24h: commodity avg `0.0604` n `12`; crypto_alt avg `-7.6764` n `230`; crypto_major avg `-3.7739` n `8`; equity avg `-0.315` n `121`; fx avg `0.0946` n `6`; index avg `-0.0486` n `25`; metal avg `-0.024` n `20`; unknown avg `3.1013` n `778`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1488`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
