# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T03:52:23.387778+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `2.3315` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0167` n `12`; crypto_alt avg `-0.4352` n `231`; crypto_major avg `-0.4672` n `8`; equity avg `-0.0854` n `122`; fx avg `0.0139` n `6`; index avg `-0.0212` n `25`; metal avg `-0.0373` n `20`; unknown avg `0.0201` n `794`
- 1h: commodity avg `-0.0355` n `12`; crypto_alt avg `0.0187` n `231`; crypto_major avg `0.046` n `8`; equity avg `0.32` n `122`; fx avg `0.0134` n `6`; index avg `0.0551` n `25`; metal avg `0.0276` n `20`; unknown avg `0.3178` n `794`
- 4h: commodity avg `0.0483` n `12`; crypto_alt avg `1.4256` n `231`; crypto_major avg `1.9026` n `8`; equity avg `0.6772` n `122`; fx avg `0.0406` n `6`; index avg `0.0724` n `25`; metal avg `-0.4289` n `20`; unknown avg `0.4706` n `794`
- 24h: commodity avg `0.0378` n `12`; crypto_alt avg `1.9688` n `231`; crypto_major avg `2.7529` n `8`; equity avg `-0.6091` n `122`; fx avg `0.0315` n `6`; index avg `-0.1209` n `25`; metal avg `-0.1863` n `20`; unknown avg `0.5552` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
