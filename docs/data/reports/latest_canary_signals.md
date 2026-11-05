# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T02:37:27.906300+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0487` n `13`; crypto_alt avg `0.0207` n `239`; crypto_major avg `-0.126` n `8`; equity avg `-0.1627` n `158`; fx avg `0.0251` n `6`; index avg `-0.0151` n `27`; metal avg `-0.0003` n `20`; unknown avg `1.0625` n `1265`
- 1h: commodity avg `0.0821` n `13`; crypto_alt avg `0.4159` n `239`; crypto_major avg `0.2147` n `8`; equity avg `0.736` n `158`; fx avg `0.0254` n `6`; index avg `0.1156` n `27`; metal avg `0.0899` n `20`; unknown avg `1.9641` n `1256`
- 4h: commodity avg `-0.1105` n `13`; crypto_alt avg `-0.3105` n `239`; crypto_major avg `-0.1703` n `8`; equity avg `-0.7238` n `158`; fx avg `0.0527` n `6`; index avg `-0.1989` n `27`; metal avg `0.3864` n `20`; unknown avg `1.6142` n `1196`
- 24h: commodity avg `-1.5402` n `13`; crypto_alt avg `3.7583` n `239`; crypto_major avg `4.1639` n `8`; equity avg `0.9844` n `158`; fx avg `0.1626` n `6`; index avg `0.5257` n `27`; metal avg `1.75` n `20`; unknown avg `32.5993` n `1034`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2548`, n `668`, moderate_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1888`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1839`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1584`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1532`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1527`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1523`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1457`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1384`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1368`, n `668`, weak_sample_signal
