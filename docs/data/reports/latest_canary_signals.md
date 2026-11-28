# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T21:37:35.689215+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0006` n `13`; crypto_alt avg `-0.0015` n `239`; crypto_major avg `-0.0812` n `8`; equity avg `0.0122` n `168`; fx avg `-0.0007` n `6`; index avg `0.0002` n `27`; metal avg `0.0064` n `20`; unknown avg `5.4359` n `1266`
- 1h: commodity avg `0.0212` n `13`; crypto_alt avg `-0.1189` n `239`; crypto_major avg `-0.1206` n `8`; equity avg `0.025` n `168`; fx avg `-0.0019` n `6`; index avg `-0.0004` n `27`; metal avg `0.0036` n `20`; unknown avg `46.4802` n `1218`
- 4h: commodity avg `0.1465` n `13`; crypto_alt avg `-0.3217` n `239`; crypto_major avg `-0.287` n `8`; equity avg `0.1813` n `168`; fx avg `-0.0061` n `6`; index avg `0.0223` n `27`; metal avg `0.0215` n `20`; unknown avg `23.6781` n `1182`
- 24h: commodity avg `0.0104` n `13`; crypto_alt avg `-3.5973` n `239`; crypto_major avg `-1.5463` n `8`; equity avg `-0.0932` n `168`; fx avg `-0.0159` n `6`; index avg `-0.0423` n `27`; metal avg `0.0341` n `20`; unknown avg `2.3249` n `1083`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1609`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.145`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1264`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1245`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0582`, n `668`, weak_sample_signal
