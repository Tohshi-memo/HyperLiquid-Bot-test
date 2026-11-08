# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T03:22:28.822677+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0204` n `13`; crypto_alt avg `-0.0689` n `239`; crypto_major avg `-0.0269` n `8`; equity avg `-0.0204` n `158`; fx avg `0.0059` n `6`; index avg `0.005` n `27`; metal avg `-0.0045` n `20`; unknown avg `10.7378` n `1262`
- 1h: commodity avg `-0.0201` n `13`; crypto_alt avg `0.0664` n `239`; crypto_major avg `0.143` n `8`; equity avg `0.0956` n `158`; fx avg `0.0058` n `6`; index avg `0.0239` n `27`; metal avg `0.0046` n `20`; unknown avg `0.6895` n `1254`
- 4h: commodity avg `-0.0492` n `13`; crypto_alt avg `-0.4538` n `239`; crypto_major avg `0.0351` n `8`; equity avg `0.0801` n `158`; fx avg `0.0315` n `6`; index avg `0.008` n `27`; metal avg `-0.0061` n `20`; unknown avg `-0.2091` n `1246`
- 24h: commodity avg `0.0602` n `13`; crypto_alt avg `-1.5555` n `239`; crypto_major avg `-0.6297` n `8`; equity avg `-0.075` n `158`; fx avg `0.0278` n `6`; index avg `0.0548` n `27`; metal avg `-0.0493` n `20`; unknown avg `160.8719` n `1085`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2114`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1635`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1611`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1246`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
