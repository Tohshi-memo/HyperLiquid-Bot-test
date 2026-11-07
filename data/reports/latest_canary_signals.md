# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T09:52:25.105025+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0138` n `13`; crypto_alt avg `-0.1411` n `239`; crypto_major avg `-0.025` n `8`; equity avg `-0.0684` n `158`; fx avg `0.0` n `6`; index avg `-0.0035` n `27`; metal avg `0.0052` n `20`; unknown avg `0.4321` n `1261`
- 1h: commodity avg `0.0003` n `13`; crypto_alt avg `-0.3237` n `239`; crypto_major avg `-0.251` n `8`; equity avg `-0.0188` n `158`; fx avg `0.0038` n `6`; index avg `-0.0019` n `27`; metal avg `-0.01` n `20`; unknown avg `130.5067` n `1239`
- 4h: commodity avg `0.0512` n `13`; crypto_alt avg `-0.5573` n `239`; crypto_major avg `-0.1223` n `8`; equity avg `0.0329` n `158`; fx avg `-0.0054` n `6`; index avg `0.0217` n `27`; metal avg `-0.0148` n `20`; unknown avg `137.2125` n `1177`
- 24h: commodity avg `0.2547` n `13`; crypto_alt avg `-0.6781` n `239`; crypto_major avg `-0.2421` n `8`; equity avg `-0.2817` n `158`; fx avg `0.0374` n `6`; index avg `-0.0214` n `27`; metal avg `0.0255` n `20`; unknown avg `8.1594` n `1046`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2134`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1588`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1551`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1344`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
