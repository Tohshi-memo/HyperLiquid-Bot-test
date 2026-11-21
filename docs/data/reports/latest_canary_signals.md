# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T16:37:27.862532+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0066` n `13`; crypto_alt avg `-0.0057` n `239`; crypto_major avg `0.1194` n `8`; equity avg `-0.0143` n `166`; fx avg `0.0016` n `6`; index avg `-0.0066` n `27`; metal avg `-0.0029` n `20`; unknown avg `357.2592` n `1262`
- 1h: commodity avg `0.0134` n `13`; crypto_alt avg `-0.3474` n `239`; crypto_major avg `0.0367` n `8`; equity avg `0.0688` n `166`; fx avg `-0.0161` n `6`; index avg `0.0001` n `27`; metal avg `-0.0223` n `20`; unknown avg `159.7453` n `1252`
- 4h: commodity avg `0.0051` n `13`; crypto_alt avg `1.1156` n `239`; crypto_major avg `1.3561` n `8`; equity avg `0.677` n `166`; fx avg `0.0025` n `6`; index avg `0.0705` n `27`; metal avg `0.059` n `20`; unknown avg `154.7763` n `1246`
- 24h: commodity avg `0.4827` n `13`; crypto_alt avg `0.3488` n `239`; crypto_major avg `0.6144` n `8`; equity avg `-0.373` n `166`; fx avg `-0.1109` n `6`; index avg `-0.1067` n `27`; metal avg `-0.0048` n `20`; unknown avg `0.1336` n `1141`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1499`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1482`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
