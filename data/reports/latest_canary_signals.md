# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T15:37:26.516509+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1553` n `13`; crypto_alt avg `-0.5778` n `239`; crypto_major avg `-0.5477` n `8`; equity avg `-1.0958` n `158`; fx avg `-0.0079` n `6`; index avg `-0.1187` n `27`; metal avg `-0.1145` n `20`; unknown avg `0.4419` n `1257`
- 1h: commodity avg `-0.0687` n `13`; crypto_alt avg `-0.4034` n `239`; crypto_major avg `-0.3766` n `8`; equity avg `-0.9061` n `158`; fx avg `-0.0254` n `6`; index avg `-0.0762` n `27`; metal avg `0.0554` n `20`; unknown avg `1.088` n `1251`
- 4h: commodity avg `-0.4643` n `13`; crypto_alt avg `-0.2502` n `239`; crypto_major avg `-0.6526` n `8`; equity avg `-1.7695` n `158`; fx avg `-0.0127` n `6`; index avg `-0.0674` n `27`; metal avg `-0.1142` n `20`; unknown avg `61.5982` n `1187`
- 24h: commodity avg `-0.0481` n `13`; crypto_alt avg `1.2775` n `239`; crypto_major avg `-1.878` n `8`; equity avg `-0.3355` n `158`; fx avg `-0.0838` n `6`; index avg `-0.1322` n `27`; metal avg `-0.3169` n `20`; unknown avg `49.9529` n `1078`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2178`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1658`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1433`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1378`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1273`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
