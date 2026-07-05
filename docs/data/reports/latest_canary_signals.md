# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T06:07:26.624904+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0011` n `12`; crypto_alt avg `-0.1424` n `229`; crypto_major avg `-0.0668` n `8`; equity avg `-0.0182` n `88`; fx avg `-0.0007` n `6`; index avg `-0.019` n `25`; metal avg `-0.0004` n `20`; unknown avg `-0.0261` n `733`
- 1h: commodity avg `-0.0067` n `12`; crypto_alt avg `-0.2733` n `229`; crypto_major avg `-0.0955` n `8`; equity avg `0.0131` n `88`; fx avg `0.001` n `6`; index avg `-0.0361` n `25`; metal avg `-0.0012` n `20`; unknown avg `0.004` n `733`
- 4h: commodity avg `0.0128` n `12`; crypto_alt avg `-0.5175` n `229`; crypto_major avg `-0.2582` n `8`; equity avg `0.1085` n `88`; fx avg `-0.0031` n `6`; index avg `0.0123` n `25`; metal avg `-0.017` n `20`; unknown avg `-0.0711` n `733`
- 24h: commodity avg `0.0583` n `12`; crypto_alt avg `-1.237` n `229`; crypto_major avg `-1.3609` n `8`; equity avg `0.1471` n `88`; fx avg `-0.0141` n `6`; index avg `0.0364` n `25`; metal avg `0.069` n `20`; unknown avg `-1.1186` n `727`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
