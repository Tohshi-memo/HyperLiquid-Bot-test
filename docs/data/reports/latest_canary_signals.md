# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T17:22:29.393558+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0061` n `12`; crypto_alt avg `-0.0471` n `229`; crypto_major avg `0.0012` n `8`; equity avg `0.0203` n `88`; fx avg `-0.0056` n `6`; index avg `-0.0008` n `25`; metal avg `0.0026` n `20`; unknown avg `-0.0582` n `765`
- 1h: commodity avg `0.0112` n `12`; crypto_alt avg `0.2177` n `229`; crypto_major avg `0.1189` n `8`; equity avg `0.0475` n `88`; fx avg `-0.0181` n `6`; index avg `0.0211` n `25`; metal avg `0.0509` n `20`; unknown avg `0.0235` n `765`
- 4h: commodity avg `0.0164` n `12`; crypto_alt avg `0.2222` n `229`; crypto_major avg `0.3544` n `8`; equity avg `0.0755` n `88`; fx avg `-0.0439` n `6`; index avg `0.0088` n `25`; metal avg `0.0353` n `20`; unknown avg `0.4362` n `765`
- 24h: commodity avg `0.287` n `12`; crypto_alt avg `2.5423` n `229`; crypto_major avg `1.9971` n `8`; equity avg `2.2622` n `88`; fx avg `-0.0407` n `6`; index avg `0.6241` n `25`; metal avg `0.6702` n `20`; unknown avg `8.3596` n `738`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0502`, n `668`, weak_sample_signal
