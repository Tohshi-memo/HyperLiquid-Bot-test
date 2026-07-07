# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T18:07:34.053312+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.91` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0096` n `12`; crypto_alt avg `-0.1483` n `229`; crypto_major avg `-0.2445` n `8`; equity avg `-0.0121` n `91`; fx avg `-0.0016` n `6`; index avg `0.0006` n `25`; metal avg `-0.0184` n `20`; unknown avg `-0.0405` n `763`
- 1h: commodity avg `-0.0227` n `12`; crypto_alt avg `-0.4332` n `229`; crypto_major avg `-0.2031` n `8`; equity avg `-0.0278` n `91`; fx avg `-0.0027` n `6`; index avg `0.034` n `25`; metal avg `-0.0257` n `20`; unknown avg `-0.0435` n `763`
- 4h: commodity avg `0.0352` n `12`; crypto_alt avg `0.3408` n `229`; crypto_major avg `0.9391` n `8`; equity avg `0.3721` n `91`; fx avg `-0.0399` n `6`; index avg `0.085` n `25`; metal avg `-0.0703` n `20`; unknown avg `-0.0436` n `755`
- 24h: commodity avg `0.5585` n `12`; crypto_alt avg `-0.9781` n `229`; crypto_major avg `-0.1689` n `8`; equity avg `-2.4807` n `91`; fx avg `-0.2417` n `6`; index avg `-0.4617` n `25`; metal avg `-0.143` n `20`; unknown avg `-0.3621` n `731`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0655`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0603`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.048`, n `668`, weak_sample_signal
