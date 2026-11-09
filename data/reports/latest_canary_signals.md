# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T19:22:43.835127+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0283` n `13`; crypto_alt avg `-0.0746` n `239`; crypto_major avg `-0.0316` n `8`; equity avg `-0.0426` n `160`; fx avg `-0.0062` n `6`; index avg `-0.0066` n `27`; metal avg `-0.0054` n `20`; unknown avg `0.1847` n `1259`
- 1h: commodity avg `-0.0276` n `13`; crypto_alt avg `-0.0539` n `239`; crypto_major avg `-0.1324` n `8`; equity avg `-0.097` n `160`; fx avg `0.0012` n `6`; index avg `-0.0025` n `27`; metal avg `0.0313` n `20`; unknown avg `19.283` n `1255`
- 4h: commodity avg `0.1214` n `13`; crypto_alt avg `-0.3967` n `239`; crypto_major avg `-0.7024` n `8`; equity avg `0.3601` n `160`; fx avg `0.0272` n `6`; index avg `0.0437` n `27`; metal avg `-0.0067` n `20`; unknown avg `-0.5073` n `1249`
- 24h: commodity avg `-0.0985` n `13`; crypto_alt avg `0.4473` n `239`; crypto_major avg `-2.5965` n `8`; equity avg `3.2392` n `160`; fx avg `-0.133` n `6`; index avg `0.3904` n `27`; metal avg `0.3885` n `20`; unknown avg `4.9527` n `1074`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1754`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1516`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1417`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1371`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1334`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1332`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
