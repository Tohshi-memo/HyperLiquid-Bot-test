# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T22:52:37.310110+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0085` n `12`; crypto_alt avg `-0.0711` n `230`; crypto_major avg `-0.0103` n `8`; equity avg `0.0722` n `112`; fx avg `-0.0005` n `6`; index avg `0.0153` n `25`; metal avg `0.0047` n `20`; unknown avg `-0.0138` n `782`
- 1h: commodity avg `-0.0372` n `12`; crypto_alt avg `-0.3327` n `230`; crypto_major avg `-0.0313` n `8`; equity avg `0.1339` n `112`; fx avg `0.0138` n `6`; index avg `0.0236` n `25`; metal avg `-0.0065` n `20`; unknown avg `-0.0467` n `782`
- 4h: commodity avg `0.2617` n `12`; crypto_alt avg `-0.3863` n `230`; crypto_major avg `-0.4052` n `8`; equity avg `-0.604` n `112`; fx avg `0.0048` n `6`; index avg `-0.0651` n `25`; metal avg `-0.1014` n `20`; unknown avg `-0.2269` n `781`
- 24h: commodity avg `0.6392` n `12`; crypto_alt avg `0.1542` n `230`; crypto_major avg `-0.9714` n `8`; equity avg `0.3811` n `109`; fx avg `0.0269` n `6`; index avg `-0.1907` n `25`; metal avg `-0.105` n `20`; unknown avg `113.2642` n `749`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1196`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1152`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
