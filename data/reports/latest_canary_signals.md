# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T15:32:26.736287+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0022` n `12`; crypto_alt avg `0.0999` n `229`; crypto_major avg `0.0136` n `8`; equity avg `-0.016` n `88`; fx avg `-0.0062` n `6`; index avg `-0.036` n `25`; metal avg `-0.0351` n `20`; unknown avg `0.0058` n `765`
- 1h: commodity avg `-0.1067` n `12`; crypto_alt avg `0.3475` n `229`; crypto_major avg `0.3883` n `8`; equity avg `0.071` n `88`; fx avg `-0.0041` n `6`; index avg `-0.0114` n `25`; metal avg `0.0197` n `20`; unknown avg `0.0083` n `765`
- 4h: commodity avg `-0.0085` n `12`; crypto_alt avg `0.6065` n `229`; crypto_major avg `0.5137` n `8`; equity avg `-0.1604` n `88`; fx avg `-0.0237` n `6`; index avg `-0.0228` n `25`; metal avg `-0.0964` n `20`; unknown avg `1.1689` n `765`
- 24h: commodity avg `0.3876` n `12`; crypto_alt avg `2.5899` n `229`; crypto_major avg `2.1122` n `8`; equity avg `0.6452` n `88`; fx avg `-0.0448` n `6`; index avg `0.2743` n `25`; metal avg `0.3916` n `20`; unknown avg `7.8862` n `737`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0625`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0505`, n `668`, weak_sample_signal
