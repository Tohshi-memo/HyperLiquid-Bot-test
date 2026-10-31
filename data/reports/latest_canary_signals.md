# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T22:52:27.442831+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0003` n `13`; crypto_alt avg `-0.2156` n `238`; crypto_major avg `-0.3129` n `8`; equity avg `-0.0532` n `156`; fx avg `0.0087` n `6`; index avg `-0.0108` n `27`; metal avg `-0.0043` n `20`; unknown avg `1.1531` n `1254`
- 1h: commodity avg `0.0328` n `13`; crypto_alt avg `-0.1752` n `238`; crypto_major avg `-0.2226` n `8`; equity avg `-0.0416` n `156`; fx avg `0.0049` n `6`; index avg `-0.0002` n `27`; metal avg `0.0083` n `20`; unknown avg `0.3118` n `1184`
- 4h: commodity avg `0.0455` n `13`; crypto_alt avg `-0.5591` n `238`; crypto_major avg `-0.4108` n `8`; equity avg `-0.07` n `156`; fx avg `0.0115` n `6`; index avg `-0.0067` n `27`; metal avg `0.0103` n `20`; unknown avg `3.1609` n `1104`
- 24h: commodity avg `-0.0514` n `13`; crypto_alt avg `-0.5109` n `238`; crypto_major avg `-0.1705` n `8`; equity avg `0.1568` n `156`; fx avg `0.0293` n `6`; index avg `-0.0551` n `27`; metal avg `0.0433` n `20`; unknown avg `1.67` n `1043`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1465`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1427`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1414`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1383`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1315`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
