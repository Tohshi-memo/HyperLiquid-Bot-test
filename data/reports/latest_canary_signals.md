# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T13:07:24.904907+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0198` n `13`; crypto_alt avg `-0.0174` n `235`; crypto_major avg `0.0088` n `8`; equity avg `0.0052` n `144`; fx avg `-0.0067` n `6`; index avg `-0.0044` n `26`; metal avg `-0.0012` n `20`; unknown avg `0.0334` n `1076`
- 1h: commodity avg `0.0049` n `13`; crypto_alt avg `-0.0392` n `235`; crypto_major avg `-0.1517` n `8`; equity avg `-0.0093` n `144`; fx avg `-0.0048` n `6`; index avg `-0.0074` n `26`; metal avg `-0.0065` n `20`; unknown avg `0.1376` n `1076`
- 4h: commodity avg `0.0238` n `13`; crypto_alt avg `-0.2189` n `235`; crypto_major avg `0.1095` n `8`; equity avg `0.0414` n `144`; fx avg `0.0237` n `6`; index avg `0.0041` n `26`; metal avg `-0.0144` n `20`; unknown avg `0.0129` n `1070`
- 24h: commodity avg `0.1906` n `13`; crypto_alt avg `1.6196` n `235`; crypto_major avg `1.044` n `8`; equity avg `0.2598` n `144`; fx avg `0.0031` n `6`; index avg `0.0303` n `26`; metal avg `-0.0038` n `20`; unknown avg `-0.1827` n `901`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2057`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1791`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.151`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1504`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1421`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
