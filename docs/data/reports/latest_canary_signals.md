# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T14:22:26.235887+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0006` n `12`; crypto_alt avg `0.0121` n `229`; crypto_major avg `0.0165` n `8`; equity avg `-0.0405` n `88`; fx avg `-0.0254` n `6`; index avg `0.0169` n `25`; metal avg `0.004` n `20`; unknown avg `0.0007` n `765`
- 1h: commodity avg `0.0002` n `12`; crypto_alt avg `-0.034` n `229`; crypto_major avg `0.1269` n `8`; equity avg `-0.0762` n `88`; fx avg `-0.0249` n `6`; index avg `0.0068` n `25`; metal avg `-0.0146` n `20`; unknown avg `0.0703` n `765`
- 4h: commodity avg `-0.0093` n `12`; crypto_alt avg `0.3672` n `229`; crypto_major avg `0.6851` n `8`; equity avg `0.0328` n `88`; fx avg `-0.0652` n `6`; index avg `0.0219` n `25`; metal avg `0.014` n `20`; unknown avg `0.1548` n `765`
- 24h: commodity avg `0.0247` n `12`; crypto_alt avg `-0.9634` n `229`; crypto_major avg `-0.4714` n `8`; equity avg `0.246` n `88`; fx avg `-0.0531` n `6`; index avg `0.0501` n `25`; metal avg `0.0869` n `20`; unknown avg `-1.1211` n `731`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
