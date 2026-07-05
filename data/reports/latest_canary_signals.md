# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T10:52:29.858285+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0056` n `12`; crypto_alt avg `-0.0253` n `229`; crypto_major avg `0.1156` n `8`; equity avg `0.0572` n `88`; fx avg `-0.0031` n `6`; index avg `-0.002` n `25`; metal avg `0.0028` n `20`; unknown avg `0.0398` n `765`
- 1h: commodity avg `0.0085` n `12`; crypto_alt avg `0.2538` n `229`; crypto_major avg `0.3889` n `8`; equity avg `0.1161` n `88`; fx avg `-0.0031` n `6`; index avg `0.007` n `25`; metal avg `0.0111` n `20`; unknown avg `-0.0592` n `765`
- 4h: commodity avg `0.0195` n `12`; crypto_alt avg `-0.2321` n `229`; crypto_major avg `-0.0199` n `8`; equity avg `0.0485` n `88`; fx avg `-0.0017` n `6`; index avg `-0.0079` n `25`; metal avg `0.0255` n `20`; unknown avg `-0.2146` n `765`
- 24h: commodity avg `-0.017` n `12`; crypto_alt avg `-0.8379` n `229`; crypto_major avg `-0.6603` n `8`; equity avg `0.1905` n `88`; fx avg `0.0405` n `6`; index avg `0.0327` n `25`; metal avg `0.0803` n `20`; unknown avg `-1.2226` n `725`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
