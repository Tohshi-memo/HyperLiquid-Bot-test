# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T01:22:26.760590+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0035` n `13`; crypto_alt avg `-0.2099` n `239`; crypto_major avg `-0.0429` n `8`; equity avg `-0.0068` n `158`; fx avg `0.0007` n `6`; index avg `-0.0022` n `27`; metal avg `0.0018` n `20`; unknown avg `-0.1599` n `1262`
- 1h: commodity avg `0.0334` n `13`; crypto_alt avg `-0.3629` n `239`; crypto_major avg `-0.1925` n `8`; equity avg `-0.0361` n `158`; fx avg `-0.0085` n `6`; index avg `-0.0071` n `27`; metal avg `-0.0014` n `20`; unknown avg `-0.2174` n `1256`
- 4h: commodity avg `-0.0335` n `13`; crypto_alt avg `0.2492` n `239`; crypto_major avg `0.3781` n `8`; equity avg `0.1363` n `158`; fx avg `0.0104` n `6`; index avg `0.0188` n `27`; metal avg `0.0085` n `20`; unknown avg `-0.1248` n `1228`
- 24h: commodity avg `0.0257` n `13`; crypto_alt avg `-1.8686` n `239`; crypto_major avg `-0.8252` n `8`; equity avg `0.0484` n `158`; fx avg `-0.0057` n `6`; index avg `0.0498` n `27`; metal avg `-0.0359` n `20`; unknown avg `160.5134` n `1087`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2114`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1617`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1611`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
