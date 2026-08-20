# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T23:18:08.268964+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.001` n `12`; crypto_alt avg `0.0484` n `230`; crypto_major avg `0.1709` n `8`; equity avg `0.045` n `121`; fx avg `-0.0057` n `6`; index avg `-0.0019` n `25`; metal avg `0.0133` n `20`; unknown avg `-0.0494` n `793`
- 1h: commodity avg `0.012` n `12`; crypto_alt avg `0.1482` n `230`; crypto_major avg `0.1952` n `8`; equity avg `0.0902` n `121`; fx avg `0.0212` n `6`; index avg `0.0271` n `25`; metal avg `0.0867` n `20`; unknown avg `-0.2214` n `793`
- 4h: commodity avg `-0.0552` n `12`; crypto_alt avg `0.8154` n `230`; crypto_major avg `0.5962` n `8`; equity avg `0.3446` n `121`; fx avg `-0.0157` n `6`; index avg `0.0206` n `25`; metal avg `0.0943` n `20`; unknown avg `-0.363` n `792`
- 24h: commodity avg `0.3235` n `12`; crypto_alt avg `4.7615` n `230`; crypto_major avg `5.2914` n `8`; equity avg `-1.0877` n `121`; fx avg `0.1906` n `6`; index avg `-0.1355` n `25`; metal avg `0.1622` n `20`; unknown avg `2.636` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2186`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1864`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1832`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1798`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1155`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
