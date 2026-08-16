# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T01:52:26.113685+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0358` n `12`; crypto_alt avg `-0.0294` n `230`; crypto_major avg `-0.0015` n `8`; equity avg `0.0069` n `114`; fx avg `0.0048` n `6`; index avg `0.003` n `25`; metal avg `-0.0034` n `20`; unknown avg `-0.0346` n `791`
- 1h: commodity avg `0.0781` n `12`; crypto_alt avg `-0.2342` n `230`; crypto_major avg `0.0115` n `8`; equity avg `0.0089` n `114`; fx avg `0.0054` n `6`; index avg `0.0032` n `25`; metal avg `0.0006` n `20`; unknown avg `0.0323` n `791`
- 4h: commodity avg `0.0659` n `12`; crypto_alt avg `-0.6437` n `230`; crypto_major avg `-0.2754` n `8`; equity avg `-0.0261` n `114`; fx avg `-0.0011` n `6`; index avg `0.0165` n `25`; metal avg `-0.0037` n `20`; unknown avg `0.0952` n `791`
- 24h: commodity avg `0.0094` n `12`; crypto_alt avg `0.035` n `230`; crypto_major avg `0.0285` n `8`; equity avg `0.1483` n `114`; fx avg `0.0411` n `6`; index avg `0.0108` n `25`; metal avg `-0.0216` n `20`; unknown avg `-0.067` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2229`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1841`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.175`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1733`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1706`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1542`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1501`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1478`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1468`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1423`, n `668`, weak_sample_signal
