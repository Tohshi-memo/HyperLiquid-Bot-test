# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T11:37:31.172440+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0136` n `13`; crypto_alt avg `-0.0709` n `239`; crypto_major avg `-0.0926` n `8`; equity avg `-0.0255` n `157`; fx avg `-0.0025` n `6`; index avg `0.0075` n `27`; metal avg `-0.0137` n `20`; unknown avg `0.2169` n `1262`
- 1h: commodity avg `0.1326` n `13`; crypto_alt avg `0.3425` n `239`; crypto_major avg `-0.037` n `8`; equity avg `-0.103` n `157`; fx avg `0.0013` n `6`; index avg `-0.0289` n `27`; metal avg `0.0116` n `20`; unknown avg `1.1355` n `1228`
- 4h: commodity avg `0.2203` n `13`; crypto_alt avg `0.9401` n `239`; crypto_major avg `0.3905` n `8`; equity avg `0.9116` n `157`; fx avg `0.0639` n `6`; index avg `0.1058` n `27`; metal avg `-0.0576` n `20`; unknown avg `1.8534` n `1202`
- 24h: commodity avg `-0.132` n `13`; crypto_alt avg `-1.2311` n `238`; crypto_major avg `-0.9312` n `8`; equity avg `-3.4833` n `157`; fx avg `0.0191` n `6`; index avg `-0.241` n `27`; metal avg `-0.4624` n `20`; unknown avg `4.0665` n `1021`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1667`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1618`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1585`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1508`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1272`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1148`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
