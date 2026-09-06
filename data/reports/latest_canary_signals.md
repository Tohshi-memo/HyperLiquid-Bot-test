# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T21:22:24.836818+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0015` n `12`; crypto_alt avg `0.2526` n `232`; crypto_major avg `0.1312` n `8`; equity avg `-0.0134` n `134`; fx avg `-0.0027` n `6`; index avg `0.004` n `26`; metal avg `0.0152` n `20`; unknown avg `1.5691` n `793`
- 1h: commodity avg `-0.0018` n `12`; crypto_alt avg `0.4074` n `232`; crypto_major avg `0.4735` n `8`; equity avg `-0.0141` n `134`; fx avg `0.0211` n `6`; index avg `0.006` n `26`; metal avg `0.0032` n `20`; unknown avg `148.7737` n `781`
- 4h: commodity avg `-0.0523` n `12`; crypto_alt avg `0.7574` n `232`; crypto_major avg `0.5582` n `8`; equity avg `0.1681` n `134`; fx avg `0.0309` n `6`; index avg `0.028` n `26`; metal avg `0.0372` n `20`; unknown avg `1.7288` n `755`
- 24h: commodity avg `0.0077` n `12`; crypto_alt avg `1.4611` n `232`; crypto_major avg `0.4896` n `8`; equity avg `0.3527` n `134`; fx avg `0.0176` n `6`; index avg `0.0266` n `26`; metal avg `-0.0113` n `20`; unknown avg `106.2963` n `678`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1748`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1272`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
