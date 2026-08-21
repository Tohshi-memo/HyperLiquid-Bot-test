# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T00:07:26.575036+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0076` n `12`; crypto_alt avg `0.1672` n `230`; crypto_major avg `0.0905` n `8`; equity avg `0.1417` n `121`; fx avg `-0.0213` n `6`; index avg `0.0596` n `25`; metal avg `-0.0498` n `20`; unknown avg `0.2096` n `793`
- 1h: commodity avg `0.0041` n `12`; crypto_alt avg `0.4133` n `230`; crypto_major avg `0.461` n `8`; equity avg `0.0603` n `121`; fx avg `-0.0438` n `6`; index avg `0.0021` n `25`; metal avg `-0.0382` n `20`; unknown avg `-0.0199` n `793`
- 4h: commodity avg `-0.033` n `12`; crypto_alt avg `1.2984` n `230`; crypto_major avg `0.9434` n `8`; equity avg `0.0517` n `121`; fx avg `-0.0348` n `6`; index avg `0.0228` n `25`; metal avg `-0.0053` n `20`; unknown avg `-0.2822` n `792`
- 24h: commodity avg `0.338` n `12`; crypto_alt avg `4.787` n `230`; crypto_major avg `5.4966` n `8`; equity avg `-0.7425` n `121`; fx avg `0.1519` n `6`; index avg `-0.0255` n `25`; metal avg `0.1405` n `20`; unknown avg `2.6357` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2186`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1868`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1848`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.182`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
