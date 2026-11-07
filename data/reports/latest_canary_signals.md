# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T09:07:31.625485+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0008` n `13`; crypto_alt avg `-0.0567` n `239`; crypto_major avg `-0.0153` n `8`; equity avg `0.2105` n `158`; fx avg `0.0032` n `6`; index avg `0.0199` n `27`; metal avg `-0.0053` n `20`; unknown avg `0.0663` n `1241`
- 1h: commodity avg `0.0156` n `13`; crypto_alt avg `-0.2331` n `239`; crypto_major avg `0.0054` n `8`; equity avg `0.29` n `158`; fx avg `0.0049` n `6`; index avg `0.0248` n `27`; metal avg `0.0013` n `20`; unknown avg `0.0378` n `1215`
- 4h: commodity avg `0.0433` n `13`; crypto_alt avg `-0.1792` n `239`; crypto_major avg `0.3267` n `8`; equity avg `0.2196` n `158`; fx avg `-0.0287` n `6`; index avg `0.0377` n `27`; metal avg `-0.0065` n `20`; unknown avg `0.011` n `1177`
- 24h: commodity avg `0.024` n `13`; crypto_alt avg `-0.3461` n `239`; crypto_major avg `0.0641` n `8`; equity avg `0.2221` n `158`; fx avg `0.0131` n `6`; index avg `0.0614` n `27`; metal avg `-0.0744` n `20`; unknown avg `7.8258` n `1046`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2124`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1561`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1527`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1346`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
