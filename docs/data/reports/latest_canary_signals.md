# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T10:37:25.640698+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0039` n `12`; crypto_alt avg `-0.027` n `229`; crypto_major avg `-0.0749` n `8`; equity avg `0.0178` n `88`; fx avg `0.0` n `6`; index avg `0.0024` n `25`; metal avg `0.0012` n `20`; unknown avg `-0.0114` n `765`
- 1h: commodity avg `-0.0084` n `12`; crypto_alt avg `-0.2363` n `229`; crypto_major avg `-0.0588` n `8`; equity avg `0.0211` n `88`; fx avg `0.0015` n `6`; index avg `0.0057` n `25`; metal avg `0.002` n `20`; unknown avg `-0.145` n `765`
- 4h: commodity avg `0.0303` n `12`; crypto_alt avg `-0.1326` n `229`; crypto_major avg `-0.1028` n `8`; equity avg `-0.0039` n `88`; fx avg `0.0031` n `6`; index avg `-0.0134` n `25`; metal avg `0.0172` n `20`; unknown avg `-0.2365` n `765`
- 24h: commodity avg `-0.0181` n `12`; crypto_alt avg `-0.6793` n `229`; crypto_major avg `-0.6994` n `8`; equity avg `0.1327` n `88`; fx avg `0.0212` n `6`; index avg `0.0361` n `25`; metal avg `0.0751` n `20`; unknown avg `-1.2655` n `725`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
