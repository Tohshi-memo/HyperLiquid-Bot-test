# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T07:37:28.290066+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0131` n `12`; crypto_alt avg `0.1449` n `230`; crypto_major avg `0.0462` n `8`; equity avg `-0.0004` n `114`; fx avg `0.0006` n `6`; index avg `0.0039` n `25`; metal avg `0.0007` n `20`; unknown avg `-0.0008` n `791`
- 1h: commodity avg `-0.0064` n `12`; crypto_alt avg `0.3975` n `230`; crypto_major avg `0.1494` n `8`; equity avg `-0.0175` n `114`; fx avg `0.0022` n `6`; index avg `0.0102` n `25`; metal avg `-0.0084` n `20`; unknown avg `-0.0004` n `791`
- 4h: commodity avg `-0.0505` n `12`; crypto_alt avg `0.2142` n `230`; crypto_major avg `-0.0179` n `8`; equity avg `0.097` n `114`; fx avg `0.0089` n `6`; index avg `0.0251` n `25`; metal avg `0.0076` n `20`; unknown avg `-0.0147` n `759`
- 24h: commodity avg `0.1195` n `12`; crypto_alt avg `0.1224` n `230`; crypto_major avg `0.0578` n `8`; equity avg `0.366` n `114`; fx avg `-0.0041` n `6`; index avg `0.0494` n `25`; metal avg `0.0281` n `20`; unknown avg `0.0515` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2103`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.184`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1808`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1752`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1738`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.152`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1508`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1445`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1426`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1342`, n `668`, weak_sample_signal
