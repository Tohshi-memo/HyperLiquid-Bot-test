# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T19:18:13.479057+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.025` n `12`; crypto_alt avg `0.1077` n `232`; crypto_major avg `0.0697` n `8`; equity avg `-0.0059` n `134`; fx avg `-0.008` n `6`; index avg `-0.0059` n `26`; metal avg `-0.0031` n `20`; unknown avg `0.586` n `796`
- 1h: commodity avg `-0.0448` n `12`; crypto_alt avg `0.0605` n `232`; crypto_major avg `-0.022` n `8`; equity avg `-0.0241` n `134`; fx avg `-0.0057` n `6`; index avg `0.0102` n `26`; metal avg `0.0319` n `20`; unknown avg `-0.0222` n `794`
- 4h: commodity avg `-0.0704` n `12`; crypto_alt avg `-0.3729` n `232`; crypto_major avg `-0.2232` n `8`; equity avg `0.1457` n `134`; fx avg `-0.0192` n `6`; index avg `0.0675` n `26`; metal avg `0.004` n `20`; unknown avg `-0.8845` n `768`
- 24h: commodity avg `0.1399` n `12`; crypto_alt avg `0.2841` n `232`; crypto_major avg `-0.8288` n `8`; equity avg `0.3916` n `134`; fx avg `-0.129` n `6`; index avg `0.0842` n `26`; metal avg `-0.0038` n `20`; unknown avg `0.6861` n `661`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
