# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T15:52:28.772818+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0439` n `13`; crypto_alt avg `0.5281` n `239`; crypto_major avg `0.4425` n `8`; equity avg `0.6273` n `162`; fx avg `0.0007` n `6`; index avg `0.0595` n `27`; metal avg `0.0436` n `20`; unknown avg `5.6781` n `1261`
- 1h: commodity avg `-0.0405` n `13`; crypto_alt avg `-0.0885` n `239`; crypto_major avg `0.1883` n `8`; equity avg `0.1376` n `162`; fx avg `-0.0253` n `6`; index avg `0.0282` n `27`; metal avg `-0.1429` n `20`; unknown avg `-0.1116` n `1253`
- 4h: commodity avg `0.1512` n `13`; crypto_alt avg `-0.6249` n `239`; crypto_major avg `-0.7482` n `8`; equity avg `-0.4027` n `162`; fx avg `-0.042` n `6`; index avg `0.0604` n `27`; metal avg `-0.4577` n `20`; unknown avg `23.1384` n `1239`
- 24h: commodity avg `-0.3815` n `13`; crypto_alt avg `-3.9496` n `239`; crypto_major avg `-3.4469` n `8`; equity avg `-2.8425` n `162`; fx avg `-0.1376` n `6`; index avg `-0.1218` n `27`; metal avg `-1.0557` n `20`; unknown avg `6.9962` n `1150`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.138`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1307`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
