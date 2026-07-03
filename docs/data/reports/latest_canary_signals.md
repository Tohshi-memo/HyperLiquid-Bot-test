# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T14:07:33.252101+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0906` n `12`; crypto_alt avg `-0.1435` n `229`; crypto_major avg `-0.1325` n `8`; equity avg `-0.0648` n `88`; fx avg `-0.015` n `6`; index avg `-0.0536` n `25`; metal avg `-0.0188` n `20`; unknown avg `-0.032` n `765`
- 1h: commodity avg `0.1372` n `12`; crypto_alt avg `0.1206` n `229`; crypto_major avg `0.1771` n `8`; equity avg `-0.0535` n `88`; fx avg `-0.0194` n `6`; index avg `-0.0087` n `25`; metal avg `-0.0284` n `20`; unknown avg `-0.0251` n `765`
- 4h: commodity avg `0.1425` n `12`; crypto_alt avg `0.9654` n `229`; crypto_major avg `1.0097` n `8`; equity avg `-0.0536` n `88`; fx avg `-0.0171` n `6`; index avg `0.0085` n `25`; metal avg `-0.1775` n `20`; unknown avg `1.3977` n `765`
- 24h: commodity avg `0.5426` n `12`; crypto_alt avg `1.5076` n `229`; crypto_major avg `1.2753` n `8`; equity avg `-1.524` n `88`; fx avg `-0.1046` n `6`; index avg `-0.0445` n `25`; metal avg `0.314` n `20`; unknown avg `6.7374` n `737`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0705`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0694`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0571`, n `668`, weak_sample_signal
