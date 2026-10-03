# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T17:07:33.382575+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0058` n `13`; crypto_alt avg `0.1374` n `235`; crypto_major avg `0.1525` n `8`; equity avg `0.0166` n `143`; fx avg `-0.0039` n `6`; index avg `0.0038` n `26`; metal avg `0.002` n `20`; unknown avg `-0.0418` n `1076`
- 1h: commodity avg `-0.0179` n `13`; crypto_alt avg `0.2005` n `235`; crypto_major avg `0.2547` n `8`; equity avg `0.0344` n `143`; fx avg `-0.0007` n `6`; index avg `0.0069` n `26`; metal avg `-0.0068` n `20`; unknown avg `-0.1038` n `1076`
- 4h: commodity avg `0.2273` n `13`; crypto_alt avg `0.8489` n `235`; crypto_major avg `0.4237` n `8`; equity avg `0.0733` n `143`; fx avg `-0.0078` n `6`; index avg `0.0254` n `26`; metal avg `-0.0034` n `20`; unknown avg `-0.1468` n `950`
- 24h: commodity avg `0.3238` n `13`; crypto_alt avg `-0.351` n `235`; crypto_major avg `-0.2201` n `8`; equity avg `0.1667` n `143`; fx avg `-0.0346` n `6`; index avg `0.0459` n `26`; metal avg `0.102` n `20`; unknown avg `-0.243` n `868`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1968`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1844`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.166`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1559`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1198`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
