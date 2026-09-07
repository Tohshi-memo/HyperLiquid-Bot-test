# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T02:37:24.159341+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.002` n `12`; crypto_alt avg `0.3979` n `232`; crypto_major avg `0.3919` n `8`; equity avg `0.1413` n `134`; fx avg `-0.0083` n `6`; index avg `0.0063` n `26`; metal avg `0.0664` n `20`; unknown avg `0.7336` n `794`
- 1h: commodity avg `0.0284` n `12`; crypto_alt avg `0.2489` n `232`; crypto_major avg `0.4243` n `8`; equity avg `0.2444` n `134`; fx avg `0.0514` n `6`; index avg `0.0086` n `26`; metal avg `0.0274` n `20`; unknown avg `2.8879` n `792`
- 4h: commodity avg `-0.019` n `12`; crypto_alt avg `-0.0599` n `232`; crypto_major avg `0.1179` n `8`; equity avg `0.2889` n `134`; fx avg `-0.0311` n `6`; index avg `0.015` n `26`; metal avg `0.0041` n `20`; unknown avg `2.6682` n `783`
- 24h: commodity avg `-0.0192` n `12`; crypto_alt avg `0.3467` n `232`; crypto_major avg `0.3771` n `8`; equity avg `0.454` n `134`; fx avg `0.0033` n `6`; index avg `0.0423` n `26`; metal avg `-0.0598` n `20`; unknown avg `151.0545` n `678`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1964`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
