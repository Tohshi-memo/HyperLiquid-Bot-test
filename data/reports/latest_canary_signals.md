# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T21:07:28.224915+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0114` n `12`; crypto_alt avg `-0.0043` n `233`; crypto_major avg `-0.0062` n `8`; equity avg `0.0596` n `136`; fx avg `0.0325` n `6`; index avg `0.0083` n `27`; metal avg `0.0222` n `20`; unknown avg `1.187` n `838`
- 1h: commodity avg `0.0591` n `12`; crypto_alt avg `0.2139` n `233`; crypto_major avg `0.2366` n `8`; equity avg `0.097` n `136`; fx avg `0.0334` n `6`; index avg `0.0203` n `27`; metal avg `0.0091` n `20`; unknown avg `19.0447` n `802`
- 4h: commodity avg `0.1316` n `12`; crypto_alt avg `0.1232` n `233`; crypto_major avg `0.2237` n `8`; equity avg `0.0962` n `136`; fx avg `0.0338` n `6`; index avg `0.0017` n `27`; metal avg `-0.0084` n `20`; unknown avg `3.2341` n `756`
- 24h: commodity avg `0.375` n `12`; crypto_alt avg `0.1838` n `233`; crypto_major avg `-0.4457` n `8`; equity avg `-1.1077` n `136`; fx avg `0.0509` n `6`; index avg `-0.2276` n `26`; metal avg `-0.0488` n `20`; unknown avg `2.4143` n `690`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0666`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0562`, n `668`, weak_sample_signal
