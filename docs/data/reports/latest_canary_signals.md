# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T07:07:28.861798+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0089` n `12`; crypto_alt avg `-0.0591` n `229`; crypto_major avg `-0.0984` n `8`; equity avg `-0.0075` n `88`; fx avg `0.0195` n `6`; index avg `-0.0084` n `25`; metal avg `-0.0165` n `20`; unknown avg `-0.0456` n `765`
- 1h: commodity avg `-0.0106` n `12`; crypto_alt avg `-0.3382` n `229`; crypto_major avg `-0.5719` n `8`; equity avg `-0.02` n `88`; fx avg `-0.0002` n `6`; index avg `0.0091` n `25`; metal avg `-0.0106` n `20`; unknown avg `0.2072` n `765`
- 4h: commodity avg `-0.0279` n `12`; crypto_alt avg `-0.1144` n `229`; crypto_major avg `0.1625` n `8`; equity avg `0.088` n `88`; fx avg `0.0308` n `6`; index avg `0.0241` n `25`; metal avg `0.0074` n `20`; unknown avg `0.1683` n `745`
- 24h: commodity avg `-0.1304` n `12`; crypto_alt avg `1.6473` n `229`; crypto_major avg `2.1715` n `8`; equity avg `0.4215` n `88`; fx avg `-0.0064` n `6`; index avg `-0.0192` n `25`; metal avg `-0.1541` n `20`; unknown avg `5.3806` n `733`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0549`, n `668`, weak_sample_signal
