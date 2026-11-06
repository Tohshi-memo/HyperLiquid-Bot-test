# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T13:07:27.035048+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1281` n `13`; crypto_alt avg `-0.0357` n `239`; crypto_major avg `-0.0524` n `8`; equity avg `-0.1911` n `158`; fx avg `-0.0074` n `6`; index avg `-0.0101` n `27`; metal avg `0.0143` n `20`; unknown avg `-0.1579` n `1253`
- 1h: commodity avg `-0.0678` n `13`; crypto_alt avg `-0.2022` n `239`; crypto_major avg `-0.4716` n `8`; equity avg `-0.6424` n `158`; fx avg `-0.0086` n `6`; index avg `-0.0511` n `27`; metal avg `0.0024` n `20`; unknown avg `0.1432` n `1249`
- 4h: commodity avg `0.1085` n `13`; crypto_alt avg `0.4258` n `239`; crypto_major avg `0.036` n `8`; equity avg `0.2944` n `158`; fx avg `0.0535` n `6`; index avg `0.0247` n `27`; metal avg `-0.1073` n `20`; unknown avg `7.6187` n `1176`
- 24h: commodity avg `0.4955` n `13`; crypto_alt avg `-2.2511` n `239`; crypto_major avg `-4.607` n `8`; equity avg `-3.5883` n `158`; fx avg `-0.0115` n `6`; index avg `-0.5571` n `27`; metal avg `-0.3573` n `20`; unknown avg `9.2351` n `1079`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2186`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1602`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1426`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1416`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1404`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1338`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
