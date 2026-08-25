# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T04:07:57.902270+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.9022` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.005` n `12`; crypto_alt avg `-0.1037` n `231`; crypto_major avg `-0.1013` n `8`; equity avg `0.1789` n `122`; fx avg `-0.0088` n `6`; index avg `0.0452` n `25`; metal avg `0.0005` n `20`; unknown avg `0.5943` n `794`
- 1h: commodity avg `0.0276` n `12`; crypto_alt avg `-0.3857` n `231`; crypto_major avg `-0.5262` n `8`; equity avg `0.3371` n `122`; fx avg `0.0013` n `6`; index avg `0.0641` n `25`; metal avg `0.006` n `20`; unknown avg `0.5952` n `794`
- 4h: commodity avg `0.0549` n `12`; crypto_alt avg `1.0181` n `231`; crypto_major avg `1.474` n `8`; equity avg `0.9922` n `122`; fx avg `0.0426` n `6`; index avg `0.1755` n `25`; metal avg `-0.4282` n `20`; unknown avg `0.3719` n `794`
- 24h: commodity avg `0.0519` n `12`; crypto_alt avg `1.825` n `231`; crypto_major avg `2.6599` n `8`; equity avg `-0.4355` n `122`; fx avg `0.0204` n `6`; index avg `-0.0766` n `25`; metal avg `-0.1352` n `20`; unknown avg `0.6309` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0633`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0628`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
