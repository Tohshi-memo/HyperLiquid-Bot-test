# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T20:07:32.940186+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0027` n `12`; crypto_alt avg `-0.2532` n `231`; crypto_major avg `-0.1988` n `8`; equity avg `-0.0186` n `122`; fx avg `0.0185` n `6`; index avg `-0.0042` n `25`; metal avg `-0.0052` n `20`; unknown avg `1.5539` n `793`
- 1h: commodity avg `0.0003` n `12`; crypto_alt avg `-0.1883` n `231`; crypto_major avg `-0.156` n `8`; equity avg `0.0227` n `122`; fx avg `-0.0356` n `6`; index avg `0.0031` n `25`; metal avg `-0.0107` n `20`; unknown avg `0.5245` n `793`
- 4h: commodity avg `-0.0419` n `12`; crypto_alt avg `0.324` n `231`; crypto_major avg `0.1825` n `8`; equity avg `0.2681` n `122`; fx avg `-0.0374` n `6`; index avg `0.0602` n `25`; metal avg `0.0072` n `20`; unknown avg `0.9477` n `793`
- 24h: commodity avg `-0.0355` n `12`; crypto_alt avg `1.8717` n `231`; crypto_major avg `-0.0593` n `8`; equity avg `0.7685` n `122`; fx avg `-0.0241` n `6`; index avg `0.1307` n `25`; metal avg `0.08` n `20`; unknown avg `5.5024` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1085`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
