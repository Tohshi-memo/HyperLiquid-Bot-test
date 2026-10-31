# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T05:52:26.002133+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0132` n `13`; crypto_alt avg `-0.0653` n `238`; crypto_major avg `0.0027` n `8`; equity avg `-0.0082` n `156`; fx avg `0.0045` n `6`; index avg `-0.0034` n `27`; metal avg `-0.0001` n `20`; unknown avg `-0.2451` n `1262`
- 1h: commodity avg `-0.0163` n `13`; crypto_alt avg `-0.3053` n `238`; crypto_major avg `0.08` n `8`; equity avg `0.0453` n `156`; fx avg `0.0047` n `6`; index avg `0.0072` n `27`; metal avg `0.0069` n `20`; unknown avg `-0.2492` n `1254`
- 4h: commodity avg `0.1087` n `13`; crypto_alt avg `-1.0678` n `238`; crypto_major avg `-0.5436` n `8`; equity avg `-0.0519` n `156`; fx avg `0.0021` n `6`; index avg `-0.0493` n `27`; metal avg `-0.0087` n `20`; unknown avg `-0.5457` n `1230`
- 24h: commodity avg `-0.0618` n `13`; crypto_alt avg `0.5721` n `238`; crypto_major avg `-1.6404` n `8`; equity avg `-2.4507` n `156`; fx avg `-0.0703` n `6`; index avg `-0.1702` n `27`; metal avg `-0.6346` n `20`; unknown avg `4.5431` n `1004`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1499`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1422`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1323`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1202`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
