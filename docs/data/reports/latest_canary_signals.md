# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T13:07:27.293666+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.019` n `13`; crypto_alt avg `-0.025` n `239`; crypto_major avg `0.0436` n `8`; equity avg `0.0171` n `160`; fx avg `0.0088` n `6`; index avg `0.0004` n `27`; metal avg `0.0307` n `20`; unknown avg `19.1321` n `1258`
- 1h: commodity avg `-0.108` n `13`; crypto_alt avg `0.1237` n `239`; crypto_major avg `0.0479` n `8`; equity avg `-0.4234` n `160`; fx avg `-0.0077` n `6`; index avg `-0.0234` n `27`; metal avg `-0.0164` n `20`; unknown avg `19.2518` n `1256`
- 4h: commodity avg `-0.0582` n `13`; crypto_alt avg `-0.0767` n `239`; crypto_major avg `-0.3197` n `8`; equity avg `-0.8242` n `160`; fx avg `-0.0286` n `6`; index avg `-0.0459` n `27`; metal avg `-0.1157` n `20`; unknown avg `319.23` n `1248`
- 24h: commodity avg `-0.4963` n `13`; crypto_alt avg `-0.584` n `239`; crypto_major avg `-0.8448` n `8`; equity avg `2.3954` n `160`; fx avg `-0.0344` n `6`; index avg `0.3208` n `27`; metal avg `-0.1388` n `20`; unknown avg `2.9112` n `1161`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2303`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1499`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1372`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1308`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1229`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1155`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
