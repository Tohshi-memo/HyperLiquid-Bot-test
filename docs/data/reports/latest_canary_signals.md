# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T01:22:24.662933+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.99` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0371` n `12`; crypto_alt avg `0.2717` n `229`; crypto_major avg `0.2927` n `8`; equity avg `0.2263` n `88`; fx avg `-0.0544` n `6`; index avg `0.0702` n `25`; metal avg `0.1906` n `20`; unknown avg `-0.1931` n `765`
- 1h: commodity avg `-0.0057` n `12`; crypto_alt avg `0.5009` n `229`; crypto_major avg `0.3857` n `8`; equity avg `0.4941` n `88`; fx avg `-0.0854` n `6`; index avg `0.1472` n `25`; metal avg `0.5187` n `20`; unknown avg `0.6843` n `765`
- 4h: commodity avg `-0.0279` n `12`; crypto_alt avg `0.5291` n `229`; crypto_major avg `0.3895` n `8`; equity avg `0.6561` n `88`; fx avg `-0.0051` n `6`; index avg `0.1707` n `25`; metal avg `0.6639` n `20`; unknown avg `5.3563` n `765`
- 24h: commodity avg `0.2372` n `12`; crypto_alt avg `2.5704` n `228`; crypto_major avg `3.6951` n `8`; equity avg `-1.7575` n `88`; fx avg `-0.1391` n `6`; index avg `-0.283` n `25`; metal avg `1.3954` n `20`; unknown avg `5.8134` n `739`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0666`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0603`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0571`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0549`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0517`, n `668`, weak_sample_signal
