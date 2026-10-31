# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T05:22:30.723315+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0166` n `13`; crypto_alt avg `-0.3008` n `238`; crypto_major avg `-0.0991` n `8`; equity avg `0.01` n `156`; fx avg `0.0015` n `6`; index avg `-0.0072` n `27`; metal avg `0.0009` n `20`; unknown avg `-0.0729` n `1262`
- 1h: commodity avg `-0.0437` n `13`; crypto_alt avg `-0.5917` n `238`; crypto_major avg `-0.2531` n `8`; equity avg `-0.0391` n `156`; fx avg `-0.008` n `6`; index avg `-0.0095` n `27`; metal avg `0.007` n `20`; unknown avg `-0.1276` n `1256`
- 4h: commodity avg `0.1083` n `13`; crypto_alt avg `-1.1795` n `238`; crypto_major avg `-0.6845` n `8`; equity avg `-0.079` n `156`; fx avg `-0.0115` n `6`; index avg `-0.0584` n `27`; metal avg `-0.0027` n `20`; unknown avg `-0.4131` n `1232`
- 24h: commodity avg `0.0237` n `13`; crypto_alt avg `0.4653` n `238`; crypto_major avg `-1.8112` n `8`; equity avg `-2.7069` n `156`; fx avg `-0.0809` n `6`; index avg `-0.2201` n `27`; metal avg `-0.6531` n `20`; unknown avg `3.9614` n `1006`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1518`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.144`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1367`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1333`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1217`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
