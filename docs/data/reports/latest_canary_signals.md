# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T22:37:23.587871+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0018` n `12`; crypto_alt avg `-0.4021` n `232`; crypto_major avg `-0.241` n `8`; equity avg `-0.0759` n `134`; fx avg `-0.0116` n `6`; index avg `-0.0199` n `26`; metal avg `-0.0228` n `20`; unknown avg `0.3752` n `797`
- 1h: commodity avg `0.0499` n `12`; crypto_alt avg `-0.7278` n `232`; crypto_major avg `-0.3915` n `8`; equity avg `-0.1947` n `134`; fx avg `-0.0088` n `6`; index avg `-0.041` n `26`; metal avg `-0.0162` n `20`; unknown avg `16.2055` n `794`
- 4h: commodity avg `0.0169` n `12`; crypto_alt avg `-0.1031` n `232`; crypto_major avg `-0.1345` n `8`; equity avg `-0.0555` n `134`; fx avg `-0.0084` n `6`; index avg `-0.0216` n `26`; metal avg `0.0127` n `20`; unknown avg `7.923` n `752`
- 24h: commodity avg `0.1853` n `12`; crypto_alt avg `-0.4878` n `232`; crypto_major avg `-1.5012` n `8`; equity avg `0.3704` n `134`; fx avg `-0.1618` n `6`; index avg `0.0457` n `26`; metal avg `0.0591` n `20`; unknown avg `7801.7859` n `641`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1272`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
