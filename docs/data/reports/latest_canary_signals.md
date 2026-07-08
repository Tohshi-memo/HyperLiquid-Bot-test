# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T20:52:26.331654+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0659` n `12`; crypto_alt avg `-0.0664` n `229`; crypto_major avg `0.0255` n `8`; equity avg `0.1094` n `91`; fx avg `0.0106` n `6`; index avg `0.0187` n `25`; metal avg `0.0504` n `20`; unknown avg `-0.01` n `764`
- 1h: commodity avg `0.132` n `12`; crypto_alt avg `-0.1214` n `229`; crypto_major avg `-0.0086` n `8`; equity avg `0.0134` n `91`; fx avg `-0.0007` n `6`; index avg `-0.024` n `25`; metal avg `-0.0903` n `20`; unknown avg `-0.0609` n `764`
- 4h: commodity avg `-0.0063` n `12`; crypto_alt avg `-0.0537` n `229`; crypto_major avg `0.0602` n `8`; equity avg `0.6408` n `91`; fx avg `-0.0132` n `6`; index avg `0.0757` n `25`; metal avg `0.1017` n `20`; unknown avg `1.0958` n `764`
- 24h: commodity avg `0.4454` n `12`; crypto_alt avg `-2.2363` n `229`; crypto_major avg `-2.6843` n `8`; equity avg `0.8554` n `91`; fx avg `-0.0025` n `6`; index avg `-0.0573` n `25`; metal avg `-0.8082` n `20`; unknown avg `0.0421` n `739`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1472`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0613`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0592`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0532`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.052`, n `668`, weak_sample_signal
