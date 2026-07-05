# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T13:07:29.030192+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.006` n `12`; crypto_alt avg `0.1186` n `229`; crypto_major avg `0.1466` n `8`; equity avg `-0.0024` n `88`; fx avg `-0.0058` n `6`; index avg `0.005` n `25`; metal avg `0.0015` n `20`; unknown avg `0.0012` n `765`
- 1h: commodity avg `-0.0114` n `12`; crypto_alt avg `0.6643` n `229`; crypto_major avg `0.6795` n `8`; equity avg `0.0463` n `88`; fx avg `-0.0417` n `6`; index avg `0.0014` n `25`; metal avg `0.0187` n `20`; unknown avg `0.1338` n `765`
- 4h: commodity avg `-0.0623` n `12`; crypto_alt avg `0.1077` n `229`; crypto_major avg `0.4246` n `8`; equity avg `0.039` n `88`; fx avg `-0.041` n `6`; index avg `0.01` n `25`; metal avg `0.0285` n `20`; unknown avg `-0.0611` n `765`
- 24h: commodity avg `-0.0377` n `12`; crypto_alt avg `-0.7301` n `229`; crypto_major avg `-0.1512` n `8`; equity avg `0.3313` n `88`; fx avg `-0.0281` n `6`; index avg `0.0492` n `25`; metal avg `0.0898` n `20`; unknown avg `-1.1534` n `731`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
