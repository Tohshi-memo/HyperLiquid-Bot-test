# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T23:07:30.301328+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1789` n `13`; crypto_alt avg `0.082` n `239`; crypto_major avg `0.1318` n `8`; equity avg `-0.4098` n `166`; fx avg `0.0113` n `6`; index avg `-0.0662` n `27`; metal avg `0.1985` n `20`; unknown avg `0.1115` n `1246`
- 1h: commodity avg `-0.1713` n `13`; crypto_alt avg `-0.1407` n `239`; crypto_major avg `0.1183` n `8`; equity avg `-0.2541` n `166`; fx avg `0.0038` n `6`; index avg `-0.0916` n `27`; metal avg `0.1806` n `20`; unknown avg `0.2473` n `1228`
- 4h: commodity avg `-0.2425` n `13`; crypto_alt avg `-0.2584` n `239`; crypto_major avg `0.0906` n `8`; equity avg `-0.2658` n `166`; fx avg `0.0967` n `6`; index avg `-0.101` n `27`; metal avg `0.1547` n `20`; unknown avg `-0.2888` n `1188`
- 24h: commodity avg `-0.3209` n `13`; crypto_alt avg `0.5247` n `239`; crypto_major avg `1.0078` n `8`; equity avg `0.5945` n `166`; fx avg `0.0765` n `6`; index avg `0.0234` n `27`; metal avg `0.1915` n `20`; unknown avg `194.0825` n `1030`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1634`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1551`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1497`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1464`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1425`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1418`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1279`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1254`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1222`, n `668`, weak_sample_signal
