# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T20:07:32.876061+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0166` n `12`; crypto_alt avg `-0.1577` n `229`; crypto_major avg `-0.293` n `8`; equity avg `-0.0056` n `91`; fx avg `0.001` n `6`; index avg `-0.0111` n `25`; metal avg `-0.0588` n `20`; unknown avg `0.1742` n `763`
- 1h: commodity avg `0.0097` n `12`; crypto_alt avg `-0.0654` n `229`; crypto_major avg `-0.1119` n `8`; equity avg `0.1085` n `91`; fx avg `-0.0023` n `6`; index avg `-0.0111` n `25`; metal avg `-0.0214` n `20`; unknown avg `-0.0316` n `763`
- 4h: commodity avg `0.019` n `12`; crypto_alt avg `0.0505` n `229`; crypto_major avg `0.1041` n `8`; equity avg `-0.4858` n `91`; fx avg `0.004` n `6`; index avg `-0.0675` n `25`; metal avg `0.1633` n `20`; unknown avg `0.1057` n `763`
- 24h: commodity avg `0.0547` n `12`; crypto_alt avg `0.6405` n `229`; crypto_major avg `0.3926` n `8`; equity avg `-0.6448` n `90`; fx avg `0.2115` n `6`; index avg `0.0151` n `25`; metal avg `-0.2174` n `20`; unknown avg `0.2725` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.062`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0618`, n `668`, weak_sample_signal
