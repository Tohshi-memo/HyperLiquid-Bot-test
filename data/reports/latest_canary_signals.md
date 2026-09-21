# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T20:38:05.351667+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.5965` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0212` n `12`; crypto_alt avg `-0.0702` n `234`; crypto_major avg `-0.1961` n `8`; equity avg `0.0026` n `140`; fx avg `-0.0085` n `6`; index avg `0.0001` n `26`; metal avg `-0.0021` n `20`; unknown avg `53.3611` n `922`
- 1h: commodity avg `0.0141` n `12`; crypto_alt avg `0.6021` n `234`; crypto_major avg `0.7207` n `8`; equity avg `-0.199` n `140`; fx avg `-0.0194` n `6`; index avg `-0.0596` n `26`; metal avg `-0.0668` n `20`; unknown avg `39.2633` n `852`
- 4h: commodity avg `0.1116` n `12`; crypto_alt avg `0.4122` n `234`; crypto_major avg `1.567` n `8`; equity avg `0.292` n `140`; fx avg `-0.006` n `6`; index avg `0.0322` n `26`; metal avg `-0.0295` n `20`; unknown avg `17.1297` n `852`
- 24h: commodity avg `-1.0366` n `12`; crypto_alt avg `3.9742` n `234`; crypto_major avg `6.1688` n `8`; equity avg `2.7836` n `140`; fx avg `-0.091` n `6`; index avg `0.5914` n `26`; metal avg `0.0388` n `20`; unknown avg `10.9581` n `727`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1874`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.17`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1381`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1328`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
