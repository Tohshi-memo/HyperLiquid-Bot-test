# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T23:06:57.126366+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0115` n `12`; crypto_alt avg `0.2028` n `230`; crypto_major avg `0.1883` n `8`; equity avg `0.005` n `92`; fx avg `0.0016` n `6`; index avg `-0.0053` n `25`; metal avg `-0.0377` n `20`; unknown avg `-0.0205` n `765`
- 1h: commodity avg `-0.1379` n `12`; crypto_alt avg `0.0071` n `230`; crypto_major avg `0.0131` n `8`; equity avg `-0.1242` n `92`; fx avg `0.0163` n `6`; index avg `-0.0218` n `25`; metal avg `-0.097` n `20`; unknown avg `-0.0712` n `765`
- 4h: commodity avg `-0.1173` n `12`; crypto_alt avg `-0.8442` n `230`; crypto_major avg `-0.8879` n `8`; equity avg `-0.3187` n `92`; fx avg `-0.0768` n `6`; index avg `-0.0894` n `25`; metal avg `-0.2599` n `20`; unknown avg `0.1855` n `765`
- 24h: commodity avg `0.2129` n `12`; crypto_alt avg `-1.6884` n `230`; crypto_major avg `-1.087` n `8`; equity avg `-0.4311` n `92`; fx avg `-0.0587` n `6`; index avg `-0.1501` n `25`; metal avg `-0.353` n `20`; unknown avg `0.2916` n `741`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1668`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1522`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
