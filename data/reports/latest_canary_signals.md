# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T10:22:28.321374+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0021` n `12`; crypto_alt avg `0.2627` n `229`; crypto_major avg `0.1721` n `8`; equity avg `0.0307` n `88`; fx avg `0.0` n `6`; index avg `0.0048` n `25`; metal avg `0.0055` n `20`; unknown avg `-0.055` n `765`
- 1h: commodity avg `-0.0162` n `12`; crypto_alt avg `-0.4307` n `229`; crypto_major avg `-0.1383` n `8`; equity avg `-0.0218` n `88`; fx avg `0.0015` n `6`; index avg `-0.0119` n `25`; metal avg `0.001` n `20`; unknown avg `-0.0461` n `765`
- 4h: commodity avg `0.0208` n `12`; crypto_alt avg `0.0208` n `229`; crypto_major avg `0.0119` n `8`; equity avg `-0.0435` n `88`; fx avg `0.0119` n `6`; index avg `-0.02` n `25`; metal avg `0.0202` n `20`; unknown avg `-0.2626` n `765`
- 24h: commodity avg `-0.008` n `12`; crypto_alt avg `-0.621` n `229`; crypto_major avg `-0.7066` n `8`; equity avg `0.1207` n `88`; fx avg `0.0219` n `6`; index avg `0.0358` n `25`; metal avg `0.0731` n `20`; unknown avg `-1.2611` n `725`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
