# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T09:52:29.832393+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0034` n `12`; crypto_alt avg `0.0487` n `230`; crypto_major avg `-0.0342` n `8`; equity avg `0.0009` n `114`; fx avg `-0.0044` n `6`; index avg `0.0004` n `25`; metal avg `-0.0015` n `20`; unknown avg `0.0747` n `791`
- 1h: commodity avg `-0.0305` n `12`; crypto_alt avg `0.1367` n `230`; crypto_major avg `-0.0432` n `8`; equity avg `-0.0199` n `114`; fx avg `-0.0027` n `6`; index avg `0.0036` n `25`; metal avg `-0.002` n `20`; unknown avg `0.0759` n `791`
- 4h: commodity avg `-0.0045` n `12`; crypto_alt avg `0.4427` n `230`; crypto_major avg `0.1458` n `8`; equity avg `0.0416` n `114`; fx avg `0.0011` n `6`; index avg `0.0177` n `25`; metal avg `-0.0012` n `20`; unknown avg `0.009` n `759`
- 24h: commodity avg `0.0832` n `12`; crypto_alt avg `0.1464` n `230`; crypto_major avg `0.1815` n `8`; equity avg `0.3738` n `114`; fx avg `-0.0128` n `6`; index avg `0.0671` n `25`; metal avg `0.026` n `20`; unknown avg `0.0601` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2058`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1843`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1819`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1772`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1756`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1505`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1471`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1466`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1391`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1389`, n `668`, weak_sample_signal
