# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T20:22:32.088274+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0081` n `13`; crypto_alt avg `-0.0281` n `239`; crypto_major avg `0.0154` n `8`; equity avg `0.0648` n `168`; fx avg `-0.0028` n `6`; index avg `-0.0063` n `27`; metal avg `0.0026` n `20`; unknown avg `1.1232` n `1263`
- 1h: commodity avg `-0.0854` n `13`; crypto_alt avg `-0.6706` n `239`; crypto_major avg `-0.3757` n `8`; equity avg `-0.4879` n `168`; fx avg `-0.0159` n `6`; index avg `-0.0772` n `27`; metal avg `-0.0476` n `20`; unknown avg `3.2064` n `1255`
- 4h: commodity avg `0.1797` n `13`; crypto_alt avg `-0.0923` n `239`; crypto_major avg `-0.0541` n `8`; equity avg `0.5779` n `168`; fx avg `-0.0334` n `6`; index avg `0.0677` n `27`; metal avg `-0.0489` n `20`; unknown avg `446.4919` n `1225`
- 24h: commodity avg `0.6697` n `13`; crypto_alt avg `-3.6628` n `239`; crypto_major avg `-3.3575` n `8`; equity avg `-4.2464` n `167`; fx avg `0.2322` n `6`; index avg `-0.303` n `27`; metal avg `-1.1512` n `20`; unknown avg `488.3504` n `1115`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1301`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.127`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
