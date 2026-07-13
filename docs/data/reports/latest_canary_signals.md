# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T09:52:28.078790+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0478` n `12`; crypto_alt avg `-0.0911` n `230`; crypto_major avg `-0.103` n `8`; equity avg `-0.0449` n `92`; fx avg `-0.0197` n `6`; index avg `-0.0335` n `25`; metal avg `-0.0118` n `20`; unknown avg `-0.0266` n `766`
- 1h: commodity avg `-0.0245` n `12`; crypto_alt avg `-0.1865` n `230`; crypto_major avg `-0.3192` n `8`; equity avg `0.0822` n `92`; fx avg `-0.0306` n `6`; index avg `-0.0224` n `25`; metal avg `-0.0425` n `20`; unknown avg `-0.0565` n `766`
- 4h: commodity avg `-0.4162` n `12`; crypto_alt avg `0.3184` n `230`; crypto_major avg `0.0964` n `8`; equity avg `0.2308` n `92`; fx avg `-0.1067` n `6`; index avg `0.0684` n `25`; metal avg `0.2685` n `20`; unknown avg `0.0763` n `750`
- 24h: commodity avg `-0.3409` n `12`; crypto_alt avg `-1.1855` n `230`; crypto_major avg `-1.1273` n `8`; equity avg `-1.9145` n `92`; fx avg `-0.0563` n `6`; index avg `-0.4153` n `25`; metal avg `-0.1782` n `20`; unknown avg `-0.0089` n `743`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1934`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1767`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1399`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1295`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
