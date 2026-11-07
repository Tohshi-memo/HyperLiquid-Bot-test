# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T15:37:29.568765+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0002` n `13`; crypto_alt avg `-0.1633` n `239`; crypto_major avg `-0.154` n `8`; equity avg `-0.1168` n `158`; fx avg `-0.0117` n `6`; index avg `0.0106` n `27`; metal avg `-0.0039` n `20`; unknown avg `0.9923` n `1253`
- 1h: commodity avg `-0.005` n `13`; crypto_alt avg `-0.421` n `239`; crypto_major avg `-0.3833` n `8`; equity avg `-0.1697` n `158`; fx avg `-0.0078` n `6`; index avg `0.012` n `27`; metal avg `-0.0108` n `20`; unknown avg `161.4007` n `1247`
- 4h: commodity avg `-0.0157` n `13`; crypto_alt avg `-0.3305` n `239`; crypto_major avg `-0.4427` n `8`; equity avg `-0.1647` n `158`; fx avg `0.0106` n `6`; index avg `0.0284` n `27`; metal avg `-0.0063` n `20`; unknown avg `0.0117` n `1241`
- 24h: commodity avg `0.3545` n `13`; crypto_alt avg `-1.5695` n `239`; crypto_major avg `-0.3225` n `8`; equity avg `1.0286` n `158`; fx avg `-0.0048` n `6`; index avg `0.0764` n `27`; metal avg `0.1046` n `20`; unknown avg `-0.1089` n `1111`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2133`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1647`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1639`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
