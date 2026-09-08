# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T03:07:31.912097+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0283` n `12`; crypto_alt avg `-0.1245` n `232`; crypto_major avg `-0.183` n `8`; equity avg `-0.013` n `134`; fx avg `0.0103` n `6`; index avg `-0.0021` n `26`; metal avg `0.0236` n `20`; unknown avg `-0.2151` n `795`
- 1h: commodity avg `0.0539` n `12`; crypto_alt avg `-0.8587` n `232`; crypto_major avg `-0.701` n `8`; equity avg `-0.0728` n `134`; fx avg `0.0105` n `6`; index avg `-0.0032` n `26`; metal avg `-0.1043` n `20`; unknown avg `0.2684` n `795`
- 4h: commodity avg `-0.0687` n `12`; crypto_alt avg `0.1961` n `232`; crypto_major avg `-0.4221` n `8`; equity avg `0.4858` n `134`; fx avg `-0.1638` n `6`; index avg `0.1323` n `26`; metal avg `0.1` n `20`; unknown avg `0.2777` n `783`
- 24h: commodity avg `0.1506` n `12`; crypto_alt avg `0.067` n `232`; crypto_major avg `-1.357` n `8`; equity avg `0.5764` n `134`; fx avg `-0.3372` n `6`; index avg `0.1914` n `26`; metal avg `0.2495` n `20`; unknown avg `7374.1093` n `678`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
