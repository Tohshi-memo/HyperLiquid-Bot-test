# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T15:52:37.343141+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0029` n `13`; crypto_alt avg `0.3651` n `234`; crypto_major avg `0.185` n `8`; equity avg `0.0588` n `142`; fx avg `-0.002` n `6`; index avg `-0.0083` n `26`; metal avg `-0.0164` n `20`; unknown avg `0.3065` n `975`
- 1h: commodity avg `0.0859` n `13`; crypto_alt avg `0.6977` n `234`; crypto_major avg `0.1993` n `8`; equity avg `-0.0279` n `142`; fx avg `-0.0519` n `6`; index avg `-0.0386` n `26`; metal avg `-0.0611` n `20`; unknown avg `0.4786` n `961`
- 4h: commodity avg `0.2234` n `13`; crypto_alt avg `-0.777` n `234`; crypto_major avg `-0.7667` n `8`; equity avg `-0.7131` n `142`; fx avg `-0.1755` n `6`; index avg `-0.2697` n `26`; metal avg `-0.2698` n `20`; unknown avg `1.4317` n `909`
- 24h: commodity avg `-0.1585` n `13`; crypto_alt avg `-1.4679` n `234`; crypto_major avg `-0.5949` n `8`; equity avg `-0.2808` n `142`; fx avg `-0.1162` n `6`; index avg `-0.1793` n `26`; metal avg `-0.1499` n `20`; unknown avg `2.8301` n `840`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1739`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1552`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
