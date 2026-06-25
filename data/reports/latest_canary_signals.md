# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T20:07:30.560659+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0506` n `12`; crypto_alt avg `0.4775` n `228`; crypto_major avg `0.7204` n `8`; equity avg `0.3662` n `86`; fx avg `0.0006` n `6`; index avg `0.0838` n `23`; metal avg `0.0541` n `20`; unknown avg `0.0517` n `765`
- 1h: commodity avg `0.0043` n `12`; crypto_alt avg `0.2646` n `228`; crypto_major avg `0.5659` n `8`; equity avg `0.4216` n `86`; fx avg `-0.0032` n `6`; index avg `0.0647` n `23`; metal avg `-0.0436` n `20`; unknown avg `-0.058` n `765`
- 4h: commodity avg `0.0275` n `12`; crypto_alt avg `-0.4832` n `228`; crypto_major avg `0.4605` n `8`; equity avg `0.1017` n `86`; fx avg `0.0173` n `6`; index avg `0.0356` n `23`; metal avg `-0.1939` n `20`; unknown avg `0.3165` n `765`
- 24h: commodity avg `0.509` n `12`; crypto_alt avg `-1.5168` n `228`; crypto_major avg `-0.9277` n `8`; equity avg `-0.7859` n `86`; fx avg `0.0848` n `6`; index avg `0.174` n `23`; metal avg `0.3448` n `20`; unknown avg `0.1254` n `700`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1814`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0618`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0598`, n `668`, weak_sample_signal
