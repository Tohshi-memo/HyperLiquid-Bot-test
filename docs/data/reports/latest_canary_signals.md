# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T21:32:14.444207+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0071` n `12`; crypto_alt avg `-0.0149` n `230`; crypto_major avg `0.0092` n `8`; equity avg `0.005` n `114`; fx avg `0.0016` n `6`; index avg `-0.0019` n `25`; metal avg `0.0016` n `20`; unknown avg `0.0874` n `791`
- 1h: commodity avg `-0.0219` n `12`; crypto_alt avg `0.1339` n `230`; crypto_major avg `0.0971` n `8`; equity avg `-0.0077` n `114`; fx avg `0.0002` n `6`; index avg `-0.0039` n `25`; metal avg `-0.0018` n `20`; unknown avg `0.116` n `791`
- 4h: commodity avg `0.0271` n `12`; crypto_alt avg `-0.0889` n `230`; crypto_major avg `0.0633` n `8`; equity avg `0.0649` n `114`; fx avg `0.0081` n `6`; index avg `-0.0144` n `25`; metal avg `0.0059` n `20`; unknown avg `0.9159` n `791`
- 24h: commodity avg `-0.0163` n `12`; crypto_alt avg `0.9585` n `230`; crypto_major avg `0.6561` n `8`; equity avg `0.1875` n `114`; fx avg `0.028` n `6`; index avg `-0.0178` n `25`; metal avg `0.02` n `20`; unknown avg `0.1482` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2218`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1992`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.181`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1794`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1601`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1512`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1492`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1485`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1468`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1405`, n `668`, weak_sample_signal
