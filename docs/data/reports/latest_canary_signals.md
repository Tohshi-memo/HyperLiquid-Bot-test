# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T21:22:35.595865+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0044` n `12`; crypto_alt avg `-0.0715` n `230`; crypto_major avg `-0.0898` n `8`; equity avg `-0.0159` n `108`; fx avg `-0.0092` n `6`; index avg `0.0014` n `25`; metal avg `-0.0114` n `20`; unknown avg `-0.0051` n `781`
- 1h: commodity avg `0.0405` n `12`; crypto_alt avg `0.1328` n `230`; crypto_major avg `0.0526` n `8`; equity avg `0.0922` n `108`; fx avg `0.0041` n `6`; index avg `-0.0078` n `25`; metal avg `0.0102` n `20`; unknown avg `0.0282` n `781`
- 4h: commodity avg `-0.0713` n `12`; crypto_alt avg `0.2331` n `230`; crypto_major avg `-0.0036` n `8`; equity avg `-0.3653` n `108`; fx avg `0.0588` n `6`; index avg `0.0315` n `25`; metal avg `-0.1855` n `20`; unknown avg `-0.1151` n `781`
- 24h: commodity avg `-1.2448` n `12`; crypto_alt avg `-0.0987` n `230`; crypto_major avg `0.4396` n `8`; equity avg `3.0394` n `107`; fx avg `0.1277` n `6`; index avg `0.7325` n `25`; metal avg `0.841` n `20`; unknown avg `0.4247` n `764`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1565`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.155`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1535`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1338`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
