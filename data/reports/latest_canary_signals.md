# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T13:22:26.403353+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0191` n `13`; crypto_alt avg `0.0547` n `239`; crypto_major avg `0.0978` n `8`; equity avg `0.1075` n `166`; fx avg `-0.0031` n `6`; index avg `0.0204` n `27`; metal avg `0.0554` n `20`; unknown avg `-0.0432` n `1264`
- 1h: commodity avg `-0.1267` n `13`; crypto_alt avg `-0.1947` n `239`; crypto_major avg `0.1663` n `8`; equity avg `0.3826` n `166`; fx avg `-0.0253` n `6`; index avg `0.042` n `27`; metal avg `0.0488` n `20`; unknown avg `207.5249` n `1258`
- 4h: commodity avg `-0.2327` n `13`; crypto_alt avg `-0.4405` n `239`; crypto_major avg `-0.2443` n `8`; equity avg `-0.7328` n `166`; fx avg `-0.0817` n `6`; index avg `-0.0585` n `27`; metal avg `-0.0995` n `20`; unknown avg `0.06` n `1250`
- 24h: commodity avg `-1.0116` n `13`; crypto_alt avg `0.6635` n `239`; crypto_major avg `1.3996` n `8`; equity avg `1.7997` n `166`; fx avg `0.1365` n `6`; index avg `0.0956` n `27`; metal avg `0.3699` n `20`; unknown avg `-0.1248` n `1059`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.154`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1521`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1401`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1396`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.139`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.127`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.125`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.121`, n `668`, weak_sample_signal
