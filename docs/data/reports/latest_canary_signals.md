# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T07:22:33.499763+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0448` n `12`; crypto_alt avg `-0.0272` n `232`; crypto_major avg `-0.0031` n `8`; equity avg `-0.0647` n `134`; fx avg `-0.0118` n `6`; index avg `-0.0246` n `26`; metal avg `-0.0217` n `20`; unknown avg `0.012` n `797`
- 1h: commodity avg `0.0933` n `12`; crypto_alt avg `-0.0084` n `232`; crypto_major avg `0.0962` n `8`; equity avg `0.2557` n `134`; fx avg `0.0106` n `6`; index avg `0.0168` n `26`; metal avg `0.0605` n `20`; unknown avg `0.3387` n `793`
- 4h: commodity avg `0.2772` n `12`; crypto_alt avg `-0.0122` n `232`; crypto_major avg `0.0236` n `8`; equity avg `-0.7022` n `134`; fx avg `0.1162` n `6`; index avg `-0.2219` n `26`; metal avg `-0.1521` n `20`; unknown avg `0.8677` n `747`
- 24h: commodity avg `0.3792` n `12`; crypto_alt avg `0.2871` n `232`; crypto_major avg `-1.1447` n `8`; equity avg `-0.2033` n `134`; fx avg `-0.1645` n `6`; index avg `-0.0761` n `26`; metal avg `0.1903` n `20`; unknown avg `7508.8791` n `666`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
