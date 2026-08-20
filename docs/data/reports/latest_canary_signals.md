# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T22:52:43.077039+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0035` n `12`; crypto_alt avg `0.0981` n `230`; crypto_major avg `0.1189` n `8`; equity avg `0.0397` n `121`; fx avg `-0.0185` n `6`; index avg `0.0266` n `25`; metal avg `0.0362` n `20`; unknown avg `-0.0169` n `793`
- 1h: commodity avg `0.006` n `12`; crypto_alt avg `0.1344` n `230`; crypto_major avg `-0.2521` n `8`; equity avg `0.023` n `121`; fx avg `-0.0213` n `6`; index avg `0.0214` n `25`; metal avg `0.0692` n `20`; unknown avg `0.0103` n `793`
- 4h: commodity avg `-0.0801` n `12`; crypto_alt avg `0.8679` n `230`; crypto_major avg `0.4188` n `8`; equity avg `0.5516` n `121`; fx avg `-0.0382` n `6`; index avg `0.0612` n `25`; metal avg `0.1041` n `20`; unknown avg `-0.2638` n `792`
- 24h: commodity avg `0.3909` n `12`; crypto_alt avg `4.6756` n `230`; crypto_major avg `5.2034` n `8`; equity avg `-1.0615` n `121`; fx avg `0.1699` n `6`; index avg `-0.1301` n `25`; metal avg `0.1541` n `20`; unknown avg `2.7051` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2195`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1867`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1834`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1796`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1155`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
