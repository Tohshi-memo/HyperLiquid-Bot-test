# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T01:22:26.965704+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.24` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0362` n `12`; crypto_alt avg `0.0353` n `229`; crypto_major avg `-0.0449` n `8`; equity avg `-0.0252` n `88`; fx avg `0.0108` n `6`; index avg `0.0191` n `25`; metal avg `0.0126` n `20`; unknown avg `0.0067` n `765`
- 1h: commodity avg `-0.0078` n `12`; crypto_alt avg `0.3595` n `229`; crypto_major avg `0.5959` n `8`; equity avg `-0.2794` n `88`; fx avg `-0.0266` n `6`; index avg `-0.0912` n `25`; metal avg `0.0176` n `20`; unknown avg `3.1487` n `765`
- 4h: commodity avg `-0.1744` n `12`; crypto_alt avg `0.3829` n `229`; crypto_major avg `0.9248` n `8`; equity avg `-0.3142` n `88`; fx avg `0.0862` n `6`; index avg `0.0387` n `25`; metal avg `0.0345` n `20`; unknown avg `1.2856` n `765`
- 24h: commodity avg `-0.176` n `12`; crypto_alt avg `0.834` n `229`; crypto_major avg `1.9966` n `8`; equity avg `0.0321` n `88`; fx avg `0.0348` n `6`; index avg `0.1075` n `25`; metal avg `0.0584` n `20`; unknown avg `1.5297` n `663`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0636`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0606`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0596`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0596`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0574`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0502`, n `668`, weak_sample_signal
