# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T04:37:32.519787+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0052` n `13`; crypto_alt avg `0.2252` n `239`; crypto_major avg `0.3825` n `8`; equity avg `0.1669` n `158`; fx avg `-0.0059` n `6`; index avg `0.0314` n `27`; metal avg `0.0398` n `20`; unknown avg `1.2086` n `1261`
- 1h: commodity avg `0.0208` n `13`; crypto_alt avg `-0.3858` n `239`; crypto_major avg `-0.2552` n `8`; equity avg `-0.4063` n `158`; fx avg `-0.003` n `6`; index avg `-0.0944` n `27`; metal avg `-0.0496` n `20`; unknown avg `0.2791` n `1239`
- 4h: commodity avg `-0.2841` n `13`; crypto_alt avg `0.3664` n `239`; crypto_major avg `-0.0139` n `8`; equity avg `-0.6761` n `158`; fx avg `0.0184` n `6`; index avg `-0.1573` n `27`; metal avg `0.3664` n `20`; unknown avg `-0.0317` n `1238`
- 24h: commodity avg `-1.7182` n `13`; crypto_alt avg `4.1327` n `239`; crypto_major avg `4.2205` n `8`; equity avg `0.9172` n `158`; fx avg `0.1457` n `6`; index avg `0.4101` n `27`; metal avg `1.9457` n `20`; unknown avg `35.1816` n `1020`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2524`, n `668`, moderate_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1933`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1907`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1533`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1532`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1467`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1439`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.137`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1339`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1328`, n `668`, weak_sample_signal
