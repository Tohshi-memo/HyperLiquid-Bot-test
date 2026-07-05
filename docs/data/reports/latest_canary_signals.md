# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T19:22:26.980090+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0156` n `12`; crypto_alt avg `0.0765` n `229`; crypto_major avg `0.0153` n `8`; equity avg `-0.016` n `88`; fx avg `-0.0157` n `6`; index avg `-0.0063` n `25`; metal avg `0.0037` n `20`; unknown avg `-0.1396` n `765`
- 1h: commodity avg `-0.0151` n `12`; crypto_alt avg `0.1917` n `229`; crypto_major avg `0.1817` n `8`; equity avg `0.0229` n `88`; fx avg `-0.0233` n `6`; index avg `0.0058` n `25`; metal avg `0.0003` n `20`; unknown avg `0.6095` n `765`
- 4h: commodity avg `0.0003` n `12`; crypto_alt avg `0.4859` n `229`; crypto_major avg `0.2007` n `8`; equity avg `0.0779` n `88`; fx avg `-0.0` n `6`; index avg `0.0041` n `25`; metal avg `-0.0144` n `20`; unknown avg `0.7604` n `695`
- 24h: commodity avg `0.036` n `12`; crypto_alt avg `-1.0944` n `229`; crypto_major avg `-0.7149` n `8`; equity avg `0.3134` n `88`; fx avg `-0.0996` n `6`; index avg `0.1058` n `25`; metal avg `0.0308` n `20`; unknown avg `0.8387` n `663`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.072`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
