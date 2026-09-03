# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T19:07:31.237383+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.009` n `12`; crypto_alt avg `0.0567` n `232`; crypto_major avg `0.0658` n `8`; equity avg `-0.0967` n `133`; fx avg `0.0052` n `6`; index avg `-0.01` n `26`; metal avg `-0.0055` n `20`; unknown avg `5.669` n `790`
- 1h: commodity avg `0.1091` n `12`; crypto_alt avg `0.1975` n `232`; crypto_major avg `0.0846` n `8`; equity avg `-0.0726` n `133`; fx avg `0.014` n `6`; index avg `-0.0089` n `26`; metal avg `-0.0546` n `20`; unknown avg `5.4654` n `790`
- 4h: commodity avg `-0.157` n `12`; crypto_alt avg `1.324` n `232`; crypto_major avg `0.6419` n `8`; equity avg `0.5542` n `133`; fx avg `0.0287` n `6`; index avg `0.105` n `26`; metal avg `-0.0448` n `20`; unknown avg `36.352` n `790`
- 24h: commodity avg `-0.0917` n `12`; crypto_alt avg `4.7493` n `232`; crypto_major avg `5.4086` n `8`; equity avg `1.4822` n `133`; fx avg `-0.2594` n `6`; index avg `0.2062` n `26`; metal avg `0.8462` n `20`; unknown avg `1.1109` n `736`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0658`, n `668`, weak_sample_signal
