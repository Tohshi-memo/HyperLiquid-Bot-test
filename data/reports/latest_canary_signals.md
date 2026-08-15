# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T16:22:42.472936+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0131` n `12`; crypto_alt avg `0.025` n `230`; crypto_major avg `0.0521` n `8`; equity avg `0.0036` n `114`; fx avg `0.0012` n `6`; index avg `-0.0005` n `25`; metal avg `-0.0019` n `20`; unknown avg `-0.0465` n `791`
- 1h: commodity avg `-0.0024` n `12`; crypto_alt avg `0.1509` n `230`; crypto_major avg `0.1549` n `8`; equity avg `-0.009` n `114`; fx avg `-0.0001` n `6`; index avg `0.0022` n `25`; metal avg `-0.0014` n `20`; unknown avg `-0.0313` n `791`
- 4h: commodity avg `-0.0538` n `12`; crypto_alt avg `0.5064` n `230`; crypto_major avg `0.3316` n `8`; equity avg `0.0508` n `114`; fx avg `-0.0016` n `6`; index avg `0.0038` n `25`; metal avg `-0.0136` n `20`; unknown avg `-0.0683` n `791`
- 24h: commodity avg `-0.0813` n `12`; crypto_alt avg `0.9886` n `230`; crypto_major avg `0.3396` n `8`; equity avg `0.173` n `114`; fx avg `0.0108` n `6`; index avg `0.0297` n `25`; metal avg `-0.0436` n `20`; unknown avg `0.0268` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2137`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.21`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1847`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1781`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1577`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1549`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1501`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.147`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1443`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1399`, n `668`, weak_sample_signal
