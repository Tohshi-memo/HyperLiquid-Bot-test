# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T07:52:30.265254+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0509` n `12`; crypto_alt avg `-0.0569` n `231`; crypto_major avg `0.0009` n `8`; equity avg `-0.1842` n `122`; fx avg `-0.0219` n `6`; index avg `-0.0346` n `25`; metal avg `-0.0891` n `20`; unknown avg `-0.0025` n `793`
- 1h: commodity avg `0.1468` n `12`; crypto_alt avg `-0.0625` n `231`; crypto_major avg `-0.1876` n `8`; equity avg `-0.065` n `122`; fx avg `0.0206` n `6`; index avg `0.0092` n `25`; metal avg `-0.1221` n `20`; unknown avg `-0.0532` n `793`
- 4h: commodity avg `0.0723` n `12`; crypto_alt avg `0.2528` n `231`; crypto_major avg `0.2551` n `8`; equity avg `-0.2795` n `122`; fx avg `0.0253` n `6`; index avg `-0.0466` n `25`; metal avg `-0.0281` n `20`; unknown avg `-0.0841` n `777`
- 24h: commodity avg `-0.2192` n `12`; crypto_alt avg `3.0468` n `231`; crypto_major avg `1.3571` n `8`; equity avg `-1.3105` n `122`; fx avg `-0.1796` n `6`; index avg `-0.1238` n `25`; metal avg `0.1224` n `20`; unknown avg `5.2306` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1179`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0656`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0625`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0549`, n `668`, weak_sample_signal
