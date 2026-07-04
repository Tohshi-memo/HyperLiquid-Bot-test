# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T12:22:26.368811+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0155` n `12`; crypto_alt avg `0.0153` n `229`; crypto_major avg `0.0118` n `8`; equity avg `-0.0248` n `88`; fx avg `-0.0062` n `6`; index avg `0.0016` n `25`; metal avg `-0.0008` n `20`; unknown avg `-0.039` n `765`
- 1h: commodity avg `-0.0044` n `12`; crypto_alt avg `0.5114` n `229`; crypto_major avg `0.1703` n `8`; equity avg `-0.0626` n `88`; fx avg `0.0123` n `6`; index avg `-0.0112` n `25`; metal avg `-0.0067` n `20`; unknown avg `-0.0085` n `765`
- 4h: commodity avg `0.1068` n `12`; crypto_alt avg `0.6072` n `229`; crypto_major avg `-0.1712` n `8`; equity avg `-0.0679` n `88`; fx avg `0.0082` n `6`; index avg `0.0058` n `25`; metal avg `0.0104` n `20`; unknown avg `-0.0229` n `765`
- 24h: commodity avg `0.1299` n `12`; crypto_alt avg `1.0868` n `229`; crypto_major avg `1.4907` n `8`; equity avg `0.1328` n `88`; fx avg `-0.0432` n `6`; index avg `-0.0379` n `25`; metal avg `0.0266` n `20`; unknown avg `2.9263` n `743`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0582`, n `668`, weak_sample_signal
