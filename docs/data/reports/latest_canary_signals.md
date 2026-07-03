# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T13:22:25.390660+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0346` n `12`; crypto_alt avg `0.1486` n `229`; crypto_major avg `0.1245` n `8`; equity avg `0.0292` n `88`; fx avg `0.0029` n `6`; index avg `-0.0004` n `25`; metal avg `-0.0174` n `20`; unknown avg `1.0672` n `765`
- 1h: commodity avg `0.0841` n `12`; crypto_alt avg `0.2782` n `229`; crypto_major avg `0.3694` n `8`; equity avg `-0.0755` n `88`; fx avg `0.0213` n `6`; index avg `-0.0002` n `25`; metal avg `-0.0137` n `20`; unknown avg `1.8448` n `765`
- 4h: commodity avg `0.0176` n `12`; crypto_alt avg `1.113` n `229`; crypto_major avg `0.922` n `8`; equity avg `0.0574` n `88`; fx avg `0.0284` n `6`; index avg `0.0408` n `25`; metal avg `-0.1683` n `20`; unknown avg `3.0394` n `755`
- 24h: commodity avg `0.4687` n `12`; crypto_alt avg `1.8305` n `229`; crypto_major avg `1.7338` n `8`; equity avg `-0.9115` n `88`; fx avg `-0.1043` n `6`; index avg `0.0387` n `25`; metal avg `0.5704` n `20`; unknown avg `8.5307` n `737`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.063`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0604`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0602`, n `668`, weak_sample_signal
