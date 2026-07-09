# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T02:07:28.435576+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0108` n `12`; crypto_alt avg `0.1526` n `229`; crypto_major avg `0.1615` n `8`; equity avg `-0.2067` n `91`; fx avg `-0.0106` n `6`; index avg `-0.0599` n `25`; metal avg `0.0551` n `20`; unknown avg `0.0699` n `764`
- 1h: commodity avg `0.0049` n `12`; crypto_alt avg `0.112` n `229`; crypto_major avg `-0.2817` n `8`; equity avg `-0.1831` n `91`; fx avg `0.0383` n `6`; index avg `-0.1226` n `25`; metal avg `0.1303` n `20`; unknown avg `-0.0618` n `764`
- 4h: commodity avg `-0.0906` n `12`; crypto_alt avg `0.1509` n `229`; crypto_major avg `-0.0776` n `8`; equity avg `0.3286` n `91`; fx avg `0.0006` n `6`; index avg `-0.0514` n `25`; metal avg `0.0454` n `20`; unknown avg `-0.1231` n `764`
- 24h: commodity avg `0.3119` n `12`; crypto_alt avg `-0.1691` n `229`; crypto_major avg `-0.882` n `8`; equity avg `1.1929` n `91`; fx avg `0.0389` n `6`; index avg `-0.0694` n `25`; metal avg `-0.7556` n `20`; unknown avg `0.0674` n `739`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0644`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0612`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0535`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0529`, n `668`, weak_sample_signal
