# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T05:22:25.939810+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0258` n `12`; crypto_alt avg `0.1304` n `230`; crypto_major avg `0.3322` n `8`; equity avg `0.0555` n `121`; fx avg `0.007` n `6`; index avg `0.0164` n `25`; metal avg `-0.0303` n `20`; unknown avg `0.0265` n `793`
- 1h: commodity avg `-0.0426` n `12`; crypto_alt avg `0.298` n `230`; crypto_major avg `0.4041` n `8`; equity avg `0.2245` n `121`; fx avg `0.0013` n `6`; index avg `0.0423` n `25`; metal avg `-0.0779` n `20`; unknown avg `0.1251` n `793`
- 4h: commodity avg `-0.0938` n `12`; crypto_alt avg `1.2235` n `230`; crypto_major avg `1.1017` n `8`; equity avg `0.5538` n `121`; fx avg `-0.0127` n `6`; index avg `0.099` n `25`; metal avg `0.0736` n `20`; unknown avg `0.0192` n `793`
- 24h: commodity avg `0.2605` n `12`; crypto_alt avg `5.7786` n `230`; crypto_major avg `7.1423` n `8`; equity avg `-0.4231` n `121`; fx avg `-0.0239` n `6`; index avg `-0.0677` n `25`; metal avg `0.5223` n `20`; unknown avg `2.6967` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2122`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1884`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1865`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1814`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
