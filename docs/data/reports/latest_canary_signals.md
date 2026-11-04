# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T12:07:24.944486+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0302` n `13`; crypto_alt avg `-0.5333` n `239`; crypto_major avg `-0.5658` n `8`; equity avg `-0.7041` n `158`; fx avg `-0.0149` n `6`; index avg `-0.0588` n `27`; metal avg `-0.0547` n `20`; unknown avg `0.3381` n `1252`
- 1h: commodity avg `0.0127` n `13`; crypto_alt avg `-0.2849` n `239`; crypto_major avg `-0.423` n `8`; equity avg `-1.1312` n `158`; fx avg `0.0067` n `6`; index avg `-0.0521` n `27`; metal avg `-0.1158` n `20`; unknown avg `1.446` n `1254`
- 4h: commodity avg `-0.1859` n `13`; crypto_alt avg `-0.3008` n `239`; crypto_major avg `-0.0836` n `8`; equity avg `-0.0877` n `158`; fx avg `0.0443` n `6`; index avg `0.1303` n `27`; metal avg `0.1065` n `20`; unknown avg `11.7834` n `1176`
- 24h: commodity avg `-0.7797` n `13`; crypto_alt avg `1.715` n `239`; crypto_major avg `1.1554` n `8`; equity avg `1.9495` n `158`; fx avg `0.1325` n `6`; index avg `0.2535` n `27`; metal avg `1.0854` n `20`; unknown avg `1.9398` n `1087`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2541`, n `668`, moderate_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1722`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1702`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1625`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1578`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1528`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1506`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1473`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1403`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1401`, n `668`, weak_sample_signal
