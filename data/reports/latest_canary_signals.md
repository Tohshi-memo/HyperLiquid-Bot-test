# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T07:07:21.116704+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2051` n `12`; crypto_alt avg `-0.2554` n `228`; crypto_major avg `-0.0643` n `8`; equity avg `0.0043` n `69`; fx avg `-0.0034` n `6`; index avg `0.0032` n `23`; metal avg `-0.0036` n `18`; unknown avg `0.307` n `421`
- 1h: commodity avg `0.173` n `12`; crypto_alt avg `-0.0781` n `228`; crypto_major avg `-0.1891` n `8`; equity avg `0.1238` n `69`; fx avg `0.0189` n `6`; index avg `0.0027` n `23`; metal avg `0.0094` n `18`; unknown avg `0.1453` n `421`
- 4h: commodity avg `0.2909` n `12`; crypto_alt avg `-0.0725` n `228`; crypto_major avg `-0.0896` n `8`; equity avg `0.2232` n `69`; fx avg `0.0183` n `6`; index avg `-0.019` n `23`; metal avg `0.015` n `18`; unknown avg `-0.0282` n `401`
- 24h: commodity avg `0.2765` n `12`; crypto_alt avg `0.5353` n `228`; crypto_major avg `2.0408` n `8`; equity avg `1.0473` n `69`; fx avg `0.0596` n `6`; index avg `0.0042` n `23`; metal avg `-0.0269` n `18`; unknown avg `0.7086` n `401`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1313`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1162`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
