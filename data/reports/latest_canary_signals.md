# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T06:22:34.369007+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0089` n `12`; crypto_alt avg `-0.4233` n `229`; crypto_major avg `-0.5951` n `8`; equity avg `-0.0519` n `88`; fx avg `0.0034` n `6`; index avg `0.003` n `25`; metal avg `-0.0` n `20`; unknown avg `0.0981` n `765`
- 1h: commodity avg `0.0293` n `12`; crypto_alt avg `-0.1699` n `229`; crypto_major avg `-0.2695` n `8`; equity avg `0.0175` n `88`; fx avg `0.0087` n `6`; index avg `0.0166` n `25`; metal avg `0.0141` n `20`; unknown avg `0.1971` n `745`
- 4h: commodity avg `-0.0139` n `12`; crypto_alt avg `-0.026` n `229`; crypto_major avg `0.269` n `8`; equity avg `0.1511` n `88`; fx avg `0.0247` n `6`; index avg `0.0191` n `25`; metal avg `0.0217` n `20`; unknown avg `0.1183` n `745`
- 24h: commodity avg `-0.0997` n `12`; crypto_alt avg `1.5418` n `229`; crypto_major avg `2.1138` n `8`; equity avg `0.3575` n `88`; fx avg `-0.062` n `6`; index avg `-0.0134` n `25`; metal avg `-0.0198` n `20`; unknown avg `4.7356` n `733`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0685`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0602`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0538`, n `668`, weak_sample_signal
