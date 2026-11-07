# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T08:22:23.692083+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0028` n `13`; crypto_alt avg `-0.1297` n `239`; crypto_major avg `0.036` n `8`; equity avg `0.1021` n `158`; fx avg `-0.0064` n `6`; index avg `0.0113` n `27`; metal avg `0.0007` n `20`; unknown avg `1.585` n `1257`
- 1h: commodity avg `0.0206` n `13`; crypto_alt avg `-0.1958` n `239`; crypto_major avg `0.1149` n `8`; equity avg `0.1554` n `158`; fx avg `-0.0206` n `6`; index avg `0.0184` n `27`; metal avg `0.0001` n `20`; unknown avg `1.5901` n `1235`
- 4h: commodity avg `0.0692` n `13`; crypto_alt avg `0.052` n `239`; crypto_major avg `0.3373` n `8`; equity avg `0.0633` n `158`; fx avg `-0.0443` n `6`; index avg `0.0284` n `27`; metal avg `-0.0081` n `20`; unknown avg `2.3316` n `1197`
- 24h: commodity avg `-0.0914` n `13`; crypto_alt avg `-0.056` n `239`; crypto_major avg `0.3943` n `8`; equity avg `1.0365` n `158`; fx avg `0.0056` n `6`; index avg `0.1786` n `27`; metal avg `0.0073` n `20`; unknown avg `9.8324` n `1046`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1582`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1513`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
