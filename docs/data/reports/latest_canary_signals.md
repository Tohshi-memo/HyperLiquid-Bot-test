# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T14:22:31.961248+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0002` n `13`; crypto_alt avg `-0.138` n `239`; crypto_major avg `-0.0253` n `8`; equity avg `0.0011` n `158`; fx avg `0.0053` n `6`; index avg `-0.016` n `27`; metal avg `0.0038` n `20`; unknown avg `-0.0134` n `1262`
- 1h: commodity avg `0.0868` n `13`; crypto_alt avg `-0.7206` n `239`; crypto_major avg `-0.5649` n `8`; equity avg `-0.1229` n `158`; fx avg `-0.0182` n `6`; index avg `-0.0044` n `27`; metal avg `-0.0044` n `20`; unknown avg `1.4744` n `1256`
- 4h: commodity avg `0.0284` n `13`; crypto_alt avg `-0.5265` n `239`; crypto_major avg `0.0942` n `8`; equity avg `0.0243` n `158`; fx avg `-0.0022` n `6`; index avg `-0.0086` n `27`; metal avg `0.0002` n `20`; unknown avg `0.9982` n `1250`
- 24h: commodity avg `0.1012` n `13`; crypto_alt avg `-1.9465` n `239`; crypto_major avg `-0.4766` n `8`; equity avg `0.1235` n `158`; fx avg `0.0282` n `6`; index avg `0.0045` n `27`; metal avg `-0.0409` n `20`; unknown avg `5.9944` n `1097`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1525`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.119`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1102`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
