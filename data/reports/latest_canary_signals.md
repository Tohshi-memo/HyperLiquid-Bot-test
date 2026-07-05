# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T11:07:26.065233+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0009` n `12`; crypto_alt avg `0.0358` n `229`; crypto_major avg `-0.0162` n `8`; equity avg `0.0243` n `88`; fx avg `0.0` n `6`; index avg `-0.0046` n `25`; metal avg `0.0039` n `20`; unknown avg `0.0249` n `765`
- 1h: commodity avg `0.0126` n `12`; crypto_alt avg `0.2453` n `229`; crypto_major avg `0.1964` n `8`; equity avg `0.1301` n `88`; fx avg `-0.0031` n `6`; index avg `0.0006` n `25`; metal avg `0.0133` n `20`; unknown avg `0.0007` n `765`
- 4h: commodity avg `0.0212` n `12`; crypto_alt avg `-0.2064` n `229`; crypto_major avg `0.0006` n `8`; equity avg `0.0759` n `88`; fx avg `-0.0031` n `6`; index avg `-0.0126` n `25`; metal avg `0.0336` n `20`; unknown avg `-0.1799` n `765`
- 24h: commodity avg `-0.0121` n `12`; crypto_alt avg `-0.8239` n `229`; crypto_major avg `-0.6384` n `8`; equity avg `0.266` n `88`; fx avg `0.015` n `6`; index avg `0.0276` n `25`; metal avg `0.0827` n `20`; unknown avg `-1.2094` n `725`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
