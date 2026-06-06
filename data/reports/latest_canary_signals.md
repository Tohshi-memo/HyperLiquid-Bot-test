# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T14:05:51.236723+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0029` n `12`; crypto_alt avg `0.2769` n `228`; crypto_major avg `0.2209` n `8`; equity avg `0.0432` n `74`; fx avg `0.0` n `6`; index avg `-0.0191` n `23`; metal avg `-0.0912` n `18`; unknown avg `2.9919` n `515`
- 1h: commodity avg `0.0112` n `12`; crypto_alt avg `0.0306` n `228`; crypto_major avg `-0.1377` n `8`; equity avg `-0.0574` n `74`; fx avg `0.0056` n `6`; index avg `-0.0528` n `23`; metal avg `-0.0909` n `18`; unknown avg `-0.1651` n `415`
- 4h: commodity avg `0.167` n `12`; crypto_alt avg `1.301` n `228`; crypto_major avg `0.7166` n `8`; equity avg `0.785` n `74`; fx avg `0.0048` n `6`; index avg `0.5068` n `23`; metal avg `0.0242` n `18`; unknown avg `1.1486` n `411`
- 24h: commodity avg `-0.3917` n `12`; crypto_alt avg `-1.6725` n `228`; crypto_major avg `-1.6181` n `8`; equity avg `-3.8865` n `74`; fx avg `-0.1771` n `6`; index avg `-2.3404` n `23`; metal avg `-2.3161` n `18`; unknown avg `0.5071` n `400`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0635`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0626`, n `668`, weak_sample_signal
