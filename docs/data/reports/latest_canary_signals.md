# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T15:52:28.978189+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0707` n `12`; crypto_alt avg `-0.2066` n `230`; crypto_major avg `-0.1022` n `8`; equity avg `-0.3376` n `92`; fx avg `0.0083` n `6`; index avg `-0.0722` n `25`; metal avg `-0.0607` n `20`; unknown avg `0.0071` n `766`
- 1h: commodity avg `0.1747` n `12`; crypto_alt avg `-0.3085` n `230`; crypto_major avg `-0.1528` n `8`; equity avg `-0.1634` n `92`; fx avg `-0.0067` n `6`; index avg `-0.0533` n `25`; metal avg `0.0121` n `20`; unknown avg `-0.1169` n `766`
- 4h: commodity avg `0.2158` n `12`; crypto_alt avg `-0.3314` n `230`; crypto_major avg `-0.5458` n `8`; equity avg `-0.4846` n `92`; fx avg `-0.0309` n `6`; index avg `-0.0535` n `25`; metal avg `-0.2101` n `20`; unknown avg `-0.0539` n `766`
- 24h: commodity avg `0.1255` n `12`; crypto_alt avg `-1.6441` n `230`; crypto_major avg `-2.4582` n `8`; equity avg `-2.4463` n `92`; fx avg `-0.0876` n `6`; index avg `-0.5108` n `25`; metal avg `-0.408` n `20`; unknown avg `-0.1687` n `743`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2061`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1874`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1475`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1312`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
