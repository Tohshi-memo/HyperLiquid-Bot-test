# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T09:37:29.238727+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.55` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0851` n `13`; crypto_alt avg `0.1115` n `239`; crypto_major avg `0.1684` n `8`; equity avg `0.3618` n `158`; fx avg `0.0161` n `6`; index avg `0.0674` n `27`; metal avg `0.0227` n `20`; unknown avg `0.6233` n `1262`
- 1h: commodity avg `-0.0761` n `13`; crypto_alt avg `-0.316` n `239`; crypto_major avg `-0.0188` n `8`; equity avg `0.2418` n `158`; fx avg `0.0714` n `6`; index avg `0.0928` n `27`; metal avg `0.113` n `20`; unknown avg `25.2295` n `1214`
- 4h: commodity avg `0.0637` n `13`; crypto_alt avg `1.234` n `239`; crypto_major avg `0.9419` n `8`; equity avg `1.7378` n `158`; fx avg `0.1316` n `6`; index avg `0.2808` n `27`; metal avg `0.6139` n `20`; unknown avg `26.818` n `1148`
- 24h: commodity avg `-0.434` n `13`; crypto_alt avg `2.5287` n `239`; crypto_major avg `1.5374` n `8`; equity avg `2.3367` n `158`; fx avg `0.1679` n `6`; index avg `0.2428` n `27`; metal avg `1.0999` n `20`; unknown avg `1.0912` n `1057`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2518`, n `668`, moderate_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1556`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1539`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1503`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1502`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1452`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1445`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1398`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1389`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1382`, n `668`, weak_sample_signal
