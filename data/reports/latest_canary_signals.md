# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T05:52:25.826273+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0266` n `12`; crypto_alt avg `-0.0001` n `230`; crypto_major avg `0.0208` n `8`; equity avg `-0.0058` n `114`; fx avg `-0.0041` n `6`; index avg `-0.0019` n `25`; metal avg `-0.0027` n `20`; unknown avg `-0.1664` n `791`
- 1h: commodity avg `-0.0009` n `12`; crypto_alt avg `0.3058` n `230`; crypto_major avg `-0.1754` n `8`; equity avg `-0.0593` n `114`; fx avg `-0.0032` n `6`; index avg `-0.007` n `25`; metal avg `0.0002` n `20`; unknown avg `-0.4272` n `791`
- 4h: commodity avg `0.0387` n `12`; crypto_alt avg `0.5723` n `230`; crypto_major avg `0.0193` n `8`; equity avg `-0.0012` n `114`; fx avg `0.0511` n `6`; index avg `-0.0177` n `25`; metal avg `-0.0191` n `20`; unknown avg `-0.4851` n `791`
- 24h: commodity avg `0.0977` n `12`; crypto_alt avg `0.9452` n `230`; crypto_major avg `-0.3549` n `8`; equity avg `-0.1277` n `114`; fx avg `0.1659` n `6`; index avg `-0.073` n `25`; metal avg `0.3536` n `20`; unknown avg `-0.1723` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.217`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1929`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1791`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1766`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1615`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.16`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1487`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1445`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1391`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
