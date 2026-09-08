# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T05:52:27.789965+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.08` n `12`; crypto_alt avg `-0.0607` n `232`; crypto_major avg `-0.0754` n `8`; equity avg `-0.1851` n `134`; fx avg `0.0019` n `6`; index avg `-0.0494` n `26`; metal avg `-0.01` n `20`; unknown avg `2.5339` n `797`
- 1h: commodity avg `0.1024` n `12`; crypto_alt avg `0.0568` n `232`; crypto_major avg `-0.0691` n `8`; equity avg `-0.5755` n `134`; fx avg `0.0166` n `6`; index avg `-0.1395` n `26`; metal avg `-0.1177` n `20`; unknown avg `2.8983` n `795`
- 4h: commodity avg `0.2606` n `12`; crypto_alt avg `-0.5149` n `232`; crypto_major avg `-0.6789` n `8`; equity avg `-0.4207` n `134`; fx avg `0.0403` n `6`; index avg `-0.1313` n `26`; metal avg `-0.1437` n `20`; unknown avg `0.0889` n `767`
- 24h: commodity avg `0.1786` n `12`; crypto_alt avg `0.4875` n `232`; crypto_major avg `-1.2192` n `8`; equity avg `0.0535` n `134`; fx avg `-0.2314` n `6`; index avg `0.0218` n `26`; metal avg `0.2708` n `20`; unknown avg `7462.6868` n `670`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0836`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
