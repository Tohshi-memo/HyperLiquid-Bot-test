# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T16:22:30.228456+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0414` n `12`; crypto_alt avg `-0.2984` n `230`; crypto_major avg `-0.2915` n `8`; equity avg `-0.2296` n `92`; fx avg `0.0003` n `6`; index avg `-0.0369` n `25`; metal avg `-0.0103` n `20`; unknown avg `-0.0214` n `766`
- 1h: commodity avg `0.1027` n `12`; crypto_alt avg `-0.6793` n `230`; crypto_major avg `-0.7763` n `8`; equity avg `-0.7766` n `92`; fx avg `-0.0042` n `6`; index avg `-0.1407` n `25`; metal avg `-0.0743` n `20`; unknown avg `0.0091` n `766`
- 4h: commodity avg `0.1939` n `12`; crypto_alt avg `-0.3791` n `230`; crypto_major avg `-0.6723` n `8`; equity avg `-0.6173` n `92`; fx avg `-0.0528` n `6`; index avg `-0.0567` n `25`; metal avg `-0.1785` n `20`; unknown avg `-0.1052` n `766`
- 24h: commodity avg `0.1815` n `12`; crypto_alt avg `-1.8211` n `230`; crypto_major avg `-2.7966` n `8`; equity avg `-2.6682` n `92`; fx avg `-0.0836` n `6`; index avg `-0.5705` n `25`; metal avg `-0.4064` n `20`; unknown avg `-0.2291` n `743`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2052`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1897`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1443`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1328`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1246`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
