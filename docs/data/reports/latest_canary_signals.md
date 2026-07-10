# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T19:37:25.343749+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0147` n `12`; crypto_alt avg `0.3521` n `229`; crypto_major avg `0.4603` n `8`; equity avg `0.0668` n `92`; fx avg `-0.0008` n `6`; index avg `0.0031` n `25`; metal avg `-0.0006` n `20`; unknown avg `0.1786` n `765`
- 1h: commodity avg `-0.0168` n `12`; crypto_alt avg `0.1226` n `229`; crypto_major avg `0.2118` n `8`; equity avg `-0.0083` n `92`; fx avg `0.003` n `6`; index avg `-0.006` n `25`; metal avg `-0.005` n `20`; unknown avg `-0.061` n `765`
- 4h: commodity avg `0.2669` n `12`; crypto_alt avg `0.1328` n `229`; crypto_major avg `0.1335` n `8`; equity avg `0.2611` n `92`; fx avg `-0.0327` n `6`; index avg `0.0289` n `25`; metal avg `-0.0466` n `20`; unknown avg `-0.2509` n `765`
- 24h: commodity avg `-0.2284` n `12`; crypto_alt avg `0.6588` n `229`; crypto_major avg `0.9558` n `8`; equity avg `-0.6283` n `92`; fx avg `-0.1531` n `6`; index avg `0.0353` n `25`; metal avg `0.0936` n `20`; unknown avg `-0.2335` n `732`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
