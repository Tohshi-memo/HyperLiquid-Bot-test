# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T06:52:24.076296+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0058` n `12`; crypto_alt avg `-0.3033` n `231`; crypto_major avg `-0.1615` n `8`; equity avg `-0.0659` n `122`; fx avg `-0.011` n `6`; index avg `-0.0083` n `25`; metal avg `-0.042` n `20`; unknown avg `-0.0394` n `794`
- 1h: commodity avg `-0.0292` n `12`; crypto_alt avg `-0.823` n `231`; crypto_major avg `-0.707` n `8`; equity avg `0.062` n `122`; fx avg `0.0089` n `6`; index avg `0.0476` n `25`; metal avg `0.0814` n `20`; unknown avg `-0.1501` n `778`
- 4h: commodity avg `-0.2703` n `12`; crypto_alt avg `-0.2731` n `231`; crypto_major avg `-0.2039` n `8`; equity avg `0.9989` n `122`; fx avg `0.0227` n `6`; index avg `0.2032` n `25`; metal avg `0.0936` n `20`; unknown avg `-0.1266` n `778`
- 24h: commodity avg `-0.1235` n `12`; crypto_alt avg `1.3584` n `231`; crypto_major avg `2.036` n `8`; equity avg `0.272` n `122`; fx avg `0.0361` n `6`; index avg `0.0803` n `25`; metal avg `-0.2145` n `20`; unknown avg `0.4358` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.118`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0563`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0559`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0545`, n `668`, weak_sample_signal
