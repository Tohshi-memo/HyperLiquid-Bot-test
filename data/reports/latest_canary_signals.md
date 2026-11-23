# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T10:37:39.735377+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.057` n `13`; crypto_alt avg `-0.011` n `239`; crypto_major avg `0.1508` n `8`; equity avg `-0.2001` n `166`; fx avg `-0.0027` n `6`; index avg `-0.0072` n `27`; metal avg `-0.0383` n `20`; unknown avg `0.2556` n `1266`
- 1h: commodity avg `-0.0422` n `13`; crypto_alt avg `-0.0682` n `239`; crypto_major avg `-0.0777` n `8`; equity avg `-0.1659` n `166`; fx avg `-0.0234` n `6`; index avg `0.0083` n `27`; metal avg `-0.0621` n `20`; unknown avg `0.2184` n `1262`
- 4h: commodity avg `-0.2734` n `13`; crypto_alt avg `0.1087` n `239`; crypto_major avg `0.3072` n `8`; equity avg `0.8214` n `166`; fx avg `-0.0628` n `6`; index avg `0.0879` n `27`; metal avg `-0.0175` n `20`; unknown avg `254.6345` n `1108`
- 24h: commodity avg `-0.793` n `13`; crypto_alt avg `0.7466` n `239`; crypto_major avg `1.1505` n `8`; equity avg `2.1586` n `166`; fx avg `0.1933` n `6`; index avg `0.1276` n `27`; metal avg `0.3718` n `20`; unknown avg `0.3262` n `1061`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.152`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1516`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1402`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1368`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1338`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1254`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1246`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
