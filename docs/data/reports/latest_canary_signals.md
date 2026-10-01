# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T16:37:33.302925+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0197` n `13`; crypto_alt avg `0.0837` n `234`; crypto_major avg `0.0188` n `8`; equity avg `0.1612` n `142`; fx avg `-0.0064` n `6`; index avg `0.0373` n `26`; metal avg `0.0063` n `20`; unknown avg `0.3013` n `975`
- 1h: commodity avg `-0.2685` n `13`; crypto_alt avg `0.366` n `234`; crypto_major avg `0.1348` n `8`; equity avg `0.4083` n `142`; fx avg `0.0129` n `6`; index avg `0.0951` n `26`; metal avg `0.0492` n `20`; unknown avg `1.1534` n `967`
- 4h: commodity avg `-0.0099` n `13`; crypto_alt avg `-0.5463` n `234`; crypto_major avg `-0.6367` n `8`; equity avg `-0.2843` n `142`; fx avg `-0.1326` n `6`; index avg `-0.1636` n `26`; metal avg `-0.2675` n `20`; unknown avg `2.5672` n `909`
- 24h: commodity avg `-0.3687` n `13`; crypto_alt avg `-1.7217` n `234`; crypto_major avg `-0.8638` n `8`; equity avg `0.093` n `142`; fx avg `-0.0997` n `6`; index avg `-0.0534` n `26`; metal avg `-0.1016` n `20`; unknown avg `0.102` n `840`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1746`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1562`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
