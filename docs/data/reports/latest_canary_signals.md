# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T23:15:19.773200+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0334` n `12`; crypto_alt avg `0.0818` n `230`; crypto_major avg `0.0318` n `8`; equity avg `0.0351` n `112`; fx avg `0.0012` n `6`; index avg `0.006` n `25`; metal avg `-0.0102` n `20`; unknown avg `0.0215` n `783`
- 1h: commodity avg `0.0563` n `12`; crypto_alt avg `0.0777` n `230`; crypto_major avg `0.0251` n `8`; equity avg `0.0094` n `112`; fx avg `0.0083` n `6`; index avg `0.0001` n `25`; metal avg `0.0204` n `20`; unknown avg `0.0815` n `782`
- 4h: commodity avg `-0.0262` n `12`; crypto_alt avg `-0.3214` n `230`; crypto_major avg `-0.1556` n `8`; equity avg `0.1121` n `112`; fx avg `0.0322` n `6`; index avg `-0.0035` n `25`; metal avg `-0.0107` n `20`; unknown avg `-0.0835` n `782`
- 24h: commodity avg `-0.1621` n `12`; crypto_alt avg `-0.1885` n `230`; crypto_major avg `0.1119` n `8`; equity avg `1.5982` n `112`; fx avg `-0.1083` n `6`; index avg `0.0924` n `25`; metal avg `0.4564` n `20`; unknown avg `0.1275` n `766`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1563`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0636`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.059`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0582`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
