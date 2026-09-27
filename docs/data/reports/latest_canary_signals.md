# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T07:52:26.968785+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0007` n `12`; crypto_alt avg `0.3454` n `234`; crypto_major avg `0.2688` n `8`; equity avg `0.0085` n `141`; fx avg `-0.002` n `6`; index avg `0.0027` n `26`; metal avg `0.0045` n `20`; unknown avg `3.7658` n `961`
- 1h: commodity avg `-0.043` n `12`; crypto_alt avg `0.8651` n `234`; crypto_major avg `0.5054` n `8`; equity avg `0.0419` n `141`; fx avg `-0.0089` n `6`; index avg `0.005` n `26`; metal avg `0.0138` n `20`; unknown avg `5.0662` n `959`
- 4h: commodity avg `-0.0034` n `12`; crypto_alt avg `1.4173` n `234`; crypto_major avg `0.7959` n `8`; equity avg `0.1065` n `141`; fx avg `0.005` n `6`; index avg `0.0161` n `26`; metal avg `0.0083` n `20`; unknown avg `3.7066` n `933`
- 24h: commodity avg `0.0203` n `12`; crypto_alt avg `1.4137` n `234`; crypto_major avg `0.5333` n `8`; equity avg `0.3142` n `141`; fx avg `-0.0076` n `6`; index avg `0.0174` n `26`; metal avg `0.0015` n `20`; unknown avg `4.7995` n `887`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1692`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1523`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1508`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1444`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1227`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
