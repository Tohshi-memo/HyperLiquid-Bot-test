# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T00:22:29.748251+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0405` n `12`; crypto_alt avg `0.3013` n `230`; crypto_major avg `0.4511` n `8`; equity avg `0.1866` n `121`; fx avg `-0.0361` n `6`; index avg `0.0307` n `25`; metal avg `0.0063` n `20`; unknown avg `-0.0921` n `793`
- 1h: commodity avg `-0.0436` n `12`; crypto_alt avg `0.5471` n `230`; crypto_major avg `0.6072` n `8`; equity avg `0.2004` n `121`; fx avg `-0.083` n `6`; index avg `0.0404` n `25`; metal avg `-0.0411` n `20`; unknown avg `-0.0883` n `793`
- 4h: commodity avg `-0.0729` n `12`; crypto_alt avg `1.3794` n `230`; crypto_major avg `1.2218` n `8`; equity avg `0.307` n `121`; fx avg `-0.0718` n `6`; index avg `0.0591` n `25`; metal avg `0.0315` n `20`; unknown avg `-0.2562` n `792`
- 24h: commodity avg `0.2769` n `12`; crypto_alt avg `4.8091` n `230`; crypto_major avg `5.7228` n `8`; equity avg `-0.9218` n `121`; fx avg `0.1511` n `6`; index avg `-0.0981` n `25`; metal avg `0.1442` n `20`; unknown avg `2.5557` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2188`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1869`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1856`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.183`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
