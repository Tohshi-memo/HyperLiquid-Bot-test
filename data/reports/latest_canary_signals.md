# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T07:22:24.168680+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0102` n `12`; crypto_alt avg `0.2841` n `230`; crypto_major avg `0.182` n `8`; equity avg `0.0307` n `121`; fx avg `0.1526` n `6`; index avg `0.0001` n `25`; metal avg `0.0042` n `20`; unknown avg `0.0825` n `794`
- 1h: commodity avg `-0.0089` n `12`; crypto_alt avg `0.7296` n `230`; crypto_major avg `0.3095` n `8`; equity avg `0.0489` n `121`; fx avg `0.1563` n `6`; index avg `-0.0065` n `25`; metal avg `0.0142` n `20`; unknown avg `0.1016` n `794`
- 4h: commodity avg `-0.0116` n `12`; crypto_alt avg `-0.2077` n `230`; crypto_major avg `-0.8258` n `8`; equity avg `-0.1889` n `121`; fx avg `0.1557` n `6`; index avg `-0.0326` n `25`; metal avg `-0.0174` n `20`; unknown avg `0.377` n `778`
- 24h: commodity avg `-0.0222` n `12`; crypto_alt avg `-3.9443` n `230`; crypto_major avg `-2.3928` n `8`; equity avg `-0.0976` n `121`; fx avg `0.2617` n `6`; index avg `-0.0286` n `25`; metal avg `0.0721` n `20`; unknown avg `2.3012` n `778`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1552`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1307`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1204`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
