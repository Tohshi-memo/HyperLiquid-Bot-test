# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T07:37:33.912178+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0103` n `12`; crypto_alt avg `-0.096` n `228`; crypto_major avg `-0.1218` n `8`; equity avg `-0.0065` n `88`; fx avg `0.0157` n `6`; index avg `0.0009` n `23`; metal avg `-0.0084` n `20`; unknown avg `-0.0157` n `748`
- 1h: commodity avg `0.0408` n `12`; crypto_alt avg `0.0611` n `228`; crypto_major avg `-0.0034` n `8`; equity avg `0.0408` n `88`; fx avg `0.0315` n `6`; index avg `0.0065` n `23`; metal avg `-0.0189` n `20`; unknown avg `-0.0732` n `748`
- 4h: commodity avg `0.0156` n `12`; crypto_alt avg `-0.2029` n `228`; crypto_major avg `-0.2627` n `8`; equity avg `0.1038` n `88`; fx avg `0.0299` n `6`; index avg `0.0124` n `23`; metal avg `-0.0249` n `20`; unknown avg `-0.3701` n `716`
- 24h: commodity avg `-0.083` n `12`; crypto_alt avg `0.6439` n `228`; crypto_major avg `0.0954` n `8`; equity avg `1.3223` n `87`; fx avg `0.0766` n `6`; index avg `0.0016` n `23`; metal avg `0.5831` n `20`; unknown avg `-0.2431` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2037`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1606`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
