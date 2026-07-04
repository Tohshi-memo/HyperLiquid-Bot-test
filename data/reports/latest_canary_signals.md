# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T13:22:27.165200+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0008` n `12`; crypto_alt avg `0.2612` n `229`; crypto_major avg `0.3076` n `8`; equity avg `0.0351` n `88`; fx avg `-0.0031` n `6`; index avg `-0.0071` n `25`; metal avg `-0.0003` n `20`; unknown avg `0.0955` n `765`
- 1h: commodity avg `-0.0261` n `12`; crypto_alt avg `0.151` n `229`; crypto_major avg `0.3465` n `8`; equity avg `0.0398` n `88`; fx avg `-0.0044` n `6`; index avg `0.0017` n `25`; metal avg `0.0101` n `20`; unknown avg `0.0636` n `759`
- 4h: commodity avg `0.0793` n `12`; crypto_alt avg `0.6649` n `229`; crypto_major avg `0.2355` n `8`; equity avg `-0.0144` n `88`; fx avg `-0.0009` n `6`; index avg `0.006` n `25`; metal avg `0.007` n `20`; unknown avg `-0.0453` n `759`
- 24h: commodity avg `0.0195` n `12`; crypto_alt avg `0.8893` n `229`; crypto_major avg `1.468` n `8`; equity avg `0.2476` n `88`; fx avg `-0.0689` n `6`; index avg `-0.0361` n `25`; metal avg `0.0505` n `20`; unknown avg `2.2418` n `741`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0608`, n `668`, weak_sample_signal
