# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T06:22:26.835722+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0334` n `12`; crypto_alt avg `0.07` n `229`; crypto_major avg `-0.1093` n `8`; equity avg `-0.0067` n `88`; fx avg `-0.0159` n `6`; index avg `0.0163` n `25`; metal avg `-0.065` n `20`; unknown avg `0.0588` n `765`
- 1h: commodity avg `0.0081` n `12`; crypto_alt avg `0.5831` n `229`; crypto_major avg `0.4333` n `8`; equity avg `0.2023` n `88`; fx avg `-0.1237` n `6`; index avg `0.0673` n `25`; metal avg `-0.0383` n `20`; unknown avg `0.0344` n `745`
- 4h: commodity avg `0.0992` n `12`; crypto_alt avg `0.1573` n `229`; crypto_major avg `0.2872` n `8`; equity avg `0.582` n `88`; fx avg `-0.0464` n `6`; index avg `0.2077` n `25`; metal avg `-0.1` n `20`; unknown avg `-0.0173` n `745`
- 24h: commodity avg `0.4011` n `12`; crypto_alt avg `2.3902` n `228`; crypto_major avg `3.3161` n `8`; equity avg `0.3262` n `88`; fx avg `-0.1451` n `6`; index avg `0.2109` n `25`; metal avg `1.0022` n `20`; unknown avg `6.0629` n `743`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1272`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0666`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0597`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0552`, n `668`, weak_sample_signal
