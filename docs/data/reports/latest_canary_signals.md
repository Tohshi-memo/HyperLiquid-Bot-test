# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T11:52:28.282571+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.081` n `13`; crypto_alt avg `0.004` n `239`; crypto_major avg `-0.0361` n `8`; equity avg `0.0953` n `166`; fx avg `-0.0104` n `6`; index avg `0.0048` n `27`; metal avg `0.0185` n `20`; unknown avg `0.0097` n `1266`
- 1h: commodity avg `0.0097` n `13`; crypto_alt avg `0.0798` n `239`; crypto_major avg `0.1011` n `8`; equity avg `-0.1226` n `166`; fx avg `-0.0214` n `6`; index avg `-0.0184` n `27`; metal avg `-0.0307` n `20`; unknown avg `-0.0834` n `1262`
- 4h: commodity avg `-0.2772` n `13`; crypto_alt avg `0.1718` n `239`; crypto_major avg `0.4537` n `8`; equity avg `0.669` n `166`; fx avg `-0.0707` n `6`; index avg `0.0907` n `27`; metal avg `-0.0351` n `20`; unknown avg `49.3163` n `1106`
- 24h: commodity avg `-0.9009` n `13`; crypto_alt avg `0.8149` n `239`; crypto_major avg `1.2048` n `8`; equity avg `2.0439` n `166`; fx avg `0.1762` n `6`; index avg `0.14` n `27`; metal avg `0.4057` n `20`; unknown avg `0.0334` n `1059`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1573`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1566`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1402`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1398`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1366`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1362`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1342`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1264`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1233`, n `668`, weak_sample_signal
