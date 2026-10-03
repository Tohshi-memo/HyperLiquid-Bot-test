# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T13:52:32.022868+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.019` n `13`; crypto_alt avg `0.1` n `235`; crypto_major avg `0.0027` n `8`; equity avg `-0.0097` n `143`; fx avg `-0.0002` n `6`; index avg `0.0048` n `26`; metal avg `-0.0034` n `20`; unknown avg `0.3768` n `970`
- 1h: commodity avg `0.1104` n `13`; crypto_alt avg `0.4143` n `235`; crypto_major avg `0.0619` n `8`; equity avg `-0.0032` n `143`; fx avg `-0.0022` n `6`; index avg `0.0108` n `26`; metal avg `-0.0001` n `20`; unknown avg `0.2432` n `968`
- 4h: commodity avg `0.0479` n `13`; crypto_alt avg `0.4834` n `235`; crypto_major avg `0.1981` n `8`; equity avg `0.0093` n `143`; fx avg `-0.011` n `6`; index avg `-0.0005` n `26`; metal avg `-0.0109` n `20`; unknown avg `0.1254` n `958`
- 24h: commodity avg `0.48` n `13`; crypto_alt avg `-2.4383` n `235`; crypto_major avg `-2.2757` n `8`; equity avg `-0.356` n `143`; fx avg `-0.0251` n `6`; index avg `-0.0538` n `26`; metal avg `-0.3431` n `20`; unknown avg `0.6438` n `868`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1971`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1868`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1595`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1574`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
