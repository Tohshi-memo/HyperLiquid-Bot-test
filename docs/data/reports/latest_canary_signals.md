# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T11:07:35.230034+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.47` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0356` n `13`; crypto_alt avg `-0.1217` n `238`; crypto_major avg `-0.2217` n `8`; equity avg `-0.1252` n `154`; fx avg `0.0105` n `6`; index avg `-0.0233` n `27`; metal avg `-0.0048` n `20`; unknown avg `2.7238` n `1233`
- 1h: commodity avg `0.1021` n `13`; crypto_alt avg `-0.1464` n `238`; crypto_major avg `-0.1293` n `8`; equity avg `0.3213` n `154`; fx avg `-0.0072` n `6`; index avg `0.0354` n `27`; metal avg `-0.0156` n `20`; unknown avg `2.4809` n `1233`
- 4h: commodity avg `0.0129` n `13`; crypto_alt avg `0.5666` n `238`; crypto_major avg `0.6273` n `8`; equity avg `0.2112` n `154`; fx avg `0.0072` n `6`; index avg `0.0089` n `27`; metal avg `-0.0005` n `20`; unknown avg `80.6211` n `1186`
- 24h: commodity avg `0.2849` n `13`; crypto_alt avg `1.9685` n `238`; crypto_major avg `2.3027` n `8`; equity avg `3.0159` n `154`; fx avg `0.0975` n `6`; index avg `0.3691` n `27`; metal avg `0.2122` n `20`; unknown avg `7.7523` n `1046`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1718`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1461`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1448`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.063`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0602`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0585`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0585`, n `668`, weak_sample_signal
