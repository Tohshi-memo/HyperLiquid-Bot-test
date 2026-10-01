# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T18:22:35.808800+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1083` n `13`; crypto_alt avg `0.0833` n `234`; crypto_major avg `0.1209` n `8`; equity avg `0.1442` n `142`; fx avg `-0.0247` n `6`; index avg `0.0274` n `26`; metal avg `0.0747` n `20`; unknown avg `0.5192` n `975`
- 1h: commodity avg `0.1789` n `13`; crypto_alt avg `0.2361` n `234`; crypto_major avg `0.0301` n `8`; equity avg `0.0414` n `142`; fx avg `0.0171` n `6`; index avg `0.0062` n `26`; metal avg `-0.0253` n `20`; unknown avg `-0.3322` n `973`
- 4h: commodity avg `0.1091` n `13`; crypto_alt avg `0.9663` n `234`; crypto_major avg `0.4115` n `8`; equity avg `1.2338` n `142`; fx avg `-0.1377` n `6`; index avg `0.195` n `26`; metal avg `0.1042` n `20`; unknown avg `0.5289` n `909`
- 24h: commodity avg `-0.0875` n `13`; crypto_alt avg `-0.2501` n `234`; crypto_major avg `0.0779` n `8`; equity avg `0.8067` n `142`; fx avg `-0.1152` n `6`; index avg `0.0875` n `26`; metal avg `-0.0037` n `20`; unknown avg `-0.2095` n `840`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1826`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1652`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
