# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T06:52:29.454436+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0058` n `13`; crypto_alt avg `0.0787` n `235`; crypto_major avg `0.0587` n `8`; equity avg `-0.0035` n `143`; fx avg `0.0012` n `6`; index avg `-0.0002` n `26`; metal avg `0.0004` n `20`; unknown avg `0.181` n `1079`
- 1h: commodity avg `0.0051` n `13`; crypto_alt avg `0.023` n `235`; crypto_major avg `0.1057` n `8`; equity avg `-0.0193` n `143`; fx avg `0.0007` n `6`; index avg `-0.0045` n `26`; metal avg `-0.0025` n `20`; unknown avg `0.2333` n `1049`
- 4h: commodity avg `-0.0298` n `13`; crypto_alt avg `0.6489` n `235`; crypto_major avg `0.3433` n `8`; equity avg `0.0368` n `143`; fx avg `-0.0188` n `6`; index avg `0.0011` n `26`; metal avg `0.0036` n `20`; unknown avg `0.427` n `1043`
- 24h: commodity avg `0.1836` n `13`; crypto_alt avg `1.9244` n `235`; crypto_major avg `0.9806` n `8`; equity avg `0.2602` n `143`; fx avg `-0.0341` n `6`; index avg `0.0235` n `26`; metal avg `-0.0006` n `20`; unknown avg `0.3701` n `898`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1877`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1685`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1471`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1401`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1206`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
