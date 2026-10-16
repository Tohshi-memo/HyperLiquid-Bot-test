# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T13:22:28.306583+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0751` n `13`; crypto_alt avg `0.2398` n `236`; crypto_major avg `0.0873` n `8`; equity avg `0.0527` n `151`; fx avg `0.0074` n `6`; index avg `-0.0066` n `26`; metal avg `-0.0537` n `20`; unknown avg `2.3744` n `1136`
- 1h: commodity avg `-0.1528` n `13`; crypto_alt avg `-0.4435` n `236`; crypto_major avg `-0.4347` n `8`; equity avg `-0.2412` n `151`; fx avg `-0.005` n `6`; index avg `-0.0338` n `26`; metal avg `-0.132` n `20`; unknown avg `3.4314` n `1134`
- 4h: commodity avg `-0.0587` n `13`; crypto_alt avg `-0.1496` n `236`; crypto_major avg `-0.3463` n `8`; equity avg `-0.7158` n `151`; fx avg `0.0053` n `6`; index avg `-0.0648` n `26`; metal avg `-0.1855` n `20`; unknown avg `5.87` n `1128`
- 24h: commodity avg `-0.1935` n `13`; crypto_alt avg `4.93` n `236`; crypto_major avg `2.8719` n `8`; equity avg `2.4661` n `151`; fx avg `0.0367` n `6`; index avg `0.3178` n `26`; metal avg `0.1173` n `20`; unknown avg `25.0588` n `944`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `-0.0999`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0902`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0814`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.08`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0779`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
