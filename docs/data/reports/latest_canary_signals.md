# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T06:37:25.961949+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0269` n `13`; crypto_alt avg `-0.0385` n `238`; crypto_major avg `0.0237` n `8`; equity avg `0.0056` n `156`; fx avg `-0.0034` n `6`; index avg `-0.0026` n `27`; metal avg `0.0196` n `20`; unknown avg `0.0713` n `1258`
- 1h: commodity avg `0.0027` n `13`; crypto_alt avg `0.2961` n `238`; crypto_major avg `0.0243` n `8`; equity avg `-0.0084` n `156`; fx avg `0.0018` n `6`; index avg `-0.0017` n `27`; metal avg `0.029` n `20`; unknown avg `-0.1274` n `1226`
- 4h: commodity avg `0.0209` n `13`; crypto_alt avg `-0.4969` n `238`; crypto_major avg `-0.5251` n `8`; equity avg `-0.0108` n `156`; fx avg `-0.0039` n `6`; index avg `-0.0403` n `27`; metal avg `0.051` n `20`; unknown avg `1.1505` n `1212`
- 24h: commodity avg `0.094` n `13`; crypto_alt avg `0.6729` n `238`; crypto_major avg `-1.8625` n `8`; equity avg `-2.6599` n `156`; fx avg `-0.0656` n `6`; index avg `-0.2168` n `27`; metal avg `-0.4962` n `20`; unknown avg `3.8609` n `1002`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1468`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1384`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1346`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.132`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1186`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
