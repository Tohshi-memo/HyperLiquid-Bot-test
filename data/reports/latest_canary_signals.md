# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T12:07:25.913026+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0033` n `12`; crypto_alt avg `-0.0015` n `230`; crypto_major avg `0.0088` n `8`; equity avg `0.0151` n `114`; fx avg `0.0015` n `6`; index avg `0.0017` n `25`; metal avg `-0.0026` n `20`; unknown avg `0.0091` n `791`
- 1h: commodity avg `-0.0024` n `12`; crypto_alt avg `-0.0327` n `230`; crypto_major avg `-0.0198` n `8`; equity avg `-0.0027` n `114`; fx avg `-0.0076` n `6`; index avg `0.0027` n `25`; metal avg `0.0065` n `20`; unknown avg `0.0796` n `791`
- 4h: commodity avg `-0.0075` n `12`; crypto_alt avg `0.059` n `230`; crypto_major avg `-0.0581` n `8`; equity avg `-0.0167` n `114`; fx avg `-0.0169` n `6`; index avg `-0.0042` n `25`; metal avg `0.0153` n `20`; unknown avg `0.0877` n `791`
- 24h: commodity avg `0.0183` n `12`; crypto_alt avg `0.0038` n `230`; crypto_major avg `0.121` n `8`; equity avg `0.3395` n `114`; fx avg `-0.0114` n `6`; index avg `0.0491` n `25`; metal avg `0.0342` n `20`; unknown avg `0.1877` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2143`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1902`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1798`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1763`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1761`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1567`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1566`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1514`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1379`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1349`, n `668`, weak_sample_signal
