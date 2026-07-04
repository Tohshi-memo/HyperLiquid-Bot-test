# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T08:22:32.323722+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0004` n `12`; crypto_alt avg `-0.0787` n `229`; crypto_major avg `0.0379` n `8`; equity avg `0.0221` n `88`; fx avg `0.0022` n `6`; index avg `0.0132` n `25`; metal avg `0.0015` n `20`; unknown avg `0.0128` n `765`
- 1h: commodity avg `0.0073` n `12`; crypto_alt avg `-0.1789` n `229`; crypto_major avg `0.1062` n `8`; equity avg `-0.0014` n `88`; fx avg `-0.0188` n `6`; index avg `0.0025` n `25`; metal avg `0.0127` n `20`; unknown avg `0.1138` n `765`
- 4h: commodity avg `-0.0058` n `12`; crypto_alt avg `-0.3723` n `229`; crypto_major avg `-0.1381` n `8`; equity avg `0.0545` n `88`; fx avg `-0.013` n `6`; index avg `0.0022` n `25`; metal avg `0.0142` n `20`; unknown avg `0.4036` n `745`
- 24h: commodity avg `-0.0327` n `12`; crypto_alt avg `1.4086` n `229`; crypto_major avg `2.4035` n `8`; equity avg `0.3383` n `88`; fx avg `-0.03` n `6`; index avg `-0.0194` n `25`; metal avg `-0.2118` n `20`; unknown avg `5.337` n `733`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0565`, n `668`, weak_sample_signal
