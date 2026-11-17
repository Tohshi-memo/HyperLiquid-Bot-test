# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T22:22:33.134271+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0018` n `13`; crypto_alt avg `0.1711` n `239`; crypto_major avg `0.1747` n `8`; equity avg `0.0269` n `163`; fx avg `0.01` n `6`; index avg `0.0004` n `27`; metal avg `0.0091` n `20`; unknown avg `1.9717` n `1263`
- 1h: commodity avg `0.0319` n `13`; crypto_alt avg `0.1566` n `239`; crypto_major avg `0.1358` n `8`; equity avg `0.5523` n `163`; fx avg `0.0044` n `6`; index avg `0.0337` n `27`; metal avg `0.034` n `20`; unknown avg `2.7805` n `1257`
- 4h: commodity avg `-0.1406` n `13`; crypto_alt avg `1.2556` n `239`; crypto_major avg `1.0528` n `8`; equity avg `1.6188` n `163`; fx avg `-0.0347` n `6`; index avg `0.1439` n `27`; metal avg `-0.0414` n `20`; unknown avg `2.5505` n `1233`
- 24h: commodity avg `0.2503` n `13`; crypto_alt avg `0.1145` n `239`; crypto_major avg `-0.1429` n `8`; equity avg `-0.0148` n `163`; fx avg `0.0153` n `6`; index avg `-0.0192` n `27`; metal avg `-0.0118` n `20`; unknown avg `11.1111` n `1107`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1598`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1463`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1264`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
