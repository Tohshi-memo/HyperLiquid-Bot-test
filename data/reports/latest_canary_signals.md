# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T06:22:34.945652+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0419` n `13`; crypto_alt avg `0.0634` n `239`; crypto_major avg `-0.0545` n `8`; equity avg `-0.0819` n `160`; fx avg `0.0143` n `6`; index avg `-0.0048` n `27`; metal avg `-0.0217` n `20`; unknown avg `0.012` n `1261`
- 1h: commodity avg `0.0248` n `13`; crypto_alt avg `0.0609` n `239`; crypto_major avg `-0.1568` n `8`; equity avg `0.0609` n `160`; fx avg `-0.0339` n `6`; index avg `0.0266` n `27`; metal avg `-0.0354` n `20`; unknown avg `1.0246` n `1235`
- 4h: commodity avg `-0.0327` n `13`; crypto_alt avg `0.5721` n `239`; crypto_major avg `0.099` n `8`; equity avg `-0.0978` n `160`; fx avg `-0.0872` n `6`; index avg `0.0173` n `27`; metal avg `-0.0252` n `20`; unknown avg `1.3702` n `1217`
- 24h: commodity avg `-0.4476` n `13`; crypto_alt avg `1.7333` n `239`; crypto_major avg `0.4276` n `8`; equity avg `4.5203` n `160`; fx avg `0.0325` n `6`; index avg `0.5286` n `27`; metal avg `0.1695` n `20`; unknown avg `191.0694` n `1065`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2027`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1493`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1401`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1398`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1388`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1318`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
