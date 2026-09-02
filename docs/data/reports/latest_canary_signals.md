# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T09:07:33.439928+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0098` n `12`; crypto_alt avg `0.2803` n `232`; crypto_major avg `0.3514` n `8`; equity avg `0.0063` n `132`; fx avg `0.0055` n `6`; index avg `-0.0074` n `26`; metal avg `0.0257` n `20`; unknown avg `0.2187` n `790`
- 1h: commodity avg `0.0455` n `12`; crypto_alt avg `-0.493` n `232`; crypto_major avg `-0.605` n `8`; equity avg `-0.3556` n `132`; fx avg `-0.0041` n `6`; index avg `-0.0684` n `26`; metal avg `-0.0494` n `20`; unknown avg `0.6626` n `790`
- 4h: commodity avg `-0.1236` n `12`; crypto_alt avg `-0.2035` n `232`; crypto_major avg `-0.5441` n `8`; equity avg `-0.2477` n `132`; fx avg `-0.0669` n `6`; index avg `-0.0365` n `26`; metal avg `0.0886` n `20`; unknown avg `0.1911` n `770`
- 24h: commodity avg `0.5362` n `12`; crypto_alt avg `0.3097` n `232`; crypto_major avg `-1.388` n `8`; equity avg `-1.5371` n `130`; fx avg `-0.1863` n `6`; index avg `-0.2472` n `26`; metal avg `-0.4058` n `20`; unknown avg `0.1513` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0631`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0606`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0543`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0523`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0454`, n `668`, weak_sample_signal
