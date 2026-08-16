# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T01:54:31.911437+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0335` n `12`; crypto_alt avg `-0.0572` n `230`; crypto_major avg `-0.0175` n `8`; equity avg `0.0062` n `114`; fx avg `0.0048` n `6`; index avg `0.0032` n `25`; metal avg `-0.004` n `20`; unknown avg `-0.0384` n `791`
- 1h: commodity avg `0.0758` n `12`; crypto_alt avg `-0.262` n `230`; crypto_major avg `-0.0045` n `8`; equity avg `0.0082` n `114`; fx avg `0.0054` n `6`; index avg `0.0034` n `25`; metal avg `-0.0` n `20`; unknown avg `0.0319` n `791`
- 4h: commodity avg `0.0636` n `12`; crypto_alt avg `-0.6709` n `230`; crypto_major avg `-0.2913` n `8`; equity avg `-0.0269` n `114`; fx avg `-0.0011` n `6`; index avg `0.0166` n `25`; metal avg `-0.0043` n `20`; unknown avg `0.1022` n `791`
- 24h: commodity avg `0.007` n `12`; crypto_alt avg `0.0081` n `230`; crypto_major avg `0.0125` n `8`; equity avg `0.1476` n `114`; fx avg `0.0411` n `6`; index avg `0.011` n `25`; metal avg `-0.0221` n `20`; unknown avg `-0.0707` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2229`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1841`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1747`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1731`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1706`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1542`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1501`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1478`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1468`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1423`, n `668`, weak_sample_signal
