# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T12:22:24.033113+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0191` n `12`; crypto_alt avg `-0.1313` n `230`; crypto_major avg `-0.0704` n `8`; equity avg `-0.1448` n `114`; fx avg `-0.0127` n `6`; index avg `-0.0324` n `25`; metal avg `0.0167` n `20`; unknown avg `-0.0197` n `786`
- 1h: commodity avg `0.1169` n `12`; crypto_alt avg `-0.2059` n `230`; crypto_major avg `-0.1338` n `8`; equity avg `-0.2068` n `114`; fx avg `-0.0104` n `6`; index avg `-0.0369` n `25`; metal avg `0.133` n `20`; unknown avg `-0.0619` n `786`
- 4h: commodity avg `-0.1706` n `12`; crypto_alt avg `-0.2348` n `230`; crypto_major avg `-0.2485` n `8`; equity avg `0.1804` n `114`; fx avg `0.0066` n `6`; index avg `0.0261` n `25`; metal avg `0.2129` n `20`; unknown avg `3.2784` n `786`
- 24h: commodity avg `-0.0183` n `12`; crypto_alt avg `-0.8942` n `230`; crypto_major avg `-0.8275` n `8`; equity avg `1.7365` n `114`; fx avg `-0.0341` n `6`; index avg `0.3174` n `25`; metal avg `-0.0791` n `20`; unknown avg `1.0045` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2078`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1879`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1781`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1745`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1692`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1616`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1606`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1592`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1515`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
