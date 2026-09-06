# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T02:37:26.993872+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.004` n `12`; crypto_alt avg `0.0783` n `232`; crypto_major avg `0.1113` n `8`; equity avg `0.0065` n `134`; fx avg `-0.0074` n `6`; index avg `-0.0146` n `26`; metal avg `-0.0002` n `20`; unknown avg `1.8347` n `794`
- 1h: commodity avg `-0.0051` n `12`; crypto_alt avg `-0.1051` n `232`; crypto_major avg `-0.0721` n `8`; equity avg `-0.0131` n `134`; fx avg `0.0118` n `6`; index avg `-0.0043` n `26`; metal avg `-0.0067` n `20`; unknown avg `0.6087` n `790`
- 4h: commodity avg `-0.0059` n `12`; crypto_alt avg `0.6399` n `232`; crypto_major avg `0.2253` n `8`; equity avg `0.0904` n `134`; fx avg `-0.0062` n `6`; index avg `-0.0233` n `26`; metal avg `-0.0235` n `20`; unknown avg `-0.4018` n `784`
- 24h: commodity avg `0.1489` n `12`; crypto_alt avg `3.116` n `232`; crypto_major avg `2.616` n `8`; equity avg `0.4323` n `134`; fx avg `-0.0641` n `6`; index avg `0.0451` n `26`; metal avg `0.0292` n `20`; unknown avg `0.7809` n `692`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1632`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.154`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1338`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
