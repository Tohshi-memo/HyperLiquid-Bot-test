# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T21:07:31.265462+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.03` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0` n `12`; crypto_alt avg `-0.0125` n `229`; crypto_major avg `-0.0374` n `8`; equity avg `0.0246` n `88`; fx avg `0.0072` n `6`; index avg `0.006` n `25`; metal avg `-0.0003` n `20`; unknown avg `1.0779` n `765`
- 1h: commodity avg `-0.0486` n `12`; crypto_alt avg `0.3566` n `229`; crypto_major avg `0.3829` n `8`; equity avg `0.0308` n `88`; fx avg `-0.0116` n `6`; index avg `-0.0148` n `25`; metal avg `0.0142` n `20`; unknown avg `0.8058` n `765`
- 4h: commodity avg `-0.1014` n `12`; crypto_alt avg `0.7098` n `229`; crypto_major avg `1.1013` n `8`; equity avg `-0.0058` n `88`; fx avg `-0.011` n `6`; index avg `-0.0196` n `25`; metal avg `-0.0118` n `20`; unknown avg `1.1099` n `765`
- 24h: commodity avg `0.0944` n `12`; crypto_alt avg `3.3738` n `229`; crypto_major avg `3.4898` n `8`; equity avg `1.8527` n `88`; fx avg `-0.0311` n `6`; index avg `0.4782` n `25`; metal avg `0.5376` n `20`; unknown avg `8.2328` n `739`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
