# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T23:07:30.636357+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2909` n `13`; crypto_alt avg `0.1632` n `239`; crypto_major avg `0.2719` n `8`; equity avg `0.5657` n `162`; fx avg `-0.0076` n `6`; index avg `0.1324` n `27`; metal avg `0.2621` n `20`; unknown avg `0.1298` n `1257`
- 1h: commodity avg `-0.3097` n `13`; crypto_alt avg `0.347` n `239`; crypto_major avg `0.4298` n `8`; equity avg `0.6289` n `162`; fx avg `-0.0002` n `6`; index avg `0.1424` n `27`; metal avg `0.2964` n `20`; unknown avg `0.498` n `1219`
- 4h: commodity avg `-0.3533` n `13`; crypto_alt avg `0.8123` n `239`; crypto_major avg `1.165` n `8`; equity avg `1.0143` n `162`; fx avg `0.0142` n `6`; index avg `0.1753` n `27`; metal avg `0.3509` n `20`; unknown avg `1.2984` n `1185`
- 24h: commodity avg `-0.3519` n `13`; crypto_alt avg `4.0064` n `239`; crypto_major avg `5.0258` n `8`; equity avg `2.0795` n `162`; fx avg `0.0051` n `6`; index avg `0.2569` n `27`; metal avg `0.5263` n `20`; unknown avg `3.2977` n `1138`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.137`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1293`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.064`, n `668`, weak_sample_signal
