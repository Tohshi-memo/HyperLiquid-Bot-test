# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T11:37:30.734214+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.008` n `12`; crypto_alt avg `0.0028` n `229`; crypto_major avg `0.1281` n `8`; equity avg `0.0414` n `88`; fx avg `-0.0014` n `6`; index avg `0.0045` n `25`; metal avg `0.0036` n `20`; unknown avg `-0.0575` n `765`
- 1h: commodity avg `-0.0162` n `12`; crypto_alt avg `-0.0099` n `229`; crypto_major avg `0.2158` n `8`; equity avg `0.0969` n `88`; fx avg `-0.0031` n `6`; index avg `-0.0022` n `25`; metal avg `0.0006` n `20`; unknown avg `0.0074` n `765`
- 4h: commodity avg `-0.0105` n `12`; crypto_alt avg `-0.3088` n `229`; crypto_major avg `-0.0215` n `8`; equity avg `0.0619` n `88`; fx avg `-0.0031` n `6`; index avg `-0.0069` n `25`; metal avg `0.031` n `20`; unknown avg `-0.1377` n `765`
- 24h: commodity avg `-0.0483` n `12`; crypto_alt avg `-1.179` n `229`; crypto_major avg `-0.6178` n `8`; equity avg `0.2746` n `88`; fx avg `0.0119` n `6`; index avg `0.0377` n `25`; metal avg `0.0661` n `20`; unknown avg `-1.2669` n `725`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
