# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T07:52:29.836365+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0249` n `12`; crypto_alt avg `0.4468` n `230`; crypto_major avg `0.0238` n `8`; equity avg `-0.0341` n `121`; fx avg `-0.0117` n `6`; index avg `0.0015` n `25`; metal avg `0.076` n `20`; unknown avg `0.0056` n `793`
- 1h: commodity avg `0.016` n `12`; crypto_alt avg `1.3031` n `230`; crypto_major avg `0.562` n `8`; equity avg `0.2399` n `121`; fx avg `-0.0478` n `6`; index avg `0.0326` n `25`; metal avg `0.0793` n `20`; unknown avg `0.2679` n `793`
- 4h: commodity avg `0.0413` n `12`; crypto_alt avg `2.22` n `230`; crypto_major avg `1.088` n `8`; equity avg `0.541` n `121`; fx avg `-0.0093` n `6`; index avg `0.0898` n `25`; metal avg `0.2338` n `20`; unknown avg `0.1048` n `777`
- 24h: commodity avg `0.2227` n `12`; crypto_alt avg `7.446` n `230`; crypto_major avg `7.272` n `8`; equity avg `0.0505` n `121`; fx avg `-0.042` n `6`; index avg `-0.0175` n `25`; metal avg `0.8053` n `20`; unknown avg `2.4513` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2117`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1956`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1888`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
