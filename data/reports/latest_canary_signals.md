# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T15:22:31.291414+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2403` n `13`; crypto_alt avg `-0.0749` n `239`; crypto_major avg `-0.0814` n `8`; equity avg `-0.0329` n `161`; fx avg `0.0329` n `6`; index avg `-0.0024` n `27`; metal avg `-0.0167` n `20`; unknown avg `0.8779` n `1261`
- 1h: commodity avg `0.3845` n `13`; crypto_alt avg `-0.0482` n `239`; crypto_major avg `-0.0015` n `8`; equity avg `0.3581` n `161`; fx avg `0.0254` n `6`; index avg `0.0234` n `27`; metal avg `-0.161` n `20`; unknown avg `0.3547` n `1237`
- 4h: commodity avg `0.5369` n `13`; crypto_alt avg `0.1022` n `239`; crypto_major avg `-0.237` n `8`; equity avg `0.3045` n `161`; fx avg `-0.0043` n `6`; index avg `-0.0058` n `27`; metal avg `-0.335` n `20`; unknown avg `20.3815` n `1231`
- 24h: commodity avg `1.273` n `13`; crypto_alt avg `-1.3749` n `239`; crypto_major avg `-1.093` n `8`; equity avg `2.7785` n `161`; fx avg `-0.1806` n `6`; index avg `0.2233` n `27`; metal avg `0.0949` n `20`; unknown avg `1.6572` n `1155`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.3342`, n `668`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1599`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1306`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
