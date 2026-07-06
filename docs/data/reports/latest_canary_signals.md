# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T21:52:30.093350+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0146` n `12`; crypto_alt avg `0.133` n `229`; crypto_major avg `0.2693` n `8`; equity avg `0.0199` n `91`; fx avg `0.0328` n `6`; index avg `0.001` n `25`; metal avg `-0.0016` n `20`; unknown avg `-0.1814` n `763`
- 1h: commodity avg `0.0188` n `12`; crypto_alt avg `0.6888` n `229`; crypto_major avg `0.8043` n `8`; equity avg `0.0857` n `91`; fx avg `0.0366` n `6`; index avg `0.0361` n `25`; metal avg `0.0321` n `20`; unknown avg `0.0782` n `763`
- 4h: commodity avg `0.095` n `12`; crypto_alt avg `0.6865` n `229`; crypto_major avg `0.9043` n `8`; equity avg `0.1241` n `91`; fx avg `0.0288` n `6`; index avg `0.0545` n `25`; metal avg `0.0396` n `20`; unknown avg `-0.2294` n `763`
- 24h: commodity avg `0.0483` n `12`; crypto_alt avg `1.0301` n `229`; crypto_major avg `0.9802` n `8`; equity avg `-0.6104` n `90`; fx avg `0.1919` n `6`; index avg `0.0545` n `25`; metal avg `-0.1603` n `20`; unknown avg `-0.0996` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0612`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0604`, n `668`, weak_sample_signal
