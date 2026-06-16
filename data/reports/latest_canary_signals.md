# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-16T00:22:30.978463+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0075` n `12`; crypto_alt avg `-0.0177` n `228`; crypto_major avg `-0.1055` n `8`; equity avg `-0.1526` n `77`; fx avg `-0.0056` n `6`; index avg `0.0276` n `23`; metal avg `-0.1723` n `18`; unknown avg `-0.297` n `687`
- 1h: commodity avg `-0.03` n `12`; crypto_alt avg `0.6121` n `228`; crypto_major avg `0.3026` n `8`; equity avg `-0.1431` n `77`; fx avg `-0.0098` n `6`; index avg `0.0835` n `23`; metal avg `-0.2373` n `18`; unknown avg `1.0255` n `687`
- 4h: commodity avg `-0.1116` n `12`; crypto_alt avg `-0.508` n `228`; crypto_major avg `-1.0316` n `8`; equity avg `-0.3536` n `77`; fx avg `0.0126` n `6`; index avg `-0.0516` n `23`; metal avg `-0.3123` n `18`; unknown avg `0.1781` n `679`
- 24h: commodity avg `0.7658` n `12`; crypto_alt avg `1.0307` n `228`; crypto_major avg `2.0008` n `8`; equity avg `1.1133` n `76`; fx avg `0.0547` n `6`; index avg `0.6451` n `23`; metal avg `-0.2906` n `18`; unknown avg `1.6293` n `519`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0574`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0571`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0535`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.044`, n `668`, weak_sample_signal
