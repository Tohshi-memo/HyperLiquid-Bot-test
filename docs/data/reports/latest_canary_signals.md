# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T08:22:25.214163+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0562` n `13`; crypto_alt avg `-0.0241` n `239`; crypto_major avg `-0.0553` n `8`; equity avg `-0.0663` n `160`; fx avg `0.0112` n `6`; index avg `-0.0099` n `27`; metal avg `0.0155` n `20`; unknown avg `-0.0103` n `1261`
- 1h: commodity avg `-0.1354` n `13`; crypto_alt avg `-0.1114` n `239`; crypto_major avg `-0.2894` n `8`; equity avg `0.2763` n `160`; fx avg `-0.0046` n `6`; index avg `0.0188` n `27`; metal avg `0.0165` n `20`; unknown avg `-0.1807` n `1239`
- 4h: commodity avg `-0.2157` n `13`; crypto_alt avg `0.1814` n `239`; crypto_major avg `-0.053` n `8`; equity avg `0.4227` n `160`; fx avg `-0.0712` n `6`; index avg `0.0839` n `27`; metal avg `-0.0871` n `20`; unknown avg `1.589` n `1211`
- 24h: commodity avg `-0.5291` n `13`; crypto_alt avg `2.11` n `239`; crypto_major avg `0.6728` n `8`; equity avg `5.1383` n `160`; fx avg `-0.0221` n `6`; index avg `0.579` n `27`; metal avg `0.2534` n `20`; unknown avg `177.4366` n `1149`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2189`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1479`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1418`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.137`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1349`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1296`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
