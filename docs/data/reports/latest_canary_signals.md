# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T07:52:24.866476+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0791` n `13`; crypto_alt avg `-0.2336` n `239`; crypto_major avg `-0.3293` n `8`; equity avg `0.0406` n `162`; fx avg `0.0112` n `6`; index avg `0.0063` n `27`; metal avg `0.0381` n `20`; unknown avg `3.394` n `1262`
- 1h: commodity avg `-0.1433` n `13`; crypto_alt avg `0.5776` n `239`; crypto_major avg `0.1436` n `8`; equity avg `0.3252` n `162`; fx avg `0.0344` n `6`; index avg `0.0368` n `27`; metal avg `0.0123` n `20`; unknown avg `4.5476` n `1260`
- 4h: commodity avg `-0.055` n `13`; crypto_alt avg `2.2078` n `239`; crypto_major avg `0.8309` n `8`; equity avg `-0.0622` n `162`; fx avg `0.0578` n `6`; index avg `-0.0027` n `27`; metal avg `-0.2118` n `20`; unknown avg `0.6437` n `1218`
- 24h: commodity avg `0.4947` n `13`; crypto_alt avg `-0.7552` n `239`; crypto_major avg `-3.3819` n `8`; equity avg `-0.8601` n `162`; fx avg `-0.0188` n `6`; index avg `0.0676` n `27`; metal avg `-0.5278` n `20`; unknown avg `98.9556` n `1133`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.126`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
