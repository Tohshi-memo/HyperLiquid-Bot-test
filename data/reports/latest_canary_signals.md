# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T22:52:34.277147+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.3077` n `12`; crypto_alt avg `-0.0619` n `228`; crypto_major avg `-0.0022` n `8`; equity avg `0.0468` n `74`; fx avg `0.0115` n `6`; index avg `0.0464` n `23`; metal avg `0.0632` n `18`; unknown avg `0.0186` n `643`
- 1h: commodity avg `-0.3386` n `12`; crypto_alt avg `-0.0985` n `228`; crypto_major avg `-0.1523` n `8`; equity avg `0.0867` n `74`; fx avg `0.007` n `6`; index avg `0.0641` n `23`; metal avg `-0.0085` n `18`; unknown avg `0.0291` n `643`
- 4h: commodity avg `-0.1564` n `12`; crypto_alt avg `-0.4302` n `228`; crypto_major avg `-0.8584` n `8`; equity avg `-0.1745` n `74`; fx avg `-0.0275` n `6`; index avg `0.0569` n `23`; metal avg `-0.0362` n `18`; unknown avg `0.3771` n `643`
- 24h: commodity avg `-0.6061` n `12`; crypto_alt avg `-0.4642` n `228`; crypto_major avg `-0.0289` n `8`; equity avg `-0.6151` n `74`; fx avg `-0.0161` n `6`; index avg `0.2922` n `23`; metal avg `0.1127` n `18`; unknown avg `41.6058` n `514`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0633`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0611`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0604`, n `668`, weak_sample_signal
