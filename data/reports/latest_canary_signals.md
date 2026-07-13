# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T06:52:25.585289+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0294` n `12`; crypto_alt avg `0.0604` n `230`; crypto_major avg `0.0776` n `8`; equity avg `0.0926` n `92`; fx avg `0.0032` n `6`; index avg `0.0112` n `25`; metal avg `-0.0175` n `20`; unknown avg `-0.0241` n `766`
- 1h: commodity avg `-0.1517` n `12`; crypto_alt avg `0.1542` n `230`; crypto_major avg `-0.0625` n `8`; equity avg `-0.3555` n `92`; fx avg `-0.0403` n `6`; index avg `-0.0468` n `25`; metal avg `0.0359` n `20`; unknown avg `0.0149` n `750`
- 4h: commodity avg `-0.1097` n `12`; crypto_alt avg `-0.348` n `230`; crypto_major avg `-1.0179` n `8`; equity avg `-1.0675` n `92`; fx avg `-0.0012` n `6`; index avg `-0.2022` n `25`; metal avg `-0.1171` n `20`; unknown avg `-0.2118` n `750`
- 24h: commodity avg `0.0365` n `12`; crypto_alt avg `-1.1004` n `230`; crypto_major avg `-0.8493` n `8`; equity avg `-2.4393` n `92`; fx avg `0.0224` n `6`; index avg `-0.5059` n `25`; metal avg `-0.4169` n `20`; unknown avg `-0.051` n `741`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1834`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1677`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1292`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
