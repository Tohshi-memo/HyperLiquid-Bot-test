# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T15:07:38.333844+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0337` n `13`; crypto_alt avg `-0.9328` n `239`; crypto_major avg `-0.9768` n `8`; equity avg `-1.0807` n `167`; fx avg `0.0061` n `6`; index avg `-0.095` n `27`; metal avg `-0.2318` n `20`; unknown avg `12.8206` n `1256`
- 1h: commodity avg `0.1384` n `13`; crypto_alt avg `-0.6123` n `239`; crypto_major avg `-0.8147` n `8`; equity avg `-0.8462` n `167`; fx avg `0.0194` n `6`; index avg `-0.0035` n `27`; metal avg `-0.0726` n `20`; unknown avg `13.8885` n `1256`
- 4h: commodity avg `0.4486` n `13`; crypto_alt avg `-1.1471` n `239`; crypto_major avg `-0.7536` n `8`; equity avg `-0.7173` n `166`; fx avg `0.0944` n `6`; index avg `-0.0284` n `27`; metal avg `-0.0468` n `20`; unknown avg `51.7469` n `1242`
- 24h: commodity avg `0.4097` n `13`; crypto_alt avg `-5.5468` n `239`; crypto_major avg `-6.2303` n `8`; equity avg `-4.1137` n `166`; fx avg `0.1589` n `6`; index avg `-0.3054` n `27`; metal avg `-0.9724` n `20`; unknown avg `23.0052` n `1132`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1303`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1249`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
