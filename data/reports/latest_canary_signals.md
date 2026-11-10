# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T21:07:27.967403+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0244` n `13`; crypto_alt avg `0.1997` n `239`; crypto_major avg `0.1747` n `8`; equity avg `0.1738` n `160`; fx avg `-0.0022` n `6`; index avg `0.0249` n `27`; metal avg `-0.0288` n `20`; unknown avg `0.9954` n `1242`
- 1h: commodity avg `-0.0082` n `13`; crypto_alt avg `0.4678` n `239`; crypto_major avg `0.6395` n `8`; equity avg `0.9904` n `160`; fx avg `-0.0035` n `6`; index avg `0.0898` n `27`; metal avg `0.0397` n `20`; unknown avg `1.956` n `1240`
- 4h: commodity avg `0.0338` n `13`; crypto_alt avg `1.2248` n `239`; crypto_major avg `1.5797` n `8`; equity avg `1.3146` n `160`; fx avg `0.0285` n `6`; index avg `0.1317` n `27`; metal avg `0.1013` n `20`; unknown avg `19.8695` n `1232`
- 24h: commodity avg `0.0119` n `13`; crypto_alt avg `-1.3078` n `239`; crypto_major avg `-2.3094` n `8`; equity avg `-0.9297` n `160`; fx avg `-0.0893` n `6`; index avg `-0.1679` n `27`; metal avg `-0.6336` n `20`; unknown avg `0.6165` n `1171`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2587`, n `668`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1995`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1102`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
