# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T23:22:31.475904+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.021` n `13`; crypto_alt avg `-0.0467` n `239`; crypto_major avg `-0.0804` n `8`; equity avg `-0.3908` n `168`; fx avg `-0.0041` n `6`; index avg `-0.0415` n `27`; metal avg `0.0179` n `20`; unknown avg `0.2682` n `1255`
- 1h: commodity avg `0.0381` n `13`; crypto_alt avg `0.1681` n `239`; crypto_major avg `0.1942` n `8`; equity avg `-0.1502` n `168`; fx avg `-0.0024` n `6`; index avg `-0.0069` n `27`; metal avg `0.0304` n `20`; unknown avg `268.4377` n `1207`
- 4h: commodity avg `-0.0303` n `13`; crypto_alt avg `-0.3576` n `239`; crypto_major avg `0.2416` n `8`; equity avg `-0.0994` n `168`; fx avg `-0.0381` n `6`; index avg `-0.0364` n `27`; metal avg `0.0456` n `20`; unknown avg `2.9637` n `1163`
- 24h: commodity avg `0.6071` n `13`; crypto_alt avg `-2.5793` n `239`; crypto_major avg `-2.1591` n `8`; equity avg `-4.1917` n `167`; fx avg `0.2051` n `6`; index avg `-0.3058` n `27`; metal avg `-1.0362` n `20`; unknown avg `431.0998` n `1055`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1289`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1265`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
