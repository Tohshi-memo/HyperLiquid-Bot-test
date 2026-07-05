# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T21:37:27.984323+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0065` n `12`; crypto_alt avg `0.1251` n `229`; crypto_major avg `0.0537` n `8`; equity avg `0.0174` n `88`; fx avg `-0.0042` n `6`; index avg `0.0039` n `25`; metal avg `-0.0063` n `20`; unknown avg `0.1324` n `765`
- 1h: commodity avg `0.0412` n `12`; crypto_alt avg `0.4505` n `229`; crypto_major avg `0.4525` n `8`; equity avg `-0.0031` n `88`; fx avg `0.0207` n `6`; index avg `-0.0022` n `25`; metal avg `-0.008` n `20`; unknown avg `0.0366` n `765`
- 4h: commodity avg `-0.0219` n `12`; crypto_alt avg `0.658` n `229`; crypto_major avg `0.5816` n `8`; equity avg `0.1214` n `88`; fx avg `0.0025` n `6`; index avg `0.0098` n `25`; metal avg `-0.0015` n `20`; unknown avg `0.8087` n `765`
- 24h: commodity avg `0.0375` n `12`; crypto_alt avg `-0.7289` n `229`; crypto_major avg `-0.1465` n `8`; equity avg `0.3154` n `88`; fx avg `-0.0387` n `6`; index avg `0.0847` n `25`; metal avg `0.0078` n `20`; unknown avg `1.1567` n `663`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0685`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
