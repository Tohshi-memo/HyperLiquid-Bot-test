# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T22:07:25.875029+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0142` n `13`; crypto_alt avg `0.0933` n `239`; crypto_major avg `0.0392` n `8`; equity avg `0.009` n `158`; fx avg `-0.003` n `6`; index avg `0.0018` n `27`; metal avg `0.0006` n `20`; unknown avg `-0.4007` n `1252`
- 1h: commodity avg `-0.0109` n `13`; crypto_alt avg `0.2062` n `239`; crypto_major avg `0.212` n `8`; equity avg `-0.0125` n `158`; fx avg `0.0011` n `6`; index avg `-0.0134` n `27`; metal avg `-0.0002` n `20`; unknown avg `0.419` n `1250`
- 4h: commodity avg `0.0712` n `13`; crypto_alt avg `-0.8454` n `239`; crypto_major avg `-0.3621` n `8`; equity avg `-0.1573` n `158`; fx avg `0.0073` n `6`; index avg `-0.009` n `27`; metal avg `-0.0083` n `20`; unknown avg `-0.1774` n `1214`
- 24h: commodity avg `0.0669` n `13`; crypto_alt avg `-2.0116` n `239`; crypto_major avg `-1.0521` n `8`; equity avg `-0.3131` n `158`; fx avg `-0.0066` n `6`; index avg `0.0293` n `27`; metal avg `-0.0272` n `20`; unknown avg `146.4195` n `1097`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2129`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1689`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1681`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1289`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
