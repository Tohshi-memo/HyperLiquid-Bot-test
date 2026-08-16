# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T08:37:29.931877+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0018` n `12`; crypto_alt avg `-0.0248` n `230`; crypto_major avg `0.0009` n `8`; equity avg `-0.0108` n `114`; fx avg `-0.0` n `6`; index avg `-0.0029` n `25`; metal avg `0.0155` n `20`; unknown avg `0.0033` n `791`
- 1h: commodity avg `0.0255` n `12`; crypto_alt avg `0.0106` n `230`; crypto_major avg `0.0519` n `8`; equity avg `0.0095` n `114`; fx avg `-0.0038` n `6`; index avg `-0.0051` n `25`; metal avg `0.0112` n `20`; unknown avg `-0.0582` n `791`
- 4h: commodity avg `-0.0381` n `12`; crypto_alt avg `0.355` n `230`; crypto_major avg `0.0897` n `8`; equity avg `0.1111` n `114`; fx avg `-0.0028` n `6`; index avg `0.0219` n `25`; metal avg `0.024` n `20`; unknown avg `-0.0564` n `759`
- 24h: commodity avg `0.0917` n `12`; crypto_alt avg `0.0312` n `230`; crypto_major avg `0.2058` n `8`; equity avg `0.3708` n `114`; fx avg `-0.0101` n `6`; index avg `0.0544` n `25`; metal avg `0.0304` n `20`; unknown avg `-0.0156` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2085`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1837`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1801`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1755`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.175`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.151`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1442`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1434`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1418`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
