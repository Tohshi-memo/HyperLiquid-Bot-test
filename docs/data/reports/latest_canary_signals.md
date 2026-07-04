# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T10:22:28.796573+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0003` n `12`; crypto_alt avg `0.0396` n `229`; crypto_major avg `-0.0064` n `8`; equity avg `0.0101` n `88`; fx avg `-0.0051` n `6`; index avg `0.004` n `25`; metal avg `0.0035` n `20`; unknown avg `0.0071` n `765`
- 1h: commodity avg `0.0766` n `12`; crypto_alt avg `-0.1715` n `229`; crypto_major avg `-0.1584` n `8`; equity avg `0.0277` n `88`; fx avg `-0.0068` n `6`; index avg `0.0121` n `25`; metal avg `-0.0018` n `20`; unknown avg `-0.0744` n `765`
- 4h: commodity avg `0.0725` n `12`; crypto_alt avg `-0.159` n `229`; crypto_major avg `0.0559` n `8`; equity avg `0.0317` n `88`; fx avg `-0.0276` n `6`; index avg `0.0111` n `25`; metal avg `0.0194` n `20`; unknown avg `0.2815` n `765`
- 24h: commodity avg `0.0743` n `12`; crypto_alt avg `0.9796` n `229`; crypto_major avg `1.8562` n `8`; equity avg `0.2628` n `88`; fx avg `-0.0699` n `6`; index avg `-0.0146` n `25`; metal avg `-0.1428` n `20`; unknown avg `5.4523` n `743`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0569`, n `668`, weak_sample_signal
