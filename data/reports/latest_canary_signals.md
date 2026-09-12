# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T22:22:25.911262+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0064` n `12`; crypto_alt avg `0.1085` n `233`; crypto_major avg `0.1205` n `8`; equity avg `-0.0156` n `136`; fx avg `-0.0016` n `6`; index avg `-0.0042` n `26`; metal avg `0.0065` n `20`; unknown avg `0.1915` n `830`
- 1h: commodity avg `0.0127` n `12`; crypto_alt avg `0.1425` n `233`; crypto_major avg `0.1278` n `8`; equity avg `-0.0213` n `136`; fx avg `0.001` n `6`; index avg `-0.0011` n `26`; metal avg `-0.0001` n `20`; unknown avg `2.2098` n `810`
- 4h: commodity avg `-0.0108` n `12`; crypto_alt avg `-0.1554` n `233`; crypto_major avg `-0.0647` n `8`; equity avg `-0.2919` n `136`; fx avg `-0.0009` n `6`; index avg `-0.0308` n `26`; metal avg `-0.0267` n `20`; unknown avg `0.6737` n `756`
- 24h: commodity avg `-0.0595` n `12`; crypto_alt avg `1.4831` n `233`; crypto_major avg `0.1674` n `8`; equity avg `-0.2817` n `136`; fx avg `-0.0091` n `6`; index avg `-0.0016` n `26`; metal avg `-0.0078` n `20`; unknown avg `0.6566` n `720`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0643`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0633`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0529`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0498`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0476`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0455`, n `668`, weak_sample_signal
