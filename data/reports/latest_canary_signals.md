# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T12:37:26.946050+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0418` n `12`; crypto_alt avg `-0.062` n `229`; crypto_major avg `-0.0825` n `8`; equity avg `0.0047` n `88`; fx avg `0.0148` n `6`; index avg `-0.0012` n `25`; metal avg `0.0229` n `20`; unknown avg `-0.0128` n `765`
- 1h: commodity avg `-0.053` n `12`; crypto_alt avg `0.0875` n `229`; crypto_major avg `-0.1811` n `8`; equity avg `-0.0586` n `88`; fx avg `-0.0121` n `6`; index avg `0.0014` n `25`; metal avg `-0.0916` n `20`; unknown avg `-0.0343` n `765`
- 4h: commodity avg `-0.011` n `12`; crypto_alt avg `0.8336` n `229`; crypto_major avg `0.5499` n `8`; equity avg `0.2002` n `88`; fx avg `0.0197` n `6`; index avg `0.0175` n `25`; metal avg `-0.2032` n `20`; unknown avg `0.9761` n `755`
- 24h: commodity avg `0.4033` n `12`; crypto_alt avg `1.7008` n `229`; crypto_major avg `1.6727` n `8`; equity avg `-1.0878` n `88`; fx avg `-0.0606` n `6`; index avg `-0.0615` n `25`; metal avg `0.3859` n `20`; unknown avg `6.0792` n `737`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1215`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0698`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0659`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
