# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T04:52:21.869987+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0294` n `12`; crypto_alt avg `0.1598` n `230`; crypto_major avg `0.155` n `8`; equity avg `0.1373` n `121`; fx avg `-0.0099` n `6`; index avg `0.0449` n `25`; metal avg `-0.0047` n `20`; unknown avg `-0.1309` n `793`
- 1h: commodity avg `-0.0407` n `12`; crypto_alt avg `0.25` n `230`; crypto_major avg `0.1324` n `8`; equity avg `0.0104` n `121`; fx avg `-0.0214` n `6`; index avg `0.0318` n `25`; metal avg `0.0698` n `20`; unknown avg `-0.0759` n `793`
- 4h: commodity avg `-0.0295` n `12`; crypto_alt avg `1.0924` n `230`; crypto_major avg `0.9507` n `8`; equity avg `0.1721` n `121`; fx avg `-0.0562` n `6`; index avg `0.0512` n `25`; metal avg `0.2745` n `20`; unknown avg `-0.0244` n `793`
- 24h: commodity avg `0.3013` n `12`; crypto_alt avg `5.8769` n `230`; crypto_major avg `7.0144` n `8`; equity avg `-0.6192` n `121`; fx avg `-0.0388` n `6`; index avg `-0.0992` n `25`; metal avg `0.5343` n `20`; unknown avg `2.6538` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.212`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1872`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1858`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1812`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
