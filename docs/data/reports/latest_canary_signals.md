# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T20:58:11.377966+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.02` n `12`; crypto_alt avg `0.0373` n `230`; crypto_major avg `0.0345` n `8`; equity avg `-0.0078` n `114`; fx avg `-0.0055` n `6`; index avg `-0.0089` n `25`; metal avg `0.0007` n `20`; unknown avg `0.0992` n `791`
- 1h: commodity avg `-0.0674` n `12`; crypto_alt avg `-0.1425` n `230`; crypto_major avg `-0.101` n `8`; equity avg `-0.0103` n `114`; fx avg `-0.0025` n `6`; index avg `-0.0182` n `25`; metal avg `-0.0051` n `20`; unknown avg `0.0602` n `791`
- 4h: commodity avg `0.0559` n `12`; crypto_alt avg `-0.1462` n `230`; crypto_major avg `-0.0544` n `8`; equity avg `0.0977` n `114`; fx avg `-0.004` n `6`; index avg `-0.0131` n `25`; metal avg `0.0106` n `20`; unknown avg `0.9777` n `791`
- 24h: commodity avg `-0.0301` n `12`; crypto_alt avg `0.8862` n `230`; crypto_major avg `0.66` n `8`; equity avg `0.1905` n `114`; fx avg `0.0027` n `6`; index avg `-0.0099` n `25`; metal avg `0.0487` n `20`; unknown avg `0.1517` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2204`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.2002`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1813`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1788`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1589`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1507`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1485`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1478`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1452`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1402`, n `668`, weak_sample_signal
