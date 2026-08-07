# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T23:22:37.957605+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0419` n `12`; crypto_alt avg `0.0258` n `230`; crypto_major avg `-0.0222` n `8`; equity avg `0.0435` n `112`; fx avg `0.0012` n `6`; index avg `0.0086` n `25`; metal avg `-0.0132` n `20`; unknown avg `-0.0954` n `783`
- 1h: commodity avg `0.0648` n `12`; crypto_alt avg `0.0215` n `230`; crypto_major avg `-0.0289` n `8`; equity avg `0.0178` n `112`; fx avg `0.0083` n `6`; index avg `0.0027` n `25`; metal avg `0.0174` n `20`; unknown avg `-0.0143` n `782`
- 4h: commodity avg `-0.0178` n `12`; crypto_alt avg `-0.377` n `230`; crypto_major avg `-0.2095` n `8`; equity avg `0.1205` n `112`; fx avg `0.0322` n `6`; index avg `-0.0009` n `25`; metal avg `-0.0137` n `20`; unknown avg `-0.1467` n `782`
- 24h: commodity avg `-0.1538` n `12`; crypto_alt avg `-0.2454` n `230`; crypto_major avg `0.0581` n `8`; equity avg `1.6075` n `112`; fx avg `-0.1083` n `6`; index avg `0.0949` n `25`; metal avg `0.4533` n `20`; unknown avg `0.1002` n `766`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1563`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0636`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0588`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0582`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
