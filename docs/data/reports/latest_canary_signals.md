# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T02:07:37.667673+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0172` n `13`; crypto_alt avg `0.1059` n `239`; crypto_major avg `0.1285` n `8`; equity avg `0.1118` n `168`; fx avg `-0.0248` n `6`; index avg `0.0115` n `27`; metal avg `0.2019` n `20`; unknown avg `20.748` n `1257`
- 1h: commodity avg `-0.0602` n `13`; crypto_alt avg `0.3865` n `239`; crypto_major avg `0.4001` n `8`; equity avg `-0.0835` n `168`; fx avg `-0.0384` n `6`; index avg `-0.0159` n `27`; metal avg `0.1567` n `20`; unknown avg `160.1432` n `1259`
- 4h: commodity avg `-0.0044` n `13`; crypto_alt avg `1.2889` n `239`; crypto_major avg `0.8568` n `8`; equity avg `1.3678` n `168`; fx avg `-0.0666` n `6`; index avg `0.1111` n `27`; metal avg `0.0483` n `20`; unknown avg `-0.1224` n `1191`
- 24h: commodity avg `0.5228` n `13`; crypto_alt avg `4.2096` n `239`; crypto_major avg `3.2795` n `8`; equity avg `1.7581` n `168`; fx avg `-0.0418` n `6`; index avg `0.1763` n `27`; metal avg `0.2711` n `20`; unknown avg `770.6563` n `1017`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1935`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1317`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
