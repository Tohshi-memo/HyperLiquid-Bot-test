# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T06:22:22.745500+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0138` n `12`; crypto_alt avg `0.3053` n `231`; crypto_major avg `0.2782` n `8`; equity avg `0.0267` n `122`; fx avg `0.0182` n `6`; index avg `0.0039` n `25`; metal avg `0.0264` n `20`; unknown avg `0.0247` n `793`
- 1h: commodity avg `-0.0426` n `12`; crypto_alt avg `-0.0239` n `231`; crypto_major avg `0.0554` n `8`; equity avg `-0.2441` n `122`; fx avg `0.0179` n `6`; index avg `-0.0655` n `25`; metal avg `0.0973` n `20`; unknown avg `-0.0051` n `777`
- 4h: commodity avg `0.0155` n `12`; crypto_alt avg `0.1114` n `231`; crypto_major avg `-0.3426` n `8`; equity avg `-0.9077` n `122`; fx avg `0.0225` n `6`; index avg `-0.1465` n `25`; metal avg `-0.0043` n `20`; unknown avg `-0.1038` n `777`
- 24h: commodity avg `-0.3412` n `12`; crypto_alt avg `4.2433` n `231`; crypto_major avg `1.6985` n `8`; equity avg `-1.1931` n `122`; fx avg `-0.1998` n `6`; index avg `-0.1251` n `25`; metal avg `0.2223` n `20`; unknown avg `5.565` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0695`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
