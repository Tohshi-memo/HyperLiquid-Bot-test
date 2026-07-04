# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T09:52:30.788781+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0232` n `12`; crypto_alt avg `0.0867` n `229`; crypto_major avg `0.126` n `8`; equity avg `0.0479` n `88`; fx avg `0.0076` n `6`; index avg `0.0171` n `25`; metal avg `0.0015` n `20`; unknown avg `-0.0723` n `765`
- 1h: commodity avg `0.0802` n `12`; crypto_alt avg `-0.3314` n `229`; crypto_major avg `-0.3245` n `8`; equity avg `0.0162` n `88`; fx avg `0.0125` n `6`; index avg `0.001` n `25`; metal avg `0.0109` n `20`; unknown avg `-0.2265` n `765`
- 4h: commodity avg `0.0801` n `12`; crypto_alt avg `-0.6613` n `229`; crypto_major avg `-0.4607` n `8`; equity avg `-0.0237` n `88`; fx avg `-0.0108` n `6`; index avg `0.018` n `25`; metal avg `0.019` n `20`; unknown avg `0.4662` n `745`
- 24h: commodity avg `0.0376` n `12`; crypto_alt avg `0.9844` n `229`; crypto_major avg `2.032` n `8`; equity avg `0.3504` n `88`; fx avg `-0.0518` n `6`; index avg `-0.0135` n `25`; metal avg `-0.115` n `20`; unknown avg `5.4232` n `743`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0567`, n `668`, weak_sample_signal
