# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T20:22:25.348864+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0099` n `12`; crypto_alt avg `-0.3629` n `229`; crypto_major avg `-0.3563` n `8`; equity avg `-0.0612` n `88`; fx avg `0.0098` n `6`; index avg `0.005` n `25`; metal avg `-0.0105` n `20`; unknown avg `0.0507` n `765`
- 1h: commodity avg `0.0192` n `12`; crypto_alt avg `-0.3882` n `229`; crypto_major avg `-0.4548` n `8`; equity avg `-0.0345` n `88`; fx avg `-0.0383` n `6`; index avg `0.0233` n `25`; metal avg `-0.0131` n `20`; unknown avg `-0.0094` n `765`
- 4h: commodity avg `-0.059` n `12`; crypto_alt avg `-0.5632` n `229`; crypto_major avg `-0.4422` n `8`; equity avg `-0.0208` n `88`; fx avg `-0.0385` n `6`; index avg `0.0029` n `25`; metal avg `0.0092` n `20`; unknown avg `-0.9187` n `765`
- 24h: commodity avg `0.003` n `12`; crypto_alt avg `0.2161` n `229`; crypto_major avg `0.4383` n `8`; equity avg `0.2869` n `88`; fx avg `-0.0458` n `6`; index avg `-0.0227` n `25`; metal avg `0.0828` n `20`; unknown avg `0.6519` n `741`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0624`, n `668`, weak_sample_signal
