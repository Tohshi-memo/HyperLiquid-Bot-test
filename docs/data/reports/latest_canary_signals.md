# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T10:07:35.359798+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0258` n `13`; crypto_alt avg `0.1434` n `239`; crypto_major avg `0.1684` n `8`; equity avg `0.0764` n `166`; fx avg `-0.0148` n `6`; index avg `0.0067` n `27`; metal avg `0.0052` n `20`; unknown avg `0.5003` n `1256`
- 1h: commodity avg `-0.0672` n `13`; crypto_alt avg `-0.0837` n `239`; crypto_major avg `-0.2034` n `8`; equity avg `-0.0524` n `166`; fx avg `-0.0273` n `6`; index avg `-0.0223` n `27`; metal avg `0.002` n `20`; unknown avg `0.4773` n `1258`
- 4h: commodity avg `-0.3052` n `13`; crypto_alt avg `0.0472` n `239`; crypto_major avg `-0.1394` n `8`; equity avg `0.5671` n `166`; fx avg `-0.0547` n `6`; index avg `0.0258` n `27`; metal avg `-0.0775` n `20`; unknown avg `450.5366` n `1110`
- 24h: commodity avg `-0.7466` n `13`; crypto_alt avg `0.6996` n `239`; crypto_major avg `0.809` n `8`; equity avg `2.3229` n `166`; fx avg `0.2168` n `6`; index avg `0.1161` n `27`; metal avg `0.4015` n `20`; unknown avg `0.5649` n `1059`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1525`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1523`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1402`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1378`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1328`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1208`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
