# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T20:07:24.824233+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0119` n `13`; crypto_alt avg `0.142` n `239`; crypto_major avg `0.0236` n `8`; equity avg `-0.0425` n `158`; fx avg `0.0075` n `6`; index avg `0.0018` n `27`; metal avg `0.0021` n `20`; unknown avg `-0.0328` n `1250`
- 1h: commodity avg `0.0189` n `13`; crypto_alt avg `-0.1539` n `239`; crypto_major avg `-0.0875` n `8`; equity avg `-0.0576` n `158`; fx avg `0.0175` n `6`; index avg `-0.0097` n `27`; metal avg `-0.0058` n `20`; unknown avg `0.7019` n `1248`
- 4h: commodity avg `0.0355` n `13`; crypto_alt avg `0.1542` n `239`; crypto_major avg `0.0604` n `8`; equity avg `0.0864` n `158`; fx avg `0.0116` n `6`; index avg `0.0046` n `27`; metal avg `-0.0053` n `20`; unknown avg `0.4151` n `1217`
- 24h: commodity avg `-0.0577` n `13`; crypto_alt avg `-1.6265` n `239`; crypto_major avg `-0.7735` n `8`; equity avg `-0.1001` n `158`; fx avg `0.0016` n `6`; index avg `0.0107` n `27`; metal avg `0.0038` n `20`; unknown avg `0.0149` n `1081`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1645`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1624`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
