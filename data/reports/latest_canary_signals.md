# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T04:52:25.981157+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0032` n `13`; crypto_alt avg `-0.1342` n `239`; crypto_major avg `-0.1019` n `8`; equity avg `-0.007` n `158`; fx avg `-0.0062` n `6`; index avg `-0.0014` n `27`; metal avg `-0.0039` n `20`; unknown avg `-0.0389` n `1262`
- 1h: commodity avg `0.005` n `13`; crypto_alt avg `-0.3198` n `239`; crypto_major avg `-0.116` n `8`; equity avg `-0.0669` n `158`; fx avg `-0.0006` n `6`; index avg `-0.0081` n `27`; metal avg `-0.0106` n `20`; unknown avg `-0.4532` n `1244`
- 4h: commodity avg `0.0276` n `13`; crypto_alt avg `-0.6758` n `239`; crypto_major avg `-0.1423` n `8`; equity avg `-0.0937` n `158`; fx avg `0.0152` n `6`; index avg `-0.0184` n `27`; metal avg `-0.0251` n `20`; unknown avg `-0.3986` n `1240`
- 24h: commodity avg `0.1484` n `13`; crypto_alt avg `-1.9092` n `239`; crypto_major avg `-0.5033` n `8`; equity avg `-0.2206` n `158`; fx avg `0.0111` n `6`; index avg `0.0274` n `27`; metal avg `-0.0642` n `20`; unknown avg `162.1841` n `1089`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2111`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1644`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1587`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
