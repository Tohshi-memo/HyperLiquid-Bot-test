# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T21:52:26.705784+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0017` n `12`; crypto_alt avg `0.0763` n `231`; crypto_major avg `0.2348` n `8`; equity avg `-0.0152` n `122`; fx avg `0.0073` n `6`; index avg `-0.0016` n `25`; metal avg `0.0123` n `20`; unknown avg `-0.0547` n `793`
- 1h: commodity avg `-0.0493` n `12`; crypto_alt avg `0.7195` n `231`; crypto_major avg `0.8542` n `8`; equity avg `0.03` n `122`; fx avg `-0.0207` n `6`; index avg `0.0035` n `25`; metal avg `-0.0081` n `20`; unknown avg `0.9671` n `793`
- 4h: commodity avg `-0.0676` n `12`; crypto_alt avg `0.8378` n `231`; crypto_major avg `1.0267` n `8`; equity avg `0.2098` n `122`; fx avg `-0.1071` n `6`; index avg `0.0487` n `25`; metal avg `0.0444` n `20`; unknown avg `2.5767` n `793`
- 24h: commodity avg `-0.1533` n `12`; crypto_alt avg `4.9641` n `231`; crypto_major avg `2.4952` n `8`; equity avg `0.7977` n `122`; fx avg `-0.0911` n `6`; index avg `0.1319` n `25`; metal avg `0.0953` n `20`; unknown avg `7.8177` n `776`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
