# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T20:07:25.867025+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0433` n `12`; crypto_alt avg `-0.0029` n `230`; crypto_major avg `-0.0401` n `8`; equity avg `-0.0135` n `114`; fx avg `-0.0012` n `6`; index avg `-0.0021` n `25`; metal avg `-0.0022` n `20`; unknown avg `-0.0725` n `791`
- 1h: commodity avg `0.0164` n `12`; crypto_alt avg `0.0643` n `230`; crypto_major avg `0.1056` n `8`; equity avg `0.0334` n `114`; fx avg `-0.0003` n `6`; index avg `-0.0017` n `25`; metal avg `0.0066` n `20`; unknown avg `-0.1234` n `791`
- 4h: commodity avg `0.0765` n `12`; crypto_alt avg `-0.0084` n `230`; crypto_major avg `0.1137` n `8`; equity avg `0.0761` n `114`; fx avg `0.0001` n `6`; index avg `0.0014` n `25`; metal avg `0.0064` n `20`; unknown avg `0.0637` n `791`
- 24h: commodity avg `-0.0167` n `12`; crypto_alt avg `0.9859` n `230`; crypto_major avg `0.6074` n `8`; equity avg `0.2126` n `114`; fx avg `0.0194` n `6`; index avg `0.0054` n `25`; metal avg `0.0517` n `20`; unknown avg `0.0919` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2205`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.2043`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1824`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1788`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1578`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1496`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1491`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1485`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1453`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1375`, n `668`, weak_sample_signal
