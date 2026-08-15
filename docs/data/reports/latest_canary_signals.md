# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T17:37:23.955337+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0223` n `12`; crypto_alt avg `-0.0457` n `230`; crypto_major avg `-0.003` n `8`; equity avg `0.0435` n `114`; fx avg `0.0005` n `6`; index avg `0.0064` n `25`; metal avg `0.0019` n `20`; unknown avg `-0.0091` n `791`
- 1h: commodity avg `0.0236` n `12`; crypto_alt avg `0.0897` n `230`; crypto_major avg `0.0793` n `8`; equity avg `0.0328` n `114`; fx avg `-0.0035` n `6`; index avg `0.0035` n `25`; metal avg `0.0004` n `20`; unknown avg `1.4725` n `791`
- 4h: commodity avg `0.0246` n `12`; crypto_alt avg `0.3977` n `230`; crypto_major avg `0.1309` n `8`; equity avg `0.0605` n `114`; fx avg `-0.004` n `6`; index avg `0.007` n `25`; metal avg `-0.0098` n `20`; unknown avg `-0.0304` n `791`
- 24h: commodity avg `-0.1368` n `12`; crypto_alt avg `0.8208` n `230`; crypto_major avg `0.2861` n `8`; equity avg `0.2328` n `114`; fx avg `0.0247` n `6`; index avg `0.0447` n `25`; metal avg `0.0048` n `20`; unknown avg `-0.017` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2175`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.2124`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1832`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1782`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1584`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1561`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1476`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.146`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.145`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1432`, n `668`, weak_sample_signal
