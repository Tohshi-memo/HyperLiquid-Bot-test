# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T00:07:29.030402+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.007` n `13`; crypto_alt avg `-0.1673` n `239`; crypto_major avg `-0.3089` n `8`; equity avg `-0.0676` n `162`; fx avg `0.0101` n `6`; index avg `-0.0614` n `27`; metal avg `-0.0487` n `20`; unknown avg `1.2758` n `1254`
- 1h: commodity avg `-0.0093` n `13`; crypto_alt avg `-0.2267` n `239`; crypto_major avg `-0.573` n `8`; equity avg `-0.0909` n `162`; fx avg `0.0081` n `6`; index avg `-0.0345` n `27`; metal avg `0.0023` n `20`; unknown avg `162.9919` n `1258`
- 4h: commodity avg `-0.1065` n `13`; crypto_alt avg `-0.6399` n `239`; crypto_major avg `-0.4566` n `8`; equity avg `-0.6156` n `162`; fx avg `0.0059` n `6`; index avg `-0.0962` n `27`; metal avg `-0.0388` n `20`; unknown avg `3.3894` n `1188`
- 24h: commodity avg `-0.9639` n `13`; crypto_alt avg `-0.8504` n `239`; crypto_major avg `-0.648` n `8`; equity avg `-4.5051` n `162`; fx avg `-0.117` n `6`; index avg `-0.5452` n `27`; metal avg `-0.6687` n `20`; unknown avg `506.0288` n `995`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1474`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1233`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1211`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
