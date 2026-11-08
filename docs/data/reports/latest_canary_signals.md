# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T18:22:26.116392+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0806` n `13`; crypto_alt avg `0.3695` n `239`; crypto_major avg `0.2821` n `8`; equity avg `0.4007` n `158`; fx avg `0.0034` n `6`; index avg `0.0379` n `27`; metal avg `0.0034` n `20`; unknown avg `1.4493` n `1238`
- 1h: commodity avg `-0.1822` n `13`; crypto_alt avg `0.5056` n `239`; crypto_major avg `0.3701` n `8`; equity avg `0.4542` n `158`; fx avg `0.0028` n `6`; index avg `0.0309` n `27`; metal avg `0.0147` n `20`; unknown avg `1.5973` n `1208`
- 4h: commodity avg `-0.1587` n `13`; crypto_alt avg `0.1402` n `239`; crypto_major avg `0.0885` n `8`; equity avg `0.3192` n `158`; fx avg `0.0365` n `6`; index avg `0.0254` n `27`; metal avg `-0.0201` n `20`; unknown avg `1.0666` n `1196`
- 24h: commodity avg `-0.0686` n `13`; crypto_alt avg `-1.8789` n `239`; crypto_major avg `-0.3075` n `8`; equity avg `0.3721` n `158`; fx avg `0.0788` n `6`; index avg `-0.0003` n `27`; metal avg `-0.0407` n `20`; unknown avg `0.38` n `1048`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2077`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1651`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1522`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
