# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T13:37:32.020319+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0428` n `13`; crypto_alt avg `0.0152` n `239`; crypto_major avg `-0.1427` n `8`; equity avg `-0.2247` n `158`; fx avg `-0.0292` n `6`; index avg `-0.0304` n `27`; metal avg `-0.1608` n `20`; unknown avg `66.9645` n `1257`
- 1h: commodity avg `0.1197` n `13`; crypto_alt avg `-0.0846` n `239`; crypto_major avg `-0.4002` n `8`; equity avg `-0.5468` n `158`; fx avg `-0.0413` n `6`; index avg `-0.0096` n `27`; metal avg `-0.1269` n `20`; unknown avg `53.2405` n `1253`
- 4h: commodity avg `0.3251` n `13`; crypto_alt avg `0.429` n `239`; crypto_major avg `-0.2178` n `8`; equity avg `-0.3333` n `158`; fx avg `0.0466` n `6`; index avg `-0.0395` n `27`; metal avg `-0.1704` n `20`; unknown avg `259.3367` n `1176`
- 24h: commodity avg `0.6444` n `13`; crypto_alt avg `-2.3151` n `239`; crypto_major avg `-4.5673` n `8`; equity avg `-3.7702` n `158`; fx avg `-0.026` n `6`; index avg `-0.5614` n `27`; metal avg `-0.491` n `20`; unknown avg `81.2929` n `1080`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2192`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1613`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1428`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1404`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1365`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1292`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
