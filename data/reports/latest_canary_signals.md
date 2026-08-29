# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T20:37:24.430361+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0076` n `12`; crypto_alt avg `-0.0843` n `231`; crypto_major avg `-0.0702` n `8`; equity avg `0.0175` n `128`; fx avg `0.002` n `6`; index avg `-0.0004` n `26`; metal avg `0.0042` n `20`; unknown avg `0.0125` n `792`
- 1h: commodity avg `-0.016` n `12`; crypto_alt avg `-0.0731` n `231`; crypto_major avg `-0.1173` n `8`; equity avg `0.0592` n `128`; fx avg `0.008` n `6`; index avg `0.0142` n `26`; metal avg `0.0062` n `20`; unknown avg `0.3866` n `792`
- 4h: commodity avg `-0.0177` n `12`; crypto_alt avg `-0.1083` n `231`; crypto_major avg `0.0098` n `8`; equity avg `0.1881` n `128`; fx avg `-0.0064` n `6`; index avg `0.0329` n `26`; metal avg `0.0326` n `20`; unknown avg `0.0384` n `792`
- 24h: commodity avg `-0.0263` n `12`; crypto_alt avg `0.8109` n `231`; crypto_major avg `1.1664` n `8`; equity avg `0.4178` n `128`; fx avg `-0.0284` n `6`; index avg `0.0866` n `26`; metal avg `0.1688` n `20`; unknown avg `0.1955` n `728`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2302`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1518`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0576`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0573`, n `668`, weak_sample_signal
