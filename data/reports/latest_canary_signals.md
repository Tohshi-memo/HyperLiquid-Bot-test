# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T09:58:44.506927+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.52` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0315` n `13`; crypto_alt avg `0.0418` n `239`; crypto_major avg `0.0607` n `8`; equity avg `0.193` n `158`; fx avg `-0.0014` n `6`; index avg `-0.0005` n `27`; metal avg `0.0125` n `20`; unknown avg `0.0434` n `1260`
- 1h: commodity avg `-0.0917` n `13`; crypto_alt avg `-0.248` n `239`; crypto_major avg `-0.086` n `8`; equity avg `0.4141` n `158`; fx avg `0.0518` n `6`; index avg `0.0938` n `27`; metal avg `0.0857` n `20`; unknown avg `0.6501` n `1232`
- 4h: commodity avg `0.0269` n `13`; crypto_alt avg `0.5932` n `239`; crypto_major avg `0.5669` n `8`; equity avg `1.4341` n `158`; fx avg `0.1134` n `6`; index avg `0.234` n `27`; metal avg `0.4036` n `20`; unknown avg `0.6548` n `1144`
- 24h: commodity avg `-0.3212` n `13`; crypto_alt avg `2.5351` n `239`; crypto_major avg `1.5614` n `8`; equity avg `2.4435` n `158`; fx avg `0.1662` n `6`; index avg `0.2113` n `27`; metal avg `1.1081` n `20`; unknown avg `1.0276` n `1057`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2548`, n `668`, moderate_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1591`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1552`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1552`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1528`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1465`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1458`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1421`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1408`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.14`, n `668`, weak_sample_signal
