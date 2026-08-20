# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T04:22:30.078399+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0075` n `12`; crypto_alt avg `0.0748` n `230`; crypto_major avg `-0.0558` n `8`; equity avg `0.0211` n `121`; fx avg `0.0048` n `6`; index avg `0.0115` n `25`; metal avg `0.0013` n `20`; unknown avg `0.0276` n `792`
- 1h: commodity avg `0.0396` n `12`; crypto_alt avg `0.2491` n `230`; crypto_major avg `0.3059` n `8`; equity avg `0.2704` n `121`; fx avg `0.0041` n `6`; index avg `0.0355` n `25`; metal avg `0.0311` n `20`; unknown avg `0.0322` n `792`
- 4h: commodity avg `0.049` n `12`; crypto_alt avg `-0.3712` n `230`; crypto_major avg `-0.5548` n `8`; equity avg `0.2397` n `121`; fx avg `0.1422` n `6`; index avg `0.1143` n `25`; metal avg `-0.0979` n `20`; unknown avg `-0.0763` n `792`
- 24h: commodity avg `-0.0312` n `12`; crypto_alt avg `5.2837` n `230`; crypto_major avg `9.3763` n `8`; equity avg `1.3601` n `120`; fx avg `0.0591` n `6`; index avg `0.3503` n `25`; metal avg `1.08` n `20`; unknown avg `1.7033` n `757`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1907`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.158`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1433`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1347`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.13`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1229`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
