# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T00:07:26.458207+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0254` n `12`; crypto_alt avg `-0.1103` n `229`; crypto_major avg `-0.0452` n `8`; equity avg `-0.1157` n `88`; fx avg `0.0857` n `6`; index avg `0.0136` n `25`; metal avg `-0.1186` n `20`; unknown avg `-0.0462` n `765`
- 1h: commodity avg `-0.0493` n `12`; crypto_alt avg `-0.2872` n `229`; crypto_major avg `-0.2963` n `8`; equity avg `-0.3144` n `88`; fx avg `0.093` n `6`; index avg `0.0572` n `25`; metal avg `-0.2116` n `20`; unknown avg `-0.1604` n `765`
- 4h: commodity avg `-0.1757` n `12`; crypto_alt avg `0.4019` n `229`; crypto_major avg `0.7618` n `8`; equity avg `-0.1165` n `88`; fx avg `0.1841` n `6`; index avg `0.0706` n `25`; metal avg `-0.0458` n `20`; unknown avg `0.8843` n `765`
- 24h: commodity avg `-0.1726` n `12`; crypto_alt avg `0.1262` n `229`; crypto_major avg `0.8581` n `8`; equity avg `0.2393` n `88`; fx avg `0.1087` n `6`; index avg `0.152` n `25`; metal avg `-0.0303` n `20`; unknown avg `1.3037` n `663`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0617`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0568`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0531`, n `668`, weak_sample_signal
