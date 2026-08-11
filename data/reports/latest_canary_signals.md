# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T07:22:25.691072+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1088` n `12`; crypto_alt avg `-0.1713` n `230`; crypto_major avg `-0.1589` n `8`; equity avg `0.0209` n `113`; fx avg `-0.0043` n `6`; index avg `-0.0017` n `25`; metal avg `-0.023` n `20`; unknown avg `0.0169` n `785`
- 1h: commodity avg `0.2246` n `12`; crypto_alt avg `-0.341` n `230`; crypto_major avg `-0.306` n `8`; equity avg `-0.157` n `113`; fx avg `0.007` n `6`; index avg `-0.0377` n `25`; metal avg `-0.0688` n `20`; unknown avg `0.0064` n `785`
- 4h: commodity avg `0.3265` n `12`; crypto_alt avg `-0.5875` n `230`; crypto_major avg `-0.4909` n `8`; equity avg `-0.2844` n `113`; fx avg `0.0179` n `6`; index avg `-0.0707` n `25`; metal avg `-0.3722` n `20`; unknown avg `0.0874` n `753`
- 24h: commodity avg `1.1842` n `12`; crypto_alt avg `-1.4033` n `230`; crypto_major avg `-1.3336` n `8`; equity avg `-1.4652` n `113`; fx avg `0.058` n `6`; index avg `-0.0655` n `25`; metal avg `0.0175` n `20`; unknown avg `0.1309` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1695`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1676`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1671`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1639`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1459`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1448`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
