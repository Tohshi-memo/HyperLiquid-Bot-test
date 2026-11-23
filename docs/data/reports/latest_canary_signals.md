# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T13:07:34.129756+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0857` n `13`; crypto_alt avg `0.0542` n `239`; crypto_major avg `0.1691` n `8`; equity avg `0.5122` n `166`; fx avg `0.0102` n `6`; index avg `0.0799` n `27`; metal avg `0.0981` n `20`; unknown avg `170.0742` n `1256`
- 1h: commodity avg `-0.0353` n `13`; crypto_alt avg `-0.3595` n `239`; crypto_major avg `-0.103` n `8`; equity avg `-0.152` n `166`; fx avg `-0.0303` n `6`; index avg `-0.0309` n `27`; metal avg `-0.0893` n `20`; unknown avg `255.0279` n `1256`
- 4h: commodity avg `-0.3464` n `13`; crypto_alt avg `-0.2908` n `239`; crypto_major avg `-0.123` n `8`; equity avg `-0.5392` n `166`; fx avg `-0.0911` n `6`; index avg `-0.0552` n `27`; metal avg `-0.0863` n `20`; unknown avg `10.4014` n `1246`
- 24h: commodity avg `-0.9961` n `13`; crypto_alt avg `0.5451` n `239`; crypto_major avg `1.3243` n `8`; equity avg `1.7105` n `166`; fx avg `0.1405` n `6`; index avg `0.0674` n `27`; metal avg `0.3161` n `20`; unknown avg `2.607` n `1059`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1542`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1524`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1402`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1397`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1387`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1303`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1273`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1251`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
