# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T01:07:28.710789+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.17` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `1.6735` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0128` n `12`; crypto_alt avg `0.1098` n `229`; crypto_major avg `0.1727` n `8`; equity avg `-0.1804` n `88`; fx avg `-0.0123` n `6`; index avg `-0.0736` n `25`; metal avg `-0.0351` n `20`; unknown avg `-0.0768` n `765`
- 1h: commodity avg `-0.0256` n `12`; crypto_alt avg `0.1299` n `229`; crypto_major avg `0.4976` n `8`; equity avg `-0.1865` n `88`; fx avg `-0.0847` n `6`; index avg `-0.0631` n `25`; metal avg `0.0707` n `20`; unknown avg `-0.1114` n `765`
- 4h: commodity avg `-0.1934` n `12`; crypto_alt avg `0.7788` n `229`; crypto_major avg `1.3948` n `8`; equity avg `-0.2787` n `88`; fx avg `0.0693` n `6`; index avg `0.0133` n `25`; metal avg `0.0151` n `20`; unknown avg `1.9312` n `765`
- 24h: commodity avg `-0.2119` n `12`; crypto_alt avg `0.255` n `229`; crypto_major avg `1.5905` n `8`; equity avg `0.0154` n `88`; fx avg `0.0273` n `6`; index avg `0.0542` n `25`; metal avg `0.0434` n `20`; unknown avg `1.4723` n `663`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0636`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.063`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0598`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0595`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0519`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.05`, n `668`, weak_sample_signal
