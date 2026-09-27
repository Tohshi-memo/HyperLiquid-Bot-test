# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T09:22:31.440966+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0014` n `12`; crypto_alt avg `0.063` n `234`; crypto_major avg `0.0465` n `8`; equity avg `-0.003` n `141`; fx avg `0.0082` n `6`; index avg `-0.0026` n `26`; metal avg `0.0049` n `20`; unknown avg `-0.0085` n `961`
- 1h: commodity avg `-0.009` n `12`; crypto_alt avg `-0.373` n `234`; crypto_major avg `-0.2742` n `8`; equity avg `0.0006` n `141`; fx avg `0.0085` n `6`; index avg `0.0014` n `26`; metal avg `-0.0067` n `20`; unknown avg `0.4294` n `959`
- 4h: commodity avg `-0.0299` n `12`; crypto_alt avg `0.8391` n `234`; crypto_major avg `0.8643` n `8`; equity avg `0.153` n `141`; fx avg `-0.0122` n `6`; index avg `0.0234` n `26`; metal avg `0.005` n `20`; unknown avg `3.953` n `923`
- 24h: commodity avg `0.0466` n `12`; crypto_alt avg `1.3971` n `234`; crypto_major avg `0.8742` n `8`; equity avg `0.4176` n `141`; fx avg `-0.0002` n `6`; index avg `0.0324` n `26`; metal avg `-0.002` n `20`; unknown avg `6.6097` n `887`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1615`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.149`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1475`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1425`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
