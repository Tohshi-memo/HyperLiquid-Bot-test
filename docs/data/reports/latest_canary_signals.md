# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T23:07:27.333481+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.009` n `13`; crypto_alt avg `-0.0572` n `235`; crypto_major avg `-0.1293` n `8`; equity avg `0.007` n `143`; fx avg `-0.0013` n `6`; index avg `-0.0011` n `26`; metal avg `0.0007` n `20`; unknown avg `0.0634` n `1077`
- 1h: commodity avg `-0.0519` n `13`; crypto_alt avg `0.0891` n `235`; crypto_major avg `-0.0744` n `8`; equity avg `0.06` n `143`; fx avg `0.0095` n `6`; index avg `0.0023` n `26`; metal avg `0.0034` n `20`; unknown avg `0.3625` n `1077`
- 4h: commodity avg `0.0764` n `13`; crypto_alt avg `0.4324` n `235`; crypto_major avg `-0.05` n `8`; equity avg `0.1336` n `143`; fx avg `0.03` n `6`; index avg `0.0068` n `26`; metal avg `0.0053` n `20`; unknown avg `0.5397` n `1046`
- 24h: commodity avg `-0.0545` n `13`; crypto_alt avg `2.196` n `235`; crypto_major avg `0.8639` n `8`; equity avg `0.2351` n `143`; fx avg `-0.0073` n `6`; index avg `0.0506` n `26`; metal avg `-0.0277` n `20`; unknown avg `0.1145` n `898`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1847`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1547`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1543`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1323`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
