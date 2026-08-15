# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T08:11:39.796611+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0007` n `12`; crypto_alt avg `0.034` n `230`; crypto_major avg `-0.0305` n `8`; equity avg `-0.0097` n `114`; fx avg `0.0076` n `6`; index avg `-0.0079` n `25`; metal avg `0.0083` n `20`; unknown avg `1.2754` n `791`
- 1h: commodity avg `-0.1416` n `12`; crypto_alt avg `-0.0689` n `230`; crypto_major avg `-0.1368` n `8`; equity avg `0.0067` n `114`; fx avg `0.0048` n `6`; index avg `-0.0019` n `25`; metal avg `0.0022` n `20`; unknown avg `1.3228` n `791`
- 4h: commodity avg `-0.1664` n `12`; crypto_alt avg `0.2095` n `230`; crypto_major avg `-0.1646` n `8`; equity avg `-0.07` n `114`; fx avg `0.0014` n `6`; index avg `-0.0258` n `25`; metal avg `0.0094` n `20`; unknown avg `1.2657` n `759`
- 24h: commodity avg `-0.2915` n `12`; crypto_alt avg `1.0879` n `230`; crypto_major avg `0.0582` n `8`; equity avg `-0.3933` n `114`; fx avg `0.1483` n `6`; index avg `-0.1015` n `25`; metal avg `0.2761` n `20`; unknown avg `1.2338` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2158`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1899`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1767`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1746`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1567`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.155`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1471`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1434`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1419`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.137`, n `668`, weak_sample_signal
