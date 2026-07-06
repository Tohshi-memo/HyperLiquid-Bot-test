# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T22:37:26.524447+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0041` n `12`; crypto_alt avg `-0.1758` n `229`; crypto_major avg `-0.174` n `8`; equity avg `-0.0241` n `91`; fx avg `0.0097` n `6`; index avg `-0.0163` n `25`; metal avg `0.0161` n `20`; unknown avg `-0.0475` n `763`
- 1h: commodity avg `0.0077` n `12`; crypto_alt avg `-0.181` n `229`; crypto_major avg `-0.1076` n `8`; equity avg `0.0366` n `91`; fx avg `0.0259` n `6`; index avg `0.0106` n `25`; metal avg `0.0131` n `20`; unknown avg `-0.2882` n `763`
- 4h: commodity avg `0.048` n `12`; crypto_alt avg `0.2112` n `229`; crypto_major avg `0.3413` n `8`; equity avg `0.1669` n `91`; fx avg `0.0147` n `6`; index avg `0.0343` n `25`; metal avg `-0.0488` n `20`; unknown avg `-0.4318` n `763`
- 24h: commodity avg `0.1812` n `12`; crypto_alt avg `0.5669` n `229`; crypto_major avg `0.0514` n `8`; equity avg `-0.7381` n `90`; fx avg `0.1347` n `6`; index avg `0.0583` n `25`; metal avg `-0.2922` n `20`; unknown avg `-0.5073` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0612`, n `668`, weak_sample_signal
