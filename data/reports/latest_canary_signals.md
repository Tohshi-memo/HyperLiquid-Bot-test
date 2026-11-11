# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T22:37:28.878992+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0041` n `13`; crypto_alt avg `-0.7576` n `239`; crypto_major avg `-0.6117` n `8`; equity avg `-0.5982` n `161`; fx avg `-0.0061` n `6`; index avg `-0.067` n `27`; metal avg `-0.0134` n `20`; unknown avg `2.6209` n `1262`
- 1h: commodity avg `-0.0057` n `13`; crypto_alt avg `-0.6572` n `239`; crypto_major avg `-0.6887` n `8`; equity avg `-1.0863` n `161`; fx avg `-0.0151` n `6`; index avg `-0.1087` n `27`; metal avg `0.0098` n `20`; unknown avg `4.3757` n `1248`
- 4h: commodity avg `-0.0946` n `13`; crypto_alt avg `-1.2744` n `239`; crypto_major avg `-1.102` n `8`; equity avg `-1.8963` n `161`; fx avg `-0.0281` n `6`; index avg `-0.1764` n `27`; metal avg `-0.1175` n `20`; unknown avg `4.6956` n `1204`
- 24h: commodity avg `0.197` n `13`; crypto_alt avg `-0.4206` n `239`; crypto_major avg `0.379` n `8`; equity avg `3.3871` n `161`; fx avg `-0.1616` n `6`; index avg `0.3543` n `27`; metal avg `-0.0702` n `20`; unknown avg `3.4473` n `1141`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1371`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.125`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1186`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
