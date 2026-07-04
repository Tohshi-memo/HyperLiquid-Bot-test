# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T22:22:30.545606+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0089` n `12`; crypto_alt avg `-0.1951` n `229`; crypto_major avg `-0.0549` n `8`; equity avg `-0.0074` n `88`; fx avg `0.0` n `6`; index avg `0.0032` n `25`; metal avg `-0.0079` n `20`; unknown avg `0.0564` n `765`
- 1h: commodity avg `0.0318` n `12`; crypto_alt avg `-0.4493` n `229`; crypto_major avg `-0.2338` n `8`; equity avg `0.0014` n `88`; fx avg `0.0012` n `6`; index avg `0.0167` n `25`; metal avg `-0.0048` n `20`; unknown avg `0.2534` n `765`
- 4h: commodity avg `-0.016` n `12`; crypto_alt avg `-0.6906` n `229`; crypto_major avg `-0.4684` n `8`; equity avg `0.0839` n `88`; fx avg `-0.0238` n `6`; index avg `0.0254` n `25`; metal avg `0.0293` n `20`; unknown avg `-0.4229` n `765`
- 24h: commodity avg `0.0025` n `12`; crypto_alt avg `0.0526` n `229`; crypto_major avg `0.5627` n `8`; equity avg `0.2651` n `88`; fx avg `-0.0256` n `6`; index avg `0.0019` n `25`; metal avg `0.0946` n `20`; unknown avg `0.0272` n `741`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.061`, n `668`, weak_sample_signal
