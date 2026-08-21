# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T01:22:33.972521+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0398` n `12`; crypto_alt avg `-0.0708` n `230`; crypto_major avg `0.0569` n `8`; equity avg `0.0762` n `121`; fx avg `-0.0457` n `6`; index avg `0.0478` n `25`; metal avg `0.0819` n `20`; unknown avg `0.1033` n `793`
- 1h: commodity avg `0.1051` n `12`; crypto_alt avg `-0.3344` n `230`; crypto_major avg `0.0224` n `8`; equity avg `0.0891` n `121`; fx avg `-0.024` n `6`; index avg `0.0298` n `25`; metal avg `0.1204` n `20`; unknown avg `-0.021` n `793`
- 4h: commodity avg `0.0752` n `12`; crypto_alt avg `0.6618` n `230`; crypto_major avg `0.8273` n `8`; equity avg `0.3398` n `121`; fx avg `-0.0964` n `6`; index avg `0.0528` n `25`; metal avg `0.1764` n `20`; unknown avg `-0.2656` n `793`
- 24h: commodity avg `0.3419` n `12`; crypto_alt avg `4.7058` n `230`; crypto_major avg `6.2814` n `8`; equity avg `-0.9597` n `121`; fx avg `0.0212` n `6`; index avg `-0.1362` n `25`; metal avg `0.4116` n `20`; unknown avg `2.6233` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2185`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1862`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1851`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1804`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
