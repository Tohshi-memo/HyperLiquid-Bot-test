# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T14:22:26.813257+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0356` n `12`; crypto_alt avg `-0.0401` n `230`; crypto_major avg `-0.0532` n `8`; equity avg `-0.5171` n `121`; fx avg `-0.0022` n `6`; index avg `-0.031` n `25`; metal avg `0.0756` n `20`; unknown avg `-0.1134` n `793`
- 1h: commodity avg `-0.0353` n `12`; crypto_alt avg `0.535` n `230`; crypto_major avg `0.3788` n `8`; equity avg `-0.684` n `121`; fx avg `-0.0021` n `6`; index avg `-0.0894` n `25`; metal avg `0.0199` n `20`; unknown avg `-0.0414` n `793`
- 4h: commodity avg `-0.0662` n `12`; crypto_alt avg `1.328` n `230`; crypto_major avg `-0.1159` n `8`; equity avg `-0.8796` n `121`; fx avg `-0.0107` n `6`; index avg `-0.0954` n `25`; metal avg `0.1203` n `20`; unknown avg `0.2264` n `793`
- 24h: commodity avg `0.2397` n `12`; crypto_alt avg `8.1124` n `230`; crypto_major avg `5.9959` n `8`; equity avg `0.5648` n `121`; fx avg `-0.0869` n `6`; index avg `-0.0007` n `25`; metal avg `0.907` n `20`; unknown avg `3.2616` n `776`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2345`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.197`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1954`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1935`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
