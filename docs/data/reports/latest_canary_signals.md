# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T02:22:28.660237+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2779` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0246` n `12`; crypto_alt avg `-0.0805` n `229`; crypto_major avg `-0.0159` n `8`; equity avg `-0.0082` n `88`; fx avg `0.0015` n `6`; index avg `0.001` n `25`; metal avg `-0.0099` n `20`; unknown avg `-0.0558` n `765`
- 1h: commodity avg `0.0359` n `12`; crypto_alt avg `-0.1802` n `229`; crypto_major avg `-0.1998` n `8`; equity avg `0.0517` n `88`; fx avg `0.0024` n `6`; index avg `0.0017` n `25`; metal avg `-0.0123` n `20`; unknown avg `0.2902` n `765`
- 4h: commodity avg `0.0392` n `12`; crypto_alt avg `-1.1189` n `229`; crypto_major avg `-1.2741` n `8`; equity avg `0.0112` n `88`; fx avg `0.0157` n `6`; index avg `0.0038` n `25`; metal avg `-0.0085` n `20`; unknown avg `-0.4946` n `763`
- 24h: commodity avg `0.0471` n `12`; crypto_alt avg `-0.4061` n `229`; crypto_major avg `-0.2719` n `8`; equity avg `0.2332` n `88`; fx avg `0.0116` n `6`; index avg `0.0412` n `25`; metal avg `0.0979` n `20`; unknown avg `-0.9088` n `741`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
