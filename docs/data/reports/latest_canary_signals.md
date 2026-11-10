# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T09:37:27.142929+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1814` n `13`; crypto_alt avg `-0.0733` n `239`; crypto_major avg `-0.0441` n `8`; equity avg `0.0912` n `160`; fx avg `-0.0317` n `6`; index avg `0.0111` n `27`; metal avg `-0.0243` n `20`; unknown avg `31.0047` n `1262`
- 1h: commodity avg `-0.16` n `13`; crypto_alt avg `-0.0636` n `239`; crypto_major avg `-0.2509` n `8`; equity avg `0.0112` n `160`; fx avg `-0.0222` n `6`; index avg `-0.0214` n `27`; metal avg `-0.1523` n `20`; unknown avg `19.0633` n `1235`
- 4h: commodity avg `-0.5761` n `13`; crypto_alt avg `-0.0549` n `239`; crypto_major avg `-0.8065` n `8`; equity avg `-0.0806` n `160`; fx avg `-0.0246` n `6`; index avg `-0.0323` n `27`; metal avg `-0.2732` n `20`; unknown avg `21.3984` n `1201`
- 24h: commodity avg `-0.9294` n `13`; crypto_alt avg `0.9692` n `239`; crypto_major avg `-0.1572` n `8`; equity avg `4.6449` n `160`; fx avg `-0.0771` n `6`; index avg `0.5185` n `27`; metal avg `0.0498` n `20`; unknown avg `5.827` n `1159`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2324`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1557`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1508`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1413`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1321`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1277`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1255`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
