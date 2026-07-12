# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T16:52:33.919436+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0405` n `12`; crypto_alt avg `0.0417` n `230`; crypto_major avg `0.0826` n `8`; equity avg `0.0129` n `92`; fx avg `-0.0006` n `6`; index avg `0.0044` n `25`; metal avg `0.0033` n `20`; unknown avg `-0.0874` n `765`
- 1h: commodity avg `0.0912` n `12`; crypto_alt avg `-0.1095` n `230`; crypto_major avg `0.0054` n `8`; equity avg `-0.0247` n `92`; fx avg `0.0001` n `6`; index avg `0.0068` n `25`; metal avg `-0.0108` n `20`; unknown avg `-0.0994` n `759`
- 4h: commodity avg `0.127` n `12`; crypto_alt avg `0.1362` n `230`; crypto_major avg `0.5373` n `8`; equity avg `0.0072` n `92`; fx avg `0.0042` n `6`; index avg `0.0531` n `25`; metal avg `-0.0195` n `20`; unknown avg `-0.0859` n `759`
- 24h: commodity avg `0.6039` n `12`; crypto_alt avg `-1.0709` n `230`; crypto_major avg `-0.1674` n `8`; equity avg `-0.052` n `92`; fx avg `0.0454` n `6`; index avg `-0.0749` n `25`; metal avg `-0.103` n `20`; unknown avg `0.3907` n `741`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1802`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1639`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.135`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.133`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1224`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
