# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T00:23:05.583808+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0277` n `12`; crypto_alt avg `0.0784` n `232`; crypto_major avg `-0.1664` n `8`; equity avg `0.0395` n `134`; fx avg `-0.0487` n `6`; index avg `0.0127` n `26`; metal avg `0.0021` n `20`; unknown avg `-0.1176` n `794`
- 1h: commodity avg `-0.0359` n `12`; crypto_alt avg `0.3375` n `232`; crypto_major avg `-0.0306` n `8`; equity avg `0.1575` n `134`; fx avg `-0.0378` n `6`; index avg `0.0316` n `26`; metal avg `-0.0073` n `20`; unknown avg `142.4921` n `788`
- 4h: commodity avg `-0.0308` n `12`; crypto_alt avg `0.8645` n `232`; crypto_major avg `0.5375` n `8`; equity avg `0.0931` n `134`; fx avg `-0.0165` n `6`; index avg `-0.0027` n `26`; metal avg `-0.0792` n `20`; unknown avg `145.2448` n `777`
- 24h: commodity avg `-0.0254` n `12`; crypto_alt avg `1.5972` n `232`; crypto_major avg `0.8439` n `8`; equity avg `0.3793` n `134`; fx avg `-0.0001` n `6`; index avg `0.013` n `26`; metal avg `-0.0836` n `20`; unknown avg `151.0837` n `676`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1892`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
