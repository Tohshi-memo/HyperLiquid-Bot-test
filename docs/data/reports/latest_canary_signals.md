# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T11:52:32.423354+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.41` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0342` n `13`; crypto_alt avg `-0.0241` n `238`; crypto_major avg `-0.0385` n `8`; equity avg `0.0212` n `154`; fx avg `0.0029` n `6`; index avg `0.0064` n `27`; metal avg `-0.0082` n `20`; unknown avg `-0.27` n `1239`
- 1h: commodity avg `0.0103` n `13`; crypto_alt avg `0.0229` n `238`; crypto_major avg `-0.1696` n `8`; equity avg `-0.1221` n `154`; fx avg `0.045` n `6`; index avg `0.0019` n `27`; metal avg `0.0494` n `20`; unknown avg `-0.042` n `1235`
- 4h: commodity avg `-0.0513` n `13`; crypto_alt avg `0.5056` n `238`; crypto_major avg `0.5565` n `8`; equity avg `0.3002` n `154`; fx avg `0.0538` n `6`; index avg `0.0463` n `27`; metal avg `0.0395` n `20`; unknown avg `79.1714` n `1186`
- 24h: commodity avg `0.1064` n `13`; crypto_alt avg `2.528` n `238`; crypto_major avg `2.5592` n `8`; equity avg `3.1614` n `154`; fx avg `0.1197` n `6`; index avg `0.434` n `27`; metal avg `0.2982` n `20`; unknown avg `7.0933` n `1070`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1564`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1416`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1364`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0642`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0614`, n `668`, weak_sample_signal
