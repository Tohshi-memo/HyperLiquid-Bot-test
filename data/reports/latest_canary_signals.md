# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T03:22:27.154769+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0096` n `12`; crypto_alt avg `-0.1562` n `233`; crypto_major avg `-0.2085` n `8`; equity avg `-0.0114` n `134`; fx avg `0.0042` n `6`; index avg `-0.0069` n `26`; metal avg `0.0021` n `20`; unknown avg `0.537` n `797`
- 1h: commodity avg `0.0262` n `12`; crypto_alt avg `-0.2633` n `233`; crypto_major avg `-0.2847` n `8`; equity avg `-0.0271` n `134`; fx avg `-0.0293` n `6`; index avg `-0.0101` n `26`; metal avg `0.0535` n `20`; unknown avg `0.1027` n `791`
- 4h: commodity avg `0.0146` n `12`; crypto_alt avg `-0.5583` n `233`; crypto_major avg `-0.1548` n `8`; equity avg `0.3819` n `134`; fx avg `-0.0059` n `6`; index avg `0.0778` n `26`; metal avg `0.1648` n `20`; unknown avg `0.2825` n `785`
- 24h: commodity avg `0.1322` n `12`; crypto_alt avg `-0.7115` n `232`; crypto_major avg `0.5503` n `8`; equity avg `0.3312` n `134`; fx avg `0.0269` n `6`; index avg `-0.1927` n `26`; metal avg `-0.3529` n `20`; unknown avg `0.9612` n `681`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1515`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
