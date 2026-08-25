# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T02:22:27.732042+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `2.2323` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.8041` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0294` n `12`; crypto_alt avg `0.7616` n `231`; crypto_major avg `0.7757` n `8`; equity avg `0.13` n `122`; fx avg `0.0066` n `6`; index avg `0.0252` n `25`; metal avg `0.0792` n `20`; unknown avg `0.0915` n `794`
- 1h: commodity avg `0.1129` n `12`; crypto_alt avg `0.7055` n `231`; crypto_major avg `0.6789` n `8`; equity avg `0.4547` n `122`; fx avg `0.0155` n `6`; index avg `0.0744` n `25`; metal avg `-0.1921` n `20`; unknown avg `-0.08` n `794`
- 4h: commodity avg `0.1702` n `12`; crypto_alt avg `1.4371` n `231`; crypto_major avg `2.135` n `8`; equity avg `0.3309` n `122`; fx avg `0.0174` n `6`; index avg `0.0082` n `25`; metal avg `-0.0973` n `20`; unknown avg `0.6048` n `794`
- 24h: commodity avg `0.1893` n `12`; crypto_alt avg `1.6581` n `231`; crypto_major avg `2.2142` n `8`; equity avg `-1.4287` n `122`; fx avg `0.0463` n `6`; index avg `-0.258` n `25`; metal avg `-0.0696` n `20`; unknown avg `0.5352` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0633`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0585`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0478`, n `668`, weak_sample_signal
