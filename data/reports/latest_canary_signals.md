# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T14:52:31.880521+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0114` n `13`; crypto_alt avg `0.1964` n `239`; crypto_major avg `0.1985` n `8`; equity avg `0.5874` n `166`; fx avg `-0.0028` n `6`; index avg `0.1077` n `27`; metal avg `0.0956` n `20`; unknown avg `158.0287` n `1267`
- 1h: commodity avg `0.22` n `13`; crypto_alt avg `0.4034` n `239`; crypto_major avg `0.2521` n `8`; equity avg `0.2711` n `166`; fx avg `0.0167` n `6`; index avg `0.102` n `27`; metal avg `0.1406` n `20`; unknown avg `244.1359` n `1251`
- 4h: commodity avg `0.4089` n `13`; crypto_alt avg `-0.0475` n `239`; crypto_major avg `0.5535` n `8`; equity avg `0.4982` n `166`; fx avg `0.0854` n `6`; index avg `0.0923` n `27`; metal avg `0.2481` n `20`; unknown avg `2.4427` n `1246`
- 24h: commodity avg `0.1296` n `13`; crypto_alt avg `-4.4537` n `239`; crypto_major avg `-4.8177` n `8`; equity avg `-1.7428` n `166`; fx avg `0.1318` n `6`; index avg `-0.0784` n `27`; metal avg `-0.7221` n `20`; unknown avg `6.1798` n `1138`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1303`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
