# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T12:22:30.583034+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0298` n `12`; crypto_alt avg `-0.0011` n `230`; crypto_major avg `-0.1027` n `8`; equity avg `-0.0596` n `93`; fx avg `0.0081` n `6`; index avg `-0.0219` n `25`; metal avg `0.0172` n `20`; unknown avg `-0.0056` n `767`
- 1h: commodity avg `-0.0533` n `12`; crypto_alt avg `0.1205` n `230`; crypto_major avg `-0.0204` n `8`; equity avg `-0.1804` n `93`; fx avg `0.0149` n `6`; index avg `-0.0548` n `25`; metal avg `0.062` n `20`; unknown avg `0.0335` n `767`
- 4h: commodity avg `-0.1595` n `12`; crypto_alt avg `0.3788` n `230`; crypto_major avg `0.2785` n `8`; equity avg `-0.0253` n `93`; fx avg `-0.0093` n `6`; index avg `-0.05` n `25`; metal avg `-0.0437` n `20`; unknown avg `-0.0285` n `767`
- 24h: commodity avg `-0.1002` n `12`; crypto_alt avg `1.7133` n `230`; crypto_major avg `2.8666` n `8`; equity avg `1.2894` n `92`; fx avg `0.0227` n `6`; index avg `0.3003` n `25`; metal avg `0.3383` n `20`; unknown avg `0.2618` n `738`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `0.1647`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1389`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1297`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1267`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
