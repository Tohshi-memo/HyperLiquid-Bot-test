# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T12:09:44.172819+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0101` n `12`; crypto_alt avg `-0.071` n `229`; crypto_major avg `-0.1105` n `8`; equity avg `-0.0126` n `88`; fx avg `-0.0005` n `6`; index avg `0.0091` n `25`; metal avg `-0.0156` n `20`; unknown avg `0.0325` n `765`
- 1h: commodity avg `-0.0281` n `12`; crypto_alt avg `-0.135` n `229`; crypto_major avg `-0.0113` n `8`; equity avg `-0.032` n `88`; fx avg `0.0039` n `6`; index avg `0.0184` n `25`; metal avg `-0.0016` n `20`; unknown avg `0.0248` n `765`
- 4h: commodity avg `-0.0116` n `12`; crypto_alt avg `-0.6018` n `229`; crypto_major avg `-0.2345` n `8`; equity avg `0.0273` n `88`; fx avg `0.0022` n `6`; index avg `0.006` n `25`; metal avg `0.0336` n `20`; unknown avg `-0.0775` n `765`
- 24h: commodity avg `-0.0362` n `12`; crypto_alt avg `-1.4699` n `229`; crypto_major avg `-0.7743` n `8`; equity avg `0.2645` n `88`; fx avg `0.006` n `6`; index avg `0.0583` n `25`; metal avg `0.0807` n `20`; unknown avg `-1.1979` n `725`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
