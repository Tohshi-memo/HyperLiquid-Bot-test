# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T00:52:26.720297+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0596` n `13`; crypto_alt avg `-0.0518` n `239`; crypto_major avg `-0.0316` n `8`; equity avg `-0.0267` n `168`; fx avg `0.0017` n `6`; index avg `-0.0079` n `27`; metal avg `-0.0042` n `20`; unknown avg `3.2135` n `1265`
- 1h: commodity avg `-0.1431` n `13`; crypto_alt avg `-0.1401` n `239`; crypto_major avg `0.1809` n `8`; equity avg `-0.0348` n `168`; fx avg `0.0072` n `6`; index avg `0.0081` n `27`; metal avg `-0.0015` n `20`; unknown avg `0.7479` n `1251`
- 4h: commodity avg `-0.1343` n `13`; crypto_alt avg `0.139` n `239`; crypto_major avg `-0.0331` n `8`; equity avg `-0.0237` n `168`; fx avg `-0.0037` n `6`; index avg `-0.0281` n `27`; metal avg `0.0235` n `20`; unknown avg `2.7509` n `1163`
- 24h: commodity avg `-0.7077` n `13`; crypto_alt avg `0.1772` n `239`; crypto_major avg `0.1349` n `8`; equity avg `3.4051` n `168`; fx avg `-0.1445` n `6`; index avg `0.342` n `27`; metal avg `1.0714` n `20`; unknown avg `213.5997` n `991`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1389`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1344`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0649`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
