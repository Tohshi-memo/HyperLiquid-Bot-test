# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T09:22:26.691566+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1386` n `13`; crypto_alt avg `0.0994` n `238`; crypto_major avg `0.0052` n `8`; equity avg `-0.0584` n `155`; fx avg `-0.0035` n `6`; index avg `-0.0237` n `27`; metal avg `-0.0621` n `20`; unknown avg `-0.044` n `1230`
- 1h: commodity avg `0.0218` n `13`; crypto_alt avg `0.435` n `238`; crypto_major avg `0.1167` n `8`; equity avg `0.2523` n `155`; fx avg `-0.012` n `6`; index avg `0.0653` n `27`; metal avg `-0.0616` n `20`; unknown avg `1.0984` n `1224`
- 4h: commodity avg `0.0584` n `13`; crypto_alt avg `-0.636` n `238`; crypto_major avg `-0.4058` n `8`; equity avg `-0.464` n `155`; fx avg `-0.0087` n `6`; index avg `-0.0563` n `27`; metal avg `-0.2802` n `20`; unknown avg `0.8137` n `1190`
- 24h: commodity avg `-0.0459` n `13`; crypto_alt avg `-2.4673` n `238`; crypto_major avg `-1.8043` n `8`; equity avg `-1.2454` n `154`; fx avg `0.0208` n `6`; index avg `-0.0125` n `27`; metal avg `-0.4711` n `20`; unknown avg `30.5708` n `984`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
