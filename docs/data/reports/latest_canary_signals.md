# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T22:37:24.613523+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0436` n `13`; crypto_alt avg `0.184` n `235`; crypto_major avg `0.0861` n `8`; equity avg `0.0058` n `143`; fx avg `0.0102` n `6`; index avg `0.0011` n `26`; metal avg `0.0011` n `20`; unknown avg `0.3461` n `1079`
- 1h: commodity avg `-0.0383` n `13`; crypto_alt avg `0.1788` n `235`; crypto_major avg `0.1527` n `8`; equity avg `0.048` n `143`; fx avg `0.0133` n `6`; index avg `0.0054` n `26`; metal avg `-0.0009` n `20`; unknown avg `0.381` n `1061`
- 4h: commodity avg `0.0615` n `13`; crypto_alt avg `0.4893` n `235`; crypto_major avg `0.024` n `8`; equity avg `0.0927` n `143`; fx avg `0.0336` n `6`; index avg `0.0076` n `26`; metal avg `0.0065` n `20`; unknown avg `0.6021` n `1046`
- 24h: commodity avg `-0.0785` n `13`; crypto_alt avg `2.4609` n `235`; crypto_major avg `1.106` n `8`; equity avg `0.2131` n `143`; fx avg `0.004` n `6`; index avg `0.0594` n `26`; metal avg `-0.0123` n `20`; unknown avg `0.0845` n `898`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1993`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1849`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1548`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1547`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1356`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
