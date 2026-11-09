# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T02:07:29.220030+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0983` n `13`; crypto_alt avg `-0.0311` n `239`; crypto_major avg `-0.0353` n `8`; equity avg `0.2096` n `158`; fx avg `-0.0169` n `6`; index avg `0.0078` n `27`; metal avg `0.0829` n `20`; unknown avg `0.1868` n `1258`
- 1h: commodity avg `0.0884` n `13`; crypto_alt avg `0.0905` n `239`; crypto_major avg `-0.116` n `8`; equity avg `0.7957` n `158`; fx avg `-0.026` n `6`; index avg `0.0673` n `27`; metal avg `0.199` n `20`; unknown avg `-0.0876` n `1248`
- 4h: commodity avg `-0.0942` n `13`; crypto_alt avg `2.0057` n `239`; crypto_major avg `1.038` n `8`; equity avg `1.3664` n `158`; fx avg `-0.04` n `6`; index avg `0.1954` n `27`; metal avg `0.7034` n `20`; unknown avg `2.0643` n `1212`
- 24h: commodity avg `-0.0368` n `13`; crypto_alt avg `-1.5193` n `239`; crypto_major avg `-1.8734` n `8`; equity avg `0.6248` n `158`; fx avg `-0.0554` n `6`; index avg `0.0731` n `27`; metal avg `0.5863` n `20`; unknown avg `1.4058` n `994`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1709`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1595`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1556`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1444`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1348`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
