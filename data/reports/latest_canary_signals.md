# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T20:37:25.383316+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.89` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0286` n `12`; crypto_alt avg `0.0674` n `233`; crypto_major avg `0.0258` n `8`; equity avg `-0.0106` n `136`; fx avg `0.0011` n `6`; index avg `-0.0021` n `26`; metal avg `-0.0009` n `20`; unknown avg `0.1047` n `804`
- 1h: commodity avg `-0.0528` n `12`; crypto_alt avg `0.3491` n `233`; crypto_major avg `0.2848` n `8`; equity avg `-0.0314` n `136`; fx avg `-0.0119` n `6`; index avg `-0.0297` n `26`; metal avg `0.009` n `20`; unknown avg `-0.1998` n `790`
- 4h: commodity avg `0.0065` n `12`; crypto_alt avg `-0.6607` n `233`; crypto_major avg `-0.3936` n `8`; equity avg `-0.1949` n `136`; fx avg `0.0029` n `6`; index avg `-0.0187` n `26`; metal avg `-0.0273` n `20`; unknown avg `-0.1533` n `726`
- 24h: commodity avg `-0.6607` n `12`; crypto_alt avg `0.3777` n `233`; crypto_major avg `1.1322` n `8`; equity avg `0.6445` n `136`; fx avg `-0.1686` n `6`; index avg `0.2959` n `26`; metal avg `0.2841` n `20`; unknown avg `1.3416` n `670`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0596`, n `668`, weak_sample_signal
