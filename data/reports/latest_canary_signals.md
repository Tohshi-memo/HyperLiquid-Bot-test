# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T06:22:26.932347+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1102` n `13`; crypto_alt avg `0.3118` n `239`; crypto_major avg `0.1885` n `8`; equity avg `0.2761` n `158`; fx avg `-0.0056` n `6`; index avg `0.0346` n `27`; metal avg `0.0448` n `20`; unknown avg `4.5625` n `1265`
- 1h: commodity avg `0.0227` n `13`; crypto_alt avg `0.1723` n `239`; crypto_major avg `0.059` n `8`; equity avg `0.0429` n `158`; fx avg `0.0082` n `6`; index avg `0.0081` n `27`; metal avg `-0.047` n `20`; unknown avg `-0.1667` n `1239`
- 4h: commodity avg `-0.1058` n `13`; crypto_alt avg `-0.2761` n `239`; crypto_major avg `-0.3762` n `8`; equity avg `-1.1574` n `158`; fx avg `0.013` n `6`; index avg `-0.2185` n `27`; metal avg `-0.0579` n `20`; unknown avg `-0.3076` n `1217`
- 24h: commodity avg `-2.0127` n `13`; crypto_alt avg `1.2866` n `239`; crypto_major avg `2.3086` n `8`; equity avg `-2.2942` n `158`; fx avg `0.0926` n `6`; index avg `-0.0739` n `27`; metal avg `0.7776` n `20`; unknown avg `31.7796` n `1012`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2525`, n `668`, moderate_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.178`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1778`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1533`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.151`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1508`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1356`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1351`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1338`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1297`, n `668`, weak_sample_signal
