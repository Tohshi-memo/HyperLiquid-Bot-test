# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T23:55:17.957282+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0137` n `13`; crypto_alt avg `-0.0093` n `235`; crypto_major avg `-0.0269` n `8`; equity avg `-0.0058` n `143`; fx avg `0.0013` n `6`; index avg `0.0019` n `26`; metal avg `0.0002` n `20`; unknown avg `0.4848` n `1079`
- 1h: commodity avg `-0.0172` n `13`; crypto_alt avg `0.2228` n `235`; crypto_major avg `-0.1442` n `8`; equity avg `-0.0189` n `143`; fx avg `-0.011` n `6`; index avg `-0.0023` n `26`; metal avg `0.0014` n `20`; unknown avg `0.6328` n `1077`
- 4h: commodity avg `0.063` n `13`; crypto_alt avg `0.5254` n `235`; crypto_major avg `-0.0443` n `8`; equity avg `0.0759` n `143`; fx avg `0.0126` n `6`; index avg `0.0002` n `26`; metal avg `-0.0022` n `20`; unknown avg `0.656` n `1055`
- 24h: commodity avg `-0.0256` n `13`; crypto_alt avg `1.7521` n `235`; crypto_major avg `0.5131` n `8`; equity avg `0.1689` n `143`; fx avg `-0.0102` n `6`; index avg `0.0484` n `26`; metal avg `-0.0167` n `20`; unknown avg `0.0661` n `898`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.199`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1854`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1557`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1544`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
