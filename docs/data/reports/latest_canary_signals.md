# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T08:37:26.266574+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0009` n `13`; crypto_alt avg `0.0082` n `239`; crypto_major avg `0.0196` n `8`; equity avg `-0.0219` n `158`; fx avg `0.0002` n `6`; index avg `-0.0072` n `27`; metal avg `0.0057` n `20`; unknown avg `-0.2159` n `1251`
- 1h: commodity avg `-0.005` n `13`; crypto_alt avg `-0.1052` n `239`; crypto_major avg `0.1993` n `8`; equity avg `0.1387` n `158`; fx avg `-0.016` n `6`; index avg `0.023` n `27`; metal avg `0.0069` n `20`; unknown avg `0.0214` n `1229`
- 4h: commodity avg `0.0481` n `13`; crypto_alt avg `-0.0783` n `239`; crypto_major avg `0.3184` n `8`; equity avg `-0.0369` n `158`; fx avg `-0.0364` n `6`; index avg `0.012` n `27`; metal avg `-0.0087` n `20`; unknown avg `0.302` n `1195`
- 24h: commodity avg `-0.0028` n `13`; crypto_alt avg `0.091` n `239`; crypto_major avg `0.5162` n `8`; equity avg `1.0178` n `158`; fx avg `-0.0005` n `6`; index avg `0.1547` n `27`; metal avg `0.0312` n `20`; unknown avg `8.1851` n `1046`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2124`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1567`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1511`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
