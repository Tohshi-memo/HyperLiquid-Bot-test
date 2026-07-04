# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T11:22:31.781783+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.016` n `12`; crypto_alt avg `0.0406` n `229`; crypto_major avg `-0.0315` n `8`; equity avg `0.0069` n `88`; fx avg `-0.0057` n `6`; index avg `0.0005` n `25`; metal avg `0.0063` n `20`; unknown avg `-0.0078` n `765`
- 1h: commodity avg `0.0306` n `12`; crypto_alt avg `0.2269` n `229`; crypto_major avg `-0.0763` n `8`; equity avg `-0.039` n `88`; fx avg `-0.002` n `6`; index avg `0.0044` n `25`; metal avg `0.0047` n `20`; unknown avg `-0.0278` n `765`
- 4h: commodity avg `0.1186` n `12`; crypto_alt avg `-0.0889` n `229`; crypto_major avg `-0.2343` n `8`; equity avg `-0.0067` n `88`; fx avg `-0.0228` n `6`; index avg `0.0196` n `25`; metal avg `0.0299` n `20`; unknown avg `0.1097` n `765`
- 24h: commodity avg `0.1161` n `12`; crypto_alt avg `0.5959` n `229`; crypto_major avg `1.0357` n `8`; equity avg `0.1016` n `88`; fx avg `-0.0801` n `6`; index avg `-0.027` n `25`; metal avg `-0.0997` n `20`; unknown avg `2.8349` n `743`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0836`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0558`, n `668`, weak_sample_signal
