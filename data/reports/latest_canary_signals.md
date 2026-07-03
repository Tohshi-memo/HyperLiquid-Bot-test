# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T02:22:31.429403+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0091` n `12`; crypto_alt avg `0.1166` n `229`; crypto_major avg `0.0709` n `8`; equity avg `-0.0958` n `88`; fx avg `0.0078` n `6`; index avg `-0.0409` n `25`; metal avg `0.0017` n `20`; unknown avg `-0.0669` n `765`
- 1h: commodity avg `0.1359` n `12`; crypto_alt avg `0.2835` n `229`; crypto_major avg `0.1985` n `8`; equity avg `0.4681` n `88`; fx avg `0.0305` n `6`; index avg `0.0715` n `25`; metal avg `-0.0109` n `20`; unknown avg `0.6947` n `765`
- 4h: commodity avg `0.1235` n `12`; crypto_alt avg `1.0405` n `229`; crypto_major avg `0.9637` n `8`; equity avg `1.0586` n `88`; fx avg `0.0425` n `6`; index avg `0.2265` n `25`; metal avg `0.6585` n `20`; unknown avg `0.3191` n `765`
- 24h: commodity avg `0.3183` n `12`; crypto_alt avg `2.4775` n `228`; crypto_major avg `3.4717` n `8`; equity avg `-1.4041` n `88`; fx avg `-0.093` n `6`; index avg `-0.2949` n `25`; metal avg `1.3466` n `20`; unknown avg `5.5762` n `739`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0597`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0577`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0529`, n `668`, weak_sample_signal
