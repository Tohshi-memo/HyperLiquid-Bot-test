# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T00:22:25.577647+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0006` n `12`; crypto_alt avg `0.2326` n `230`; crypto_major avg `0.113` n `8`; equity avg `-0.0013` n `113`; fx avg `-0.0091` n `6`; index avg `0.0361` n `25`; metal avg `0.1048` n `20`; unknown avg `0.16` n `786`
- 1h: commodity avg `-0.0465` n `12`; crypto_alt avg `0.63` n `230`; crypto_major avg `0.3717` n `8`; equity avg `0.3411` n `113`; fx avg `-0.0422` n `6`; index avg `0.0846` n `25`; metal avg `0.1815` n `20`; unknown avg `0.212` n `786`
- 4h: commodity avg `-0.0813` n `12`; crypto_alt avg `-0.0817` n `230`; crypto_major avg `-0.01` n `8`; equity avg `0.5319` n `113`; fx avg `-0.0525` n `6`; index avg `0.1033` n `25`; metal avg `0.1679` n `20`; unknown avg `0.0031` n `786`
- 24h: commodity avg `-0.1046` n `12`; crypto_alt avg `-1.0084` n `230`; crypto_major avg `-0.2547` n `8`; equity avg `3.0045` n `113`; fx avg `-0.0431` n `6`; index avg `0.4686` n `25`; metal avg `0.296` n `20`; unknown avg `0.0772` n `770`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2381`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.202`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1891`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1854`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1839`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1699`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1573`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1388`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1369`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1367`, n `668`, weak_sample_signal
