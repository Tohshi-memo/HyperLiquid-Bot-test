# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T07:37:28.960947+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0169` n `12`; crypto_alt avg `-0.0778` n `232`; crypto_major avg `-0.2281` n `8`; equity avg `-0.0369` n `134`; fx avg `0.0402` n `6`; index avg `0.0074` n `26`; metal avg `-0.0077` n `20`; unknown avg `-0.0187` n `794`
- 1h: commodity avg `-0.0299` n `12`; crypto_alt avg `-0.3294` n `232`; crypto_major avg `-0.3899` n `8`; equity avg `-0.0688` n `134`; fx avg `0.0329` n `6`; index avg `0.0068` n `26`; metal avg `-0.0125` n `20`; unknown avg `-0.0599` n `790`
- 4h: commodity avg `-0.0003` n `12`; crypto_alt avg `-0.669` n `232`; crypto_major avg `-0.5793` n `8`; equity avg `-0.007` n `134`; fx avg `0.0322` n `6`; index avg `0.0212` n `26`; metal avg `-0.017` n `20`; unknown avg `457.9609` n `728`
- 24h: commodity avg `0.134` n `12`; crypto_alt avg `1.3727` n `232`; crypto_major avg `1.8184` n `8`; equity avg `0.3863` n `134`; fx avg `-0.0009` n `6`; index avg `0.0769` n `26`; metal avg `-0.0114` n `20`; unknown avg `493.3379` n `676`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1563`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1497`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
