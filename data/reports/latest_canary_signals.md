# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T07:07:29.094262+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0156` n `13`; crypto_alt avg `-0.2098` n `239`; crypto_major avg `-0.3103` n `8`; equity avg `-0.1922` n `158`; fx avg `-0.0256` n `6`; index avg `-0.032` n `27`; metal avg `-0.0323` n `20`; unknown avg `-0.041` n `1248`
- 1h: commodity avg `-0.0257` n `13`; crypto_alt avg `0.2942` n `239`; crypto_major avg `-0.1368` n `8`; equity avg `0.0845` n `158`; fx avg `-0.0756` n `6`; index avg `-0.0112` n `27`; metal avg `-0.005` n `20`; unknown avg `-0.0966` n `1242`
- 4h: commodity avg `0.0523` n `13`; crypto_alt avg `-0.3236` n `239`; crypto_major avg `-1.1003` n `8`; equity avg `-0.8479` n `158`; fx avg `-0.1278` n `6`; index avg `-0.1368` n `27`; metal avg `-0.1517` n `20`; unknown avg `-0.5712` n `1218`
- 24h: commodity avg `1.4117` n `13`; crypto_alt avg `-4.4289` n `239`; crypto_major avg `-6.3224` n `8`; equity avg `-6.4367` n `158`; fx avg `-0.035` n `6`; index avg `-0.8461` n `27`; metal avg `-0.5338` n `20`; unknown avg `233.4646` n `1029`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2382`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1736`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.164`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1587`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1546`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1471`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1435`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
