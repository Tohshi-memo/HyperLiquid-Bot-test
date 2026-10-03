# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T21:52:29.158479+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0088` n `13`; crypto_alt avg `0.0601` n `235`; crypto_major avg `0.0193` n `8`; equity avg `0.0077` n `143`; fx avg `-0.002` n `6`; index avg `0.0015` n `26`; metal avg `-0.0009` n `20`; unknown avg `0.0647` n `1063`
- 1h: commodity avg `0.1133` n `13`; crypto_alt avg `-0.0431` n `235`; crypto_major avg `-0.0489` n `8`; equity avg `0.013` n `143`; fx avg `0.0029` n `6`; index avg `0.0034` n `26`; metal avg `0.0029` n `20`; unknown avg `-0.0855` n `1061`
- 4h: commodity avg `0.1447` n `13`; crypto_alt avg `0.1838` n `235`; crypto_major avg `-0.1452` n `8`; equity avg `0.0643` n `143`; fx avg `0.012` n `6`; index avg `0.0063` n `26`; metal avg `0.0071` n `20`; unknown avg `0.5028` n `1046`
- 24h: commodity avg `0.0293` n `13`; crypto_alt avg `2.6992` n `235`; crypto_major avg `1.3103` n `8`; equity avg `0.205` n `143`; fx avg `-0.0154` n `6`; index avg `0.0309` n `26`; metal avg `-0.0063` n `20`; unknown avg `0.0507` n `890`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1992`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1857`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1559`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1549`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
