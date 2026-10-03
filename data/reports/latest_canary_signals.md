# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T14:53:02.839871+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0072` n `13`; crypto_alt avg `0.2828` n `235`; crypto_major avg `0.2774` n `8`; equity avg `-0.0008` n `143`; fx avg `0.0` n `6`; index avg `-0.0015` n `26`; metal avg `0.0066` n `20`; unknown avg `0.0694` n `974`
- 1h: commodity avg `0.058` n `13`; crypto_alt avg `0.5809` n `235`; crypto_major avg `0.3257` n `8`; equity avg `0.0082` n `143`; fx avg `-0.0072` n `6`; index avg `-0.0021` n `26`; metal avg `-0.0014` n `20`; unknown avg `0.0225` n `970`
- 4h: commodity avg `0.1237` n `13`; crypto_alt avg `0.6838` n `235`; crypto_major avg `0.4838` n `8`; equity avg `-0.0069` n `143`; fx avg `-0.0166` n `6`; index avg `-0.0078` n `26`; metal avg `-0.0066` n `20`; unknown avg `0.1416` n `946`
- 24h: commodity avg `0.7235` n `13`; crypto_alt avg `-1.3257` n `235`; crypto_major avg `-1.2146` n `8`; equity avg `-0.5834` n `143`; fx avg `-0.0529` n `6`; index avg `-0.0854` n `26`; metal avg `-0.1948` n `20`; unknown avg `0.6346` n `868`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.197`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1866`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1609`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1573`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
