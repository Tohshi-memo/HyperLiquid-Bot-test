# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T09:07:26.309953+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0174` n `12`; crypto_alt avg `-0.2602` n `232`; crypto_major avg `0.0244` n `8`; equity avg `-0.2409` n `130`; fx avg `0.0053` n `6`; index avg `-0.0583` n `26`; metal avg `-0.0013` n `20`; unknown avg `-0.1143` n `790`
- 1h: commodity avg `-0.0257` n `12`; crypto_alt avg `-1.0568` n `232`; crypto_major avg `-0.5533` n `8`; equity avg `-0.7881` n `130`; fx avg `0.0061` n `6`; index avg `-0.1778` n `26`; metal avg `-0.3766` n `20`; unknown avg `-0.4039` n `790`
- 4h: commodity avg `0.0953` n `12`; crypto_alt avg `-1.3288` n `232`; crypto_major avg `-1.121` n `8`; equity avg `-1.3115` n `130`; fx avg `0.0181` n `6`; index avg `-0.2521` n `26`; metal avg `-0.5528` n `20`; unknown avg `-0.2689` n `770`
- 24h: commodity avg `0.415` n `12`; crypto_alt avg `0.0869` n `232`; crypto_major avg `-0.1322` n `8`; equity avg `-0.7881` n `130`; fx avg `0.0847` n `6`; index avg `-0.3019` n `26`; metal avg `-0.7424` n `20`; unknown avg `0.0642` n `749`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0706`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0461`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0454`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0393`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0354`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0322`, n `668`, weak_sample_signal
