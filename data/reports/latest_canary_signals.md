# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T04:22:26.935832+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.8351` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0426` n `12`; crypto_alt avg `0.1715` n `231`; crypto_major avg `0.1508` n `8`; equity avg `0.0869` n `122`; fx avg `0.0051` n `6`; index avg `0.0114` n `25`; metal avg `-0.0156` n `20`; unknown avg `0.027` n `794`
- 1h: commodity avg `-0.0147` n `12`; crypto_alt avg `-0.2614` n `231`; crypto_major avg `-0.3283` n `8`; equity avg `0.3592` n `122`; fx avg `0.0035` n `6`; index avg `0.0435` n `25`; metal avg `0.0075` n `20`; unknown avg `0.6872` n `794`
- 4h: commodity avg `0.0311` n `12`; crypto_alt avg `1.2599` n `231`; crypto_major avg `1.4672` n `8`; equity avg `1.157` n `122`; fx avg `0.0366` n `6`; index avg `0.2108` n `25`; metal avg `-0.3679` n `20`; unknown avg `0.5892` n `794`
- 24h: commodity avg `0.0079` n `12`; crypto_alt avg `1.4745` n `231`; crypto_major avg `2.4527` n `8`; equity avg `-0.4468` n `122`; fx avg `0.0243` n `6`; index avg `-0.0744` n `25`; metal avg `-0.1561` n `20`; unknown avg `0.5281` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0639`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.062`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.062`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0595`, n `668`, weak_sample_signal
