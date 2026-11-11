# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T22:22:29.500709+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.016` n `13`; crypto_alt avg `0.1124` n `239`; crypto_major avg `0.0392` n `8`; equity avg `-0.3688` n `161`; fx avg `-0.0114` n `6`; index avg `-0.0287` n `27`; metal avg `-0.0002` n `20`; unknown avg `39.5935` n `1262`
- 1h: commodity avg `0.0005` n `13`; crypto_alt avg `-0.1627` n `239`; crypto_major avg `-0.2576` n `8`; equity avg `-0.4254` n `161`; fx avg `-0.0055` n `6`; index avg `-0.0291` n `27`; metal avg `0.0117` n `20`; unknown avg `2.6155` n `1248`
- 4h: commodity avg `-0.1323` n `13`; crypto_alt avg `-0.5664` n `239`; crypto_major avg `-0.5047` n `8`; equity avg `-1.4191` n `161`; fx avg `-0.0118` n `6`; index avg `-0.115` n `27`; metal avg `-0.1109` n `20`; unknown avg `3.8693` n `1204`
- 24h: commodity avg `0.1948` n `13`; crypto_alt avg `0.1303` n `239`; crypto_major avg `0.7565` n `8`; equity avg `4.209` n `161`; fx avg `-0.1549` n `6`; index avg `0.4284` n `27`; metal avg `-0.0604` n `20`; unknown avg `3.8825` n `1141`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1396`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1238`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
