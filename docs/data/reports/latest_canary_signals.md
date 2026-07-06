# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T13:37:30.789523+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3349` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0873` n `12`; crypto_alt avg `0.101` n `229`; crypto_major avg `0.0001` n `8`; equity avg `-0.0955` n `88`; fx avg `-0.0026` n `6`; index avg `-0.0073` n `25`; metal avg `0.0996` n `20`; unknown avg `-0.1567` n `765`
- 1h: commodity avg `-0.0188` n `12`; crypto_alt avg `-0.4417` n `229`; crypto_major avg `-0.9591` n `8`; equity avg `-0.3868` n `88`; fx avg `0.0162` n `6`; index avg `-0.0313` n `25`; metal avg `0.0587` n `20`; unknown avg `-0.4741` n `765`
- 4h: commodity avg `-0.0489` n `12`; crypto_alt avg `-0.7731` n `229`; crypto_major avg `-1.361` n `8`; equity avg `-0.5623` n `88`; fx avg `0.0276` n `6`; index avg `-0.0261` n `25`; metal avg `-0.0271` n `20`; unknown avg `-0.3456` n `765`
- 24h: commodity avg `-0.1843` n `12`; crypto_alt avg `-1.3263` n `229`; crypto_major avg `-1.4495` n `8`; equity avg `-1.2792` n `88`; fx avg `0.1448` n `6`; index avg `-0.0501` n `25`; metal avg `-0.3518` n `20`; unknown avg `0.4768` n `661`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0694`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.056`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0559`, n `668`, weak_sample_signal
