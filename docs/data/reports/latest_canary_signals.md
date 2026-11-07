# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T00:33:52.031331+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0044` n `13`; crypto_alt avg `-0.0258` n `239`; crypto_major avg `-0.0865` n `8`; equity avg `-0.009` n `158`; fx avg `-0.0048` n `6`; index avg `0.0007` n `27`; metal avg `-0.0058` n `20`; unknown avg `0.0038` n `1261`
- 1h: commodity avg `0.0012` n `13`; crypto_alt avg `0.1147` n `239`; crypto_major avg `0.0044` n `8`; equity avg `0.0723` n `158`; fx avg `-0.0146` n `6`; index avg `0.0052` n `27`; metal avg `0.0079` n `20`; unknown avg `-0.1919` n `1249`
- 4h: commodity avg `0.0393` n `13`; crypto_alt avg `-0.2584` n `239`; crypto_major avg `0.0803` n `8`; equity avg `-0.0179` n `158`; fx avg `0.0064` n `6`; index avg `-0.0274` n `27`; metal avg `0.0107` n `20`; unknown avg `-0.433` n `1171`
- 24h: commodity avg `0.1071` n `13`; crypto_alt avg `0.7591` n `239`; crypto_major avg `-0.4003` n `8`; equity avg `1.4312` n `158`; fx avg `-0.0948` n `6`; index avg `0.2048` n `27`; metal avg `-0.0711` n `20`; unknown avg `8.2183` n `1022`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2143`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1672`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1622`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1417`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
