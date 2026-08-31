# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T23:52:26.727275+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0089` n `12`; crypto_alt avg `0.0352` n `232`; crypto_major avg `0.0042` n `8`; equity avg `0.0107` n `129`; fx avg `-0.0003` n `6`; index avg `0.0219` n `26`; metal avg `0.0298` n `20`; unknown avg `0.073` n `793`
- 1h: commodity avg `0.0243` n `12`; crypto_alt avg `-0.034` n `232`; crypto_major avg `-0.1167` n `8`; equity avg `0.0053` n `129`; fx avg `-0.0121` n `6`; index avg `0.0347` n `26`; metal avg `0.0211` n `20`; unknown avg `0.0157` n `791`
- 4h: commodity avg `0.0592` n `12`; crypto_alt avg `0.1256` n `232`; crypto_major avg `-0.3318` n `8`; equity avg `0.0281` n `129`; fx avg `-0.0041` n `6`; index avg `0.0109` n `26`; metal avg `-0.0341` n `20`; unknown avg `1.1874` n `773`
- 24h: commodity avg `0.4989` n `12`; crypto_alt avg `2.4086` n `231`; crypto_major avg `1.7952` n `8`; equity avg `1.1616` n `129`; fx avg `-0.1051` n `6`; index avg `0.163` n `26`; metal avg `-0.1995` n `20`; unknown avg `0.433` n `740`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.058`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0565`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0552`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.05`, n `668`, weak_sample_signal
