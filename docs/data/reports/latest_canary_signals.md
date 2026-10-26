# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T17:22:33.467541+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0894` n `13`; crypto_alt avg `0.1659` n `237`; crypto_major avg `0.0758` n `8`; equity avg `0.1948` n `154`; fx avg `0.0162` n `6`; index avg `0.0369` n `27`; metal avg `-0.0005` n `20`; unknown avg `-0.1353` n `1238`
- 1h: commodity avg `-0.2448` n `13`; crypto_alt avg `0.3594` n `237`; crypto_major avg `0.3561` n `8`; equity avg `0.3298` n `154`; fx avg `-0.0026` n `6`; index avg `0.0523` n `27`; metal avg `0.0539` n `20`; unknown avg `0.1991` n `1238`
- 4h: commodity avg `0.072` n `13`; crypto_alt avg `0.7548` n `237`; crypto_major avg `0.6676` n `8`; equity avg `1.5947` n `153`; fx avg `0.0187` n `6`; index avg `0.2505` n `27`; metal avg `0.1429` n `20`; unknown avg `595.3904` n `1166`
- 24h: commodity avg `-0.1519` n `13`; crypto_alt avg `-0.2951` n `237`; crypto_major avg `-0.0416` n `8`; equity avg `0.9904` n `153`; fx avg `0.0629` n `6`; index avg `-0.0204` n `27`; metal avg `0.1468` n `20`; unknown avg `781.2337` n `924`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2235`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1875`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1844`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1364`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1217`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
