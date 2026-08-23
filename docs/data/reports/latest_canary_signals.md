# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T16:47:00.454194+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0191` n `12`; crypto_alt avg `0.1407` n `231`; crypto_major avg `0.0063` n `8`; equity avg `0.0439` n `122`; fx avg `0.0016` n `6`; index avg `0.0079` n `25`; metal avg `-0.0031` n `20`; unknown avg `0.0699` n `793`
- 1h: commodity avg `-0.0038` n `12`; crypto_alt avg `-0.0412` n `231`; crypto_major avg `0.1236` n `8`; equity avg `0.0486` n `122`; fx avg `0.0013` n `6`; index avg `0.0076` n `25`; metal avg `0.0105` n `20`; unknown avg `0.078` n `793`
- 4h: commodity avg `-0.0206` n `12`; crypto_alt avg `1.7106` n `231`; crypto_major avg `0.4281` n `8`; equity avg `0.1802` n `122`; fx avg `0.0021` n `6`; index avg `0.0245` n `25`; metal avg `0.0384` n `20`; unknown avg `1.0962` n `793`
- 24h: commodity avg `0.0268` n `12`; crypto_alt avg `1.9647` n `231`; crypto_major avg `0.9237` n `8`; equity avg `0.6994` n `122`; fx avg `0.0353` n `6`; index avg `0.0728` n `25`; metal avg `0.0829` n `20`; unknown avg `7.8636` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
