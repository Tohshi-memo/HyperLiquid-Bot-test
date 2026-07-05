# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T12:37:25.174767+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0013` n `12`; crypto_alt avg `0.3587` n `229`; crypto_major avg `0.3409` n `8`; equity avg `0.0141` n `88`; fx avg `-0.0162` n `6`; index avg `-0.0079` n `25`; metal avg `0.0001` n `20`; unknown avg `0.0098` n `765`
- 1h: commodity avg `-0.0005` n `12`; crypto_alt avg `0.3997` n `229`; crypto_major avg `0.4454` n `8`; equity avg `-0.0029` n `88`; fx avg `-0.0146` n `6`; index avg `0.0101` n `25`; metal avg `0.01` n `20`; unknown avg `0.1485` n `765`
- 4h: commodity avg `-0.0276` n `12`; crypto_alt avg `0.0381` n `229`; crypto_major avg `0.3283` n `8`; equity avg `0.0051` n `88`; fx avg `-0.0177` n `6`; index avg `0.0081` n `25`; metal avg `0.0193` n `20`; unknown avg `-0.0517` n `765`
- 24h: commodity avg `-0.0681` n `12`; crypto_alt avg `-0.9723` n `229`; crypto_major avg `-0.2584` n `8`; equity avg `0.3204` n `88`; fx avg `-0.0037` n `6`; index avg `0.0313` n `25`; metal avg `0.096` n `20`; unknown avg `-1.171` n `725`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
